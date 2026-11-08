import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start_css = c.find('/* ---------- SECTION 4 : MENU')
if start_css == -1:
    print("Error: Could not find start of section 4 menu CSS")
    sys.exit(1)

end_css = c.find('/* ---------- SECTION', start_css + 30)
if end_css == -1:
    end_css = c.find('</style>', start_css)

giant_hero_wood_plaque_css = """/* ---------- SECTION 4 : MENU (GIANT FLOATING HERO DISH & COMPACT RUSTIC WOOD PLAQUE) ---------- */
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
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.75) 0%, transparent 100%);
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(48px, 6.8vh, 68px) clamp(16px, 2.5vw, 40px) clamp(16px, 2.2vh, 24px);
    }

    .menu-decor-pattern {
      position: absolute;
      left: 0;
      top: 12%;
      width: clamp(60px, 8vw, 130px);
      height: 76%;
      background-repeat: repeat-y;
      background-size: 100% auto;
      background-image: url("data:image/svg+xml,%3Csvg width='80' height='160' viewBox='0 0 80 160' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 40L40 0L80 40L40 80L0 40Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Cpath d='M0 120L40 80L80 120L40 160L0 120Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Ccircle cx='40' cy='40' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3Ccircle cx='40' cy='120' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 0;
      opacity: 0.85;
    }

    /* Biển gà nghệ thuật: 2 sợi dây thừng chạm sát mép trần trên (top: 0) */
    .menu-hero-header {
      position: absolute;
      top: 0;
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
      width: clamp(110px, 11vw, 145px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 10px 20px rgba(45, 26, 18, 0.14));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.02) translateY(-2px);
    }

    /* SÂN KHẤU PANORAMA 3D: CUNG CẤP KHÔNG GIAN CHO MÂM KHỔNG LỒ VÀ ĐẾ GỖ */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1360px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: clamp(4px, 0.8vh, 12px) auto 0;
      z-index: 2;
      perspective: 1200px;
    }

    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(480px, 62vh, 550px);
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

    /* Thẻ Card: Không có khung hộp màu be bọc ảnh, trong suốt hoàn toàn */
    .menu-card {
      position: absolute;
      top: 50%;
      left: 50%;
      width: auto;
      padding: 0;
      border-radius: 0;
      border: none !important;
      background: transparent !important;
      box-shadow: none !important;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transform-style: preserve-3d;
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1),
                  opacity 0.4s ease;
      will-change: transform, opacity;
      cursor: pointer;
    }

    /* ==========================================================================
       1. MÂM THỨC ĂN KHỔNG LỒ NẰM HOÀN TOÀN NGOÀI CARD (GIANT FLOATING DISH)
       ========================================================================== */
    .menu-card-visual {
      position: relative;
      width: clamp(330px, 36vh, 385px);
      height: clamp(330px, 36vh, 385px);
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: -36px; /* Đáy mâm tì tự nhiên lên gờ bệ gỗ */
      z-index: 5;
      transform-style: preserve-3d;
    }

    .menu-card-plate {
      width: 100%;
      height: 100%;
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 24px 38px rgba(28, 16, 10, 0.36)) drop-shadow(0 8px 16px rgba(28, 16, 10, 0.22));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1), filter 0.45s ease;
      transform-origin: center center;
    }

    /* Animation Thở Hữu Cơ cho Mâm Món Active */
    @keyframes heroTrayBreathe {
      0%, 100% {
        transform: translateZ(35px) rotateX(1.8deg) rotateY(-1.2deg) scale(1);
      }
      50% {
        transform: translateZ(44px) rotateX(-1.2deg) rotateY(1.5deg) scale(1.025);
      }
    }

    /* ==========================================================================
       2. BỆ GỖ KHẮC CHỮ TỐI GIẢN (RUSTIC WOOD BASE PLAQUE)
       ========================================================================== */
    .menu-card-body {
      position: relative;
      width: clamp(270px, 24vw, 315px);
      background: linear-gradient(165deg, #2D1A12 0%, #1A0D07 100%);
      border: 1px solid rgba(212, 163, 89, 0.40);
      border-radius: 22px;
      padding: clamp(14px, 1.8vh, 18px) clamp(16px, 2vw, 22px) clamp(16px, 2vh, 20px);
      box-shadow: 0 20px 42px rgba(22, 11, 6, 0.35), inset 0 1px 0 rgba(255, 225, 160, 0.16);
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      z-index: 3;
      transform: translateZ(15px);
      transition: all 0.4s ease;
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14px, 1.2vw, 16.5px);
      font-weight: 800;
      letter-spacing: 0.04em;
      margin: 0 0 4px;
      text-transform: uppercase;
      line-height: 1.25;
      color: #F5D061;
      text-shadow: 0 1px 3px rgba(0, 0, 0, 0.6);
      transition: color 0.35s ease;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(18px, 1.6vw, 22px);
      font-weight: 900;
      margin: 0 0 6px;
      letter-spacing: 0.03em;
      color: #FFA834;
      text-shadow: 0 1px 4px rgba(0, 0, 0, 0.5);
      transition: color 0.35s ease;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(10.5px, 0.85vw, 12px);
      line-height: 1.42;
      font-weight: 300;
      margin: 0 0 12px;
      max-width: 260px;
      color: #D4C4B5;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(11.5px, 0.9vw, 12.5px);
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(145px, 14vw, 175px);
      height: 36px;
      background: linear-gradient(135deg, #C47A3B 0%, #A85A22 100%);
      color: #FFFFFF;
      box-shadow: 0 6px 16px rgba(168, 90, 34, 0.38);
      transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
    }

    /* Active Card Behavior */
    .menu-card.is-active {
      transform: translate3d(-50%, -50%, 45px) scale(1) !important;
      opacity: 1 !important;
      z-index: 6;
      cursor: default;
    }

    .menu-card.is-active:hover {
      transform: translate3d(-50%, -50%, 45px) scale(1) !important;
    }

    .menu-card.is-active .menu-card-plate {
      animation: heroTrayBreathe 6s ease-in-out infinite;
    }

    .menu-card.is-active:hover .menu-card-plate {
      animation-play-state: paused;
      transform: translateZ(55px) scale(1.045) !important;
      filter: drop-shadow(0 30px 48px rgba(28, 16, 10, 0.44)) drop-shadow(0 10px 20px rgba(28, 16, 10, 0.28)) !important;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: linear-gradient(135deg, #DB8E4C 0%, #B8672B 100%);
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(196, 122, 59, 0.45);
    }

    /* ==========================================================================
       3. CÁC MÓN PHỤ LÀM MỜ HAI BÊN (TIERED PANORAMA INACTIVE)
       ========================================================================== */
    .menu-card:not(.is-active) .menu-card-visual {
      width: clamp(200px, 23vh, 240px);
      height: clamp(200px, 23vh, 240px);
      margin-bottom: -22px;
    }

    .menu-card:not(.is-active) .menu-card-body {
      width: clamp(210px, 18vw, 245px);
      background: linear-gradient(165deg, rgba(45, 26, 18, 0.88) 0%, rgba(26, 13, 7, 0.88) 100%);
      border: 1px solid rgba(212, 163, 89, 0.22);
      border-radius: 18px;
      padding: 10px 14px 12px;
      box-shadow: 0 10px 24px rgba(22, 11, 6, 0.20);
    }

    .menu-card:not(.is-active) .menu-card-title {
      font-size: clamp(12px, 1vw, 13.5px);
      color: rgba(245, 208, 97, 0.85);
      margin-bottom: 2px;
    }

    .menu-card:not(.is-active) .menu-card-price {
      font-size: clamp(15px, 1.3vw, 17px);
      color: rgba(255, 168, 52, 0.85);
      margin-bottom: 4px;
    }

    .menu-card:not(.is-active) .menu-card-desc {
      font-size: 10px;
      color: rgba(212, 196, 181, 0.75);
      margin-bottom: 8px;
      -webkit-line-clamp: 1;
    }

    .menu-card:not(.is-active) .menu-card-cta {
      background: transparent;
      color: #FFA834;
      border: 1px solid rgba(255, 168, 52, 0.5);
      padding: 4px 14px;
      height: 28px;
      font-size: 10.5px;
      box-shadow: none;
    }

    /* Kích thước đĩa thẻ mờ */
    .menu-card.is-near-prev .menu-card-plate,
    .menu-card.is-near-next .menu-card-plate {
      transform: none !important;
    }

    .menu-card.is-far-prev .menu-card-visual,
    .menu-card.is-far-next .menu-card-visual {
      width: clamp(150px, 18vh, 180px);
      height: clamp(150px, 18vh, 180px);
      margin-bottom: -16px;
    }

    .menu-card.is-far-prev .menu-card-body,
    .menu-card.is-far-next .menu-card-body {
      width: clamp(170px, 15vw, 195px);
      padding: 8px 10px 10px;
    }

    /* Tọa độ 3D & Hover thẻ mờ */
    /* Near Prev (-1) */
    .menu-card.is-near-prev {
      transform: translate3d(calc(-50% - 92%), calc(-50% + 14px), -40px) scale(0.85) !important;
      opacity: 0.62 !important;
      z-index: 4;
    }

    .menu-card.is-near-prev:hover {
      transform: translate3d(calc(-50% - 92%), calc(-50% + 8px), -24px) scale(0.88) !important;
      opacity: 0.90 !important;
    }

    /* Near Next (+1) */
    .menu-card.is-near-next {
      transform: translate3d(calc(-50% + 92%), calc(-50% + 14px), -40px) scale(0.85) !important;
      opacity: 0.62 !important;
      z-index: 4;
    }

    .menu-card.is-near-next:hover {
      transform: translate3d(calc(-50% + 92%), calc(-50% + 8px), -24px) scale(0.88) !important;
      opacity: 0.90 !important;
    }

    /* Far Prev (-2) */
    .menu-card.is-far-prev {
      transform: translate3d(calc(-50% - 176%), calc(-50% + 24px), -90px) scale(0.72) !important;
      opacity: 0.32 !important;
      z-index: 2;
    }

    .menu-card.is-far-prev:hover {
      transform: translate3d(calc(-50% - 176%), calc(-50% + 18px), -70px) scale(0.75) !important;
      opacity: 0.70 !important;
    }

    /* Far Next (+2) */
    .menu-card.is-far-next {
      transform: translate3d(calc(-50% + 176%), calc(-50% + 24px), -90px) scale(0.72) !important;
      opacity: 0.32 !important;
      z-index: 2;
    }

    .menu-card.is-far-next:hover {
      transform: translate3d(calc(-50% + 176%), calc(-50% + 18px), -70px) scale(0.75) !important;
      opacity: 0.70 !important;
    }

    /* Ẩn thẻ ngoài phạm vi 5 món */
    .menu-card.is-hidden {
      display: none !important;
    }

    /* Chấm điều hướng phân trang */
    .menu-dots {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
      margin: clamp(12px, 1.8vh, 18px) auto 0;
      padding: 0;
      z-index: 10;
    }

    .menu-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background-color: #D6C7B2;
      border: none;
      padding: 0;
      cursor: pointer;
      transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-dot:hover {
      background-color: #B56E35;
      transform: scale(1.2);
    }

    .menu-dot.is-active {
      width: 32px;
      border-radius: 999px;
      background-color: #9E5E2B;
      box-shadow: 0 2px 6px rgba(158, 94, 43, 0.35);
    }

    /* Thanh Footer Menu */
    .menu-footer-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      max-width: 1200px;
      margin-top: clamp(14px, 2vh, 20px);
      padding: clamp(12px, 1.8vh, 16px) clamp(16px, 2.5vw, 28px);
      background: rgba(255, 255, 255, 0.78);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border-radius: 20px;
      border: 1px solid rgba(201, 154, 74, 0.18);
      box-sizing: border-box;
      z-index: 5;
    }

    .menu-footer-contact {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .menu-footer-tagline {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #8A4A1C;
    }

    .menu-footer-phone {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(16px, 1.5vw, 19px);
      font-weight: 800;
      color: #1A1410;
      text-decoration: none;
      transition: color 0.3s ease;
    }

    .menu-footer-phone:hover {
      color: #9E5E2B;
    }

    .menu-footer-hours {
      font-size: 11px;
      color: #7A685D;
    }

    .menu-view-all-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #1A1410;
      color: #FAF8F5;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12px, 1vw, 13.5px);
      font-weight: 700;
      letter-spacing: 0.03em;
      text-decoration: none;
      padding: 10px 22px;
      border-radius: 999px;
      transition: all 0.35s ease;
    }

    .menu-view-all-btn:hover {
      background: #8A4A1C;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(138, 74, 28, 0.3);
    }

    /* RESPONSIVE QUERIES DÀNH CHO CẢ MÀN HÌNH LAPTOP & DI ĐỘNG */
    @media (max-width: 1024px) {
      #menu {
        padding-top: clamp(45px, 6.5vh, 65px);
      }
      .menu-hero-header {
        left: clamp(10px, 2vw, 20px);
      }
      .menu-rooster-img {
        width: clamp(95px, 10vw, 120px);
      }
      .menu-card-visual {
        width: clamp(290px, 32vh, 340px);
        height: clamp(290px, 32vh, 340px);
      }
      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 80%), calc(-50% + 12px), -40px) scale(0.82) !important;
      }
      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 80%), calc(-50% + 12px), -40px) scale(0.82) !important;
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
        padding: clamp(40px, 5.5vh, 50px) 12px clamp(12px, 1.8vh, 16px);
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: 0;
        left: 12px;
        margin: 0;
        padding: 0;
        z-index: 6;
      }

      .menu-rooster-img {
        width: clamp(75px, 18vw, 90px);
      }

      .menu-stage-wrapper {
        margin-top: clamp(20px, 3.5vh, 32px);
      }

      .menu-carousel-track {
        height: clamp(430px, 58vh, 480px);
      }

      .menu-card-visual {
        width: clamp(260px, 31vh, 300px);
        height: clamp(260px, 31vh, 300px);
        margin-bottom: -28px;
      }

      .menu-card-body {
        width: 82vw;
        max-width: 285px;
        padding: 12px 14px 16px;
      }

      .menu-card.is-active {
        transform: translate3d(-50%, -50%, 40px) scale(1) !important;
      }

      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 66%), calc(-50% + 10px), -40px) scale(0.78) !important;
        opacity: 0.25 !important;
      }

      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 66%), calc(-50% + 10px), -40px) scale(0.78) !important;
        opacity: 0.25 !important;
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
        align-items: center;
      }
    }
"""

c = c[:start_css] + giant_hero_wood_plaque_css + c[end_css:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: index.html updated with giant floating hero dish and rustic wood plaque base!")
