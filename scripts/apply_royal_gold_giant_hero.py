import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update Google Fonts to add Cinzel
old_font = 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Be+Vietnam+Pro:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap'
new_font = 'https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Be+Vietnam+Pro:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap'
if old_font in c:
    c = c.replace(old_font, new_font)
    print("Google Fonts updated with Cinzel!")

# 2. Fix image path leading slashes in Behind-the-Scenes & other sections
c = c.replace('src="/images/behind-scenes/', 'src="images/behind-scenes/')
c = c.replace('src="/images/testimonials-bg', 'src="images/testimonials-bg')
c = c.replace('src="/images/icon-shopee', 'src="images/icon-shopee')
c = c.replace('src="/images/icon-grab-food', 'src="images/icon-grab-food')
c = c.replace('src="/images/home/new-chicken-chef-desktop', 'src="images/home/new-chicken-chef-desktop')
c = c.replace('src="/images/menu/icon-quan-an', 'src="images/menu/icon-quan-an')

# 3. Update Section 4 Menu CSS
start_css = c.find('/* ---------- SECTION 4 : MENU')
if start_css == -1:
    print("Error: Could not find start of section 4 menu CSS")
    sys.exit(1)

end_css = c.find('/* ---------- SECTION', start_css + 30)
if end_css == -1:
    end_css = c.find('</style>', start_css)

