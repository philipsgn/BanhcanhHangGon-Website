import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Google Fonts in <head>
old_font = re.search(r'href="https://fonts\.googleapis\.com/css2\?family=Cinzel[^\"]+"', content)
if old_font:
    new_font_str = 'href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Be+Vietnam+Pro:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"'
    content = content.replace(old_font.group(0), new_font_str)
    print("Updated Google Fonts link successfully.")
else:
    print("Google Fonts link pattern not matched!")

# 2. Update #menu CSS rule
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
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.07) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.75) 0%, transparent 100%);
      color: #1A1410;
      overflow: visible;
      isolation: isolate;
      padding: clamp(48px, 6.8vh, 68px) clamp(16px, 2.5vw, 40px) clamp(16px, 2.2vh, 24px);
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
    }"""

if old_menu_css in content:
    content = content.replace(old_menu_css, new_menu_css)
    print("Updated #menu background to menu-bg-3.webp successfully.")
else:
    print("#menu CSS block exact match not found!")

# 3. Update .menu-card-visual margin-bottom
old_visual_css = """    .menu-card-visual {
      position: relative;
      width: clamp(370px, 43vh, 440px);
      height: clamp(370px, 43vh, 440px);
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: -38px; /* Đáy mâm tì tự nhiên lên gờ đế vàng kim */
      z-index: 5;
      transform-style: preserve-3d;
    }"""

new_visual_css = """    .menu-card-visual {
      position: relative;
      width: clamp(370px, 43vh, 440px);
      height: clamp(370px, 43vh, 440px);
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: -22px; /* Đáy mâm tì tự nhiên, khoảng thở thanh thoát với chữ */
      z-index: 5;
      transform-style: preserve-3d;
    }"""

if old_visual_css in content:
    content = content.replace(old_visual_css, new_visual_css)
    print("Updated .menu-card-visual margin-bottom successfully.")
else:
    print(".menu-card-visual CSS block exact match not found!")

# 4. Replace Royal Gold Card Body with Frameless Minimalist Card Body and Staggered Slide-Up Animations
old_card_block_pattern = r'/\* =+\s*2\. ĐẾ THẺ HOÀNG GIA VÀNG KIM.*?/\* =+\s*3\. CÁC MÓN PHỤ'
match = re.search(old_card_block_pattern, content, re.DOTALL)

new_card_block = """/* ==========================================================================
       2. THẺ KHÔNG KHUNG VIỀN TỐI GIẢN & TYPOGRAPHY THANH THOÁT (FRAMELESS MINIMALIST)
       ========================================================================== */
    .menu-card.is-active .menu-card-body {
      position: relative;
      width: clamp(285px, 26vw, 345px);
      background: transparent !important;
      border: none !important;
      border-radius: 0 !important;
      padding: clamp(6px, 1vh, 10px) clamp(12px, 1.5vw, 18px) 0;
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
        transform: translateY(12px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .menu-card.is-active .menu-card-title {
      font-family: 'Playfair Display', 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(18px, 1.55vw, 22px);
      font-weight: 700;
      letter-spacing: 0.015em;
      margin: 0 0 4px;
      line-height: 1.28;
      color: #2B1810;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.7);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    .menu-card.is-active .menu-card-price {
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(18px, 1.6vw, 22px);
      font-weight: 700;
      margin: 0 0 6px;
      letter-spacing: 0.01em;
      color: #C04A18;
      text-shadow: 0 1px 1px rgba(255, 255, 255, 0.6);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.04s both;
    }

    .menu-card.is-active .menu-card-desc {
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(11.5px, 0.88vw, 13px);
      line-height: 1.5;
      font-weight: 400;
      margin: 0 0 14px;
      max-width: 295px;
      color: #5A4538;
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
      font-size: clamp(11.5px, 0.9vw, 12.5px);
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(140px, 13vw, 168px);
      height: 36px;
      background: linear-gradient(135deg, #8A2B0E 0%, #B84B32 100%);
      border: none;
      color: #FFFDF5;
      box-shadow: 0 4px 14px rgba(138, 43, 14, 0.22);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.12s both;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: linear-gradient(135deg, #9C3312 0%, #C85438 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(138, 43, 14, 0.32);
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
       3. CÁC MÓN PHỤ"""

if match:
    content = content[:match.start()] + new_card_block + content[match.end() - len('/* ==========================================================================\n       3. CÁC MÓN PHỤ'):]
    print("Replaced Card Block with Frameless Minimalist successfully.")
else:
    print("Card Block regex pattern not matched!")

# 5. Mobile adjustments for .menu-card.is-active .menu-card-body
old_mob_body = """      .menu-card.is-active .menu-card-body {
        width: 84vw;
        max-width: 295px;
        padding: 14px 16px 18px;
      }"""

new_mob_body = """      .menu-card.is-active .menu-card-body {
        width: 88vw;
        max-width: 310px;
        padding: 6px 10px 0;
      }"""

if old_mob_body in content:
    content = content.replace(old_mob_body, new_mob_body)
    print("Updated mobile .menu-card-body successfully.")
else:
    print("Mobile .menu-card-body not matched!")

# 6. Title casing in HTML for the 5 dishes
titles = [
    ('<h3 class="menu-card-title">BÁNH CANH GÀ ĐẶC BIỆT</h3>', '<h3 class="menu-card-title">Bánh Canh Gà Đặc Biệt</h3>'),
    ('<h3 class="menu-card-title">CƠM GÀ XÉ</h3>', '<h3 class="menu-card-title">Cơm Gà Xé Phay</h3>'),
    ('<h3 class="menu-card-title">GỎI GÀ TA</h3>', '<h3 class="menu-card-title">Gỏi Gà Ta</h3>'),
    ('<h3 class="menu-card-title">XÔI GÀ TRỨNG NON</h3>', '<h3 class="menu-card-title">Xôi Gà Trứng Non</h3>'),
    ('<h3 class="menu-card-title">MÌ GÀ TA TRUYỀN THỐNG</h3>', '<h3 class="menu-card-title">Mì Gà Ta Truyền Thống</h3>')
]

for old_t, new_t in titles:
    if old_t in content:
        content = content.replace(old_t, new_t)
        print(f"Updated title: {old_t} -> {new_t}")

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("ALL CHANGES WRITTEN TO index.html SUCCESSFULLY!")
