import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

ORDER_HTML = 'order.html'
with open(ORDER_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .rooster-claw-top and .rooster-claw-mid in Desktop CSS
claw_desktop_re = re.compile(r'/\* Foreground Claws.*?\n\s*\.rooster-claw-top\s*\{[^}]*\}\s*\.rooster-claw-mid\s*\{[^}]*\}', re.DOTALL)
new_claw_desktop = '''    /* Foreground Claws (Layer 3 - Emerging Naturally from Behind over Board Rim) */
    .rooster-claw-top {
      position: absolute;
      left: 112px;
      top: -14px;
      width: 62px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 2px 3px rgba(10, 5, 2, 0.5));
      transition: all 0.3s ease;
    }

    .rooster-claw-mid {
      position: absolute;
      left: -12px;
      top: 154px;
      width: 38px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(1px 2px 3px rgba(10, 5, 2, 0.45));
      transition: all 0.3s ease;
    }'''

assert claw_desktop_re.search(content), 'claw_desktop_re not found'
content = claw_desktop_re.sub(new_claw_desktop, content)
print('1. Updated Desktop Claws CSS')

# 2. Update .btn-add-cart CSS
btn_add_re = re.compile(r'/\* Add-To-Cart Action Button.*?\n\s*\.btn-add-cart\s*\{[^}]*\}\s*\.btn-add-cart img\s*\{[^}]*\}\s*\.btn-add-cart:hover\s*\{[^}]*\}', re.DOTALL)
new_btn_add = '''    /* Add-To-Cart Action Button (Clean Artisan Plain Icon - Zero Card Box) */
    .btn-add-cart {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 18px;
      height: 18px;
      border: none !important;
      background: transparent !important;
      border-radius: 0 !important;
      padding: 0 !important;
      cursor: pointer;
      opacity: 0;
      visibility: hidden;
      transform: scale(0.9);
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      margin-left: 3px;
      box-shadow: none !important;
    }

    .btn-add-cart img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 1px 2px rgba(60, 40, 25, 0.25));
    }

    .btn-add-cart:hover {
      background: transparent !important;
      border: none !important;
      transform: scale(1.22);
      box-shadow: none !important;
    }'''

assert btn_add_re.search(content), 'btn_add_re not found'
content = btn_add_re.sub(new_btn_add, content)
print('2. Updated btn-add-cart CSS (nen tron, khong card box)')

# 3. Update Order Slip Column & Compact Card CSS
order_slip_re = re.compile(r'/\* ==========================================================================\s*3\. RIGHT COLUMN: ARTISAN GUEST CHECK.*?\n\s*\.order-slip-col\s*\{[^}]*\}\s*\.guest-check-card\s*\{[^}]*\}', re.DOTALL)
new_order_slip = '''    /* ==========================================================================
       3. RIGHT COLUMN: ARTISAN GUEST CHECK (COMPACT VIEWPORT FIT - ZERO SLIP)
       ========================================================================== */
    .order-slip-col {
      flex: 0 0 325px;
      width: 325px;
      position: relative;
      margin-top: clamp(82px, 9.5vh, 92px);
      align-self: flex-start;
      z-index: 20;
    }

    .guest-check-card {
      width: 100%;
      background: url('images/webp/phieu-don-order.webp') top center / 100% 100% no-repeat;
      color: var(--ink-dark);
      border-radius: 4px;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.42);
      border: none;
      display: flex;
      flex-direction: column;
      position: relative;
      z-index: 20;
      user-select: none;
      max-height: calc(100vh - 105px);
    }'''

assert order_slip_re.search(content), 'order_slip_re not found'
content = order_slip_re.sub(new_order_slip, content)
print('3. Updated order-slip-col and guest-check-card base CSS')

# 4. Compact Check Card Header, Body, Recipient, Table, and Footer
content = re.sub(r'\.check-drag-handle\s*\{[^}]*\}', '''.check-drag-handle {
      padding: 10px 14px 6px;
      background: transparent;
      border-bottom: 1px dashed rgba(60, 40, 25, 0.22);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: default;
    }''', content, count=1)

content = re.sub(r'\.check-brand-title\s*\{[^}]*\}', '''.check-brand-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 1.28rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      line-height: 1.1;
      color: var(--ink-dark);
    }''', content, count=1)

content = re.sub(r'\.check-sub-title\s*\{[^}]*\}', '''.check-sub-title {
      font-size: 0.68rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--gold-rich);
      margin-top: 1px;
      font-weight: 600;
    }''', content, count=1)

content = re.sub(r'\.check-card-body\s*\{[^}]*\}', '''.check-card-body {
      padding: 6px 12px;
      display: flex;
      flex-direction: column;
      gap: 5px;
      max-height: calc(100vh - 305px);
      overflow-y: auto;
      scrollbar-width: thin;
      scrollbar-color: rgba(60, 40, 25, 0.2) transparent;
    }''', content, count=1)

content = re.sub(r'\.check-meta-line\s*\{[^}]*\}', '''.check-meta-line {
      display: flex;
      justify-content: space-between;
      font-size: 0.68rem;
      font-family: 'JetBrains Mono', monospace;
      color: var(--ink-muted);
      padding-bottom: 4px;
      border-bottom: 1px dotted rgba(60, 40, 25, 0.18);
    }''', content, count=1)

content = re.sub(r'\.check-recipient-section\s*\{[^}]*\}', '''.check-recipient-section {
      display: flex;
      flex-direction: column;
      gap: 3px;
      padding-bottom: 5px;
      border-bottom: 1px solid var(--paper-border);
    }''', content, count=1)

content = re.sub(r'\.recipient-heading\s*\{[^}]*\}', '''.recipient-heading {
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--gold-rich);
    }''', content, count=1)

content = re.sub(r'\.recipient-row\s*\{[^}]*\}', '''.recipient-row {
      display: flex;
      align-items: baseline;
      gap: 6px;
      font-size: 0.74rem;
    }''', content, count=1)

content = re.sub(r'\.recipient-label\s*\{[^}]*\}', '''.recipient-label {
      flex: 0 0 85px;
      font-size: 0.68rem;
      font-weight: 600;
      color: var(--ink-muted);
      white-space: nowrap;
    }''', content, count=1)

content = re.sub(r'\.recipient-input\s*\{[^}]*\}', '''.recipient-input {
      flex: 1;
      font-size: 0.76rem;
      font-family: 'Be Vietnam Pro', sans-serif;
      color: var(--ink-dark);
      background: transparent;
      border: none;
      border-bottom: 1px dotted rgba(60, 40, 25, 0.25);
      padding: 1px 0;
      outline: none;
      transition: border-bottom-color 0.2s;
    }''', content, count=1)

content = re.sub(r'\.check-items-table\s*\{[^}]*\}', '''.check-items-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.76rem;
    }''', content, count=1)

content = re.sub(r'\.check-items-table th\s*\{[^}]*\}', '''.check-items-table th {
      text-align: left;
      font-size: 0.64rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--ink-light);
      padding-bottom: 4px;
      border-bottom: 1px solid var(--paper-border);
    }''', content, count=1)

content = re.sub(r'\.check-items-table td\s*\{[^}]*\}', '''.check-items-table td {
      padding: 4px 0;
      border-bottom: 1px dotted rgba(60, 40, 25, 0.15);
      vertical-align: middle;
    }''', content, count=1)

content = re.sub(r'\.slip-qty-control\s*\{[^}]*\}', '''.slip-qty-control {
      display: inline-flex;
      align-items: center;
      gap: 2px;
      background: rgba(60, 40, 25, 0.06);
      border: 1px solid rgba(60, 40, 25, 0.2);
      border-radius: 3px;
      padding: 1px 2px;
    }''', content, count=1)

content = re.sub(r'\.slip-qty-btn\s*\{[^}]*\}', '''.slip-qty-btn {
      width: 15px;
      height: 15px;
      border: none;
      background: transparent;
      color: var(--ink-dark);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.74rem;
      font-weight: 700;
      line-height: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      border-radius: 2px;
      transition: all 0.15s ease;
      padding: 0;
    }''', content, count=1)

content = re.sub(r'\.check-card-footer\s*\{[^}]*\}', '''.check-card-footer {
      padding: 6px 12px 10px;
      background: transparent;
      border-top: 1px dashed rgba(60, 40, 25, 0.25);
      display: flex;
      flex-direction: column;
      gap: 3px;
      margin-top: auto;
    }''', content, count=1)

content = re.sub(r'\.check-total-line\s*\{[^}]*\}', '''.check-total-line {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      font-size: 0.75rem;
      color: var(--ink-muted);
    }''', content, count=1)

content = re.sub(r'\.check-total-line\.grand\s*\{[^}]*\}', '''.check-total-line.grand {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink-dark);
      border-top: 1px solid rgba(60, 40, 25, 0.18);
      padding-top: 3px;
    }''', content, count=1)

content = re.sub(r'\.grand-total-amount\s*\{[^}]*\}', '''.grand-total-amount {
      font-family: 'JetBrains Mono', monospace;
      color: var(--red-stamp);
      font-size: 1.15rem;
    }''', content, count=1)

content = re.sub(r'\.btn-confirm-order\s*\{[^}]*\}', '''.btn-confirm-order {
      width: 100%;
      padding: 9px 14px;
      background: var(--ink-dark);
      color: #fff;
      border: 1px solid rgba(201, 154, 74, 0.4);
      border-radius: 4px;
      font-family: 'Cormorant Garamond', serif;
      font-size: 1.02rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-top: 2px;
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
      transition: all 0.2s ease;
    }''', content, count=1)

with open(ORDER_HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print('4. All CSS and DOM updates written successfully to order.html!')
