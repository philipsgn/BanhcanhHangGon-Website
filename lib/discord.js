const DISCORD_WEBHOOK_URL = process.env.DISCORD_WEBHOOK_URL;

/** Maximum time (ms) to wait for the Discord webhook before giving up. */
const DISCORD_TIMEOUT_MS = 5000;

/**
 * Format a Vietnamese price integer as a localised string.
 * @param {number} value - Amount in VND (integer).
 * @returns {string} e.g. "50.000 VND"
 */
function formatPrice(value) {
  return `${value.toLocaleString('vi-VN')} VND`;
}

/**
 * Build the Discord embed fields from an order record.
 * @param {Object} order - The order as stored in Supabase.
 * @returns {Object} Discord message payload.
 */
function buildDiscordPayload(order) {
  const isDelivery = order.order_type === 'delivery';

  // Format each line item
  const itemLines = Array.isArray(order.items)
    ? order.items
        .map(item => `• ${item.name} × ${item.quantity}  —  ${formatPrice(item.unit_price * item.quantity)}`)
        .join('\n')
    : 'Không có thông tin món';

  const createdAt = order.created_at
    ? new Date(order.created_at).toLocaleString('vi-VN', {
        timeZone: 'Asia/Ho_Chi_Minh',
        hour: '2-digit',
        minute: '2-digit',
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
      })
    : 'N/A';

  const lines = [
    `**👤 Khách hàng:** ${order.customer_name}`,
    `**📞 Số điện thoại:** ${order.phone}`,
    `**🛵 Hình thức:** ${isDelivery ? 'Giao hàng' : 'Đến lấy tại quán'}`,
  ];

  if (isDelivery && order.address) {
    lines.push(`**📍 Địa chỉ:** ${order.address}`);
  }

  lines.push(`\n**🧾 Món đặt:**\n${itemLines}`);
  lines.push(`\n**💰 Tổng cộng:** ${formatPrice(order.total_amount)}`);

  if (order.note) {
    lines.push(`**📝 Ghi chú:** ${order.note}`);
  }

  if (order.payment_method) {
    lines.push(`**💳 Thanh toán:** ${order.payment_method}`);
  }

  lines.push(`\n**🕐 Thời gian:** ${createdAt}`);

  return {
    content: null,
    embeds: [
      {
        title: '🍜 ĐƠN ĐẶT MÓN MỚI',
        description: lines.join('\n'),
        color: 0xc99a4a, // brand gold
        footer: {
          text: `Mã đơn: ${order.id ?? 'N/A'} · Bánh Canh Gà Hàng Gòn`,
        },
      },
    ],
  };
}

/**
 * Send an order notification to the configured Discord webhook.
 * This function NEVER throws. It returns a result object so the caller
 * can decide whether to surface a warning without crashing the API.
 *
 * @param {Object} order - The order record (as returned from Supabase).
 * @returns {Promise<{ success: boolean, error?: string }>}
 */
export async function sendDiscordNotification(order) {
  if (!DISCORD_WEBHOOK_URL) {
    console.warn('[discord] DISCORD_WEBHOOK_URL is not set — skipping notification');
    return { success: false, error: 'Webhook URL not configured' };
  }

  const payload = buildDiscordPayload(order);

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), DISCORD_TIMEOUT_MS);

  try {
    const response = await fetch(DISCORD_WEBHOOK_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      const body = await response.text().catch(() => '');
      console.error(`[discord] Webhook responded with ${response.status}: ${body}`);
      return { success: false, error: `Webhook error ${response.status}` };
    }

    return { success: true };
  } catch (err) {
    clearTimeout(timeoutId);

    if (err.name === 'AbortError') {
      console.error('[discord] Webhook request timed out');
      return { success: false, error: 'Webhook timed out' };
    }

    console.error('[discord] Network error sending webhook:', err.message);
    return { success: false, error: 'Network error' };
  }
}
