/**
 * lib/ntfy.js — ntfy push notification client.
 *
 * Sends a plain-text order notification to a configured ntfy topic.
 * This module is a pure network client:
 *   - never throws
 *   - always returns { success, error? }
 *   - has no side effects beyond the HTTP request
 *   - does not call the application logger (no request_id available here;
 *     the caller in api/order.js owns structured logging)
 *
 * Encoding:
 *   Request body → TextEncoder → Uint8Array → fetch body (BufferSource path).
 *   This bypasses the ByteString conversion that rejects code points > U+00FF.
 *   HTTP header values are ASCII-only for the same reason.
 */

// ── Configuration ─────────────────────────────────────────────────────────────

/**
 * Default timeout (ms) when NTFY_TIMEOUT_MS env var is not set.
 * Kept deliberately short — notifications are best-effort side effects.
 */
const DEFAULT_TIMEOUT_MS = 2000;

/**
 * HTTP status codes that represent transient server-side failures.
 * These are safe to retry. 4xx errors (except 408/429) are never retried
 * because retrying a bad request or an auth failure is pointless.
 */
const RETRYABLE_STATUSES = new Set([408, 429, 500, 502, 503, 504]);

/** Maximum number of delivery attempts (1 initial + N-1 retries). */
const MAX_ATTEMPTS = 3;

/** Base delay (ms) for exponential backoff between retries. */
const BACKOFF_BASE_MS = 200;

// ── Shared instances ──────────────────────────────────────────────────────────

/**
 * Module-level TextEncoder instance.
 * TextEncoder.encode() produces a Uint8Array of UTF-8 bytes.
 * Passing a Uint8Array as the fetch body uses the BufferSource code path,
 * which never triggers the ByteString conversion that throws for code points > 255.
 */
const encoder = new TextEncoder();

// ── Helpers ───────────────────────────────────────────────────────────────────

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
 * Build the plain-text notification body.
 * All Unicode (emoji, Vietnamese diacritics) is safe here because the string
 * is passed through TextEncoder before being given to fetch.
 *
 * @param {Object} order
 * @returns {string}
 */
function buildNtfyBody(order) {
  const isDelivery = order.order_type === 'delivery';

  const itemLines = Array.isArray(order.items) && order.items.length > 0
    ? order.items.map(item => `• ${item.name} × ${item.quantity}`).join('\n')
    : '(không có thông tin món)';

  const lines = [
    '🍜 ĐƠN ĐẶT MỚI',
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
 * Return true for HTTP status codes that warrant a retry.
 * Client errors (400, 401, 403, 404, …) are never retried.
 *
 * @param {number} status
 * @returns {boolean}
 */
function isRetryableStatus(status) {
  return RETRYABLE_STATUSES.has(status);
}

/**
 * Resolve the per-request timeout from the environment.
 * Falls back to DEFAULT_TIMEOUT_MS if the env var is absent or non-numeric.
 *
 * @returns {number} Timeout in milliseconds.
 */
function resolveTimeout() {
  const raw = parseInt(process.env.NTFY_TIMEOUT_MS ?? '', 10);
  return Number.isFinite(raw) && raw > 0 ? raw : DEFAULT_TIMEOUT_MS;
}

/**
 * Return the base URL for the ntfy server.
 * Reads NTFY_BASE_URL; defaults to the public ntfy.sh instance.
 *
 * @returns {string}
 */
function resolveBaseUrl() {
  return process.env.NTFY_BASE_URL?.trim() || 'https://ntfy.sh';
}

/**
 * Sleep for `ms` milliseconds. Used for retry backoff.
 *
 * @param {number} ms
 * @returns {Promise<void>}
 */
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Send one HTTP attempt to ntfy. Returns the fetch Response on any HTTP
 * reply (including non-2xx) and throws only on network/abort errors.
 *
 * @param {string}      url
 * @param {Uint8Array}  bodyBytes
 * @param {number}      timeoutMs
 * @returns {Promise<Response>}
 */
async function attempt(url, bodyBytes, timeoutMs) {
  const controller = new AbortController();
  const timeoutId  = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        // charset=utf-8 matches the TextEncoder-produced body bytes.
        'Content-Type': 'text/plain; charset=utf-8',
        // Canonical ntfy header names (https://docs.ntfy.sh/publish/).
        // X-* aliases are also accepted but these are the primary documented forms.
        // Values must remain ASCII-only — the Fetch spec applies ByteString
        // conversion to header values in some runtimes, rejecting code points > 255.
        'Title':    'Don hang moi',
        'Priority': 'urgent',
        'Tags':     'shopping_cart,restaurant',
      },
      body:   bodyBytes,
      signal: controller.signal,
    });
    return response;
  } finally {
    clearTimeout(timeoutId);
  }
}

