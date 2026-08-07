/**
 * lib/logger.js — Centralized structured logger for production observability.
 *
 * Every log entry is a single JSON object written to stdout via console.log.
 * Machine-readable for Vercel log capture and any downstream pipeline.
 *
 * Guarantees enforced inside this module (callers cannot bypass):
 *   1. Service metadata (service, env, version) is auto-attached to every entry.
 *   2. PII fields are stripped recursively before serialisation — defence-in-depth.
 *   3. duration_ms is computed from a monotonic hrtime bigint — immune to
 *      system clock adjustments, accurate to sub-millisecond.
 *   4. Serialisation errors are caught; a fallback line is emitted instead of
 *      throwing — logging can never crash request processing.
 *   5. No business logic, no async I/O, no external dependencies.
 */

// ── Application version ───────────────────────────────────────────────────────
// Prefer the git commit SHA set by Vercel, then the npm package version injected
// by Node at startup, then omit the field entirely rather than hardcode a value
// that will inevitably become stale.

const appVersion =
  process.env.VERCEL_GIT_COMMIT_SHA ??
  process.env.npm_package_version ??
  null;

// ── Service metadata ──────────────────────────────────────────────────────────
// Attached automatically to every log entry.
// Object.freeze prevents accidental runtime mutation.

const SERVICE_META = Object.freeze({
  service: 'order-api',
  env:     process.env.VERCEL_ENV ?? process.env.NODE_ENV ?? 'development',
  ...(appVersion !== null ? { version: appVersion } : {}),
});

// ── PII sanitizer ─────────────────────────────────────────────────────────────
// Sensitive field names that must never appear in any log output.
// sanitize() traverses nested objects and arrays so accidental nesting is
// also caught — pure defence-in-depth.

const REDACTED_KEYS = new Set([
  'customer_name',
  'phone',
  'address',
  'note',
  'idempotency_key',
]);

/**
 * Return true only for plain JavaScript objects — those whose prototype is
 * exactly Object.prototype or null (i.e. created via `{}`, `Object.create(null)`).
 *
 * Returns false for Error, Date, URL, Map, Set, Buffer, RegExp, and any other
 * class instance so sanitize() leaves those values untouched rather than
 * accidentally destructuring them into a bare `{}`.
 *
 * @param {unknown} value
 * @returns {boolean}
 */
function isPlainObject(value) {
  if (value === null || typeof value !== 'object') return false;
  const proto = Object.getPrototypeOf(value);
  return proto === Object.prototype || proto === null;
}

/**
 * Recursively remove all REDACTED_KEYS from a value.
 *
 * Rules:
 *  - Arrays:        map each element through sanitize().
 *  - Plain objects: shallow-copy, drop redacted keys, recurse into values.
 *  - Everything else (Error, Date, URL, Map, Set, Buffer, primitives, …):
 *                   returned as-is — never mutated, never destructured.
 *
 * Never mutates the input.
 *
 * @param {unknown} value
 * @returns {unknown}
 */
function sanitize(value) {
  if (Array.isArray(value)) {
    return value.map(sanitize);
  }

  if (isPlainObject(value)) {
    const safe = {};
    for (const key of Object.keys(value)) {
      if (!REDACTED_KEYS.has(key)) {
        safe[key] = sanitize(value[key]);
      }
    }
    return safe;
  }

  // Primitive or non-plain object (Error, Date, URL, …) — return unchanged.
  return value;
}

// ── Request context ───────────────────────────────────────────────────────────

/**
 * @typedef {Object} RequestContext
 * @property {bigint} startTime - process.hrtime.bigint() captured at request
 *                                start. Used to compute duration_ms.
 *                                Monotonic — unaffected by system clock changes.
 */

// ── Core emit ─────────────────────────────────────────────────────────────────

/**
 * Serialise one log entry to stdout as a single JSON line.
 *
 * Output field order:
 *   level, event, timestamp, service, env, [version],
 *   [duration_ms — when ctx provided], ...sanitized caller fields
 *
 * If JSON.stringify fails (circular reference, unsupported value, etc.) a
 * minimal fallback line is emitted and the error is silently swallowed so
 * that logging never interrupts request processing.
 *
 * @param {'info'|'warn'|'error'} level
 * @param {string}         event  - Snake_case identifier, e.g. "order_created".
 * @param {Object}         fields - Caller-supplied fields. PII stripped recursively.
 * @param {RequestContext} [ctx]  - When present, computes and attaches duration_ms.
 */
function emit(level, event, fields, ctx) {
  // Compute duration before constructing the entry so it is as accurate as possible.
  const duration = ctx !== undefined
    ? { duration_ms: Math.round(Number(process.hrtime.bigint() - ctx.startTime) / 1_000_000) }
    : {};

  try {
    console.log(JSON.stringify({
      level,
      event,
      timestamp: new Date().toISOString(),
      ...SERVICE_META,
      ...duration,
      ...sanitize(fields),
    }));
  } catch {
    // Serialisation failed (circular reference, BigInt, etc.).
    // Emit the smallest possible valid line so the event is never silently lost.
    console.log(JSON.stringify({ level: 'error', event: 'logger_serialization_failed', timestamp: new Date().toISOString() }));
  }
}

// ── Public API ────────────────────────────────────────────────────────────────
//
// Signature:  logger.info / warn / error (event, fields?, ctx?)
//
//   event  {string}         Snake_case event identifier.
//   fields {Object}         Structured payload. PII stripped automatically.
//   ctx    {RequestContext}  Optional. When provided, duration_ms is attached.

/**
 * Log an informational event.
 * Use for: successful operations, expected control-flow (duplicates, etc.).
 *
 * @param {string}         event
 * @param {Object}         [fields]
 * @param {RequestContext} [ctx]
 */
export function info(event, fields = {}, ctx) {
  emit('info', event, fields, ctx);
}

/**
 * Log a warning.
 * Use for: degraded but non-fatal outcomes (Discord failure, etc.).
 *
 * @param {string}         event
 * @param {Object}         [fields]
 * @param {RequestContext} [ctx]
 */
export function warn(event, fields = {}, ctx) {
  emit('warn', event, fields, ctx);
}

/**
 * Log an error.
 * Use for: failures that prevented the intended operation from completing.
 *
 * @param {string}         event
 * @param {Object}         [fields]
 * @param {RequestContext} [ctx]
 */
export function error(event, fields = {}, ctx) {
  emit('error', event, fields, ctx);
}
