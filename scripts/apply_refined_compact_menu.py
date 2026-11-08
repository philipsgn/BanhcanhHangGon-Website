import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize CRLF for matching
norm_content = content.replace('\r\n', '\n')

old_menu_css = """    .menu-editorial-container {
      position: relative;
      z-index: 1;
      max-width: 940px;
      margin: 0 auto;
      width: 100%;
    }

    /* Menu Hero Header: Chef Rooster with ropes touching ceiling */
    .menu-hero-header {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      max-width: 100%;
      margin: 0 auto clamp(10px, 1.6vw, 20px);
      padding: 0;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      position: relative;
      margin-top: 0;
      width: 100%;
    }

    /* Ropes reach y=0 to touch the ceiling of #menu */
    .menu-rooster-img {
      width: 100%;
      max-width: clamp(320px, 44vw, 540px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 16px 32px rgba(45, 26, 18, 0.2));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.012) translateY(-2px);
    }

    /* Tightened Zigzag Dish Rows (Zero page bloat) */
    .menu-dish-row {
      display: grid;
      grid-template-columns: 1fr 1.05fr;
      align-items: center;
      gap: clamp(14px, 2.5vw, 32px);
      margin-bottom: clamp(10px, 1.6vw, 18px);
      position: relative;
    }

    .menu-dish-row:last-of-type {
      margin-bottom: clamp(12px, 1.8vw, 22px);
    }

    /* Reverse variant for Zigzag */
    .menu-dish-row--reverse {
      grid-template-columns: 1.05fr 1fr;
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
      gap: 12px;
      margin-bottom: 4px;
      flex-wrap: wrap;
    }

    .menu-dish-name {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(19px, 1.9vw, 24px);
      font-weight: 800;
      letter-spacing: 0.02em;
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
      width: clamp(38px, 3.2vw, 44px);
      height: clamp(38px, 3.2vw, 44px);
      background: #111111;
      color: #FFFFFF;
      border-radius: 50%;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12.5px, 1vw, 14.5px);
      font-weight: 800;
      flex-shrink: 0;
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.18);
      user-select: none;
    }

    .menu-dish-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12.5px, 0.92vw, 13.8px);
      line-height: 1.5;
      font-weight: 300;
      color: #55443B;
      margin: 0 0 6px;
      max-width: 480px;
    }

    /* Thin Horizontal Accent Line */
    .menu-accent-line {
      width: min(240px, 75%);
      height: 1.5px;
      background: #222222;
      opacity: 0.8;
      margin: 2px 0 8px;
    }

    /* Action order button */
    .menu-order-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 16px;
      background: transparent;
      color: #9E5E2B;
      border: 1.5px solid #C48E59;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 12.5px;
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
      transform: translateX(clamp(4px, 1.5vw, 14px));
    }

    .menu-dish-row--reverse .menu-dish-visual .menu-dish-img {
      transform: translateX(clamp(-14px, -1.5vw, -4px));
    }

    .menu-dish-img {
      width: 100%;
      max-width: clamp(230px, 24vw, 320px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 16px 28px rgba(36, 22, 16, 0.22));
      transition: transform 0.35s ease;
    }"""

