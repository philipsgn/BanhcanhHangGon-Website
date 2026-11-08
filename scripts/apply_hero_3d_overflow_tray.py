import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start = c.find('/* ---------- SECTION 4 : MENU')
end = c.find('/* ---------- SECTION 3 : STORY', start)

hero_3d_menu_css = """/* ---------- SECTION 4 : MENU (HERO 3D OVERFLOWING TRAY & VIBRANT ARTISAN EXPERIENCE) ---------- */
    #menu {
      position: relative;
      min-height: 100vh;
      min-height: 100svh;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      background-color: #FAF8F5;
      background-image:
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.7) 0%, transparent 100%);
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(20px, 3vh, 32px) clamp(16px, 2.5vw, 40px) clamp(12px, 1.8vh, 18px);
    }

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

    /* Biển gà nghệ thuật nguyên bản: Treo góc trái, dây thừng cách trần an toàn */
    .menu-hero-header {
      position: absolute;
      top: clamp(10px, 1.6vh, 20px);
      left: clamp(16px, 3.5vw, 48px);
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      width: auto;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      z-index: 10;
      pointer-events: none;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      position: relative;
      margin: 0;
      width: auto;
      pointer-events: auto;
    }

    .menu-rooster-img {
      width: clamp(105px, 10.5vw, 140px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 10px 20px rgba(45, 26, 18, 0.14));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.02) translateY(-2px);
    }

    /* SÂN KHẤU PANORAMA 3D: NẰM HOÀN TOÀN TRONG BODY SECTION, CÁCH TRẦN >= 50PX */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1320px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: clamp(14px, 2vh, 26px) auto 0;
      z-index: 2;
      perspective: 1200px;
    }

    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(370px, 50vh, 440px);
      display: flex;
      align-items: center;
      justify-content: center;
      transform-style: preserve-3d;
      margin: 0;
      cursor: grab;
      user-select: none;
    }

    .menu-carousel-track:active {
      cursor: grabbing;
    }

    /* Thẻ Card: Neo chuẩn tại top: 50%, left: 50%, mở rộng ôm mâm thức ăn lớn */
    .menu-card {
      position: absolute;
      top: 50%;
      left: 50%;
      width: clamp(245px, 22vw, 290px);
      padding: 8px 18px 20px;
      border-radius: 26px;
      border: none;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transform-style: preserve-3d;
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1),
                  opacity 0.4s ease,
                  background-color 0.4s ease,
                  box-shadow 0.45s ease;
      will-change: transform, opacity;
      cursor: pointer;
    }

    /* Mâm Thức Ăn Hero: Phóng to vượt trội, nổi khối 3D đập vào mắt người dùng */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -8px;
      margin-bottom: clamp(6px, 1vh, 10px);
      z-index: 3;
      transform-style: preserve-3d;
    }

    .menu-card-plate {
      width: clamp(200px, 26vh, 255px);
      height: clamp(200px, 26vh, 255px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 14px 26px rgba(36, 22, 16, 0.22)) drop-shadow(0 4px 10px rgba(36, 22, 16, 0.14));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1), filter 0.45s ease;
      transform-origin: center center;
    }

    /* Animation Thở Hữu Cơ cho Mâm Món Active */
    @keyframes heroTrayBreathe {
      0%, 100% {
        transform: translateZ(28px) rotateX(1.8deg) rotateY(-1.2deg) scale(1);
      }
      50% {
        transform: translateZ(35px) rotateX(-1.2deg) rotateY(1.5deg) scale(1.025);
      }
    }

    /* Thân thẻ: Typography đậm chất thủ công ẩm thực */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      padding-top: 0;
      transform: translateZ(10px);
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13px, 1.15vw, 16px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 3px;
      text-transform: uppercase;
      line-height: 1.25;
      color: #1A1410;
      transition: color 0.35s ease;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(17px, 1.5vw, 20px);
      font-weight: 900;
      margin: 0 0 5px;
      letter-spacing: 0.03em;
      color: #8A4A1C;
      transition: color 0.35s ease;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(10px, 0.82vw, 11.5px);
      line-height: 1.38;
      font-weight: 300;
      margin: 0 0 10px;
      max-width: 240px;
      color: #4A3C33;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(11px, 0.9vw, 12px);
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(145px, 14vw, 170px);
      height: 34px;
      transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
    }

    /* ==========================================================================
       1. MÓN NỔI BẬT CHÍNH (ACTIVE HERO TRAY)
       ========================================================================== */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: none !important;
      transform: translate3d(-50%, -50%, 45px) scale(1) !important;
      opacity: 1 !important;
      z-index: 6;
      box-shadow: 0 24px 54px rgba(36, 22, 16, 0.16);
      cursor: default;
    }

    .menu-card.is-active:hover {
      transform: translate3d(-50%, -50%, 45px) scale(1) !important;
    }

    .menu-card.is-active .menu-card-plate {
      animation: heroTrayBreathe 6s ease-in-out infinite;
      filter: drop-shadow(0 16px 30px rgba(36, 22, 16, 0.28)) drop-shadow(0 5px 12px rgba(36, 22, 16, 0.16));
    }

    .menu-card.is-active:hover .menu-card-plate {
      animation-play-state: paused;
      transform: translateZ(48px) scale(1.045) !important;
      filter: drop-shadow(0 22px 38px rgba(36, 22, 16, 0.34)) drop-shadow(0 8px 16px rgba(36, 22, 16, 0.22)) !important;
    }

    .menu-card.is-active .menu-card-title {
      color: #1A1410;
    }

    .menu-card.is-active .menu-card-price {
      color: #8A4A1C;
    }

    .menu-card.is-active .menu-card-desc {
      color: #4A3C33;
      opacity: 1;
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

    /* ==========================================================================
       2. CÁC MÓN LÀM MỜ HAI BÊN (INACTIVE TIER)
       ========================================================================== */
    .menu-card:not(.is-active) {
      background: #FAF7F2;
      border: none !important;
    }

    .menu-card:not(.is-active) .menu-card-title {
      color: #33241C;
    }

    .menu-card:not(.is-active) .menu-card-price {
      color: #9E5E2B;
    }

    .menu-card:not(.is-active) .menu-card-desc {
      color: #6A584D;
      opacity: 0.8;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .menu-card:not(.is-active) .menu-card-cta {
      background: transparent;
      color: #9E5E2B;
      border: 1px solid #C48E59;
      padding: 6px 16px;
      font-size: 11px;
      opacity: 0.85;
    }

    /* Kích thước đĩa thẻ mờ */
    .menu-card.is-near-prev .menu-card-plate,
    .menu-card.is-near-next .menu-card-plate {
      width: clamp(155px, 20vh, 190px);
      height: clamp(155px, 20vh, 190px);
      transform: none !important;
    }

    .menu-card.is-far-prev .menu-card-plate,
    .menu-card.is-far-next .menu-card-plate {
      width: clamp(130px, 17vh, 160px);
      height: clamp(130px, 17vh, 160px);
      transform: none !important;
    }

    /* 3. Tọa độ 3D & Hover thẻ mờ */
    /* Near Prev (-1) */
    .menu-card.is-near-prev {
      transform: translate3d(calc(-50% - 94%), calc(-50% + 12px), -40px) scale(0.85) !important;
      opacity: 0.60 !important;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
    }

    .menu-card.is-near-prev:hover {
      transform: translate3d(calc(-50% - 94%), calc(-50% + 6px), -24px) scale(0.88) !important;
      opacity: 0.88 !important;
      box-shadow: 0 16px 32px rgba(36, 22, 16, 0.10);
    }

    /* Near Next (+1) */
    .menu-card.is-near-next {
      transform: translate3d(calc(-50% + 94%), calc(-50% + 12px), -40px) scale(0.85) !important;
      opacity: 0.60 !important;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
    }

    .menu-card.is-near-next:hover {
      transform: translate3d(calc(-50% + 94%), calc(-50% + 6px), -24px) scale(0.88) !important;
      opacity: 0.88 !important;
      box-shadow: 0 16px 32px rgba(36, 22, 16, 0.10);
    }

    /* Far Prev (-2) */
    .menu-card.is-far-prev {
      transform: translate3d(calc(-50% - 180%), calc(-50% + 22px), -90px) scale(0.72) !important;
      opacity: 0.30 !important;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-far-prev:hover {
      transform: translate3d(calc(-50% - 180%), calc(-50% + 16px), -70px) scale(0.75) !important;
      opacity: 0.65 !important;
      box-shadow: 0 12px 24px rgba(36, 22, 16, 0.08);
    }

    /* Far Next (+2) */
    .menu-card.is-far-next {
      transform: translate3d(calc(-50% + 180%), calc(-50% + 22px), -90px) scale(0.72) !important;
      opacity: 0.30 !important;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-far-next:hover {
      transform: translate3d(calc(-50% + 180%), calc(-50% + 16px), -70px) scale(0.75) !important;
      opacity: 0.65 !important;
      box-shadow: 0 12px 24px rgba(36, 22, 16, 0.08);
    }

    /* Hidden Cards */
    .menu-card.is-hidden {
      opacity: 0;
      transform: translate3d(-50%, calc(-50% + 30px), -140px) scale(0.65);
      pointer-events: none;
      z-index: 1;
    }

    /* Chấm chuyển trang (Pagination Dots) */
    .menu-dots {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin: clamp(6px, 1vh, 10px) auto clamp(8px, 1.2vh, 12px);
      z-index: 5;
    }

    .menu-dot {
      width: 7px;
      height: 7px;
      border-radius: 999px;
      background: #D8CEBE;
      border: none;
      padding: 0;
      cursor: pointer;
      transition: all 0.35s ease;
    }

    .menu-dot:hover {
      background: #B56E35;
      transform: scale(1.2);
    }

    .menu-dot.is-active {
      width: 22px;
      background: #9E5E2B;
      box-shadow: 0 2px 8px rgba(158, 94, 43, 0.35);
    }

    /* Menu Footer Bar */
    .menu-footer-bar {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: clamp(16px, 3vw, 40px);
      width: 100%;
      max-width: 680px;
      padding: clamp(6px, 1vh, 9px) clamp(16px, 2.5vw, 28px);
      background: #FAF7F2;
      border: 1px solid rgba(201, 154, 74, 0.22);
      border-radius: 999px;
      box-sizing: border-box;
      box-shadow: 0 6px 18px rgba(45, 26, 18, 0.04);
      margin: 2px auto 0;
      z-index: 4;
    }

    .menu-footer-contact {
      display: flex;
      align-items: baseline;
      gap: 12px;
      flex-wrap: wrap;
    }

    .menu-footer-tagline {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #7A6658;
    }

    .menu-footer-phone {
      font-size: clamp(13px, 1.1vw, 15px);
      font-weight: 800;
      color: #8A4A1C;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: color 0.2s ease;
    }

    .menu-footer-phone:hover {
      color: #6B3410;
    }

    .menu-footer-hours {
      font-size: 11px;
      color: #8C7B70;
      border-left: 1px solid rgba(201, 154, 74, 0.3);
      padding-left: 12px;
    }

    .menu-view-all-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 18px;
      background: #1A1410;
      color: #FAF8F5;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      border-radius: 999px;
      transition: all 0.3s ease;
      white-space: nowrap;
    }

    .menu-view-all-btn:hover {
      background: #8A4A1C;
      transform: translateY(-1px);
    }

    /* Responsive & Mobile Adaptation */
    @media (max-width: 1024px) {
      .menu-hero-header {
        left: clamp(10px, 2vw, 20px);
      }
      .menu-rooster-img {
        width: clamp(95px, 10vw, 120px);
      }
      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 82%), calc(-50% + 12px), -40px) scale(0.82) !important;
      }
      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 82%), calc(-50% + 12px), -40px) scale(0.82) !important;
      }
      .menu-card.is-far-prev {
        transform: translate3d(calc(-50% - 155%), calc(-50% + 22px), -80px) scale(0.68) !important;
      }
      .menu-card.is-far-next {
        transform: translate3d(calc(-50% + 155%), calc(-50% + 22px), -80px) scale(0.68) !important;
      }
    }

    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(10px, 1.5vh, 16px) 12px clamp(12px, 1.8vh, 18px);
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: 10px;
        left: 12px;
        margin: 0;
        padding: 0;
        z-index: 6;
      }

      .menu-rooster-img {
        width: clamp(80px, 20vw, 95px);
      }

      .menu-stage-wrapper {
        margin-top: clamp(44px, 6.5vh, 58px);
      }

      .menu-carousel-track {
        height: clamp(385px, 52vh, 425px);
      }

      .menu-card {
        width: 82vw;
        max-width: 290px;
        padding: 8px 14px 18px;
      }

      .menu-card.is-active {
        transform: translate3d(-50%, -50%, 45px) scale(1) !important;
      }

      .menu-card.is-active .menu-card-plate {
        width: clamp(190px, 46vw, 235px);
        height: clamp(190px, 46vw, 235px);
      }

      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 68%), calc(-50% + 8px), -40px) scale(0.78) !important;
        opacity: 0.35 !important;
      }

      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 68%), calc(-50% + 8px), -40px) scale(0.78) !important;
        opacity: 0.35 !important;
      }

      .menu-card.is-far-prev,
      .menu-card.is-far-next {
        opacity: 0 !important;
        pointer-events: none;
      }

      .menu-footer-bar {
        border-radius: 16px;
        padding: 10px 14px;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        text-align: center;
      }

      .menu-footer-contact {
        justify-content: center;
        gap: 8px;
      }

      .menu-footer-hours {
        border-left: none;
        padding-left: 0;
        width: 100%;
        text-align: center;
      }

      .menu-view-all-btn {
        width: 100%;
        justify-content: center;
        min-height: 44px;
      }
    }

    """

c = c[:start] + hero_3d_menu_css + c[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Applied Hero 3D Overflowing Tray styles successfully!")
