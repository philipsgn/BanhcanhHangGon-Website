/** Maximum time (ms) to wait for the Discord webhook before giving up. */
const DISCORD_TIMEOUT_MS = 5000;

/** Embed accent colour — Dark Orange per brand spec. */
const EMBED_COLOR = 0xD97706;

/**
 * Format a Vietnamese price integer as a localised currency string.
 *
 * Uses vi-VN locale with period thousand-separators, no decimal places,
 * and the "VNĐ" suffix required by the embed spec.
 *
 * @param {number} value - Amount in VND (integer).
 * @returns {string} e.g. "260.000 VNĐ"
 */
function formatPrice(value) {
  return `${value.toLocaleString('vi-VN')} VNĐ`;
}

/**
 * Escape characters that have special meaning inside Discord embed field
 * values so that user-supplied strings cannot inject markdown formatting.
 *
 * Escaped: backtick, asterisk, underscore, tilde, pipe, >
 *
 * @param {string} text
 * @returns {string}
 */
function escapeMarkdown(text) {
  if (typeof text !== 'string') return String(text ?? '');
  return text.replace(/([`*_~|>\\])/g, '\\$1');
}

/**
 * Build the structured Discord embed payload for a new order.
 *
 * Uses Discord's native embed `fields` array (not a flat description string)
 * so each piece of information sits in its own labelled cell — this renders
 * cleanly in both the desktop sidebar and the mobile full-screen view.
 *
 * Field layout (in order):
 *   👤 Khách hàng        📞 Điện thoại         (inline pair — row 1)
 *   🚚 Hình thức nhận   📍 Địa chỉ             (inline pair — row 2)
 *   🍲 Danh sách món                            (full-width)
 *   💰 Tổng tiền        🟡 Trạng thái          (inline pair — row 3)
 *
 * @param {Object} order - The fully-hydrated order record from Supabase.
 * @returns {Object} Complete Discord webhook message payload.
 */
function buildDiscordPayload(order) {
  const isDelivery = order.order_type === 'delivery';

  // ── Item list ────────────────────────────────────────────────────────────
  // One bullet per line, name × quantity only (no prices per spec).
  const itemLines = Array.isArray(order.items) && order.items.length > 0
    ? order.items
        .map(item => `• ${escapeMarkdown(item.name)} × ${item.quantity}`)
        .join('\n')
    : '_(không có thông tin món)_';

  // Guard against Discord's 1024-char field value limit.
  const safeItemLines = itemLines.length > 1024
    ? itemLines.slice(0, 1000) + '\n…_(danh sách bị cắt bớt)_'
    : itemLines;

  // ── Address ──────────────────────────────────────────────────────────────
  // Pickup → em dash  |  Delivery → actual address (escaped)
  const addressValue = isDelivery && order.address
    ? escapeMarkdown(order.address.trim())
    : '—';

  // ── Timestamp ────────────────────────────────────────────────────────────
  // Pass created_at as an ISO string; Discord renders it in the viewer's
  // local timezone automatically. Fallback to current time if absent.
  const isoTimestamp = order.created_at
    ? new Date(order.created_at).toISOString()
    : new Date().toISOString();

  // ── Fields array ─────────────────────────────────────────────────────────
  const fields = [
    {
      name:   '👤 Khách hàng',
      value:  escapeMarkdown(order.customer_name ?? '—'),
      inline: true,
    },
    {
      name:   '📞 Điện thoại',
      value:  escapeMarkdown(order.phone ?? '—'),
      inline: true,
    },
    {
      name:   '🚚 Hình thức nhận',
      value:  isDelivery ? 'Giao hàng' : 'Đến lấy tại quán',
      inline: true,
    },
    {
      name:   '📍 Địa chỉ',
      value:  addressValue,
      inline: true,
    },
    {
      // Full-width — Discord renders a field as full-width when it follows
      // two consecutive inline fields that already fill a row, or when
      // inline is false. Explicitly false here for clarity.
      name:   '🍲 Danh sách món',
      value:  safeItemLines,
      inline: false,
    },
    {
      name:   '💰 Tổng tiền',
      value:  formatPrice(order.total_amount ?? 0),
      inline: true,
    },
    {
      name:   '🟡 Trạng thái',
      value:  'Pending',
      inline: true,
    },
  ];

  return {
    // No plain-text content — embed carries all information.
    content: null,
    embeds: [
      {
        title:     '🍜 ĐƠN ĐẶT MỚI',
        color:     EMBED_COLOR,
        fields,
        footer:    { text: 'Bánh Canh Gà Hàng Gòn' },
        timestamp: isoTimestamp,
      },
    ],
  };
}

/**
 * Send a new-order notification to the configured Discord webhook.
 *
 * CONTRACT: this function NEVER throws. It always returns a result object.
 * The caller (api/order.js) can log a warning on failure but must never
 * block or fail the HTTP response because of a Discord error.
 *
 * @param {Object} order - The order record as built in api/order.js.
 * @returns {Promise<{ success: boolean, error?: string }>}
 */
export async function sendDiscordNotification(order) {
  // Read env var at call time so the function is easier to test and so a
  // misconfiguration is surfaced on the first real request, not at module load.
  const webhookUrl = process.env.DISCORD_WEBHOOK_URL;

  if (!webhookUrl) {
    console.warn('[discord] DISCORD_WEBHOOK_URL is not set — skipping notification');
    return { success: false, error: 'Webhook URL not configured' };
  }

  const payload = buildDiscordPayload(order);

  const controller = new AbortController();
  const timeoutId  = setTimeout(() => controller.abort(), DISCORD_TIMEOUT_MS);

  try {
    const response = await fetch(webhookUrl, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(payload),
      signal:  controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      // Read the body for logging only — never forwarded to the client.
      const detail = await response.text().catch(() => '');
      console.error(`[discord] Webhook responded with HTTP ${response.status}: ${detail}`);
      return { success: false, error: `Webhook error ${response.status}` };
    }

    return { success: true };

  } catch (err) {
    clearTimeout(timeoutId);

    if (err.name === 'AbortError') {
      console.error('[discord] Webhook request timed out after', DISCORD_TIMEOUT_MS, 'ms');
      return { success: false, error: 'Webhook timed out' };
    }

    console.error('[discord] Network error sending webhook:', err.message);
    return { success: false, error: 'Network error' };
  }
}