new_menu_css = """    .menu-editorial-container {
      position: relative;
      z-index: 1;
      max-width: 740px;
      margin: 0 auto;
      width: 100%;
    }

    /* Menu Hero Header: Chef Rooster with ropes touching ceiling */
    .menu-hero-header {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      max-width: 100%;
      margin: 0 auto clamp(6px, 1.2vw, 14px);
      padding: 0;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      position: relative;
      margin-top: 0;
      width: 100%;
    }

    /* Ropes reach y=0 to touch the ceiling of #menu */
    .menu-rooster-img {
      width: 100%;
      max-width: clamp(220px, 24vw, 340px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 14px 28px rgba(45, 26, 18, 0.18));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.012) translateY(-2px);
    }

    /* Tightened Zigzag Dish Rows (Snug 24-28px gap, Zero bloat) */
    .menu-dish-row {
      display: grid;
      grid-template-columns: minmax(0, 1.35fr) minmax(0, 1fr);
      align-items: center;
      gap: clamp(14px, 2.2vw, 28px);
      margin-bottom: clamp(6px, 1vw, 12px);
      position: relative;
    }

    .menu-dish-row:last-of-type {
      margin-bottom: clamp(8px, 1.2vw, 14px);
    }

    /* Reverse variant for Zigzag */
    .menu-dish-row--reverse {
      grid-template-columns: minmax(0, 1fr) minmax(0, 1.35fr);
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
      gap: 10px;
      margin-bottom: 3px;
      flex-wrap: wrap;
    }

    .menu-dish-name {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(17px, 1.6vw, 21px);
      font-weight: 800;
      letter-spacing: 0.02em;
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
      width: 36px;
      height: 36px;
      background: #111111;
      color: #FFFFFF;
      border-radius: 50%;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      font-weight: 800;
      flex-shrink: 0;
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.18);
      user-select: none;
    }

    .menu-dish-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12px, 0.88vw, 13px);
      line-height: 1.45;
      font-weight: 300;
      color: #55443B;
      margin: 0 0 4px;
      max-width: 440px;
    }

    /* Thin Horizontal Accent Line */
    .menu-accent-line {
      width: min(200px, 70%);
      height: 1.5px;
      background: #222222;
      opacity: 0.8;
      margin: 2px 0 6px;
    }

    /* Action order button */
    .menu-order-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 4px 14px;
      background: transparent;
      color: #9E5E2B;
      border: 1.5px solid #C48E59;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 11.5px;
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

    /* Dish Visual (Snug compact plate presentation) */
    .menu-dish-visual {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      z-index: 1;
    }

    .menu-dish-img {
      width: 100%;
      max-width: clamp(160px, 18vw, 190px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 12px 22px rgba(36, 22, 16, 0.2));
      transition: transform 0.35s ease;
    }"""

if old_menu_css in norm_content:
    norm_content = norm_content.replace(old_menu_css, new_menu_css)
    print("Main Menu CSS replaced successfully!")
else:
    print("ERROR: old_menu_css not found!")

# Update responsive CSS for max-width: 960px and 600px
old_resp_960 = """    @media (max-width: 960px) {
      .menu-hero-header {
        text-align: center;
        margin-bottom: 24px;
      }

      .menu-hero-mascot {
        max-width: 380px;
        margin: 0 auto;
      }

      .menu-dish-row,
      .menu-dish-row--reverse {
        grid-template-columns: 1fr;
        gap: 16px;
        margin-bottom: 38px;
        text-align: center;
      }"""

new_resp_960 = """    @media (max-width: 960px) {
      .menu-hero-header {
        text-align: center;
        margin-bottom: 16px;
      }

      .menu-hero-mascot {
        max-width: 300px;
        margin: 0 auto;
      }

      .menu-dish-row,
      .menu-dish-row--reverse {
        grid-template-columns: 1fr;
        gap: 12px;
        margin-bottom: 22px;
        text-align: center;
      }"""

if old_resp_960 in norm_content:
    norm_content = norm_content.replace(old_resp_960, new_resp_960)
    print("Responsive 960 CSS replaced successfully!")
else:
    print("ERROR: old_resp_960 not found!")

old_resp_600 = """      .menu-dish-visual .menu-dish-img {
        max-height: 240px;
      }"""

new_resp_600 = """      .menu-dish-visual .menu-dish-img {
        max-height: 180px;
      }"""

if old_resp_600 in norm_content:
    norm_content = norm_content.replace(old_resp_600, new_resp_600)
    print("Responsive 600 CSS replaced successfully!")
else:
    print("ERROR: old_resp_600 not found!")

# Write back preserving CRLF
final_content = norm_content.replace('\n', '\r\n')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("index.html refined successfully!")
