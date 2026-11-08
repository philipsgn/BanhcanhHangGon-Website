import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# -----------------------------------------------------------------------------
# 1. UPDATE index.html
# -----------------------------------------------------------------------------
INDEX_PATH = 'index.html'
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    idx_content = f.read()

# A. Section Story CSS: Zoom out to show wooden table surface
old_story_css = """    #story {
      position: relative;
      overflow: hidden;
      min-height: clamp(420px, 58vh, 620px);
      padding: clamp(72px, 9vw, 132px) clamp(28px, 7vw, 120px);
      background:
        linear-gradient(180deg,
          rgba(36, 22, 16, 0.04) 0%,
          rgba(36, 22, 16, 0.2) 34%,
          rgba(36, 22, 16, 0.68) 100%),
        linear-gradient(90deg,
          rgba(36, 22, 16, 0.28) 0%,
          rgba(36, 22, 16, 0.1) 46%,
          rgba(36, 22, 16, 0.44) 100%),
        url('images/story/new-background-story-chicken.webp');
      background-size: cover;
      background-position: center center;
      background-repeat: no-repeat;
      margin-top: -1px;
    }"""

new_story_css = """    #story {
      position: relative;
      overflow: hidden;
      min-height: clamp(480px, 64vh, 680px); /* Mở rộng chiều cao thấy toàn cảnh mặt bàn ăn */
      padding: clamp(72px, 9vw, 132px) clamp(28px, 7vw, 120px);
      background:
        linear-gradient(180deg,
          rgba(36, 22, 16, 0.04) 0%,
          rgba(36, 22, 16, 0.2) 34%,
          rgba(36, 22, 16, 0.68) 100%),
        linear-gradient(90deg,
          rgba(36, 22, 16, 0.28) 0%,
          rgba(36, 22, 16, 0.1) 46%,
          rgba(36, 22, 16, 0.44) 100%),
        url('images/story/new-background-story-chicken.webp');
      background-size: cover;
      background-position: center 85%; /* Zoom out căn thấp hiển thị trọn vẹn mặt bàn ăn */
      background-repeat: no-repeat;
      margin-top: -1px;
    }"""

if old_story_css in idx_content:
    idx_content = idx_content.replace(old_story_css, new_story_css)
    print("Updated #story CSS for tabletop zoom out.")
else:
    print("#story CSS block not matched!")

# B. Update .story-slide img object-position
old_img_pos = """    .story-slide img {
      position: absolute;
      inset: 0;
      z-index: -1;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
      user-select: none;
      -webkit-user-drag: none;
    }"""

new_img_pos = """    .story-slide img {
      position: absolute;
      inset: 0;
      z-index: -1;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 85%; /* Hiển thị trọn vẹn mặt bàn ăn bóng đẹp ở tiền cảnh */
      user-select: none;
      -webkit-user-drag: none;
    }"""

if old_img_pos in idx_content:
    idx_content = idx_content.replace(old_img_pos, new_img_pos)
    print("Updated .story-slide img object-position to center 85%.")
else:
    print(".story-slide img pattern not matched!")

# C. Optimize Story HTML Picture fallback from .png to .webp
idx_content = idx_content.replace('<img src="images/story/new-background-story-chicken.png"', '<img src="images/story/new-background-story-chicken.webp"')

# D. Đồng bộ Tên món và Giá tiền Section Menu với order.html
menu_dishes_sync = [
    # Card 1: Cơm gà xé -> Cơm Gỏi Gà Xé Trứng Non 52.000₫
    ('<h3 class="menu-card-title">Cơm Gà Xé Phay</h3>\n            <div class="menu-card-price">52.000₫</div>',
     '<h3 class="menu-card-title">Cơm Gỏi Gà Xé Trứng Non</h3>\n            <div class="menu-card-price">52.000₫</div>'),
    # Card 2: Gỏi Gà Ta -> Gỏi Gà Ta Nhỏ 50.000₫
    ('<h3 class="menu-card-title">Gỏi Gà Ta</h3>\n            <div class="menu-card-price">50.000₫</div>',
     '<h3 class="menu-card-title">Gỏi Gà Ta Nhỏ</h3>\n            <div class="menu-card-price">50.000₫</div>'),
    # Card 3: Xôi Gà Trứng Non -> Xôi Gà Xé Trứng Non 40.000₫
    ('<h3 class="menu-card-title">Xôi Gà Trứng Non</h3>\n            <div class="menu-card-price">40.000₫</div>',
     '<h3 class="menu-card-title">Xôi Gà Xé Trứng Non</h3>\n            <div class="menu-card-price">40.000₫</div>'),
    # Card 4: Mì Gà Ta Truyền Thống -> Mì Gà Xé Trứng Non 55.000₫
    ('<h3 class="menu-card-title">Mì Gà Ta Truyền Thống</h3>\n            <div class="menu-card-price">55.000₫</div>',
     '<h3 class="menu-card-title">Mì Gà Xé Trứng Non</h3>\n            <div class="menu-card-price">55.000₫</div>'),
]

for old_t, new_t in menu_dishes_sync:
    if old_t in idx_content:
        idx_content = idx_content.replace(old_t, new_t)
        print(f"Synchronized dish: {new_t.splitlines()[0]}")
    else:
        print(f"Dish title/price not matched: {old_t.splitlines()[0]}")

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated index.html successfully.")


# -----------------------------------------------------------------------------
# 2. UPDATE order.html: Sử dụng WebP cho toàn bộ ảnh
# -----------------------------------------------------------------------------
ORDER_PATH = 'order.html'
with open(ORDER_PATH, 'r', encoding='utf-8') as f:
    ord_content = f.read()

ord_replacements = [
    ('images/order/background-order.jpg', 'images/order/background-order.webp'),
    ('images/order/clipboard_top_clamp.png', 'images/order/clipboard_top_clamp.webp'),
    ('images/order/add-to-cart.png', 'images/order/add-to-cart.webp'),
    ('images/order/cham-bi.jpg', 'images/order/cham-bi.webp'),
    ('images/order/clipboard_board_only.png', 'images/order/clipboard_board_only.webp'),
]

for old_img, new_img in ord_replacements:
    if old_img in ord_content:
        ord_content = ord_content.replace(old_img, new_img)
        print(f"Replaced {old_img} -> {new_img} in order.html")

with open(ORDER_PATH, 'w', encoding='utf-8') as f:
    f.write(ord_content)
print("Updated order.html successfully.")
print("ALL MENU-ORDER SYNC & PRODUCTION IMAGE OPTIMIZATIONS APPLIED!")
