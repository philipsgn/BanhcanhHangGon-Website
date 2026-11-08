import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. NEW CSS FOR SECTION 4: MENU 3D FOCUS SLIDER
new_menu_css = """    #menu {
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
      padding: 0 clamp(16px, 3vw, 40px) clamp(36px, 4vw, 56px);
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
      max-width: clamp(220px, 24vw, 320px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 14px 28px rgba(45, 26, 18, 0.18));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.012) translateY(-2px);
    }

    /* ==========================================================================
       SECTION 4: 3D FOCUS SLIDER (STARBUCKS INSPIRATION & ARTISAN IDENTITY)
       ========================================================================== */
    .menu-stage-wrapper {
      position: relative;
      max-width: 980px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 2;
    }

    /* Arrow Navigation Buttons */
    .menu-nav-arrow {
      position: absolute;
      top: 48%;
      transform: translateY(-50%);
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 1.5px solid #D8C3A5;
      color: #241610;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      box-shadow: 0 6px 18px rgba(36, 22, 16, 0.16);
      transition: all 0.28s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-nav-arrow:hover {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
      transform: translateY(-50%) scale(1.08);
      box-shadow: 0 8px 22px rgba(158, 94, 43, 0.3);
    }

    .menu-nav-arrow:active {
      transform: translateY(-50%) scale(0.96);
    }

    .menu-nav-arrow--prev {
      left: clamp(4px, 2vw, 20px);
    }

    .menu-nav-arrow--next {
      right: clamp(4px, 2vw, 20px);
    }

    /* Carousel 3D Track */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: 490px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1100px;
      margin-top: 24px;
    }

    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(260px, 28vw, 310px);
      padding: 0 24px 28px;
      border-radius: 28px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1),
                  opacity 0.45s ease,
                  background-color 0.45s ease,
                  box-shadow 0.5s ease,
                  border-color 0.45s ease;
      will-change: transform, opacity;
      cursor: pointer;
    }

    /* Active Card: Gỗ Mun Sơn Mài & Vàng Hoàng Kim */
    .menu-card.is-active {
      background: #241610;
      color: #FAF7F2;
      border: 1.5px solid rgba(201, 154, 74, 0.45);
      transform: translate3d(0, -18px, 60px) scale(1.04);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 26px 52px rgba(28, 16, 10, 0.38),
                  0 0 0 1px rgba(201, 154, 74, 0.2);
      cursor: default;
    }

    /* Inactive Cards: Kem Giấy Dó */
    .menu-card.is-prev {
      background: #F4EFEB;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.22);
      transform: translate3d(-88%, 10px, -40px) scale(0.85);
      opacity: 0.62;
      z-index: 3;
      box-shadow: 0 12px 28px rgba(36, 22, 16, 0.1);
    }

    .menu-card.is-next {
      background: #F4EFEB;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.22);
      transform: translate3d(88%, 10px, -40px) scale(0.85);
      opacity: 0.62;
      z-index: 3;
      box-shadow: 0 12px 28px rgba(36, 22, 16, 0.1);
    }

    .menu-card.is-hidden {
      opacity: 0;
      transform: translate3d(0, 30px, -120px) scale(0.7);
      pointer-events: none;
      z-index: 1;
    }

    /* Card Plate Visual (Pop-out 3D Effect) */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -64px;
      margin-bottom: 12px;
      z-index: 2;
    }

    .menu-card-plate {
      width: clamp(170px, 20vw, 205px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 16px 28px rgba(24, 12, 6, 0.35));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.04) translateY(-4px);
      filter: drop-shadow(0 20px 32px rgba(0, 0, 0, 0.45));
    }

    /* Authentic Contact Shadow under plate */
    .menu-card-contact-shadow {
      position: absolute;
      bottom: -6px;
      width: 65%;
      height: 14px;
      background: radial-gradient(ellipse at center, rgba(16, 8, 4, 0.6) 0%, rgba(16, 8, 4, 0) 70%);
      border-radius: 50%;
      z-index: -1;
      pointer-events: none;
    }

    /* Card Content Typography */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(16px, 1.5vw, 19px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 6px;
      text-transform: uppercase;
      line-height: 1.25;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-title {
      color: #F6E2B6;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-title {
      color: #241610;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(21px, 2vw, 25px);
      font-weight: 900;
      margin: 0 0 8px;
      letter-spacing: 0.03em;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-price {
      color: #FFFFFF;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-price {
      color: #9E5E2B;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12px, 0.88vw, 13px);
      line-height: 1.48;
      font-weight: 300;
      margin: 0 0 16px;
      max-width: 250px;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card.is-active .menu-card-desc {
      color: #E2D9D2;
      opacity: 0.95;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-desc {
      color: #6A584D;
      opacity: 0.75;
      /* keep concise on inactive cards */
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* CTA Button */
    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 200px;
      padding: 9px 20px;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      transition: all 0.28s ease;
      cursor: pointer;
    }

    .menu-card.is-active .menu-card-cta {
      background: #C99A4A;
      color: #1A1009;
      box-shadow: 0 6px 16px rgba(201, 154, 74, 0.35);
      opacity: 1;
      pointer-events: auto;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: #DFB469;
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(201, 154, 74, 0.45);
    }

    .menu-card:not(.menu-card.is-active) .menu-card-cta {
      background: transparent;
      color: #9E5E2B;
      border: 1px solid #C48E59;
      padding: 6px 16px;
      font-size: 11.5px;
      opacity: 0.85;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-cta:hover {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
    }

    /* Pagination Dots */
    .menu-dots {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin: 16px auto 28px;
      z-index: 4;
    }

    .menu-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: #D8C3A5;
      border: none;
      padding: 0;
      cursor: pointer;
      transition: all 0.32s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-dot:hover {
      background: #B58B58;
    }

    .menu-dot.is-active {
      width: 26px;
      border-radius: 999px;
      background: #9E5E2B;
    }

    /* Menu Footer Bar */
    .menu-footer-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: 740px;
      margin: 12px auto 0;
      padding: 16px 0 0;
      border-top: 1px solid rgba(201, 154, 74, 0.24);
      width: 100%;
      z-index: 3;
    }

    .menu-footer-contact {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 2px;
    }

    .menu-footer-tagline {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 11.5px;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #8C7A70;
    }

    .menu-footer-phone {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 16px;
      font-weight: 800;
      color: #111111;
      text-decoration: none;
      transition: color 0.25s ease;
    }

    .menu-footer-phone:hover {
      color: #9E5E2B;
    }

    .menu-footer-phone svg {
      color: #9E5E2B;
    }

    .menu-footer-hours {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 11.5px;
      color: #66554D;
      font-weight: 300;
    }

    .menu-view-all-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 10px 24px;
      background: #111111;
      color: #FFFFFF;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-decoration: none;
      transition: all 0.3s ease;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.16);
    }

    .menu-view-all-btn:hover {
      background: #9E5E2B;
      color: #FFFFFF;
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(158, 94, 43, 0.28);
    }

    /* Responsive adjustments */
    @media (max-width: 960px) {
      .menu-hero-header {
        margin-bottom: 12px;
      }

      .menu-hero-mascot {
        max-width: 280px;
        margin: 0 auto;
      }

      .menu-carousel-track {
        height: 480px;
      }

      .menu-card.is-prev {
        transform: translate3d(-78%, 10px, -40px) scale(0.82);
      }

      .menu-card.is-next {
        transform: translate3d(78%, 10px, -40px) scale(0.82);
      }
    }

    @media (max-width: 600px) {
      #menu {
        padding: 0 12px 36px;
      }

      .menu-carousel-track {
        height: 470px;
        margin-top: 20px;
      }

      .menu-card {
        width: 82vw;
        max-width: 290px;
        padding: 0 18px 24px;
      }

      .menu-card.is-active {
        transform: translate3d(0, -12px, 40px) scale(1);
      }

      .menu-card.is-prev {
        transform: translate3d(-68%, 8px, -40px) scale(0.78);
        opacity: 0.35;
      }

      .menu-card.is-next {
        transform: translate3d(68%, 8px, -40px) scale(0.78);
        opacity: 0.35;
      }

      .menu-nav-arrow {
        width: 38px;
        height: 38px;
      }

      .menu-footer-bar {
        flex-direction: column;
        text-align: center;
        gap: 16px;
      }

      .menu-footer-contact {
        align-items: center;
        text-align: center;
      }
    }
"""

