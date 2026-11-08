import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #menu CSS padding and sizing
old_menu_css = """    #menu {
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
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.6) 0%, transparent 100%);
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(28px, 3.5vh, 42px) clamp(16px, 2.5vw, 40px) clamp(16px, 2vh, 24px);
    }"""

new_menu_css = """    #menu {
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
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.6) 0%, transparent 100%);
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(14px, 2.2vh, 26px) clamp(12px, 2vw, 32px) clamp(12px, 1.8vh, 18px);
    }"""

assert old_menu_css in content, 'old_menu_css not found!'
content = content.replace(old_menu_css, new_menu_css)

# 2. Update .menu-rooster-img
old_rooster_css = """    /* Ropes reach y=0 to touch the ceiling of #menu - Sát rìa trái thanh thoát */
    .menu-rooster-img {
      width: clamp(170px, 16vw, 230px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 12px 24px rgba(45, 26, 18, 0.16));
      transition: transform 0.4s ease;
    }"""

new_rooster_css = """    /* Ropes reach y=0 to touch the ceiling of #menu - Sát rìa trái thanh thoát */
    .menu-rooster-img {
      width: clamp(125px, 14vw, 175px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 10px 20px rgba(45, 26, 18, 0.14));
      transition: transform 0.4s ease;
    }"""

assert old_rooster_css in content, 'old_rooster_css not found!'
content = content.replace(old_rooster_css, new_rooster_css)

# 3. Update .menu-carousel-track
old_track_css = """    /* Carousel 3D Track - Chiều cao co giãn theo vh, không bị che ở Zoom 100% */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(380px, 48vh, 430px);
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin-top: 0;
      cursor: grab;
      user-select: none;
    }"""

new_track_css = """    /* Carousel 3D Track - Siêu gọn theo vh, vừa khít 100% màn hình Zoom 100% */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(315px, 45vh, 390px);
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin-top: 0;
      cursor: grab;
      user-select: none;
    }"""

assert old_track_css in content, 'old_track_css not found!'
content = content.replace(old_track_css, new_track_css)

# 4. Update .menu-card
old_card_css = """    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(230px, 22vw, 275px);
      padding: 0 18px 22px;
      border-radius: 24px;
      border: none;
      box-sizing: border-box;"""

new_card_css = """    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(215px, 20vw, 260px);
      padding: 0 16px 18px;
      border-radius: 22px;
      border: none;
      box-sizing: border-box;"""

assert old_card_css in content, 'old_card_css not found!'
content = content.replace(old_card_css, new_card_css)

# 5. Update .menu-card-visual & .menu-card-plate
old_vis_plate = """    /* Card Plate Visual: Tỷ lệ co giãn thông minh theo vh, không bị xén đỉnh ở Zoom 100% */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: clamp(-42px, -4.5vh, -35px);
      margin-bottom: clamp(16px, 2vh, 22px);
      z-index: 3;
    }

    .menu-card-plate {
      width: clamp(122px, 16vh, 142px);
      height: clamp(122px, 16vh, 142px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 10px 18px rgba(36, 22, 16, 0.18));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }"""

new_vis_plate = """    /* Card Plate Visual: Tỷ lệ co giãn thông minh theo vh, không bị xén đỉnh ở Zoom 100% */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: clamp(-32px, -3.8vh, -26px);
      margin-bottom: clamp(12px, 1.5vh, 16px);
      z-index: 3;
    }

    .menu-card-plate {
      width: clamp(105px, 14vh, 136px);
      height: clamp(105px, 14vh, 136px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 8px 16px rgba(36, 22, 16, 0.16));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }"""

assert old_vis_plate in content, 'old_vis_plate not found!'
content = content.replace(old_vis_plate, new_vis_plate)

# 6. Update Typography
old_typo = """    .menu-card-title {
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
    }"""

new_typo = """    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13px, 1.15vw, 15.5px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 4px;
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
      font-size: clamp(17px, 1.5vw, 19.5px);
      font-weight: 900;
      margin: 0 0 5px;
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
      font-size: clamp(10px, 0.85vw, 11.5px);
      line-height: 1.38;
      font-weight: 300;
      margin: 0 0 10px;
      max-width: 230px;
      color: #4A3C33;
      transition: opacity 0.35s ease, color 0.35s ease;
    }"""

assert old_typo in content, 'old_typo not found!'
content = content.replace(old_typo, new_typo)

# 7. Update CTA button
old_cta = """    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 190px;
      padding: 9px 20px;
      border-radius: 999px;"""

new_cta = """    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 155px;
      padding: 7px 18px;
      border-radius: 999px;"""

assert old_cta in content, 'old_cta not found!'
content = content.replace(old_cta, new_cta)

# 8. Update Dots & Footer Bar
old_dots_footer = """    /* Pagination Dots (5 món) */
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
    }"""

new_dots_footer = """    /* Pagination Dots (5 món) */
    .menu-dots {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      margin: 6px auto 10px;
      z-index: 4;
    }

    .menu-dot {
      width: 7px;
      height: 7px;
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
      width: 22px;
      border-radius: 999px;
      background: #9E5E2B;
    }

    /* Menu Footer Bar */
    .menu-footer-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      max-width: 680px;
      margin: 2px auto 0;
      padding: 6px 0 0;
      border-top: 1px solid rgba(201, 154, 74, 0.18);
      width: 100%;
      z-index: 3;
    }"""

assert old_dots_footer in content, 'old_dots_footer not found!'
content = content.replace(old_dots_footer, new_dots_footer)

# 9. Update Responsive Media Queries
old_mq = """    @media (max-width: 960px) {
      .menu-hero-header {
        position: absolute;
        top: 0;
        left: clamp(14px, 3vw, 28px);
        margin: 0;
        padding: 0;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(140px, 18vw, 180px);
      }

      .menu-carousel-track {
        height: 460px;
      }"""

new_mq = """    @media (max-width: 960px) {
      .menu-hero-header {
        position: absolute;
        top: 0;
        left: clamp(14px, 3vw, 28px);
        margin: 0;
        padding: 0;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(115px, 16vw, 155px);
      }

      .menu-carousel-track {
        height: clamp(315px, 46vh, 380px);
      }"""

assert old_mq in content, 'old_mq not found!'
content = content.replace(old_mq, new_mq)

old_mq600 = """    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(20px, 3vh, 28px) 12px 18px;
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: 0;
        left: 12px;
        margin: 0;
        padding: 0;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(120px, 24vw, 155px);
      }

      .menu-carousel-track {
        height: 440px;
        margin-top: 0;
      }

      .menu-card {
        width: 82vw;
        max-width: 290px;
        padding: 0 18px 24px;
      }"""

new_mq600 = """    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: 12px 10px 14px;
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: 0;
        left: 10px;
        margin: 0;
        padding: 0;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(100px, 22vw, 130px);
      }

      .menu-carousel-track {
        height: clamp(330px, 48vh, 375px);
        margin-top: 0;
      }

      .menu-card {
        width: 78vw;
        max-width: 260px;
        padding: 0 14px 16px;
      }"""

assert old_mq600 in content, 'old_mq600 not found!'
content = content.replace(old_mq600, new_mq600)

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print('Updated index.html with ultra-compact responsive menu successfully!')
