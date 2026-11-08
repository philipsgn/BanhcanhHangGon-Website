import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace straw sheaf CSS with wooden foot block CSS
old_straw_css = """    /* Golden Straw Sheaf Foreground Perch (Bó rơm vàng mùa lúa chín làm điểm tựa chân gà) */
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

new_block_css = """    /* Rustic Wooden Foot Block (Thớt gỗ kê dưới chân gà từ kê-chân gà.jpg) */
    .rooster-foot-block {
      position: absolute;
      left: 0;
      top: 735px;
      width: 330px;
      height: auto;
      z-index: 0;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 12px 24px rgba(0, 0, 0, 0.62));
      transition: all 0.3s ease;
    }"""

assert old_straw_css in content, "old_straw_css not found in content"
content = content.replace(old_straw_css, new_block_css, 1)

# 2. Replace HTML img in rooster-menu-holder
old_straw_html = """        <!-- 0. Golden Straw Sheaf Perch: Bó Rơm Vàng Mùa Gặt Cột Lạt Tre Làm Điểm Tựa Chân Gà (z-index: 0) -->
        <img src="images/order/rooster_straw_sheaf.webp"
             alt="Bó rơm vàng mùa gặt lúa chín Hàng Gòn"
             class="rooster-straw-sheaf"
             id="roosterStrawSheaf" />"""

new_block_html = """        <!-- 0. Rustic Wooden Foot Block: Thớt Gỗ Kê Dưới Chân Gà (Từ kê-chân gà.jpg, z-index: 0) -->
        <img src="images/order/rooster_foot_block.webp"
             alt="Thớt gỗ kê chân gà Hàng Gòn"
             class="rooster-foot-block"
             id="roosterFootBlock" />"""

assert old_straw_html in content, "old_straw_html not found in content"
content = content.replace(old_straw_html, new_block_html, 1)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: order.html successfully updated with Wooden Foot Block!")