# Replace CSS block
css_menu_start = text.find('#menu {')
css_menu_end = text.find('/* ---------- SECTION 3 : STORY ---------- */')
assert css_menu_start != -1 and css_menu_end != -1, "CSS boundary not found!"

text = text[:css_menu_start] + new_menu_css + "\n\n    " + text[css_menu_end:]
print("Replaced Section 4 CSS successfully!")

# 2. NEW HTML FOR SECTION 4
new_menu_html = """  <!-- SECTION 4: MENU (3D FOCUS SLIDER - STARBUCKS INSPIRATION & ARTISAN IDENTITY) -->
  <section id="menu">
    <!-- Decorative side pattern motif -->
    <div class="menu-decor-pattern" aria-hidden="true"></div>

    <!-- Menu Hero Header: Chef Rooster + Wooden Board (Centered Brand Anchor) -->
    <header class="menu-hero-header">
      <div class="menu-hero-mascot">
        <picture>
          <source srcset="images/menu/chef-rooster-board.webp" type="image/webp">
          <img src="images/menu/Gà trống mặc trang phục bên bảng gỗ.png" alt="Chú gà trống đầu bếp Hàng Gòn bên bảng gỗ" class="menu-rooster-img" loading="lazy" decoding="async">
        </picture>
      </div>
    </header>

    <!-- Stage Focus Carousel -->
    <div class="menu-stage-wrapper">
      <!-- Navigation Arrow Buttons -->
      <button class="menu-nav-arrow menu-nav-arrow--prev" id="menuPrevBtn" aria-label="Món trước đó">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>
      <button class="menu-nav-arrow menu-nav-arrow--next" id="menuNextBtn" aria-label="Món kế tiếp">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>

      <!-- Carousel Track with 4 Dishes -->
      <div class="menu-carousel-track" id="menuTrack" role="region" aria-label="Thực đơn món đặc sản Hàng Gòn">
        <!-- Card 0: BÁNH CANH GÀ ĐẶC BIỆT -->
        <article class="menu-card is-active" data-index="0" aria-label="Bánh Canh Gà Đặc Biệt">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" alt="Mẹt Bánh Canh Gà Đặc Biệt Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
            <div class="menu-card-contact-shadow" aria-hidden="true"></div>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">BÁNH CANH GÀ ĐẶC BIỆT</h3>
            <div class="menu-card-price">70.000₫</div>
            <p class="menu-card-desc">Thịt gà ta da vàng giòn mọng nước, trứng non béo ngậy. Nước dùng ninh xương thanh ngọt đậm đà.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 1: CƠM GỎI GÀ XÉ -->
        <article class="menu-card is-next" data-index="1" aria-label="Cơm Gỏi Gà Xé">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" alt="Mẹt Cơm Gỏi Gà Xé Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
            <div class="menu-card-contact-shadow" aria-hidden="true"></div>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">CƠM GỎI GÀ XÉ</h3>
            <div class="menu-card-price">52.000₫</div>
            <p class="menu-card-desc">Cơm nghệ thơm béo nấu từ nước luộc gà, ăn cùng gỏi gà bắp cải chua ngọt và chén mắm gừng cay nồng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 2: GỎI GÀ TA BẮP CHUỐI -->
        <article class="menu-card is-hidden" data-index="2" aria-label="Gỏi Gà Ta Bắp Chuối">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" alt="Mẹt Gỏi Gà Ta Bắp Chuối Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
            <div class="menu-card-contact-shadow" aria-hidden="true"></div>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">GỎI GÀ TA BẮP CHUỐI</h3>
            <div class="menu-card-price">50.000₫</div>
            <p class="menu-card-desc">Thịt gà thả vườn xé phay bắp chuối giòn sần sật, rau răm cay the và sốt chua ngọt béo bùi đậu phộng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 3: XÔI GÀ TRỨNG NON -->
        <article class="menu-card is-prev" data-index="3" aria-label="Xôi Gà Trứng Non">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" alt="Mẹt Xôi Gà Trứng Non Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
            <div class="menu-card-contact-shadow" aria-hidden="true"></div>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">XÔI GÀ TRỨNG NON</h3>
            <div class="menu-card-price">40.000₫</div>
            <p class="menu-card-desc">Xôi nếp nương dẻo quánh thoang thoảng mỡ gà, chùm trứng non vàng ngậy và hành phi giòn rụm ấm bụng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>
      </div>

      <!-- Pagination Indicator Dots -->
      <div class="menu-dots" id="menuDots" role="tablist" aria-label="Chọn món hiển thị">
        <button class="menu-dot is-active" data-index="0" role="tab" aria-selected="true" aria-label="Xem Bánh Canh Gà Đặc Biệt"></button>
        <button class="menu-dot" data-index="1" role="tab" aria-selected="false" aria-label="Xem Cơm Gỏi Gà Xé"></button>
        <button class="menu-dot" data-index="2" role="tab" aria-selected="false" aria-label="Xem Gỏi Gà Ta Bắp Chuối"></button>
        <button class="menu-dot" data-index="3" role="tab" aria-selected="false" aria-label="Xem Xôi Gà Trứng Non"></button>
      </div>
    </div>

    <!-- Menu Footer Bar -->
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
  </section>"""

