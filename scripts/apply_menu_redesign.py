import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Menu CSS in Desktop section
# From /* ---------- SECTION 3 : MENU (ZIGZAG 3D EDITORIAL) ---------- */
# down to the end of Menu CSS before /* ---------- SECTION 3 : STORY ---------- */
old_menu_css_re = re.compile(
    r'/\* ---------- SECTION 3 : MENU \(ZIGZAG 3D EDITORIAL\) ---------- \*/\s*'
    r'#menu\s*\{.*?'
    r'(?=/\* ---------- SECTION 3 : STORY ---------- \*/)',
    re.DOTALL
)

new_menu_css = '''/* ---------- SECTION: MENU (ZIGZAG BOUTIQUE EDITORIAL) ---------- */
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
      padding: clamp(64px, 7vw, 108px) clamp(20px, 4vw, 64px);
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
      max-width: 1240px;
      margin: 0 auto;
      width: 100%;
    }

    /* Menu Hero Header: Chef Rooster + Blackboard + Borcelle-style Badge */
    .menu-hero-header {
      display: grid;
      grid-template-columns: minmax(320px, 1fr) minmax(340px, 1.15fr);
      align-items: center;
      gap: clamp(28px, 4.5vw, 64px);
      max-width: 1120px;
      margin: 0 auto clamp(52px, 7vw, 88px);
      padding: 0 clamp(8px, 2vw, 24px);
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }

    .menu-rooster-img {
      width: 100%;
      max-width: clamp(340px, 36vw, 490px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 20px 36px rgba(45, 26, 18, 0.22));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.02) translateY(-4px);
    }

    .menu-hero-text {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
    }

    .menu-brand-script {
      font-family: 'Cormorant Garamond', cursive, serif;
      font-size: clamp(38px, 4.5vw, 60px);
      font-style: italic;
      font-weight: 600;
      color: #9E5E2B;
      line-height: 1;
      margin-bottom: 6px;
      letter-spacing: 0.02em;
    }

    /* Black brushstroke/pill badge (like FOOD MENU in reference) */
    .menu-badge-brush {
      display: inline-block;
      background: #111111;
      color: #FFFFFF;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(16px, 1.5vw, 22px);
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      padding: 10px 28px;
      border-radius: 4px;
      box-shadow: 0 6px 16px rgba(0, 0, 0, 0.22);
      margin: 6px 0 18px;
      transform: rotate(-1deg);
      user-select: none;
    }

    .menu-hero-subtitle {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14px, 1.1vw, 16.5px);
      line-height: 1.7;
      font-weight: 300;
      color: #55443B;
      max-width: 480px;
      margin: 0;
      text-wrap: balance;
    }

    /* Zigzag Dish Rows (Reference Layout: Alternating Text & Plate Bleed) */
    .menu-dish-row {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      align-items: center;
      gap: clamp(32px, 5vw, 84px);
      margin-bottom: clamp(64px, 8vw, 116px);
      position: relative;
    }

    .menu-dish-row:last-of-type {
      margin-bottom: clamp(48px, 6vw, 76px);
    }

    /* Reverse variant for Zigzag */
    .menu-dish-row--reverse {
      grid-template-columns: 1.15fr 1fr;
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
      padding: clamp(8px, 1.5vw, 20px) 0;
      position: relative;
      z-index: 2;
    }

    .menu-dish-header-row {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }

    .menu-dish-name {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(22px, 2.3vw, 32px);
      font-weight: 800;
      letter-spacing: 0.04em;
      color: #111111;
      margin: 0;
      text-transform: uppercase;
      line-height: 1.15;
    }

    /* Black Circular/Pill Price Badge (Reference Layout: $5, $7 badge) */
    .menu-price-circle {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: clamp(46px, 4vw, 54px);
      height: clamp(46px, 4vw, 54px);
      background: #111111;
      color: #FFFFFF;
      border-radius: 50%;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14px, 1.2vw, 17px);
      font-weight: 800;
      flex-shrink: 0;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.24);
      user-select: none;
    }

    .menu-dish-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14px, 1.05vw, 15.5px);
      line-height: 1.75;
      font-weight: 300;
      color: #55443B;
      margin: 0 0 16px;
      max-width: 480px;
    }

    /* Thin Horizontal Accent Line (Reference Layout) */
    .menu-accent-line {
      width: min(340px, 85%);
      height: 1.5px;
      background: #222222;
      opacity: 0.85;
      margin: 4px 0 18px;
    }

    /* Action order button */
    .menu-order-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 24px;
      background: transparent;
      color: #9E5E2B;
      border: 1.5px solid #C48E59;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 14px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
      cursor: pointer;
      box-shadow: 0 3px 10px rgba(196, 142, 89, 0.12);
    }

    .menu-order-btn:hover,
    .menu-order-btn:focus-visible {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(158, 94, 43, 0.28);
    }

    /* Dish Visual (Plate Bleeding off the margin like reference) */
    .menu-dish-visual {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      z-index: 1;
    }

    /* Bleed plate slightly outward on desktop */
    .menu-dish-row:not(.menu-dish-row--reverse) .menu-dish-visual .menu-dish-img {
      transform: translateX(clamp(10px, 3vw, 36px));
    }

    .menu-dish-row--reverse .menu-dish-visual .menu-dish-img {
      transform: translateX(clamp(-36px, -3vw, -10px));
    }

    .menu-dish-img {
      width: 100%;
      max-width: clamp(340px, 38vw, 540px);
      height: auto;
      object-fit: contain;
      display: block;
      transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.5s ease;
      filter: drop-shadow(0 22px 36px rgba(45, 26, 18, 0.18));
    }

    .menu-dish-visual:hover .menu-dish-img {
      transform: scale(1.03) translateY(-4px) !important;
      filter: drop-shadow(0 30px 48px rgba(45, 26, 18, 0.26));
    }

    /* Menu Footer Bar (Matching Reference bottom contact row) */
    .menu-footer-bar {
      max-width: 1120px;
      margin: clamp(48px, 6vw, 84px) auto 0;
      padding-top: clamp(24px, 3.5vw, 40px);
      border-top: 1.5px solid rgba(28, 19, 13, 0.16);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    .menu-footer-contact {
      display: flex;
      flex-direction: column;
      gap: 4px;
      text-align: left;
    }

    .menu-footer-tagline {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
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
      font-size: clamp(15px, 1.2vw, 18px);
      font-weight: 700;
      color: #111111;
      text-decoration: none;
    }

    .menu-footer-hours {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13.5px;
      color: #66554D;
      font-weight: 400;
    }

    .menu-view-all-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 13px 36px;
      background: #111111;
      color: #FAF8F5;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 14.5px;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-decoration: none;
      transition: all 0.35s ease;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.22);
    }

    .menu-view-all-btn:hover,
    .menu-view-all-btn:focus-visible {
      background: #9E5E2B;
      color: #FFFFFF;
      transform: translateY(-2px);
      box-shadow: 0 12px 28px rgba(158, 94, 43, 0.32);
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
        gap: 20px;
        margin-bottom: 52px;
      }

      .menu-hero-mascot {
        max-width: 360px;
        margin: 0 auto;
      }

      .menu-hero-text {
        align-items: center;
        text-align: center;
      }

      .menu-dish-row,
      .menu-dish-row--reverse {
        grid-template-columns: 1fr;
        gap: 24px;
        margin-bottom: 64px;
        text-align: center;
      }

      .menu-dish-row--reverse .menu-dish-visual,
      .menu-dish-row .menu-dish-visual {
        order: 1;
        max-width: 440px;
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
        max-width: 460px;
      }

      .menu-accent-line {
        margin: 4px auto 18px;
      }

      .menu-footer-bar {
        flex-direction: column;
        text-align: center;
        gap: 24px;
      }

      .menu-footer-contact {
        align-items: center;
        text-align: center;
      }
    }

    @media (max-width: 600px) {
      #menu {
        padding: 52px 18px 60px;
      }

      .menu-decor-pattern {
        display: none;
      }

      .menu-dish-row {
        gap: 16px;
        margin-bottom: 52px;
      }

      .menu-dish-visual .menu-dish-img {
        max-height: 280px;
      }
    }

    '''

