import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update CSS
start_css = c.find('/* ---------- SECTION 4 : MENU')
if start_css == -1:
    print("Error: Could not find start of section 4 menu CSS")
    sys.exit(1)

end_css = c.find('/* ---------- SECTION', start_css + 30)
if end_css == -1:
    end_css = c.find('</style>', start_css)

new_hero_borderless_css = """/* ---------- SECTION 4 : MENU (HERO 3D BORDERLESS TRAY & ZERO OVERFLOW ARCHITECTURE) ---------- */
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
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.7) 0%, transparent 100%);
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(52px, 7.5vh, 76px) clamp(16px, 2.5vw, 40px) clamp(16px, 2.2vh, 26px);
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

    /* Biển gà nghệ thuật: 2 sợi dây thừng chạm sát trần xà nhà (top: 0) */
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

    /* SÂN KHẤU PANORAMA 3D: CÁCH TRẦN >= 45PX, ĐIỀU HƯỚNG THÔNG MINH */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1320px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: clamp(6px, 1vh, 16px) auto 0;
      z-index: 2;
      perspective: 1200px;
    }

    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(430px, 57vh, 490px);
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

    /* Thẻ Card: Mở rộng ôm trọn mâm thức ăn lớn, cấu trúc Flex tuần tự không che chữ */
    .menu-card {
      position: absolute;
      top: 50%;
      left: 50%;
      width: clamp(265px, 23vw, 305px);
      padding: 16px 20px 22px;
      border-radius: 28px;
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

    /* Mâm Thức Ăn Hero: Phóng to cực đại tràn viền, nổi khối 3D đập vào mắt */
    .menu-card-visual {
      position: relative;
      width: 100%;
      height: clamp(200px, 24vh, 235px);
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -30px;
      margin-bottom: 6px;
      z-index: 3;
      transform-style: preserve-3d;
    }

    .menu-card-plate {
      width: clamp(245px, 28vh, 280px);
      height: clamp(245px, 28vh, 280px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 18px 30px rgba(36, 22, 16, 0.26)) drop-shadow(0 4px 10px rgba(36, 22, 16, 0.15));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1), filter 0.45s ease;
      transform-origin: center center;
    }

    /* Animation Thở Hữu Cơ cho Mâm Món Active */
    @keyframes heroTrayBreathe {
      0%, 100% {
        transform: translateZ(30px) rotateX(1.8deg) rotateY(-1.2deg) scale(1);
      }
      50% {
        transform: translateZ(38px) rotateX(-1.2deg) rotateY(1.5deg) scale(1.025);
      }
    }

    /* Thân thẻ: Nằm hoàn toàn tuần tự dưới chân mâm, 100% không bị che */
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
      font-size: clamp(14px, 1.2vw, 16.5px);
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
      font-size: clamp(17px, 1.55vw, 21px);
      font-weight: 900;
      margin: 0 0 5px;
      letter-spacing: 0.03em;
      color: #8A4A1C;
      transition: color 0.35s ease;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(10.5px, 0.85vw, 12px);
      line-height: 1.4;
      font-weight: 300;
      margin: 0 0 12px;
      max-width: 250px;
      color: #4A3C33;
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
      font-size: clamp(11px, 0.9vw, 12.5px);
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(145px, 14vw, 175px);
      height: 36px;
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
      box-shadow: 0 26px 58px rgba(36, 22, 16, 0.16);
      cursor: default;
    }

    .menu-card.is-active:hover {
      transform: translate3d(-50%, -50%, 45px) scale(1) !important;
    }

    .menu-card.is-active .menu-card-plate {
      animation: heroTrayBreathe 6s ease-in-out infinite;
      filter: drop-shadow(0 18px 32px rgba(36, 22, 16, 0.30)) drop-shadow(0 5px 12px rgba(36, 22, 16, 0.18));
    }

    .menu-card.is-active:hover .menu-card-plate {
      animation-play-state: paused;
      transform: translateZ(52px) scale(1.045) !important;
      filter: drop-shadow(0 24px 42px rgba(36, 22, 16, 0.36)) drop-shadow(0 8px 18px rgba(36, 22, 16, 0.22)) !important;
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

    .menu-card:not(.is-active) .menu-card-visual {
      height: clamp(160px, 19vh, 190px);
      margin-top: -12px;
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
      width: clamp(170px, 21vh, 205px);
      height: clamp(170px, 21vh, 205px);
      transform: none !important;
    }

    .menu-card.is-far-prev .menu-card-plate,
    .menu-card.is-far-next .menu-card-plate {
      width: clamp(135px, 17vh, 165px);
      height: clamp(135px, 17vh, 165px);
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
      transform: translate3d(calc(-50% - 176%), calc(-50% + 22px), -90px) scale(0.72) !important;
      opacity: 0.32 !important;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-far-prev:hover {
      transform: translate3d(calc(-50% - 176%), calc(-50% + 16px), -70px) scale(0.75) !important;
      opacity: 0.68 !important;
      box-shadow: 0 12px 24px rgba(36, 22, 16, 0.08);
    }

    /* Far Next (+2) */
    .menu-card.is-far-next {
      transform: translate3d(calc(-50% + 176%), calc(-50% + 22px), -90px) scale(0.72) !important;
      opacity: 0.32 !important;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-far-next:hover {
      transform: translate3d(calc(-50% + 176%), calc(-50% + 16px), -70px) scale(0.75) !important;
      opacity: 0.68 !important;
      box-shadow: 0 12px 24px rgba(36, 22, 16, 0.08);
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
      margin-top: clamp(14px, 2vh, 22px);
      padding: clamp(12px, 1.8vh, 16px) clamp(16px, 2.5vw, 28px);
      background: rgba(255, 255, 255, 0.75);
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
        padding-top: clamp(48px, 7vh, 70px);
      }
      .menu-hero-header {
        left: clamp(10px, 2vw, 20px);
      }
      .menu-rooster-img {
        width: clamp(95px, 10vw, 120px);
      }
      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 82%), calc(-50% + 10px), -40px) scale(0.82) !important;
      }
      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 82%), calc(-50% + 10px), -40px) scale(0.82) !important;
      }
      .menu-card.is-far-prev {
        transform: translate3d(calc(-50% - 155%), calc(-50% + 20px), -80px) scale(0.68) !important;
      }
      .menu-card.is-far-next {
        transform: translate3d(calc(-50% + 155%), calc(-50% + 20px), -80px) scale(0.68) !important;
      }
    }

    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(42px, 6vh, 52px) 12px clamp(12px, 1.8vh, 18px);
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
        margin-top: clamp(24px, 4vh, 36px);
      }

      .menu-carousel-track {
        height: clamp(390px, 54vh, 430px);
      }

      .menu-card {
        width: 82vw;
        max-width: 285px;
        padding: 14px 16px 20px;
      }

      .menu-card-visual {
        height: clamp(175px, 22vh, 205px);
        margin-top: -24px;
      }

      .menu-card-plate {
        width: clamp(210px, 26vh, 250px);
        height: clamp(210px, 26vh, 250px);
      }

      .menu-card.is-active {
        transform: translate3d(-50%, -50%, 40px) scale(1) !important;
      }

      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 66%), calc(-50% + 8px), -40px) scale(0.78) !important;
        opacity: 0.25 !important;
      }

      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 66%), calc(-50% + 8px), -40px) scale(0.78) !important;
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

c = c[:start_css] + new_hero_borderless_css + c[end_css:]

# 2. Update JavaScript
s1_start = c.find('(function () {\n      const track = document.getElementById(\'menuTrack\');')
if s1_start == -1:
    s1_start = c.find('const track = document.getElementById(\'menuTrack\');')
    # expand backwards to (function () {
    s1_start = c.rfind('(function ()', 0, s1_start)

s1_end = c.find('})();', s1_start)
if s1_end != -1:
    s1_end += 5

new_carousel_js = """(function () {
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

      // Smart Click & Tap Navigation (Left half -> prev, Right half -> next)
      track.addEventListener('click', (e) => {
        // Allow CTA order button to navigate naturally
        if (e.target.closest('.menu-card-cta')) return;
        if (hasDragged) return;

        // If clicked specifically on any inactive card
        const clickedCard = e.target.closest('.menu-card');
        if (clickedCard) {
          const idx = Number(clickedCard.dataset.index);
          if (!isNaN(idx) && idx !== currentIndex) {
            e.preventDefault();
            updateCarousel(idx);
            return;
          }
        }

        // Smart hit testing: click left half -> prev, right half -> next
        const rect = track.getBoundingClientRect();
        const clickX = e.clientX;
        const centerX = rect.left + rect.width / 2;
        const deadZone = 55; // safe center buffer on the active card body
        if (clickX < centerX - deadZone) {
          e.preventDefault();
          updateCarousel(currentIndex - 1);
        } else if (clickX > centerX + deadZone) {
          e.preventDefault();
          updateCarousel(currentIndex + 1);
        }
      });

      // Pagination dots click
      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => updateCarousel(idx));
      });

      // Mouse drag-to-slide
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

      // Touch / swipe for mobile
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

      // Keyboard arrow keys
      window.addEventListener('keydown', (e) => {
        const menuSec = document.getElementById('menu');
        if (!menuSec) return;
        const rect = menuSec.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
          if (e.key === 'ArrowLeft') updateCarousel(currentIndex - 1);
          else if (e.key === 'ArrowRight') updateCarousel(currentIndex + 1);
        }
      });

      updateCarousel(0);
    })();"""

c = c[:s1_start] + new_carousel_js + c[s1_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: index.html updated with borderless 3D hero tray and smart left/right navigation!")
