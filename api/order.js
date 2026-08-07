import supabase from '../lib/supabase.js';
import { sendDiscordNotification } from '../lib/discord.js';
import { sendNtfyNotification }    from '../lib/ntfy.js';
import { validateOrderPayload } from '../lib/validator.js';
import * as logger from '../lib/logger.js';

// ── Server-side menu catalogue ────────────────────────────────────────────────
//
// THIS IS THE SINGLE SOURCE OF TRUTH FOR ALL PRICING.
//
// Keys are item IDs that match order.html's menuItems array.
// Values are immutable — frozen at startup so nothing can mutate them at runtime.
//
// The client NEVER influences prices. item.name, item.unit_price, item.line_total,
// and body.total_amount from the request are all IGNORED for any calculation.
//
// Future: replace this constant with a Supabase lookup inside getMenuItem().
// Only this file (specifically getMenuItem) needs to change — api/order.js
// handler code and all downstream logic remain identical.
//
/** @type {Readonly<Record<string, {name: string, price: number}>>} */
const MENU = Object.freeze({
  'bc-xe':       Object.freeze({ name: 'Bánh canh gà xé',      price: 50000 }),
  'bc-chat':     Object.freeze({ name: 'Bánh canh gà chặt',     price: 60000 }),
  'bc-dac-biet': Object.freeze({ name: 'Bánh canh đặc biệt',    price: 70000 }),
  'xoi-xe':      Object.freeze({ name: 'Xôi gà xé trứng non',  price: 45000 }),
  'xoi-chat':    Object.freeze({ name: 'Xôi gà chặt trứng non', price: 50000 }),
});

// ── Pricing layer ─────────────────────────────────────────────────────────────
//
// These three functions are the complete pricing abstraction.
// They are pure: same input always produces same output, no side effects.
// To switch from a constant to a database source, replace getMenuItem() only.

/**
 * Look up a menu item by id.
 * O(1) — plain object property access.
 *
 * @param {string} id - The item id (trimmed).
 * @returns {{ name: string, price: number } | null} null if id is unknown.
 */
function getMenuItem(id) {
  return MENU[id] ?? null;
}

/**
 * Compute the line total for a single item.
 *
 * @param {number} unitPrice - Server-authoritative unit price in VND.
 * @param {number} quantity  - Validated positive integer quantity.
 * @returns {number} Line total in VND.
 */
function calculateLineTotal(unitPrice, quantity) {
  return unitPrice * quantity;
}

/**
 * Reconstruct a complete, server-authoritative order from a validated items array.
 *
 * Ignores ALL client-supplied monetary values (price, unit_price, line_total,
 * total_amount, subtotal). Uses only item.id and item.quantity from the request.
 * All names and prices come exclusively from MENU.
 *
 * @param {Array<{ id: string, quantity: number }>} clientItems
 *   The items array from the validated request body.
 * @returns {{ items: Array, total: number } | { error: string }}
 *   On success: fully hydrated items array and the backend-computed total.
 *   On failure: an error string describing the unknown item id.
 */
function calculateOrder(clientItems) {
  let total = 0;
  const items = [];

  for (const clientItem of clientItems) {
    const id       = clientItem.id.trim();
    const quantity = clientItem.quantity;
    const menuItem = getMenuItem(id);

    if (!menuItem) {
      return { error: `Unknown menu item: "${id}". Please refresh the page and try again.` };
    }

    const unitPrice = menuItem.price;
    const lineTotal = calculateLineTotal(unitPrice, quantity);

    total += lineTotal;

    // Store the server-authoritative version of this line item.
    // Every monetary value and the item name come from MENU — never from the client.
    items.push({
      id,
      name:       menuItem.name,   // server name, not client-supplied
      quantity,
      unit_price: unitPrice,       // server price, not client-supplied
      line_total: lineTotal,       // server-computed, not client-supplied
    });
  }

  return { items, total };
}

// ── Idempotency helpers ───────────────────────────────────────────────────────

