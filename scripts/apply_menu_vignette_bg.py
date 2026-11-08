import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()
p = os.path.join(ROOT, 'index.html')

with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace #menu::before and #menu::after in desktop styles
old_desktop_block = '''    /* Lớp nền menu-bg-3 được làm mờ 76% và khử nhiễu hạt để tôn vinh món ăn tuyệt đối */
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
    }'''

new_desktop_block = '''    /* Lớp nền menu-bg-3: Rõ nét 72% ở hai bên Left/Right, mờ dịu về 8% tại trung tâm (Spotlight Vignette) */
    #menu::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: url('images/menu/menu-bg-3.webp');
      background-position: center center;
      background-size: cover;
      background-repeat: no-repeat;
      opacity: 0.72; /* Rõ nét tự nhiên ở hai bên cánh */
      filter: none;
      -webkit-mask-image: radial-gradient(ellipse 52% 58% at 50% 38%, rgba(0, 0, 0, 0.08) 0%, rgba(0, 0, 0, 0.22) 40%, rgba(0, 0, 0, 0.85) 75%, rgba(0, 0, 0, 1) 100%);
      mask-image: radial-gradient(ellipse 52% 58% at 50% 38%, rgba(0, 0, 0, 0.08) 0%, rgba(0, 0, 0, 0.22) 40%, rgba(0, 0, 0, 0.85) 75%, rgba(0, 0, 0, 1) 100%);
      z-index: 0;
      pointer-events: none;
    }

    /* Vầng sáng hữu cơ kem ấm dịu mắt làm bừng sáng mâm gà ta, làm sạch họa tiết nền ở trung tâm */
    #menu::after {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(ellipse 56% 60% at 50% 38%, rgba(250, 245, 235, 0.94) 0%, rgba(250, 245, 235, 0.45) 52%, transparent 88%);
      z-index: 1;
      pointer-events: none;
    }'''

if old_desktop_block in content:
    content = content.replace(old_desktop_block, new_desktop_block)
    print("Replaced desktop #menu::before & #menu::after successfully!")
else:
    print("Error: Could not find exact old_desktop_block!")
    sys.exit(1)

# 2. Add mobile mask override in @media (max-width: 600px)
old_mobile_menu = '''    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(40px, 5.5vh, 50px) 12px clamp(12px, 1.8vh, 16px);
        overflow: visible;
      }'''

new_mobile_menu = '''    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(40px, 5.5vh, 50px) 12px clamp(12px, 1.8vh, 16px);
        overflow: visible;
      }

      #menu::before {
        -webkit-mask-image: radial-gradient(ellipse 68% 56% at 50% 34%, rgba(0, 0, 0, 0.08) 0%, rgba(0, 0, 0, 0.25) 45%, rgba(0, 0, 0, 0.88) 80%, rgba(0, 0, 0, 1) 100%);
        mask-image: radial-gradient(ellipse 68% 56% at 50% 34%, rgba(0, 0, 0, 0.08) 0%, rgba(0, 0, 0, 0.25) 45%, rgba(0, 0, 0, 0.88) 80%, rgba(0, 0, 0, 1) 100%);
      }'''

if old_mobile_menu in content:
    content = content.replace(old_mobile_menu, new_mobile_menu)
    print("Added mobile mask tuning in @media (max-width: 600px) successfully!")
else:
    print("Warning: Could not find exact old_mobile_menu!")

with open(p, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully with Section Menu Vignette upgrade!")
