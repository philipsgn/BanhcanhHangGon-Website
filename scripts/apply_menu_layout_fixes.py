import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .menu-hero-header and .menu-rooster-img
old_header = """    .menu-hero-header {
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
    }"""

new_header = """    .menu-hero-header {
      position: relative;
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      width: 100%;
      max-width: 100%;
      margin: 0;
      padding: 0 clamp(16px, 3.5vw, 48px);
      box-sizing: border-box;
      z-index: 5;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      position: relative;
      margin: 0;
      width: auto;
    }

    /* Ropes reach y=0 to touch the ceiling of #menu - Sát rìa trái thanh thoát */
    .menu-rooster-img {
      width: clamp(170px, 16vw, 230px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 12px 24px rgba(45, 26, 18, 0.16));
      transition: transform 0.4s ease;
    }"""

assert old_header in content, 'old_header not found!'
content = content.replace(old_header, new_header)

# 2. Update .menu-card-visual and .menu-card-plate and .menu-card-body
old_plate = """    /* Card Plate Visual: Đưa đĩa xuống vị trí tự nhiên, 100% không bị cắt nóc */
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
    }"""

new_plate = """    /* Card Plate Visual: Đĩa vuông 1:1 chuẩn hóa, khoảng cách an toàn tuyệt đối với chữ */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -12px;
      margin-bottom: 24px;
      z-index: 2;
    }

    .menu-card-plate {
      width: clamp(140px, 15vw, 156px);
      height: clamp(140px, 15vw, 156px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 12px 20px rgba(36, 22, 16, 0.2));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.04) translateY(-2px);
      filter: drop-shadow(0 16px 26px rgba(36, 22, 16, 0.28));
    }

    /* Card Content Typography - Nổi bật, hạ thấp chữ không bị đĩa che */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      padding-top: 6px;
    }"""

assert old_plate in content, 'old_plate not found!'
content = content.replace(old_plate, new_plate)

# 3. Update media queries 960px & 600px
old_mq960 = """    @media (max-width: 960px) {
      .menu-hero-header {
        justify-content: center;
        margin-bottom: 8px;
      }

      .menu-hero-mascot {
        max-width: 230px;
        margin: 0 auto;
      }"""

new_mq960 = """    @media (max-width: 960px) {
      .menu-hero-header {
        justify-content: flex-start !important;
        padding-left: clamp(14px, 3vw, 28px) !important;
        margin-bottom: 8px;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(150px, 20vw, 195px);
      }"""

assert old_mq960 in content, 'old_mq960 not found!'
content = content.replace(old_mq960, new_mq960)

old_mq600 = """    @media (max-width: 600px) {
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
      }"""

new_mq600 = """    @media (max-width: 600px) {
      #menu {
        padding: 0 12px 36px;
      }

      .menu-hero-header {
        justify-content: flex-start !important;
        padding-left: 14px !important;
        margin-bottom: 6px;
      }

      .menu-hero-mascot {
        margin: 0 !important;
      }

      .menu-rooster-img {
        width: clamp(135px, 28vw, 170px);
      }"""

assert old_mq600 in content, 'old_mq600 not found!'
content = content.replace(old_mq600, new_mq600)

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print('Updated index.html successfully!')
