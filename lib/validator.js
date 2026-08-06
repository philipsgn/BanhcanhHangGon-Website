/** Accepted order types — must match the frontend fulfillment select values. */
const VALID_ORDER_TYPES = new Set(['pickup', 'delivery']);

/** Accepted payment methods. Empty string is allowed (optional field). */
const VALID_PAYMENT_METHODS = new Set(['cash', 'transfer', '']);

/** Maximum character lengths for string fields. */
const MAX_LENGTHS = {
  customer_name: 100,
  phone: 30,
  address: 300,
  note: 500,
  payment_method: 50,
};

/** Maximum number of distinct items in a single order. */
const MAX_ITEMS = 20;

/** Maximum quantity per line item. */
const MAX_ITEM_QUANTITY = 99;

/**
 * Validate the raw request body for the POST /api/order endpoint.
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
    body.items.forEach((item, index) => {
      const prefix = `items[${index}]`;

      if (!item || typeof item !== 'object') {
        errors.push(`${prefix} must be an object`);
        return;
      }

      if (!item.id || typeof item.id !== 'string' || item.id.trim().length === 0) {
        errors.push(`${prefix}.id is required`);
      }

      if (!item.name || typeof item.name !== 'string' || item.name.trim().length === 0) {
        errors.push(`${prefix}.name is required`);
      }

      if (
        typeof item.quantity !== 'number' ||
        !Number.isInteger(item.quantity) ||
        item.quantity < 1
      ) {
        errors.push(`${prefix}.quantity must be a positive integer`);
      } else if (item.quantity > MAX_ITEM_QUANTITY) {
        errors.push(`${prefix}.quantity cannot exceed ${MAX_ITEM_QUANTITY}`);
      }
    });
  }

  // ── total_amount ──────────────────────────────────────────────────────────
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

  return { valid: errors.length === 0, errors };
}
