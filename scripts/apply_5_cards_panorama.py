import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. NEW CSS FOR SECTION 4
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
      padding: 0 clamp(16px, 2.5vw, 40px) clamp(36px, 4vw, 56px);
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

    /* TẦNG 1: Biển gà chữ nghệ thuật nguyên bản treo nóc sát rìa ngoài cùng bên trái */
    .menu-hero-header {
      position: relative;
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 clamp(8px, 1.5vw, 24px);
      z-index: 5;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      position: relative;
      margin-top: 0;
      width: auto;
    }

    /* Ropes reach y=0 to touch the ceiling of #menu */
    .menu-rooster-img {
      width: clamp(190px, 18vw, 250px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 12px 24px rgba(45, 26, 18, 0.16));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.015) translateY(-2px);
    }

    /* ==========================================================================
       TẦNG 2: SÂN KHẤU PANORAMA 5 MÓN (NẰM DƯỚI ĐÁY BIỂN GỖ HÀNG GÒN)
       ========================================================================== */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1260px;
      margin: clamp(14px, 2vw, 28px) auto 0;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 2;
    }

    /* Carousel 3D Track */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: 520px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin-top: 4px;
      cursor: grab;
      user-select: none;
    }

    .menu-carousel-track:active {
      cursor: grabbing;
    }

    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(250px, 26vw, 295px);
      padding: 0 22px 26px;
      border-radius: 26px;
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

    /* 1. Active Card: 1 Món Tâm Điểm (100% sắc nét, tone Nâu Cát Gỗ Ấm) */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: 1.5px solid #C4A482;
      transform: translate3d(0, -14px, 50px) scale(1.04);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 20px 42px rgba(36, 22, 16, 0.16),
                  0 0 0 1px rgba(196, 164, 130, 0.35);
      cursor: default;
    }

    /* 2. Near Inactive Cards: 2 Món Mờ Cận Tâm (Scale 0.85, Opacity 65%) */
    .menu-card.is-near-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(-92%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
      cursor: pointer;
    }

    .menu-card.is-near-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(92%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
      cursor: pointer;
    }

    /* 3. Far Inactive Cards: 2 Món Mờ Rìa Xa (Scale 0.72, Opacity 35%) */
    .menu-card.is-far-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.15);
      transform: translate3d(-178%, 20px, -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.06);
      cursor: pointer;
    }

    .menu-card.is-far-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.15);
      transform: translate3d(178%, 20px, -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.06);
      cursor: pointer;
    }

    .menu-card.is-hidden {
      opacity: 0;
      transform: translate3d(0, 30px, -140px) scale(0.65);
      pointer-events: none;
      z-index: 1;
    }

    /* KHÓA CỨNG: Thẻ mờ không bị dịch chuyển hay rung lắc khi chạm hờ/hover */
    .menu-card.is-near-prev:hover {
      transform: translate3d(-92%, 10px, -40px) scale(0.85) !important;
    }

    .menu-card.is-near-next:hover {
      transform: translate3d(92%, 10px, -40px) scale(0.85) !important;
    }

    .menu-card.is-far-prev:hover {
      transform: translate3d(-178%, 20px, -90px) scale(0.72) !important;
    }

    .menu-card.is-far-next:hover {
      transform: translate3d(178%, 20px, -90px) scale(0.72) !important;
    }

    .menu-card:not(.is-active) .menu-card-plate {
      transform: none !important;
    }

    /* Card Plate Visual: Đưa đĩa xuống vị trí tự nhiên, 100% không bị cắt nóc */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -15px;
      margin-bottom: 22px;
      z-index: 2;
    }

    .menu-card-plate {
      width: clamp(145px, 16vw, 165px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 12px 20px rgba(36, 22, 16, 0.2));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.05) translateY(-2px);
      filter: drop-shadow(0 16px 26px rgba(36, 22, 16, 0.28));
    }

    /* Card Content Typography - Nổi bật, hạ thấp chữ không bị đĩa che */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      padding-top: 2px;
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(15.5px, 1.4vw, 18px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 6px;
      text-transform: uppercase;
      line-height: 1.25;
      color: #1A1410;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-title {
      color: #1A1410;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-title {
      color: #33241C;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(20px, 1.8vw, 24px);
      font-weight: 900;
      margin: 0 0 8px;
      letter-spacing: 0.03em;
      color: #8A4A1C;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-price {
      color: #8A4A1C;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-price {
      color: #9E5E2B;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(11.5px, 0.85vw, 12.8px);
      line-height: 1.48;
      font-weight: 300;
      margin: 0 0 16px;
      max-width: 240px;
      color: #4A3C33;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card.is-active .menu-card-desc {
      color: #4A3C33;
      opacity: 1;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-desc {
      color: #6A584D;
      opacity: 0.8;
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
      max-width: 190px;
      padding: 9px 20px;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 12.5px;
      font-weight: 700;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      transition: all 0.28s ease;
      cursor: pointer;
    }

    .menu-card.is-active .menu-card-cta {
      background: #9E5E2B;
      color: #FFFFFF;
      box-shadow: 0 6px 16px rgba(158, 94, 43, 0.28);
      opacity: 1;
      pointer-events: auto;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: #B56E35;
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(158, 94, 43, 0.38);
    }

    .menu-card:not(.menu-card.is-active) .menu-card-cta {
      background: transparent;
      color: #9E5E2B;
      border: 1px solid #C48E59;
      padding: 6px 16px;
      font-size: 11px;
      opacity: 0.85;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-cta:hover {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
    }

    /* Pagination Dots (5 món) */
    .menu-dots {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin: 16px auto 26px;
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
        justify-content: center;
        margin-bottom: 8px;
      }

      .menu-hero-mascot {
        max-width: 230px;
        margin: 0 auto;
      }

      .menu-carousel-track {
        height: 500px;
      }

      .menu-card.is-near-prev {
        transform: translate3d(-80%, 10px, -40px) scale(0.82) !important;
      }

      .menu-card.is-near-next {
        transform: translate3d(80%, 10px, -40px) scale(0.82) !important;
      }

      .menu-card.is-far-prev {
        transform: translate3d(-150%, 20px, -80px) scale(0.68) !important;
      }

      .menu-card.is-far-next {
        transform: translate3d(150%, 20px, -80px) scale(0.68) !important;
      }
    }

    @media (max-width: 600px) {
      #menu {
        padding: 0 12px 36px;
      }

      .menu-hero-header {
        justify-content: center;
        margin-bottom: 6px;
      }

      .menu-hero-mascot {
        max-width: 190px;
        margin: 0 auto;
      }

      .menu-carousel-track {
        height: 480px;
        margin-top: 10px;
      }

      .menu-card {
        width: 82vw;
        max-width: 290px;
        padding: 0 18px 24px;
      }

      .menu-card.is-active {
        transform: translate3d(0, -12px, 40px) scale(1) !important;
      }

      .menu-card.is-near-prev {
        transform: translate3d(-68%, 8px, -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-card.is-near-next {
        transform: translate3d(68%, 8px, -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-card.is-far-prev,
      .menu-card.is-far-next {
        opacity: 0;
        pointer-events: none;
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

css_menu_start = text.find('#menu {')
css_menu_end = text.find('/* ---------- SECTION 3 : STORY ---------- */')
assert css_menu_start != -1 and css_menu_end != -1, "CSS boundary not found!"

text = text[:css_menu_start] + new_menu_css + "\n\n    " + text[css_menu_end:]
print("Updated Section 4 CSS with 2-Tier Vertical Clearance and Panorama 5 cards!")

# 2. NEW HTML FOR SECTION 4: 5 CARDS & ORIGINAL BOARD ASSET
new_menu_html = """  <!-- SECTION 4: MENU (PANORAMA 5 MÓN & BIỂN GÀ NGHỆ THUẬT NGUYÊN BẢN SÁT RÌA TRÁI) -->
  <section id="menu">
    <!-- Decorative side pattern motif -->
    <div class="menu-decor-pattern" aria-hidden="true"></div>

    <!-- TẦNG 1: Biển gà chữ nghệ thuật nguyên bản treo nóc sát rìa ngoài cùng bên trái -->
    <header class="menu-hero-header">
      <div class="menu-hero-mascot">
        <picture>
          <source srcset="images/menu/original-chef-rooster-board.webp" type="image/webp">
          <img src="images/menu/Gà trống mặc trang phục bên bảng gỗ.png" alt="Chú gà trống đầu bếp Hàng Gòn bên bảng gỗ nghệ thuật nguyên bản" class="menu-rooster-img" loading="lazy" decoding="async">
        </picture>
      </div>
    </header>

    <!-- TẦNG 2: SÂN KHẤU PANORAMA 5 MÓN (NẰM HOÀN TOÀN DƯỚI ĐÁY BIỂN GỖ) -->
    <div class="menu-stage-wrapper">
      <!-- Carousel Track with 5 Dishes -->
      <div class="menu-carousel-track" id="menuTrack" role="region" aria-label="Thực đơn món đặc sản Hàng Gòn">
        <!-- Card 0: BÁNH CANH GÀ ĐẶC BIỆT -->
        <article class="menu-card is-active" data-index="0" aria-label="Bánh Canh Gà Đặc Biệt">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" alt="Mẹt Bánh Canh Gà Đặc Biệt Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">BÁNH CANH GÀ ĐẶC BIỆT</h3>
            <div class="menu-card-price">70.000₫</div>
            <p class="menu-card-desc">Thịt gà ta da vàng giòn mọng nước, trứng non béo ngậy. Nước dùng ninh xương thanh ngọt đậm đà.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 1: CƠM GỎI GÀ XÉ -->
        <article class="menu-card is-near-next" data-index="1" aria-label="Cơm Gỏi Gà Xé">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" alt="Mẹt Cơm Gỏi Gà Xé Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">CƠM GỎI GÀ XÉ</h3>
            <div class="menu-card-price">52.000₫</div>
            <p class="menu-card-desc">Cơm nghệ thơm béo nấu từ nước luộc gà, ăn cùng gỏi gà bắp cải chua ngọt và chén mắm gừng cay nồng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 2: GỎI GÀ TA BẮP CHUỐI -->
        <article class="menu-card is-far-next" data-index="2" aria-label="Gỏi Gà Ta Bắp Chuối">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" alt="Mẹt Gỏi Gà Ta Bắp Chuối Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">GỎI GÀ TA BẮP CHUỐI</h3>
            <div class="menu-card-price">50.000₫</div>
            <p class="menu-card-desc">Thịt gà thả vườn xé phay bắp chuối giòn sần sật, rau răm cay the và sốt chua ngọt béo bùi đậu phộng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 3: XÔI GÀ TRỨNG NON -->
        <article class="menu-card is-far-prev" data-index="3" aria-label="Xôi Gà Trứng Non">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" alt="Mẹt Xôi Gà Trứng Non Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">XÔI GÀ TRỨNG NON</h3>
            <div class="menu-card-price">40.000₫</div>
            <p class="menu-card-desc">Xôi nếp nương dẻo quánh thoang thoảng mỡ gà, chùm trứng non vàng ngậy và hành phi giòn rụm ấm bụng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 4: MÌ GÀ TA TRUYỀN THỐNG (MỚI) -->
        <article class="menu-card is-near-prev" data-index="4" aria-label="Mì Gà Ta Truyền Thống">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/mi-ga.webp" type="image/webp">
              <img src="images/menu/mi-ga.webp" alt="Mẹt Mì Gà Ta Truyền Thống Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">MÌ GÀ TA TRUYỀN THỐNG</h3>
            <div class="menu-card-price">55.000₫</div>
            <p class="menu-card-desc">Sợi mì trứng dai vàng óng, thịt gà ta xé ngọt mềm, trứng non béo bùi, nước dùng hầm xương thanh ngọt thơm nồng tiêu sọ.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>
      </div>

      <!-- Pagination Indicator Dots (5 Món) -->
      <div class="menu-dots" id="menuDots" role="tablist" aria-label="Chọn món hiển thị">
        <button class="menu-dot is-active" data-index="0" role="tab" aria-selected="true" aria-label="Xem Bánh Canh Gà Đặc Biệt"></button>
        <button class="menu-dot" data-index="1" role="tab" aria-selected="false" aria-label="Xem Cơm Gỏi Gà Xé"></button>
        <button class="menu-dot" data-index="2" role="tab" aria-selected="false" aria-label="Xem Gỏi Gà Ta Bắp Chuối"></button>
        <button class="menu-dot" data-index="3" role="tab" aria-selected="false" aria-label="Xem Xôi Gà Trứng Non"></button>
        <button class="menu-dot" data-index="4" role="tab" aria-selected="false" aria-label="Xem Mì Gà Ta Truyền Thống"></button>
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
print("Updated Section 4 HTML with 5 cards and original board asset!")

# 3. UPDATE JS CONTROLLER FOR 5-ITEM PANORAMA & CLICK TO POP UP
new_js_block = """  <!-- 3D Focus Menu Carousel Controller (5 Dishes Panorama & Click to Pop Up) -->
  <script>
    (function () {
      const track = document.getElementById('menuTrack');
      if (!track) return;

      const cards = Array.from(track.querySelectorAll('.menu-card'));
      const dots = Array.from(document.querySelectorAll('.menu-dot'));
      const total = cards.length;
      let currentIndex = 0;
      let hasDragged = false;

      function updateCarousel(newIndex) {
        currentIndex = (newIndex + total) % total;

        cards.forEach((card, i) => {
          card.classList.remove('is-active', 'is-near-prev', 'is-near-next', 'is-far-prev', 'is-far-next', 'is-hidden');
          
          let diff = (i - currentIndex) % total;
          if (diff < -Math.floor(total / 2)) diff += total;
          if (diff > Math.floor(total / 2)) diff -= total;

          if (diff === 0) {
            card.classList.add('is-active');
            card.setAttribute('aria-hidden', 'false');
          } else if (diff === -1) {
            card.classList.add('is-near-prev');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === 1) {
            card.classList.add('is-near-next');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === -2) {
            card.classList.add('is-far-prev');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === 2) {
            card.classList.add('is-far-next');
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

      // Click vào bất kỳ thẻ hoặc hình món nào để đưa món đó nổi lên trung tâm ngay lập tức
      cards.forEach((card, idx) => {
        card.addEventListener('click', (e) => {
          if (e.target.closest('.menu-card-cta')) return;
          if (hasDragged) return;
          if (idx !== currentIndex) {
            e.preventDefault();
            updateCarousel(idx);
          }
        });
      });

      // Pagination dots click
      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => updateCarousel(idx));
      });

      // Mouse Drag-to-Slide Engine for Desktop
      let isDragging = false;
      let dragStartX = 0;
      let dragCurrentX = 0;

      track.addEventListener('mousedown', (e) => {
        if (e.target.closest('.menu-card-cta')) return;
        isDragging = true;
        hasDragged = false;
        dragStartX = e.pageX;
        dragCurrentX = e.pageX;
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        dragCurrentX = e.pageX;
        if (Math.abs(dragCurrentX - dragStartX) > 8) {
          hasDragged = true;
        }
      });

      window.addEventListener('mouseup', (e) => {
        if (!isDragging) return;
        isDragging = false;
        const diffX = dragCurrentX - dragStartX;
        const dragThreshold = 30;
        if (diffX < -dragThreshold) {
          updateCarousel(currentIndex + 1);
        } else if (diffX > dragThreshold) {
          updateCarousel(currentIndex - 1);
        }
        setTimeout(() => { hasDragged = false; }, 80);
      });

      // Touch / Swipe Navigation for Mobile
      let touchStartX = 0;
      let touchEndX = 0;

      track.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      track.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        const threshold = 30;
        if (touchEndX < touchStartX - threshold) {
          updateCarousel(currentIndex + 1);
        } else if (touchEndX > touchStartX + threshold) {
          updateCarousel(currentIndex - 1);
        }
      }, { passive: true });

      // Keyboard navigation
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

      // Initialize initial state (Bánh Canh Gà Đặc Biệt is active)
      updateCarousel(0);
    })();
  </script>"""

old_js_pos = text.find('<!-- 3D Focus Menu Carousel Controller')
assert old_js_pos != -1, "old JS controller not found!"
pos_body = text.rfind('</body>')
assert pos_body != -1, "</body> not found!"

text = text[:old_js_pos] + new_js_block + "\n" + text[pos_body:]
print("Updated JS controller with 5-item panorama and click-to-pop-up!")

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(text)

print("Applied 5-cards panorama & vertical clearance successfully to index.html!")
