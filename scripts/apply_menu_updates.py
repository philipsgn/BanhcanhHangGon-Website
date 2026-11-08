import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS: container, header, mascot, and dish rows
old_css_part = """    .menu-editorial-container {
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
      height: auto;"""

new_css_part = """    .menu-editorial-container {
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
      height: auto;"""

# Normalize CRLF for replacement
norm_content = content.replace('\r\n', '\n')
norm_old_css = old_css_part.replace('\r\n', '\n')
norm_new_css = new_css_part.replace('\r\n', '\n')

if norm_old_css in norm_content:
    norm_content = norm_content.replace(norm_old_css, norm_new_css)
    print("CSS replaced successfully!")
else:
    print("ERROR: old_css_part not found in content!")

# 2. Update Responsive CSS at max-width 960px
old_resp_css = """    @media (max-width: 960px) {
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
      }"""

new_resp_css = """    @media (max-width: 960px) {
      .menu-hero-header {
        text-align: center;
        margin-bottom: 24px;
      }

      .menu-hero-mascot {
        max-width: 380px;
        margin: 0 auto;
      }"""

norm_old_resp = old_resp_css.replace('\r\n', '\n')
norm_new_resp = new_resp_css.replace('\r\n', '\n')

if norm_old_resp in norm_content:
    norm_content = norm_content.replace(norm_old_resp, norm_new_resp)
    print("Responsive CSS replaced successfully!")
else:
    print("ERROR: old_resp_css not found!")

# 3. Update HTML markup: remove .menu-hero-text
old_html_header = """      <!-- Menu Hero Header: Chef Rooster + Blackboard + Borcelle-style Badge -->
      <header class="menu-hero-header">
        <div class="menu-hero-mascot">
          <picture>
            <source srcset="images/menu/chef-rooster-board.webp" type="image/webp">
            <img src="images/menu/Gà trống mặc trang phục bên bảng gỗ.png" alt="Chú gà trống đầu bếp Hàng Gòn bên bảng thực đơn gỗ" class="menu-rooster-img" loading="lazy" decoding="async">
          </picture>
        </div>
        <div class="menu-hero-text">
          <span class="menu-brand-script">Hàng Gòn</span>
          <div class="menu-badge-brush">THỰC ĐƠN ĐẶC SẢN</div>
          <p class="menu-hero-subtitle">
            Khách ghé Hàng Gòn, hãy thong thả dừng chân thưởng thức hương vị gà ta Long Khánh truyền thống — ngọt thanh từ xương ninh, thơm giòn da gà, đậm đà tình quê.
          </p>
        </div>
      </header>"""

new_html_header = """      <!-- Menu Hero Header: Chef Rooster + Wooden Board (Centered, No AI-Slop, Physical Wing Layering) -->
      <header class="menu-hero-header">
        <div class="menu-hero-mascot">
          <picture>
            <source srcset="images/menu/chef-rooster-board.webp" type="image/webp">
            <img src="images/menu/Gà trống mặc trang phục bên bảng gỗ.png" alt="Chú gà trống đầu bếp Hàng Gòn bên bảng gỗ" class="menu-rooster-img" loading="lazy" decoding="async">
          </picture>
        </div>
      </header>"""

norm_old_html = old_html_header.replace('\r\n', '\n')
norm_new_html = new_html_header.replace('\r\n', '\n')

if norm_old_html in norm_content:
    norm_content = norm_content.replace(norm_old_html, norm_new_html)
    print("HTML Header replaced successfully!")
else:
    print("ERROR: old_html_header not found!")

# Write back preserving CRLF
final_content = norm_content.replace('\n', '\r\n')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("index.html updated successfully!")
