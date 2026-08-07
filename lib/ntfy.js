/** Maximum time (ms) to wait for the ntfy server before giving up. */
const NTFY_TIMEOUT_MS = 2000;

/**
 * Format a Vietnamese price integer as a localised currency string.
 *
 * @param {number} value - Amount in VND (integer).
 * @returns {string} e.g. "155.000 VNĐ"
 */
function formatPrice(value) {
  return `${value.toLocaleString('vi-VN')} VNĐ`;
}

/**
 * Build the plain-text notification body for an order.
 * ntfy notifications are plain text — no markdown, no HTML.
 *
 * @param {Object} order - The fully-hydrated order record from Supabase.
 * @returns {string}
 */
function buildNtfyBody(order) {
  const isDelivery = order.order_type === 'delivery';

  const itemLines = Array.isArray(order.items) && order.items.length > 0
    ? order.items.map(item => `• ${item.name} × ${item.quantity}`).join('\n')
    : '(không có thông tin món)';

  const lines = [
    'ĐƠN ĐẶT MỚI',
    '',
    `Khách: ${order.customer_name ?? '—'}`,
    `Điện thoại: ${order.phone ?? '—'}`,
    `Nhận: ${isDelivery ? 'Giao hàng' : 'Đến lấy tại quán'}`,
  ];

  if (isDelivery && order.address) {
    lines.push(`Địa chỉ: ${order.address}`);
  }

  lines.push('', 'Món:', itemLines, '', `Tổng: ${formatPrice(order.total_amount ?? 0)}`);

  return lines.join('\n');
}

/**
 * Send a new-order push notification to the configured ntfy topic.
 *
 * CONTRACT: this function NEVER throws. It always returns a result object.
 * The caller (api/order.js) treats failure as a non-blocking warning and
 * must never affect the HTTP response because of an ntfy error.
 *
 * Environment variable required:
 *   NTFY_TOPIC — the ntfy topic name, e.g. "banhcanhhanggon"
 *
 * @param {Object} order - The order record as built in api/order.js.
 * @returns {Promise<{ success: boolean, error?: string }>}
 */
export async function sendNtfyNotification(order) {
  const topic = process.env.NTFY_TOPIC;

  if (!topic) {
    return { success: false, error: 'NTFY_TOPIC is not configured' };
  }

  const body    = buildNtfyBody(order);
  const baseUrl = process.env.NTFY_BASE_URL ?? 'https://ntfy.sh';
  const url     = `${baseUrl}/${encodeURIComponent(topic)}`;

  const controller = new AbortController();
  const timeoutId  = setTimeout(() => controller.abort(), NTFY_TIMEOUT_MS);

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain; charset=utf-8',
        'Title':        '🍜 Đơn hàng mới',
        'Priority':     'urgent',
        'Tags':         'shopping_cart,restaurant',
      },
      body:   body,
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      // Read the response body — ntfy includes a human-readable reason string
      // (e.g. "rate limit exceeded", "topic name too long") that is essential
      // for diagnosing failures. Failure to read the body is non-fatal.
      const detail = await response.text().catch(() => '');
      const error  = detail.trim()
        ? `ntfy error ${response.status}: ${detail.trim()}`
        : `ntfy error ${response.status}`;
      return { success: false, error };
    }

    return { success: true };

  } catch (err) {
    clearTimeout(timeoutId);

    // Build a reason string that preserves both the error class name and the
    // message, giving operators immediately actionable information:
    //   AbortError: The operation was aborted        → timeout
    //   TypeError: fetch failed                      → DNS / TLS / connection
    //   Error: socket hang up                        → mid-stream disconnect
    // Using instanceof Error guards against non-Error throws (strings, etc.).
    const reason = err instanceof Error
      ? `${err.name}: ${err.message}`
      : String(err);

    return { success: false, error: `ntfy network error: ${reason}` };
  }
}