// ── Public API ────────────────────────────────────────────────────────────────

/**
 * Send a new-order push notification to the configured ntfy topic.
 *
 * Retries up to MAX_ATTEMPTS times on transient network errors and
 * retryable HTTP status codes (408, 429, 5xx). Non-retryable failures
 * (4xx except 408/429, configuration errors) return immediately.
 *
 * CONTRACT:
 *   - Never throws under any circumstance.
 *   - Always returns { success: boolean, error?: string }.
 *   - The caller (api/order.js) owns structured logging with request_id.
 *
 * @param {Object} order - The order record as built in api/order.js.
 * @returns {Promise<{ success: boolean, error?: string }>}
 */
export async function sendNtfyNotification(order) {
  const topic = process.env.NTFY_TOPIC?.trim();
  if (!topic) {
    return { success: false, error: 'NTFY_TOPIC is not configured' };
  }

  const baseUrl  = resolveBaseUrl();
  const url      = `${baseUrl}/${encodeURIComponent(topic)}`;
  const timeoutMs = resolveTimeout();

  // Encode once — reused across retry attempts.
  const bodyBytes = encoder.encode(buildNtfyBody(order));

  let lastError = '';

  for (let i = 0; i < MAX_ATTEMPTS; i++) {
    // Exponential backoff: no delay on first attempt, then 200ms, 400ms, …
    // Formula: BACKOFF_BASE_MS * 2^(i-1) → attempt 1: 0ms, 2: 200ms, 3: 400ms.
    if (i > 0) {
      await sleep(BACKOFF_BASE_MS * (2 ** (i - 1)));
    }

    try {
      const response = await attempt(url, bodyBytes, timeoutMs);

      if (response.ok) {
        return { success: true };
      }

      // Non-OK HTTP response — read the body for diagnostic context.
      const detail = await response.text().catch(() => '');
      const reason = detail.trim()
        ? `ntfy error ${response.status}: ${detail.trim()}`
        : `ntfy error ${response.status}`;

      if (!isRetryableStatus(response.status)) {
        // Client error or unrecognised status — no point retrying.
        return { success: false, error: reason };
      }

      lastError = reason;

    } catch (err) {
      // Only retry on errors that represent transient network conditions.
      // AbortError        — our own timeout fired
      // TypeError         — undici/fetch wraps DNS, TLS, and connection failures
      //                     in TypeError; ENOTFOUND, ECONNRESET, ETIMEDOUT etc.
      //                     surface as err.cause?.code on the TypeError
      // Any other thrown value (e.g. programming error) is not retried.
      const isRetryableError =
        err instanceof TypeError ||        // fetch-level: DNS, TLS, connection
        err?.name === 'AbortError';        // our AbortController timeout fired

      const reason = err instanceof Error
        ? `${err.name}: ${err.message}`
        : String(err);

      if (!isRetryableError) {
        return { success: false, error: `ntfy network error: ${reason}` };
      }

      lastError = `ntfy network error: ${reason}`;
    }
  }

  return { success: false, error: lastError };
}