/**
 * Return true when a Supabase/PostgreSQL error is a unique constraint violation
 * caused specifically by the idempotency key index.
 *
 * PostgreSQL error code 23505 = unique_violation.
 * Supabase surfaces this as error.code === '23505'.
 *
 * Detection strategy (most-reliable first):
 *   1. error.constraint — Supabase/postgrest includes the constraint/index name
 *      as a dedicated field when available. Prefer this over string matching.
 *   2. error.message — fallback for environments or client versions that do not
 *      populate error.constraint but do include the index name in the message.
 *
 * @param {{ code?: string, constraint?: string, message?: string }} error
 * @returns {boolean}
 */
function isIdempotencyKeyViolation(error) {
  if (error?.code !== '23505') return false;

  // Prefer the structured constraint field when present.
  if (typeof error.constraint === 'string') {
    return error.constraint === 'idx_orders_idempotency_key';
  }

  // Fall back to message substring match.
  return typeof error.message === 'string' &&
    error.message.includes('idx_orders_idempotency_key');
}

/**
 * Fetch an existing order by its idempotency key.
 * Used only on the duplicate-recovery path (after a 23505 INSERT failure) —
 * never called on the normal insert path, so it adds zero latency to happy-path orders.
 *
 * Returns { id: string } if found, or null if not found.
 * Throws if the Supabase query itself fails.
 *
 * @param {string} key - The trimmed idempotency key from the request.
 * @returns {Promise<{ id: string } | null>}
 */
async function findOrderByIdempotencyKey(key) {
  const { data, error } = await supabase
    .from('orders')
    .select('id')
    .eq('idempotency_key', key)
    .single();

  if (error) throw error;
  return data;
}

// ── Request ID ────────────────────────────────────────────────────────────────

/** Maximum length accepted for a client-supplied X-Request-ID header. */
const REQUEST_ID_MAX_LENGTH = 128;

/**
 * Resolve the request ID for a given request.
 * Re-uses the client-supplied X-Request-ID header when present, non-empty,
 * and within the 128-character length limit (prevents log inflation attacks).
 * Falls back to a fresh UUID v4 generated server-side.
 *
 * @param {import('@vercel/node').VercelRequest} req
 * @returns {string}
 */
function resolveRequestId(req) {
  const forwarded = req.headers['x-request-id'];
  if (
    typeof forwarded === 'string' &&
    forwarded.trim().length > 0 &&
    forwarded.trim().length <= REQUEST_ID_MAX_LENGTH
  ) {
    return forwarded.trim();
  }
  return crypto.randomUUID();
}

// ── CORS ──────────────────────────────────────────────────────────────────────

const ALLOWED_ORIGINS = new Set([
  'https://banhcanhgahanggon.vercel.app', // production
  'http://localhost:3000',                // Vercel Dev CLI
  'http://localhost:8080',                // python -m http.server
  'http://127.0.0.1:8080',
  'http://localhost:5500',                // VS Code Live Server
  'http://127.0.0.1:5500',
]);

/**
 * Build CORS headers for a given request origin.
 * Origin is allowed only if it is on the allowlist.
 *
 * @param {string|undefined} origin
 * @returns {Object}
 */
function corsHeaders(origin) {
  const headers = {
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };

  if (origin && ALLOWED_ORIGINS.has(origin)) {
    headers['Access-Control-Allow-Origin'] = origin;
    headers['Vary'] = 'Origin';
  }

  return headers;
}

// ── Response helpers ──────────────────────────────────────────────────────────

/**
 * Write a JSON response with the given status code and optional extra headers.
 *
 * @param {import('@vercel/node').VercelResponse} res
 * @param {number} status
 * @param {Object} body
 * @param {Object} [extraHeaders]
 */
function jsonResponse(res, status, body, extraHeaders = {}) {
  res.setHeader('Content-Type', 'application/json');
  Object.entries(extraHeaders).forEach(([key, value]) => res.setHeader(key, value));
  res.status(status).json(body);
}

// ── Main handler ──────────────────────────────────────────────────────────────

