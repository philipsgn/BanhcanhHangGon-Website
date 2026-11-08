import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace feet shadows CSS with golden straw sheaf CSS
old_feet_css = """    /* Feet Contact Shadows (Bóng tiếp xúc dính sát ngay dưới móng chân gà tiếp đất) */
    .rooster-feet-shadows {
      position: absolute;
      left: 0;
      top: 15px;
      width: 620px;
      height: 780px;
      pointer-events: none;
      z-index: 0;
    }

    .foot-shadow-l {
      position: absolute;
      left: 55px;
      top: 765px;
      width: 110px;
      height: 20px;
      background: radial-gradient(ellipse at center, rgba(10, 5, 2, 0.88) 0%, rgba(18, 9, 4, 0.5) 45%, transparent 75%);
      filter: blur(2px);
      transform: rotate(-3deg);
    }

    .foot-shadow-r {
      position: absolute;
      left: 195px;
      top: 765px;
      width: 110px;
      height: 20px;
      background: radial-gradient(ellipse at center, rgba(10, 5, 2, 0.88) 0%, rgba(18, 9, 4, 0.5) 45%, transparent 75%);
      filter: blur(2px);
      transform: rotate(2deg);
    }"""

new_feet_css = """    /* Golden Straw Sheaf Foreground Perch (Bó rơm vàng mùa lúa chín làm điểm tựa chân gà) */
    .rooster-straw-sheaf {
      position: absolute;
      left: -5px;
      top: 712px;
      width: 350px;
      height: auto;
      z-index: 0;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 10px 22px rgba(0, 0, 0, 0.58));
      transition: all 0.3s ease;
    }"""

assert old_feet_css in content, "old_feet_css not found in content"
content = content.replace(old_feet_css, new_feet_css, 1)

# 2. Update HTML in rooster-menu-holder: Replace rooster-feet-shadows div with rooster-straw-sheaf img
old_holder_html = """      <div class="rooster-menu-holder" id="roosterMenuHolder">
        <!-- 0. Feet Contact Shadows: Bóng tiếp xúc 2 bàn chân gà chạm mặt thớt gỗ (z-index: 0) -->
        <div class="rooster-feet-shadows">
          <div class="foot-shadow-l"></div>
          <div class="foot-shadow-r"></div>
        </div>

        <!-- 1. Background Mascot Layer: Thân & Chân Chú Gà Trống Đầu Bếp (z-index: 1) -->"""

new_holder_html = """      <div class="rooster-menu-holder" id="roosterMenuHolder">
        <!-- 0. Golden Straw Sheaf Perch: Bó Rơm Vàng Mùa Gặt Cột Lạt Tre Làm Điểm Tựa Chân Gà (z-index: 0) -->
        <img src="images/order/rooster_straw_sheaf.webp"
             alt="Bó rơm vàng mùa gặt lúa chín Hàng Gòn"
             class="rooster-straw-sheaf"
             id="roosterStrawSheaf" />

        <!-- 1. Background Mascot Layer: Thân & Chân Chú Gà Trống Đầu Bếp (z-index: 1) -->"""

assert old_holder_html in content, "old_holder_html not found in content"
content = content.replace(old_holder_html, new_holder_html, 1)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: order.html successfully updated with Golden Straw Sheaf!")