html_menu_start = text.find('<section id="menu">')
html_menu_end = text.find('</section>', html_menu_start) + len('</section>')
assert html_menu_start != -1 and html_menu_end != -1, "HTML Section 4 not found!"

text = text[:html_menu_start] + new_menu_html + text[html_menu_end:]
print("Replaced Section 4 HTML successfully!")

# 3. ADD VANILLA JS CONTROLLER FOR FOCUS SLIDER
js_controller = """
  <!-- 3D Focus Menu Carousel Controller -->
  <script>
    (function () {
      const track = document.getElementById('menuTrack');
      if (!track) return;

      const cards = Array.from(track.querySelectorAll('.menu-card'));
      const dots = Array.from(document.querySelectorAll('.menu-dot'));
      const prevBtn = document.getElementById('menuPrevBtn');
      const nextBtn = document.getElementById('menuNextBtn');
      const total = cards.length;
      let currentIndex = 0;

      function updateCarousel(newIndex) {
        currentIndex = (newIndex + total) % total;

        cards.forEach((card, i) => {
          card.classList.remove('is-active', 'is-prev', 'is-next', 'is-hidden');
          const diff = (i - currentIndex + total) % total;

          if (diff === 0) {
            card.classList.add('is-active');
            card.setAttribute('aria-hidden', 'false');
          } else if (diff === total - 1 || diff === -1) {
            card.classList.add('is-prev');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === 1) {
            card.classList.add('is-next');
            card.setAttribute('aria-hidden', 'true');
          } else {
            card.classList.add('is-hidden');
            card.setAttribute('aria-hidden', 'true');
          }
        });

        dots.forEach((dot, i) => {
          const isActive = i === currentIndex;
          dot.classList.toggle('is-active', isActive);
          dot.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', () => updateCarousel(currentIndex - 1));
      }

      if (nextBtn) {
        nextBtn.addEventListener('click', () => updateCarousel(currentIndex + 1));
      }

      cards.forEach((card, idx) => {
        card.addEventListener('click', (e) => {
          // If clicked on CTA button, let navigation happen
          if (e.target.closest('.menu-card-cta')) return;
          if (idx !== currentIndex) {
            e.preventDefault();
            updateCarousel(idx);
          }
        });
      });

      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => updateCarousel(idx));
      });

      // Touch / Swipe Navigation for Mobile
      let touchStartX = 0;
      let touchEndX = 0;

      track.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      track.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      }, { passive: true });

      function handleSwipe() {
        const threshold = 40;
        if (touchEndX < touchStartX - threshold) {
          updateCarousel(currentIndex + 1);
        } else if (touchEndX > touchStartX + threshold) {
          updateCarousel(currentIndex - 1);
        }
      }

      // Keyboard navigation when track is focused
      window.addEventListener('keydown', (e) => {
        const menuSec = document.getElementById('menu');
        if (!menuSec) return;
        const rect = menuSec.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        if (!isInView) return;

        if (e.key === 'ArrowLeft') {
          updateCarousel(currentIndex - 1);
        } else if (e.key === 'ArrowRight') {
          updateCarousel(currentIndex + 1);
        }
      });

      // Initialize initial state
      updateCarousel(0);
    })();
  </script>
"""

# Place the JS controller right before </body>
pos_body = text.rfind('</body>')
if pos_body != -1:
    text = text[:pos_body] + js_controller + "\n" + text[pos_body:]
    print("Inserted JS Controller before </body>!")
else:
    print("ERROR: </body> not found!")

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(text)

print("Applied 3D Focus Slider successfully to index.html!")
