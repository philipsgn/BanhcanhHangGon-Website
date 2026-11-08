import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #menu and background overlay rules
old_menu_section = """    /* ---------- SECTION 4 : MENU (ROYAL GOLD METALLIC CENTER & PURE FLOATING DISH PANORAMA) ---------- */
    #menu {
      position: relative;
      min-height: 100vh;
      min-height: 100svh;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      background-color: #F8E2B3;
      background-image:
        radial-gradient(circle at 50% 36%, rgba(255, 255, 255, 0.76) 0%, rgba(255, 255, 255, 0.22) 58%, transparent 92%),
        url('images/menu/menu-bg-3.webp');
      background-position: center center;
      background-size: cover;
      background-repeat: no-repeat;
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
    }"""

new_menu_section = """    /* ---------- SECTION 4 : MENU (GIANT HERO DISH, SOFT PARCHMENT BG & ELEVATED TYPOGRAPHY) ---------- */
    #menu {
      position: relative;
      min-height: clamp(800px, 100vh, 960px);
      min-height: clamp(800px, 100svh, 960px);
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      background-color: #FAF5EB; /* Nền kem ngà tự nhiên ấm áp, sạch sẽ */
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(42px, 5.5vh, 60px) clamp(16px, 2.5vw, 40px) clamp(16px, 2.2vh, 24px);
    }

    /* Lớp nền menu-bg-3 được làm mờ 76% và khử nhiễu hạt để tôn vinh món ăn tuyệt đối */
    #menu::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url('images/menu/menu-bg-3.webp');
      background-position: center center;
      background-size: cover;
      background-repeat: no-repeat;
      opacity: 0.22; /* Làm mờ 78%, chỉ giữ lại hơi thở giấy mộc thoang thoảng */
      filter: blur(1.5px);
      z-index: 0;
      pointer-events: none;
    }

    /* Vầng sáng hữu cơ dịu mắt ở trung tâm làm bừng sáng mâm gà ta */
    #menu::after {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 36%, rgba(255, 255, 255, 0.88) 0%, rgba(255, 255, 255, 0.35) 55%, transparent 95%);
      z-index: 1;
      pointer-events: none;
    }

    /* Ẩn họa tiết hình thoi thừa để chống rối mắt theo yêu cầu của quý khách */
    .menu-decor-pattern {
      display: none !important;
    }"""

if old_menu_section in content:
    content = content.replace(old_menu_section, new_menu_section)
    print("Updated #menu background & hidden decor pattern successfully.")
else:
    print("#menu section pattern not matched!")

# 2. Update .menu-stage-wrapper and .menu-carousel-track
old_stage_track = """    .menu-stage-wrapper {
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
    }"""

new_stage_track = """    .menu-stage-wrapper {
      position: relative;
      max-width: 1540px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: clamp(0px, 0.4vh, 6px) auto 0;
      z-index: 2;
      perspective: 1500px;
    }

    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(680px, 78vh, 800px);
      display: flex;
      align-items: center;
      justify-content: center;
      transform-style: preserve-3d;
      margin: 0;
      cursor: grab;
      user-select: none;
    }"""

if old_stage_track in content:
    content = content.replace(old_stage_track, new_stage_track)
    print("Updated stage and track dimensions successfully.")
else:
    print("Stage/track pattern not matched!")

# 3. Update Giant Dishes and Elevated Typography
old_dish_and_body_pattern = r'/\* =+\s*1\. MÂM THỨC ĂN KHỔNG LỒ.*?(?=/\* =+\s*3\. CÁC MÓN PHỤ)'
match_dish = re.search(old_dish_and_body_pattern, content, re.DOTALL)

new_dish_and_body = """/* ==========================================================================
       1. MÂM THỨC ĂN PHÓNG ĐẠI KHỔNG LỒ X5 (GIANT HERO DISH X5)
       ========================================================================== */
    .menu-card-visual {
      position: relative;
      width: clamp(470px, 54vh, 580px);
      height: clamp(470px, 54vh, 580px);
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: -20px; /* Đáy mâm tì tự nhiên, khoảng thở thanh thoát với chữ */
      z-index: 5;
      transform-style: preserve-3d;
    }

    .menu-card-plate {
      width: 100%;
      height: 100%;
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 32px 50px rgba(35, 18, 10, 0.32)) drop-shadow(0 10px 20px rgba(35, 18, 10, 0.18));
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
       2. THẺ KHÔNG KHUNG VIỀN TỐI GIẢN & TYPOGRAPHY PHÓNG TO SẮC NÉT
       ========================================================================== */
    .menu-card.is-active .menu-card-body {
      position: relative;
      width: clamp(340px, 34vw, 480px);
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      padding: clamp(6px, 1vh, 10px) clamp(14px, 1.8vw, 24px) 0;
      box-shadow: none !important;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      z-index: 3;
      transform: translateZ(20px);
      transition: all 0.4s ease;
    }

    /* Keyframes trượt nhẹ nhàng, không lag, không tốn RAM */
    @keyframes gentleSlideUp {
      0% {
        opacity: 0;
        transform: translateY(14px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .menu-card.is-active .menu-card-title {
      font-family: 'Playfair Display', 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(26px, 2.3vw, 34px);
      font-weight: 700;
      letter-spacing: 0.015em;
      margin: 0 0 6px;
      line-height: 1.22;
      color: #24120A;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    .menu-card.is-active .menu-card-price {
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(26px, 2.4vw, 34px);
      font-weight: 800;
      margin: 0 0 8px;
      letter-spacing: 0.01em;
      color: #BD3C0D;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.7);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.04s both;
    }

    .menu-card.is-active .menu-card-desc {
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14px, 1.05vw, 16px);
      line-height: 1.55;
      font-weight: 400;
      margin: 0 0 18px;
      max-width: 440px;
      color: #4A3528;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.08s both;
    }

    .menu-card.is-active .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13.5px, 1.1vw, 15px);
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(180px, 16vw, 220px);
      height: 46px;
      background: linear-gradient(135deg, #8A2B0E 0%, #C24A22 100%);
      border: none;
      color: #FFFDF5;
      box-shadow: 0 6px 20px rgba(138, 43, 14, 0.28);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.12s both;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: linear-gradient(135deg, #9C3312 0%, #D45328 100%);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(138, 43, 14, 0.38);
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
      transform: translateZ(55px) scale(1.035) !important;
      filter: drop-shadow(0 38px 58px rgba(35, 18, 10, 0.40)) drop-shadow(0 14px 26px rgba(35, 18, 10, 0.25)) !important;
    }

    """