royal_gold_css = """/* ---------- SECTION 4 : MENU (ROYAL GOLD METALLIC CENTER & PURE FLOATING DISH PANORAMA) ---------- */
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

    /* SÂN KHẤU PANORAMA 3D RẢI RỘNG KHÔNG GIAN */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1440px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: clamp(4px, 0.8vh, 12px) auto 0;
      z-index: 2;
      perspective: 1400px;
    }

    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(500px, 64vh, 570px);
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

    /* Thẻ Card: Mặc định trong suốt 100% không viền không hộp */
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
       1. MÂM THỨC ĂN KHỔNG LỒ X3-X4 NẰM NGOÀI CARD (GIANT FLOATING DISH)
       ========================================================================== */
    .menu-card-visual {
      position: relative;
      width: clamp(370px, 43vh, 440px);
      height: clamp(370px, 43vh, 440px);
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: -38px; /* Đáy mâm tì tự nhiên lên gờ đế vàng kim */
      z-index: 5;
      transform-style: preserve-3d;
    }

    .menu-card-plate {
      width: 100%;
      height: 100%;
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 26px 42px rgba(28, 16, 10, 0.38)) drop-shadow(0 8px 18px rgba(28, 16, 10, 0.24));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1), filter 0.45s ease;
      transform-origin: center center;
    }

    /* Animation Thở Hữu Cơ cho Mâm Món Active */
    @keyframes heroTrayBreathe {
      0%, 100% {
        transform: translateZ(35px) rotateX(1.8deg) rotateY(-1.2deg) scale(1);
      }
      50% {
        transform: translateZ(46px) rotateX(-1.2deg) rotateY(1.5deg) scale(1.025);
      }
    }

    /* ==========================================================================
       2. ĐẾ THẺ HOÀNG GIA VÀNG KIM 24K BLING BLING (ROYAL LUXURY GOLD METALLIC)
       ========================================================================== */
    .menu-card.is-active .menu-card-body {
      position: relative;
      width: clamp(285px, 25vw, 335px);
      background:
        radial-gradient(ellipse at 50% -20%, rgba(255, 250, 220, 0.98) 0%, transparent 60%),
        linear-gradient(145deg, #FFF9EA 0%, #FBE599 22%, #DCA74E 50%, #FAF0C8 78%, #B8822A 100%);
      border: 1.5px solid rgba(255, 215, 0, 0.92);
      border-radius: 24px;
      padding: clamp(15px, 2vh, 19px) clamp(18px, 2.2vw, 24px) clamp(16px, 2vh, 20px);
      box-shadow:
        0 0 28px rgba(255, 215, 0, 0.35),
        0 22px 50px rgba(70, 37, 7, 0.28),
        inset 0 1px 2px rgba(255, 255, 255, 0.95),
        inset 0 -2px 4px rgba(138, 74, 28, 0.35);
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      z-index: 3;
      transform: translateZ(20px);
      transition: all 0.4s ease;
    }

    .menu-card.is-active .menu-card-title {
      font-family: 'Cinzel', 'Cormorant Garamond', serif;
      font-size: clamp(15px, 1.3vw, 17.5px);
      font-weight: 800;
      letter-spacing: 0.05em;
      margin: 0 0 4px;
      text-transform: uppercase;
      line-height: 1.25;
      color: #522703;
      text-shadow: 0 1px 1px rgba(255, 255, 255, 0.8), 0 2px 4px rgba(82, 39, 3, 0.22);
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-price {
      font-family: 'Cinzel', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(19px, 1.7vw, 23px);
      font-weight: 900;
      margin: 0 0 6px;
      letter-spacing: 0.03em;
      color: #8E1E0B;
      text-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(10.5px, 0.85vw, 12px);
      line-height: 1.42;
      font-weight: 400;
      margin: 0 0 12px;
      max-width: 270px;
      color: #4A2E12;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      transition: opacity 0.35s ease;
    }

    .menu-card.is-active .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Cinzel', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(11.5px, 0.9vw, 12.5px);
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(145px, 14vw, 175px);
      height: 36px;
      background: linear-gradient(135deg, #8A2B0E 0%, #C94A1E 50%, #8A2B0E 100%);
      border: 1px solid rgba(255, 215, 0, 0.65);
      color: #FFFDF0;
      box-shadow: 0 4px 14px rgba(138, 43, 14, 0.38), 0 0 10px rgba(255, 215, 0, 0.25);
      transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: linear-gradient(135deg, #A03412 0%, #DE5525 50%, #A03412 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(138, 43, 14, 0.45), 0 0 14px rgba(255, 215, 0, 0.4);
    }

    /* Active Card Coordinates */
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
      filter: drop-shadow(0 32px 52px rgba(28, 16, 10, 0.46)) drop-shadow(0 12px 22px rgba(28, 16, 10, 0.30)) !important;
    }

    /* ==========================================================================
       3. CÁC MÓN PHỤ: RẢI RỘNG RA 2 BÊN & ẨN 100% CARD BO, CHỮ, NÚT BẤM
       ========================================================================== */
    .menu-card:not(.is-active) .menu-card-body {
      display: none !important;
    }

    .menu-card:not(.is-active) .menu-card-visual {
      margin: 0 !important;
    }

    /* Near Dishes (Món Kề Bên: Dãn rộng ra ±116%) */
    .menu-card.is-near-prev .menu-card-visual,
    .menu-card.is-near-next .menu-card-visual {
      width: clamp(220px, 26vh, 265px);
      height: clamp(220px, 26vh, 265px);
    }

    .menu-card.is-near-prev {
      transform: translate3d(calc(-50% - 116%), calc(-50% + 14px), -40px) scale(0.85) !important;
      opacity: 0.65 !important;
      z-index: 4;
    }

    .menu-card.is-near-prev:hover {
      transform: translate3d(calc(-50% - 116%), calc(-50% + 8px), -24px) scale(0.89) !important;
      opacity: 0.92 !important;
    }

    .menu-card.is-near-next {
      transform: translate3d(calc(-50% + 116%), calc(-50% + 14px), -40px) scale(0.85) !important;
      opacity: 0.65 !important;
      z-index: 4;
    }

    .menu-card.is-near-next:hover {
      transform: translate3d(calc(-50% + 116%), calc(-50% + 8px), -24px) scale(0.89) !important;
      opacity: 0.92 !important;
    }

    /* Far Dishes (Món Ở Xa: Dãn rộng ra ±225%) */
    .menu-card.is-far-prev .menu-card-visual,
    .menu-card.is-far-next .menu-card-visual {
      width: clamp(160px, 19vh, 200px);
      height: clamp(160px, 19vh, 200px);
    }

    .menu-card.is-far-prev {
      transform: translate3d(calc(-50% - 225%), calc(-50% + 24px), -90px) scale(0.70) !important;
      opacity: 0.35 !important;
      z-index: 2;
    }

    .menu-card.is-far-prev:hover {
      transform: translate3d(calc(-50% - 225%), calc(-50% + 18px), -70px) scale(0.74) !important;
      opacity: 0.72 !important;
    }

    .menu-card.is-far-next {
      transform: translate3d(calc(-50% + 225%), calc(-50% + 24px), -90px) scale(0.70) !important;
      opacity: 0.35 !important;
      z-index: 2;
    }

    .menu-card.is-far-next:hover {
      transform: translate3d(calc(-50% + 225%), calc(-50% + 18px), -70px) scale(0.74) !important;
      opacity: 0.72 !important;
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
      background: linear-gradient(90deg, #DCA74E 0%, #C94A1E 100%);
      box-shadow: 0 2px 8px rgba(220, 167, 78, 0.5);
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
        width: clamp(320px, 36vh, 370px);
        height: clamp(320px, 36vh, 370px);
      }
      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 95%), calc(-50% + 12px), -40px) scale(0.82) !important;
      }
      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 95%), calc(-50% + 12px), -40px) scale(0.82) !important;
      }
      .menu-card.is-far-prev {
        transform: translate3d(calc(-50% - 185%), calc(-50% + 22px), -80px) scale(0.68) !important;
      }
      .menu-card.is-far-next {
        transform: translate3d(calc(-50% + 185%), calc(-50% + 22px), -80px) scale(0.68) !important;
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
        height: clamp(450px, 60vh, 500px);
      }

      .menu-card-visual {
        width: clamp(280px, 34vh, 320px);
        height: clamp(280px, 34vh, 320px);
        margin-bottom: -30px;
      }

      .menu-card.is-active .menu-card-body {
        width: 84vw;
        max-width: 295px;
        padding: 14px 16px 18px;
      }

      .menu-card.is-active {
        transform: translate3d(-50%, -50%, 40px) scale(1) !important;
      }

      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 78%), calc(-50% + 10px), -40px) scale(0.78) !important;
        opacity: 0.28 !important;
      }

      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 78%), calc(-50% + 10px), -40px) scale(0.78) !important;
        opacity: 0.28 !important;
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

c = c[:start_css] + royal_gold_css + c[end_css:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: index.html fully updated with Royal Gold Center & Pure Floating Dish Panorama!")
