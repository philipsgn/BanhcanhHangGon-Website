import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for Menu CSS
old_menu_css_re = re.compile(
    r'/\* ---------- SECTION: MENU \(ZIGZAG BOUTIQUE EDITORIAL\) ---------- \*/\s*'
    r'#menu\s*\{.*?'
    r'(?=/\* ---------- SECTION 3 : STORY ---------- \*/)',
    re.DOTALL
)

new_menu_css = '''/* ---------- SECTION: MENU (ZIGZAG BOUTIQUE EDITORIAL - TIGHT & REALISTIC) ---------- */
    #menu {
      position: relative;
      background-color: #FAF8F5;
      background-image:
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.6) 0%, transparent 100%);
      color: #1A1410;
      overflow: hidden;
      isolation: isolate;
      /* padding-top: 0 allows the 2 hanging ropes to physically touch the top ceiling */
      padding: 0 clamp(20px, 4vw, 64px) clamp(44px, 5vw, 68px);
    }

    /* Traditional decorative geometric pattern motif on side */
    .menu-decor-pattern {
      position: absolute;
      left: 0;
      top: 15%;
      width: clamp(60px, 8vw, 130px);
      height: 70%;
      background-repeat: repeat-y;
      background-size: 100% auto;
      background-image: url("data:image/svg+xml,%3Csvg width='80' height='160' viewBox='0 0 80 160' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 40L40 0L80 40L40 80L0 40Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Cpath d='M0 120L40 80L80 120L40 160L0 120Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Ccircle cx='40' cy='40' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3Ccircle cx='40' cy='120' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 0;
      opacity: 0.85;
    }

    .menu-editorial-container {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
    }

    /* Menu Hero Header: Chef Rooster with ropes touching ceiling */
    .menu-hero-header {
      display: grid;
      grid-template-columns: minmax(320px, 1fr) minmax(340px, 1.18fr);
      align-items: flex-start;
      gap: clamp(24px, 4vw, 56px);
      max-width: 1100px;
      margin: 0 auto clamp(24px, 3.5vw, 42px);
      padding: 0;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      position: relative;
      margin-top: 0;
    }

    /* Ropes reach y=0 to touch the ceiling of #menu */
    .menu-rooster-img {
      width: 100%;
      max-width: clamp(340px, 36vw, 480px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 20px 36px rgba(45, 26, 18, 0.22));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.015) translateY(-3px);
    }

    .menu-hero-text {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
      /* optical offset to vertically balance with the hanging wooden board */
      padding-top: clamp(48px, 6vw, 96px);
    }

    .menu-brand-script {
      font-family: 'Cormorant Garamond', cursive, serif;
      font-size: clamp(36px, 4.2vw, 58px);
      font-style: italic;
      font-weight: 600;
      color: #9E5E2B;
      line-height: 1;
      margin-bottom: 4px;
      letter-spacing: 0.02em;
    }

    /* Black brushstroke/pill badge */
    .menu-badge-brush {
      display: inline-block;
      background: #111111;
      color: #FFFFFF;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(15px, 1.35vw, 21px);
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      padding: 9px 26px;
      border-radius: 4px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
      margin: 4px 0 14px;
      transform: rotate(-1deg);
      user-select: none;
    }

    .menu-hero-subtitle {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13.5px, 1.05vw, 15.5px);
      line-height: 1.65;
      font-weight: 300;
      color: #55443B;
      max-width: 460px;
      margin: 0;
      text-wrap: balance;
    }

    /* Tightened Zigzag Dish Rows (Zero page bloat) */
    .menu-dish-row {
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      align-items: center;
      gap: clamp(24px, 4vw, 56px);
      margin-bottom: clamp(26px, 3.5vw, 42px);
      position: relative;
    }

    .menu-dish-row:last-of-type {
      margin-bottom: clamp(20px, 3vw, 32px);
    }

    /* Reverse variant for Zigzag */
    .menu-dish-row--reverse {
      grid-template-columns: 1.1fr 1fr;
    }

    .menu-dish-row--reverse .menu-dish-visual {
      order: 1;
    }

    .menu-dish-row--reverse .menu-dish-info {
      order: 2;
    }

    /* Dish Info Box (Text side) */
    .menu-dish-info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
      padding: 0;
      position: relative;
      z-index: 2;
    }

    .menu-dish-header-row {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }

    .menu-dish-name {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(20px, 2.1vw, 27px);
      font-weight: 800;
      letter-spacing: 0.03em;
      color: #111111;
      margin: 0;
      text-transform: uppercase;
      line-height: 1.15;
    }

    /* Black Circular Price Badge */
    .menu-price-circle {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: clamp(42px, 3.6vw, 48px);
      height: clamp(42px, 3.6vw, 48px);
      background: #111111;
      color: #FFFFFF;
      border-radius: 50%;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13px, 1.1vw, 15.5px);
      font-weight: 800;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
      user-select: none;
    }

    .menu-dish-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13px, 0.98vw, 14.5px);
      line-height: 1.62;
      font-weight: 300;
      color: #55443B;
      margin: 0 0 10px;
      max-width: 470px;
    }

    /* Thin Horizontal Accent Line */
    .menu-accent-line {
      width: min(300px, 80%);
      height: 1.5px;
      background: #222222;
      opacity: 0.8;
      margin: 2px 0 12px;
    }

    /* Action order button */
    .menu-order-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 20px;
      background: transparent;
      color: #9E5E2B;
      border: 1.5px solid #C48E59;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.28s ease;
      cursor: pointer;
    }

    .menu-order-btn:hover,
    .menu-order-btn:focus-visible {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
      transform: translateY(-2px);
      box-shadow: 0 5px 14px rgba(158, 94, 43, 0.24);
    }

    /* Dish Visual (Compact plate presentation with gentle bleed) */
    .menu-dish-visual {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      z-index: 1;
    }

    .menu-dish-row:not(.menu-dish-row--reverse) .menu-dish-visual .menu-dish-img {
      transform: translateX(clamp(8px, 2.5vw, 24px));
    }

    .menu-dish-row--reverse .menu-dish-visual .menu-dish-img {
      transform: translateX(clamp(-24px, -2.5vw, -8px));
    }

    .menu-dish-img {
      width: 100%;
      max-width: clamp(280px, 30vw, 400px);
      height: auto;
      object-fit: contain;
      display: block;
      transition: transform 0.4s ease, filter 0.4s ease;
      filter: drop-shadow(0 16px 28px rgba(45, 26, 18, 0.16));
    }

    .menu-dish-visual:hover .menu-dish-img {
      transform: scale(1.025) translateY(-3px) !important;
      filter: drop-shadow(0 22px 34px rgba(45, 26, 18, 0.22));
    }

    /* Tightened Menu Footer Bar */
    .menu-footer-bar {
      max-width: 1100px;
      margin: clamp(24px, 3.5vw, 40px) auto 0;
      padding-top: clamp(18px, 2.5vw, 28px);
      border-top: 1.5px solid rgba(28, 19, 13, 0.14);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }

    .menu-footer-contact {
      display: flex;
      flex-direction: column;
      gap: 3px;
      text-align: left;
    }

    .menu-footer-tagline {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: #9E5E2B;
    }

    .menu-footer-phone {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: clamp(14px, 1.1vw, 17px);
      font-weight: 700;
      color: #111111;
      text-decoration: none;
    }

    .menu-footer-hours {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      color: #66554D;
      font-weight: 400;
    }

    .menu-view-all-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 11px 30px;
      background: #111111;
      color: #FAF8F5;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13.5px;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-decoration: none;
      transition: all 0.3s ease;
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.18);
    }

    .menu-view-all-btn:hover,
    .menu-view-all-btn:focus-visible {
      background: #9E5E2B;
      color: #FFFFFF;
      transform: translateY(-2px);
      box-shadow: 0 10px 22px rgba(158, 94, 43, 0.28);
    }

    .menu-view-all-btn svg {
      transition: transform 0.3s ease;
    }

    .menu-view-all-btn:hover svg {
      transform: translateX(4px);
    }

    /* Responsive adjustments */
    @media (max-width: 960px) {
      .menu-hero-header {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 16px;
        margin-bottom: 36px;
      }

      .menu-hero-mascot {
        max-width: 340px;
        margin: 0 auto;
      }

      .menu-hero-text {
        align-items: center;
        text-align: center;
        padding-top: 0;
      }

      .menu-dish-row,
      .menu-dish-row--reverse {
        grid-template-columns: 1fr;
        gap: 16px;
        margin-bottom: 38px;
        text-align: center;
      }

      .menu-dish-row--reverse .menu-dish-visual,
      .menu-dish-row .menu-dish-visual {
        order: 1;
        max-width: 360px;
        margin: 0 auto;
      }

      .menu-dish-row:not(.menu-dish-row--reverse) .menu-dish-visual .menu-dish-img,
      .menu-dish-row--reverse .menu-dish-visual .menu-dish-img {
        transform: none !important;
      }

      .menu-dish-row--reverse .menu-dish-info,
      .menu-dish-row .menu-dish-info {
        order: 2;
        align-items: center;
        text-align: center;
      }

      .menu-dish-header-row {
        justify-content: center;
      }

      .menu-dish-desc {
        max-width: 440px;
      }

      .menu-accent-line {
        margin: 2px auto 12px;
      }

      .menu-footer-bar {
        flex-direction: column;
        text-align: center;
        gap: 20px;
      }

      .menu-footer-contact {
        align-items: center;
        text-align: center;
      }
    }

    @media (max-width: 600px) {
      #menu {
        padding: 0 16px 48px;
      }

      .menu-decor-pattern {
        display: none;
      }

      .menu-dish-row {
        gap: 14px;
        margin-bottom: 32px;
      }

      .menu-dish-visual .menu-dish-img {
        max-height: 240px;
      }
    }

    '''

assert old_menu_css_re.search(content), "old_menu_css_re not matched"
content = old_menu_css_re.sub(new_menu_css, content, count=1)
print("1. Desktop & Mobile Menu CSS updated with tight spacing and ceiling rope touch")

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)

print("-> index.html successfully updated!")