/**
 * POST /api/order
 *
 * Request flow:
 *   1. Parse body
 *   2. Structural validation (validator.js)
 *   3. Server-side price reconstruction (calculateOrder)
 *      — client prices are silently discarded here
 *   4. Supabase INSERT (server-computed values only)
 *      — on 23505 from idx_orders_idempotency_key: fetch + return existing row
 *      — normal path: exactly one INSERT, zero SELECTs
 *   5. Notifications — Discord + ntfy (both non-blocking)
 *   6. HTTP 201 response
 *
 * @param {import('@vercel/node').VercelRequest} req
 * @param {import('@vercel/node').VercelResponse} res
 */
export default async function handler(req, res) {
  // Request context — created once, passed to every logger call.
  // startTime uses the monotonic hrtime clock so duration_ms is immune to
  // system clock adjustments and accurate to sub-millisecond resolution.
  const ctx = {
    startTime: process.hrtime.bigint(),
  };

  const requestId = resolveRequestId(req);
  const origin    = req.headers['origin'];
  const cors      = corsHeaders(origin);

  // Handle CORS preflight — no logging needed, not a real request.
  if (req.method === 'OPTIONS') {
    return jsonResponse(res, 204, {}, cors);
  }

  // Reject non-POST methods.
  if (req.method !== 'POST') {
    logger.warn('request_method_not_allowed', { request_id: requestId, method: req.method }, ctx);
    return jsonResponse(
      res,
      405,
      { success: false, error: 'Method not allowed. Use POST.' },
      { ...cors, Allow: 'POST, OPTIONS' }
    );
  }

  // ── 1. Parse request body ────────────────────────────────────────────────
  let body;
  try {
    body = typeof req.body === 'object' ? req.body : JSON.parse(req.body);
  } catch {
    logger.error('request_parse_failed', { request_id: requestId }, ctx);
    return jsonResponse(
      res,
      400,
      { success: false, error: 'Invalid JSON in request body.' },
      cors
    );
  }

  // ── 2. Structural validation ─────────────────────────────────────────────
  // Checks required fields, types, lengths, phone format, duplicate ids.
  // Does NOT validate monetary values — those are ignored and recomputed below.
  const { valid, errors } = validateOrderPayload(body);
  if (!valid) {
    logger.warn('validation_failed', { request_id: requestId, error_count: errors.length, errors }, ctx);
    return jsonResponse(
      res,
      400,
      { success: false, error: 'Validation failed.', details: errors },
      cors
    );
  }

  // ── 3. Server-side price reconstruction ─────────────────────────────────
  // calculateOrder uses ONLY item.id and item.quantity from the request.
  // All prices, names, line totals, and the order total are computed from
  // the server-side MENU constant. body.total_amount is NEVER used.
  const orderCalc = calculateOrder(body.items);

  if (orderCalc.error) {
    logger.warn('unknown_menu_item', { request_id: requestId, detail: orderCalc.error }, ctx);
    return jsonResponse(
      res,
      400,
      { success: false, error: orderCalc.error },
      cors
    );
  }

  // orderCalc.items  — server-authoritative line items (name + prices from MENU)
  // orderCalc.total  — server-computed grand total (never from body.total_amount)

  // ── 4. Insert into Supabase ──────────────────────────────────────────────
  if (!supabase) {
    logger.error('supabase_not_initialised', { request_id: requestId }, ctx);
    return jsonResponse(
      res,
      500,
      { success: false, error: 'Service temporarily unavailable. Please try again later.' },
      cors
    );
  }

  // Build the record from server-authoritative values only.
  // Business logic (validation, price calculation) is complete at this point.
  // Everything below is persistence — the only place try/catch is needed.
  const orderRecord = {
    customer_name:   body.customer_name.trim(),
    phone:           body.phone.trim(),
    order_type:      body.order_type,
    address:         body.order_type === 'delivery' ? (body.address ?? '').trim() : null,
    items:           orderCalc.items,  // server-computed — no client data
    total_amount:    orderCalc.total,  // server-computed — body.total_amount ignored
    note:            body.note ? body.note.trim() : null,
    ...(body.payment_method ? { payment_method: body.payment_method.trim() } : {}),
    status:          'pending',
    idempotency_key: body.idempotency_key.trim(),
  };

  let inserted;
  try {
    const { data, error: dbError } = await supabase
      .from('orders')
      .insert(orderRecord)
      .select('id, created_at')
      .single();

    if (dbError) {
      // Duplicate key on idx_orders_idempotency_key: a concurrent request with
      // the same key already committed. Fetch and return that row — one SELECT
      // only, triggered solely by the 23505 on this specific index.
      if (isIdempotencyKeyViolation(dbError)) {
        try {
          const existing = await findOrderByIdempotencyKey(body.idempotency_key.trim());
          if (existing) {
            logger.info('order_duplicate', { request_id: requestId, order_id: existing.id, duplicated: true }, ctx);
            return jsonResponse(res, 200, {
              success:    true,
              duplicated: true,
              orderId:    existing.id,
              message:    'Order already exists.',
            }, cors);
          }
        } catch (fetchError) {
          logger.error('duplicate_recovery_failed', { request_id: requestId, message: fetchError.message }, ctx);
        }
        return jsonResponse(res, 500, { success: false, error: 'Failed to save your order. Please try again.' }, cors);
      }

      // Any other database error — log and surface a clean 500.
      logger.error('supabase_insert_failed', {
        request_id: requestId,
        error_code: dbError.code,
        constraint: dbError.constraint ?? null,
        message:    dbError.message,
      }, ctx);
      return jsonResponse(res, 500, { success: false, error: 'Failed to save your order. Please try again.' }, cors);
    }

    inserted = data;
  } catch (unexpectedError) {
    // Network-level or unexpected runtime error from the Supabase client.
    logger.error('persistence_exception', {
      request_id: requestId,
      message:    unexpectedError.message,
      stack:      unexpectedError.stack,
    }, ctx);
    return jsonResponse(res, 500, { success: false, error: 'Failed to save your order. Please try again.' }, cors);
  }

  // ── 5. Notifications (non-blocking — failures never affect the response) ──
  // fullOrder uses orderCalc.items and orderCalc.total — fully server-generated.
  const fullOrder = { ...orderRecord, id: inserted.id, created_at: inserted.created_at };

  /**
   * Log the outcome of a single notification provider.
   * Handles both fulfilled results ({ success, error? }) and rejected promises.
   *
   * @param {'discord'|'ntfy'} provider
   * @param {PromiseSettledResult} settled - One element from Promise.allSettled().
   */
  function logNotification(provider, settled) {
    const sentEvent   = `${provider}_sent`;
    const failedEvent = `${provider}_failed`;
    const base        = { request_id: requestId, order_id: inserted.id };

    if (settled.status === 'fulfilled' && settled.value.success) {
      logger.info(sentEvent, base, ctx);
    } else {
      const error = settled.status === 'rejected'
        ? settled.reason?.message ?? 'Unknown error'
        : settled.value.error;
      logger.warn(failedEvent, { ...base, error }, ctx);
    }
  }

  // Fire both notifications concurrently.
  // Array order is documented here and must match the destructuring below.
  const [discordResult, ntfyResult] = await Promise.allSettled([
    sendDiscordNotification(fullOrder), // index 0 → discordResult
    sendNtfyNotification(fullOrder),    // index 1 → ntfyResult
  ]);

  logNotification('discord', discordResult);
  logNotification('ntfy',    ntfyResult);

  const ntfyResultValue = ntfyResult.status === 'fulfilled' ? ntfyResult.value : { success: false, error: ntfyResult.reason?.message };
  console.log('NTFY RESULT:', JSON.stringify(ntfyResultValue));

  // ── 6. Respond ───────────────────────────────────────────────────────────
  logger.info('order_created', {
    request_id:   requestId,
    order_id:     inserted.id,
    order_type:   orderRecord.order_type,
    total_amount: orderRecord.total_amount,
    item_count:   orderRecord.items.length,
    duplicated:   false,
  }, ctx);

  const response = {
    success: true,
    orderId: inserted.id,
    message: 'Order created successfully.',
  };

  // Surface a client-visible warning if Discord (the primary channel) failed.
  const discordOk = discordResult.status === 'fulfilled' && discordResult.value.success;
  if (!discordOk) {
    response.warning = 'Order saved. Notification delivery was delayed — the team has been alerted.';
  }

  return jsonResponse(res, 201, response, cors);
}
