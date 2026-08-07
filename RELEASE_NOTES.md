# Bánh Canh Gà Hàng Gòn Website

Version 1.0.0

Release Date: August 8, 2026

Status: Production Stable

## Highlights

- Complete online ordering
- Desktop & Mobile support
- Safari compatibility
- Discord notifications
- ntfy notifications
- Supabase integration
- Secure server-side pricing
- Idempotency protection
- Structured logging
- Responsive UI

## Highlights Detail

### Ordering

- Desktop ordering works end-to-end: menu selection → customer form → review → confirm → success.
- Mobile ordering works with a dedicated multi-step flow (menu → details → review → submit).
- iPhone Safari ordering fixed and verified on-device.
- Android Chrome ordering works.
- Success modal confirms the order; staff call the customer to confirm before preparation.

### Backend

- Server-side validation of all required fields, phone format, lengths, and duplicate item ids.
- Prices are computed exclusively server-side from the frozen MENU catalogue — client prices are never trusted.
- Idempotency key (crypto.randomUUID) protects against duplicate submissions.
- Duplicate orders prevented: a unique constraint on `idx_orders_idempotency_key` returns the existing order on a 23505 conflict.
- Orders persist to Supabase with server-computed values only.
- Robust error handling: friendly messages for validation, network, timeout, and server failures.

### Notifications

- Discord notification via webhook: embed with customer, phone, fulfillment type, address, item list, total, and status. Vietnamese text renders correctly; customer note is displayed when present.
- ntfy notification via push: UTF-8 safe plain text with emoji, item list, total, and customer note. Retry logic with exponential backoff on transient failures.

### Database

- Orders inserted with correct column mapping.
- Customer note stored correctly in `orders.note`.
- Prices, line totals, and grand total generated server-side.
- Status defaults to `pending`.

### Security

- Client-supplied monetary values ignored (unit_price, line_total, total_amount).
- Server computes all totals from its own price table.
- Validation enabled for every order request.
- CORS configured with an allowlist of origins.
- Request IDs logged for traceability.

### UI

- Responsive across desktop and mobile.
- Hero, menu, and ordering sections polished.
- Mobile-optimized, Safari-compatible layout.
- No debug overlay, no Safari trace logs, no temporary instrumentation.

### Logging

- Structured JSON logging with request IDs.
- No debug console.log in client code.
- No temporary diagnostics in production.

## Bug Fixes

- Fixed ordering flow not submitting on iPhone Safari (root cause resolved and verified on-device).
- Fixed customer note being dropped from Discord and ntfy notifications — the note now renders in both channels only when present.
- Removed the temporary Safari diagnostic overlay and all Safari trace instrumentation from production.
- Removed debug console spam and temporary diagnostic listeners from production code.
- Ensured idempotency key is generated reliably on Safari (crypto.randomUUID).
- Prevented duplicate orders via the idempotency key unique constraint.
- Fixed mobile menu background coverage.
- Fixed menu image scaling and overflow on mobile deployment.
- Removed `backdrop-filter` and cache-busting script that caused an iOS Safari crash.
- Fixed menu bowl hover behavior and image sizing on both desktop and mobile.
- Adjusted menu spacing and layout to prevent overflow.
- Server-side pricing hardened so client-supplied prices cannot influence order totals.

## Known Issues

None.

## Release Checklist

- [x] Desktop ordering works
- [x] Mobile ordering works
- [x] iPhone Safari ordering works
- [x] Android Chrome ordering works
- [x] Validation passes
- [x] Server-side pricing works
- [x] Idempotency works
- [x] Duplicate orders prevented
- [x] Supabase persistence works
- [x] Error handling works
- [x] Discord notification delivered with correct Unicode, Vietnamese text, customer note, item list, and total
- [x] ntfy notification delivered with UTF-8-safe, Unicode-safe, emoji-safe text, retry logic, and customer note
- [x] Orders inserted correctly
- [x] Note stored correctly
- [x] Prices generated server-side
- [x] Status defaults correctly
- [x] Client prices ignored
- [x] Server computes totals
- [x] Validation enabled
- [x] CORS configured
- [x] Request IDs logged
- [x] Desktop UI responsive
- [x] Mobile UI responsive
- [x] Safari compatible
- [x] No debug overlay
- [x] No Safari trace logs
- [x] No temporary instrumentation
- [x] Structured logging enabled
- [x] No debug console.log
- [x] No temporary diagnostics
- [x] No TODO
- [x] No FIXME
- [x] No unused helper
- [x] No dead code

## Deployment

- Frontend: static `index.html` + `order.html`, deployed via Vercel.
- API: `api/order.js` as a Vercel serverless function (Node >= 18).
- Database: Supabase `orders` table.
- Environment variables: `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `DISCORD_WEBHOOK_URL`, `NTFY_TOPIC`, `NTFY_BASE_URL` (optional), `NTFY_TIMEOUT_MS` (optional).

## Assets

- `lib/discord.js` — Discord webhook client
- `lib/ntfy.js` — ntfy push client with retry
- `lib/validator.js` — request validation
- `lib/logger.js` — structured logger
- `lib/supabase.js` — Supabase client
- `api/order.js` — order handler
- `index.html` — public site
- `order.html` — ordering flow
