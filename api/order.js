import supabase from '../lib/supabase.js';
import { sendDiscordNotification } from '../lib/discord.js';
import { validateOrderPayload } from '../lib/validator.js';

/**
 * Server-side price catalogue.
 * Keys match the item `id` values in order.html's menuItems array.
 * Prices are in VND (integer). The client MUST NOT be trusted for prices.
 */
const MENU_PRICES = {
  'bc-xe':       50000,
  'bc-chat':     60000,
  'bc-dac-biet': 70000,
  'xoi-xe':      45000,
  'xoi-chat':    50000,
};

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
 * Build CORS headers. Allow the request origin if it is on the allowlist;
 * otherwise omit the Access-Control-Allow-Origin header (browser will block).
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
 * Send a JSON response.
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

// ── Price reconciliation ──────────────────────────────────────────────────────

/**
 * Recalculate the order total from server-authoritative prices.
 * Attaches `unit_price` to each item for storage and Discord formatting.
 * Returns null if any item id is unrecognised.
 *
 * @param {Array<{ id: string, name: string, quantity: number }>} items
 * @returns {{ reconciledItems: Array, serverTotal: number } | null}
 */
function reconcilePrices(items) {
  let serverTotal = 0;
  const reconciledItems = [];

  for (const item of items) {
    const unitPrice = MENU_PRICES[item.id];
    if (unitPrice === undefined) {
      console.warn(`[order] Unknown item id in request: "${item.id}"`);
      return null;
    }
    const lineTotal = unitPrice * item.quantity;
    serverTotal += lineTotal;
    reconciledItems.push({ ...item, unit_price: unitPrice, line_total: lineTotal });
  }

  return { reconciledItems, serverTotal };
}

// ── Main handler ──────────────────────────────────────────────────────────────

/**
 * POST /api/order
 *
 * Accepts an order payload, validates it, inserts into Supabase,
 * sends a Discord notification, and returns a JSON response.
 *
 * @param {import('@vercel/node').VercelRequest} req
 * @param {import('@vercel/node').VercelResponse} res
 */
export default async function handler(req, res) {
  const origin = req.headers['origin'];
  const cors = corsHeaders(origin);

  // Handle CORS preflight
  if (req.method === 'OPTIONS') {
    return jsonResponse(res, 204, {}, cors);
  }

  // Reject non-POST methods
  if (req.method !== 'POST') {
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
    return jsonResponse(
      res,
      400,
      { success: false, error: 'Invalid JSON in request body.' },
      cors
    );
  }

  // ── 2. Validate ──────────────────────────────────────────────────────────
  const { valid, errors } = validateOrderPayload(body);
  if (!valid) {
    return jsonResponse(
      res,
      400,
      { success: false, error: 'Validation failed.', details: errors },
      cors
    );
  }

  // ── 3. Reconcile prices (server-authoritative) ───────────────────────────
  const priceResult = reconcilePrices(body.items);
  if (!priceResult) {
    return jsonResponse(
      res,
      400,
      { success: false, error: 'One or more items are not recognised. Please refresh the page and try again.' },
      cors
    );
  }
  const { reconciledItems, serverTotal } = priceResult;

  // ── 4. Insert into Supabase ──────────────────────────────────────────────
  if (!supabase) {
    console.error('[order] Supabase client is not initialised — check environment variables');
    return jsonResponse(
      res,
      500,
      { success: false, error: 'Service temporarily unavailable. Please try again later.' },
      cors
    );
  }

  const orderRecord = {
    customer_name: body.customer_name.trim(),
    phone:         body.phone.trim(),
    order_type:    body.order_type,
    address:       body.order_type === 'delivery' ? (body.address ?? '').trim() : null,
    items:         reconciledItems,
    total_amount:  serverTotal,
    note:          body.note ? body.note.trim() : null,
    payment_method: body.payment_method ? body.payment_method.trim() : null,
    status:        'pending',
  };

  const { data: inserted, error: dbError } = await supabase
    .from('orders')
    .insert(orderRecord)
    .select('id, created_at')
    .single();

  if (dbError) {
    console.error('[order] Supabase insert error:', dbError.message);
    return jsonResponse(
      res,
      500,
      { success: false, error: 'Failed to save your order. Please try again.' },
      cors
    );
  }

  // ── 5. Send Discord notification (non-blocking on failure) ───────────────
  const fullOrder = { ...orderRecord, id: inserted.id, created_at: inserted.created_at };
  const discordResult = await sendDiscordNotification(fullOrder);

  if (!discordResult.success) {
    console.warn(`[order] Discord notification failed for order ${inserted.id}: ${discordResult.error}`);
  }

  // ── 6. Respond ───────────────────────────────────────────────────────────
  const response = {
    success: true,
    orderId: inserted.id,
    message: 'Order created successfully.',
  };

  if (!discordResult.success) {
    response.warning = 'Order saved. Notification delivery was delayed — the team has been alerted.';
  }

  return jsonResponse(res, 201, response, cors);
}
