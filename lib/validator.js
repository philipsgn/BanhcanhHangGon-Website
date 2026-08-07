/** Accepted order types — must match the frontend fulfillment select values. */
const VALID_ORDER_TYPES = new Set(['pickup', 'delivery']);

/** Maximum character lengths for string fields. */
const MAX_LENGTHS = {
  customer_name:  100,
  phone:          30,
  address:        300,
  note:           500,
  payment_method: 50,
};

/**
 * Maximum number of distinct line items in a single order.
 * Mirrors the frontend cap and the DB check.
 */
const MAX_ITEMS = 20;

/**
 * Maximum quantity per line item.
 * Set to 50 — a reasonable upper bound for a single restaurant order.
 */
const MAX_ITEM_QUANTITY = 50;

/**
 * Validate the raw request body for POST /api/order.
 *
 * Pricing fields (total_amount, unit_price, line_total, item name) are
 * accepted but NOT trusted — the pricing layer in api/order.js discards
 * them and recomputes everything server-side. Validation here only checks
 * structural integrity and the fields the server actually uses.
 *
 * @param {unknown} body - Parsed JSON from the request.
 * @returns {{ valid: boolean, errors: string[] }}
 */
export function validateOrderPayload(body) {
  const errors = [];

  if (!body || typeof body !== 'object' || Array.isArray(body)) {
    return { valid: false, errors: ['Request body must be a JSON object'] };
  }

  // ── customer_name ────────────────────────────────────────────────────────
  if (!body.customer_name || typeof body.customer_name !== 'string') {
    errors.push('customer_name is required');
  } else if (body.customer_name.trim().length === 0) {
    errors.push('customer_name cannot be blank');
  } else if (body.customer_name.trim().length > MAX_LENGTHS.customer_name) {
    errors.push(`customer_name must be at most ${MAX_LENGTHS.customer_name} characters`);
  }

  // ── phone ─────────────────────────────────────────────────────────────────
  if (!body.phone || typeof body.phone !== 'string') {
    errors.push('phone is required');
  } else {
    const trimmed = body.phone.trim();
    if (trimmed.length === 0) {
      errors.push('phone cannot be blank');
    } else if (trimmed.length > MAX_LENGTHS.phone) {
      errors.push(`phone must be at most ${MAX_LENGTHS.phone} characters`);
    } else if (!/^[+\d][\d\s().\-]{7,}$/.test(trimmed)) {
      errors.push('phone is not a valid phone number format');
    }
  }

  // ── order_type ────────────────────────────────────────────────────────────
  if (!body.order_type || typeof body.order_type !== 'string') {
    errors.push('order_type is required');
  } else if (!VALID_ORDER_TYPES.has(body.order_type)) {
    errors.push(`order_type must be one of: ${[...VALID_ORDER_TYPES].join(', ')}`);
  }

  // ── address (required only for delivery) ─────────────────────────────────
  const isDelivery = body.order_type === 'delivery';
  if (isDelivery) {
    if (!body.address || typeof body.address !== 'string' || body.address.trim().length === 0) {
      errors.push('address is required for delivery orders');
    } else if (body.address.trim().length > MAX_LENGTHS.address) {
      errors.push(`address must be at most ${MAX_LENGTHS.address} characters`);
    }
  }

  // ── items ─────────────────────────────────────────────────────────────────
  if (!Array.isArray(body.items)) {
    errors.push('items must be an array');
  } else if (body.items.length === 0) {
    errors.push('items cannot be empty — at least one item is required');
  } else if (body.items.length > MAX_ITEMS) {
    errors.push(`items cannot exceed ${MAX_ITEMS} distinct items`);
  } else {
    // Duplicate id detection — O(n) with a Set.
    const seenIds = new Set();

    body.items.forEach((item, index) => {
      const prefix = `items[${index}]`;

      if (!item || typeof item !== 'object' || Array.isArray(item)) {
        errors.push(`${prefix} must be an object`);
        return;
      }

      // id — the only field the pricing layer needs from each item.
      if (!item.id || typeof item.id !== 'string' || item.id.trim().length === 0) {
        errors.push(`${prefix}.id is required`);
      } else {
        const trimmedId = item.id.trim();
        if (seenIds.has(trimmedId)) {
          errors.push(`${prefix}.id "${trimmedId}" is duplicated — each item must appear once`);
        } else {
          seenIds.add(trimmedId);
        }
      }

      // quantity — must be a positive integer within bounds.
      if (
        typeof item.quantity !== 'number' ||
        !Number.isInteger(item.quantity) ||
        item.quantity < 1
      ) {
        errors.push(`${prefix}.quantity must be a positive integer (minimum 1)`);
      } else if (item.quantity > MAX_ITEM_QUANTITY) {
        errors.push(`${prefix}.quantity cannot exceed ${MAX_ITEM_QUANTITY}`);
      }

      // name, unit_price, line_total, price — intentionally NOT validated.
      // These fields are ignored by the pricing layer; the server looks up
      // all monetary values from the server-side MENU catalogue in api/order.js.
    });
  }

  // ── total_amount ──────────────────────────────────────────────────────────
  // Accepted for backward compatibility (frontend sends it) but the value is
  // NEVER used for any calculation. The backend computes its own total.
  // We validate structure only so malformed payloads are caught early.
  if (body.total_amount === undefined || body.total_amount === null) {
    errors.push('total_amount is required');
  } else if (
    typeof body.total_amount !== 'number' ||
    !Number.isInteger(body.total_amount) ||
    body.total_amount <= 0
  ) {
    errors.push('total_amount must be a positive integer (VND)');
  }

  // ── note (optional) ───────────────────────────────────────────────────────
  if (body.note !== undefined && body.note !== null) {
    if (typeof body.note !== 'string') {
      errors.push('note must be a string');
    } else if (body.note.length > MAX_LENGTHS.note) {
      errors.push(`note must be at most ${MAX_LENGTHS.note} characters`);
    }
  }

  // ── payment_method (optional) ─────────────────────────────────────────────
  if (body.payment_method !== undefined && body.payment_method !== null) {
    if (typeof body.payment_method !== 'string') {
      errors.push('payment_method must be a string');
    } else if (body.payment_method.length > MAX_LENGTHS.payment_method) {
      errors.push(`payment_method must be at most ${MAX_LENGTHS.payment_method} characters`);
    }
  }

  // ── idempotency_key ───────────────────────────────────────────────────────
  // Required. Must be a non-empty string up to 100 characters.
  // Format is not enforced here — any unique token generated by the client
  // is acceptable. The database UNIQUE index is the source of truth.
  if (!body.idempotency_key || typeof body.idempotency_key !== 'string') {
    errors.push('idempotency_key is required');
  } else if (body.idempotency_key.trim().length === 0) {
    errors.push('idempotency_key cannot be blank');
  } else if (body.idempotency_key.trim().length > 100) {
    errors.push('idempotency_key must be at most 100 characters');
  }

  return { valid: errors.length === 0, errors };
}