if match_dish:
    content = content[:match_dish.start()] + new_dish_and_body + content[match_dish.end():]
    print("Updated Giant Hero Dish & Elevated Typography successfully.")
else:
    print("Dish and body block regex not matched!")

# 4. Update Inactive Dishes (Zoom x2 - x3 for near and far dishes)
old_flanking_pattern = r'/\* Near Dishes.*?/\* Ẩn thẻ ngoài phạm vi 5 món \*/'
match_flank = re.search(old_flanking_pattern, content, re.DOTALL)

new_flanking = """/* Near Dishes (Món Kề Bên: Phóng to x2-x3 lên 340-410px, dãn rộng ±110%) */
    .menu-card.is-near-prev .menu-card-visual,
    .menu-card.is-near-next .menu-card-visual {
      width: clamp(330px, 38vh, 410px);
      height: clamp(330px, 38vh, 410px);
    }

    .menu-card.is-near-prev {
      transform: translate3d(calc(-50% - 110%), calc(-50% + 14px), -40px) scale(0.88) !important;
      opacity: 0.72 !important;
      z-index: 4;
    }

    .menu-card.is-near-prev:hover {
      transform: translate3d(calc(-50% - 110%), calc(-50% + 8px), -24px) scale(0.92) !important;
      opacity: 0.95 !important;
    }

    .menu-card.is-near-next {
      transform: translate3d(calc(-50% + 110%), calc(-50% + 14px), -40px) scale(0.88) !important;
      opacity: 0.72 !important;
      z-index: 4;
    }

    .menu-card.is-near-next:hover {
      transform: translate3d(calc(-50% + 110%), calc(-50% + 8px), -24px) scale(0.92) !important;
      opacity: 0.95 !important;
    }

    /* Far Dishes (Món Ở Xa: Phóng to x2-x3 lên 250-310px, dãn rộng ±215%) */
    .menu-card.is-far-prev .menu-card-visual,
    .menu-card.is-far-next .menu-card-visual {
      width: clamp(250px, 29vh, 310px);
      height: clamp(250px, 29vh, 310px);
    }

    .menu-card.is-far-prev {
      transform: translate3d(calc(-50% - 215%), calc(-50% + 24px), -80px) scale(0.74) !important;
      opacity: 0.45 !important;
      z-index: 2;
    }

    .menu-card.is-far-prev:hover {
      transform: translate3d(calc(-50% - 215%), calc(-50% + 18px), -60px) scale(0.78) !important;
      opacity: 0.80 !important;
    }

    .menu-card.is-far-next {
      transform: translate3d(calc(-50% + 215%), calc(-50% + 24px), -80px) scale(0.74) !important;
      opacity: 0.45 !important;
      z-index: 2;
    }

    .menu-card.is-far-next:hover {
      transform: translate3d(calc(-50% + 215%), calc(-50% + 18px), -60px) scale(0.78) !important;
      opacity: 0.80 !important;
    }

    /* Ẩn thẻ ngoài phạm vi 5 món */"""

if match_flank:
    content = content[:match_flank.start()] + new_flanking + content[match_flank.end() - len('/* Ẩn thẻ ngoài phạm vi 5 món */'):]
    print("Updated Flanking Dishes x2-x3 successfully.")
else:
    print("Flanking dishes pattern not matched!")

# 5. Mobile & Tablet responsive updates
old_mob_block = """      .menu-carousel-track {
        height: clamp(450px, 60vh, 500px);
      }

      .menu-card-visual {
        width: clamp(280px, 34vh, 320px);
        height: clamp(280px, 34vh, 320px);
        margin-bottom: -30px;
      }

      .menu-card.is-active .menu-card-body {
        width: 88vw;
        max-width: 310px;
        padding: 6px 10px 0;
      }"""

new_mob_block = """      .menu-carousel-track {
        height: clamp(580px, 72vh, 670px);
      }

      .menu-card-visual {
        width: clamp(320px, 42vh, 390px);
        height: clamp(320px, 42vh, 390px);
        margin-bottom: -18px;
      }

      .menu-card.is-active .menu-card-body {
        width: 90vw;
        max-width: 340px;
        padding: 6px 10px 0;
      }

      .menu-card.is-active .menu-card-title {
        font-size: clamp(22px, 5.8vw, 28px);
      }

      .menu-card.is-active .menu-card-price {
        font-size: clamp(22px, 5.8vw, 28px);
      }

      .menu-card.is-active .menu-card-desc {
        font-size: clamp(13px, 3.5vw, 15px);
        max-width: 310px;
      }

      .menu-card.is-active .menu-card-cta {
        width: 175px;
        height: 42px;
        font-size: 13.5px;
      }"""

if old_mob_block in content:
    content = content.replace(old_mob_block, new_mob_block)
    print("Updated Mobile dimensions successfully.")
else:
    print("Mobile block not matched!")

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("ALL GIANT ZOOM & SOFT BG UPDATES APPLIED SUCCESSFULLY!")