assert old_menu_css_re.search(content), "old_menu_css_re not matched"
content = old_menu_css_re.sub(new_menu_css, content, count=1)
print("1. Desktop Menu CSS updated successfully")

# 2. Update HTML Markup for Section 4 (#menu)
old_menu_html_re = re.compile(
    r'<!-- SECTION \d+: MENU \(ZIGZAG 3D EDITORIAL\) -->\s*'
    r'<section id="menu">.*?'
    r'</section>',
    re.DOTALL
)

new_menu_html = '''<!-- SECTION 4: MENU (ZIGZAG BOUTIQUE EDITORIAL) -->
  <section id="menu">
    <!-- Decorative side pattern motif -->
    <div class="menu-decor-pattern" aria-hidden="true"></div>

    <div class="menu-editorial-container">
      <!-- Menu Hero Header: Chef Rooster + Blackboard + Borcelle-style Badge -->
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
      </header>

      <!-- Dish 1: Bánh Canh Gà Đặc Biệt (Text Left, Plate Right Bleed) -->
      <article class="menu-dish-row">
        <div class="menu-dish-info">
          <div class="menu-dish-header-row">
            <h3 class="menu-dish-name">BÁNH CANH GÀ ĐẶC BIỆT</h3>
            <span class="menu-price-circle">70K</span>
          </div>
          <p class="menu-dish-desc">
            Tô bánh canh đầy đặn với từng lát thịt gà ta da vàng ươm mọng nước, trứng non lòng đào béo ngậy, tim mề giòn sần sật. Nước dùng ninh từ xương gà tươi ngọt thanh, thơm nồng tiêu sọ rang và hành phi giòn rụm.
          </p>
          <div class="menu-accent-line" aria-hidden="true"></div>
          <a href="order.html" class="menu-order-btn">+ Đặt Món Ngay</a>
        </div>
        <div class="menu-dish-visual">
          <picture>
            <source srcset="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" type="image/webp">
            <img src="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" alt="Mẹt Bánh Canh Gà Đặc Biệt Hàng Gòn" loading="lazy" decoding="async" class="menu-dish-img">
          </picture>
        </div>
      </article>

      <!-- Dish 2: Cơm Gỏi Gà Xé (Plate Left Bleed, Text Right - Zigzag) -->
      <article class="menu-dish-row menu-dish-row--reverse">
        <div class="menu-dish-info">
          <div class="menu-dish-header-row">
            <h3 class="menu-dish-name">CƠM GỎI GÀ XÉ</h3>
            <span class="menu-price-circle">52K</span>
          </div>
          <p class="menu-dish-desc">
            Hạt cơm vàng óng ánh màu nghệ tươi nấu từ nước luộc gà béo ngọt, ăn cùng đĩa gỏi gà xé chua ngọt bắp cải giòn sần sật, rau răm cay the. Kèm chén nước mắm gừng gia truyền thơm lừng và súp gà nóng hổi.
          </p>
          <div class="menu-accent-line" aria-hidden="true"></div>
          <a href="order.html" class="menu-order-btn">+ Đặt Món Ngay</a>
        </div>
        <div class="menu-dish-visual">
          <picture>
            <source srcset="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" type="image/webp">
            <img src="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" alt="Mẹt Cơm Gỏi Gà Xé Hàng Gòn" loading="lazy" decoding="async" class="menu-dish-img">
          </picture>
        </div>
      </article>

      <!-- Dish 3: Gỏi Gà Ta Bắp Chuối (Text Left, Plate Right Bleed) -->
      <article class="menu-dish-row">
        <div class="menu-dish-info">
          <div class="menu-dish-header-row">
            <h3 class="menu-dish-name">GỎI GÀ TA BẮP CHUỐI</h3>
            <span class="menu-price-circle">50K</span>
          </div>
          <p class="menu-dish-desc">
            Thịt gà ta thả vườn dai ngọt xé phay trộn cùng bắp chuối bào giòn sần sật, hành tây thanh mát, rau răm và đậu phộng rang củi béo bùi. Nước sốt chua ngọt đậm đà đánh thức mọi giác quan.
          </p>
          <div class="menu-accent-line" aria-hidden="true"></div>
          <a href="order.html" class="menu-order-btn">+ Đặt Món Ngay</a>
        </div>
        <div class="menu-dish-visual">
          <picture>
            <source srcset="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" type="image/webp">
            <img src="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" alt="Mẹt Gỏi Gà Ta Bắp Chuối Hàng Gòn" loading="lazy" decoding="async" class="menu-dish-img">
          </picture>
        </div>
      </article>

      <!-- Dish 4: Xôi Gà Trứng Non (Plate Left Bleed, Text Right - Zigzag) -->
      <article class="menu-dish-row menu-dish-row--reverse">
        <div class="menu-dish-info">
          <div class="menu-dish-header-row">
            <h3 class="menu-dish-name">XÔI GÀ TRỨNG NON</h3>
            <span class="menu-price-circle">40K</span>
          </div>
          <p class="menu-dish-desc">
            Xôi nếp nương đồ chín dẻo quánh, thoang thoảng mỡ gà thơm phức, đẫy đà thịt gà xé chắc ngọt, chùm trứng non vàng ngậy béo bùi và hành phi giòn tan. Đậm đà từng thìa xôi quê ấm bụng.
          </p>
          <div class="menu-accent-line" aria-hidden="true"></div>
          <a href="order.html" class="menu-order-btn">+ Đặt Món Ngay</a>
        </div>
        <div class="menu-dish-visual">
          <picture>
            <source srcset="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" type="image/webp">
            <img src="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" alt="Mẹt Xôi Gà Trứng Non Hàng Gòn" loading="lazy" decoding="async" class="menu-dish-img">
          </picture>
        </div>
      </article>

      <!-- Menu Footer Bar (Matching Reference bottom contact info & CTA) -->
      <footer class="menu-footer-bar">
        <div class="menu-footer-contact">
          <span class="menu-footer-tagline">Đặt Giao Tận Nơi • Hotline</span>
          <a href="tel:0906427938" class="menu-footer-phone">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            090 642 79 38
          </a>
          <span class="menu-footer-hours">Phục vụ: 06:00 – 23:00 hàng ngày</span>
        </div>
        <a href="order.html" class="menu-view-all-btn">
          <span>Xem Toàn Bộ Thực Đơn</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </a>
      </footer>
    </div>
  </section>'''

assert old_menu_html_re.search(content), "old_menu_html_re not matched"
content = old_menu_html_re.sub(new_menu_html, content, count=1)
print("2. HTML Markup for Section Menu updated successfully")

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)

print("-> index.html successfully updated!")
