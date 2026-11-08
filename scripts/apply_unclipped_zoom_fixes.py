import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #menu CSS
old_menu_css = """    #menu {
      position: relative;
      height: 100vh;
      min-height: 100svh;
      max-height: 100vh;
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
      overflow: hidden;
      isolation: isolate;
      padding: 0 clamp(16px, 2.5vw, 40px) clamp(14px, 1.8vw, 24px);
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
      padding: clamp(28px, 3.5vh, 42px) clamp(16px, 2.5vw, 40px) clamp(16px, 2vh, 24px);
    }"""

assert old_menu_css in content, 'old_menu_css not found!'
content = content.replace(old_menu_css, new_menu_css)

# 2. Update .menu-carousel-track
old_track_css = """    /* Carousel 3D Track - Món ăn hiển thị nổi là Dead Center của Screen */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: 480px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin-top: 0;
      cursor: grab;
      user-select: none;
    }"""

new_track_css = """    /* Carousel 3D Track - Chiều cao co giãn theo vh, không bị che ở Zoom 100% */
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

assert old_track_css in content, 'old_track_css not found!'
content = content.replace(old_track_css, new_track_css)

# 3. Update .menu-card width
old_card_base = """    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(250px, 26vw, 295px);
      padding: 0 22px 26px;
      border-radius: 26px;
      border: none;
      box-sizing: border-box;"""

new_card_base = """    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(230px, 22vw, 275px);
      padding: 0 18px 22px;
      border-radius: 24px;
      border: none;
      box-sizing: border-box;"""

assert old_card_base in content, 'old_card_base not found!'
content = content.replace(old_card_base, new_card_base)

# 4. Update .menu-card-visual & .menu-card-plate
old_visual_plate = """    /* Card Plate Visual: Mâm đĩa vươn đỉnh tự do, triệt tiêu 100% khung thừa phía sau */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -55px;
      margin-bottom: 24px;
      z-index: 3;
    }

    .menu-card-plate {
      width: clamp(138px, 15vw, 152px);
      height: clamp(138px, 15vw, 152px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 10px 18px rgba(36, 22, 16, 0.18));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }"""

new_visual_plate = """    /* Card Plate Visual: Tỷ lệ co giãn thông minh theo vh, không bị xén đỉnh ở Zoom 100% */
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

assert old_visual_plate in content, 'old_visual_plate not found!'
content = content.replace(old_visual_plate, new_visual_plate)

# 5. Update media query 600px
old_mq600 = """    @media (max-width: 600px) {
      #menu {
        height: 100vh;
        min-height: 100svh;
        max-height: 100vh;
        padding: 0 12px 18px;
      }"""

new_mq600 = """    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(20px, 3vh, 28px) 12px 18px;
        overflow: visible;
      }"""

assert old_mq600 in content, 'old_mq600 not found!'
content = content.replace(old_mq600, new_mq600)

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print('Updated index.html with unclipped responsive menu successfully!')
