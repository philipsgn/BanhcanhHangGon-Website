import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Target Card 1 block
old_card_1 = '''        <!-- Card 1: CƠM GÀ XÉ -->
        <article class="menu-card is-near-next" data-index="1" data-dish-id="com-goi-xe-trung-non" aria-label="Cơm Gà Xé">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" alt="Mẹt Cơm Gà Xé Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">Cơm Gỏi Gà Xé Trứng Non</h3>
            <div class="menu-card-price">52.000₫</div>
            <p class="menu-card-desc">Cơm nghệ vàng óng nấu từ nước luộc gà béo ngọt, thịt gà ta xé phay đậm vị ăn kèm dưa chua thanh mát và chén mắm gừng cay nồng.</p>
            <a href="order.html" class="menu-card-cta">ĐẶT MÓN</a>
          </div>
        </article>'''

new_card_1 = '''        <!-- Card 1: CƠM GÀ XÉ TRỨNG NON -->
        <article class="menu-card is-near-next" data-index="1" data-dish-id="com-xe-trung-non" aria-label="Cơm Gà Xé Trứng Non">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/com-ga-xe.webp" type="image/webp">
              <img src="images/menu/com-ga-xe.webp" alt="Mẹt Cơm Gà Xé Trứng Non Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">Cơm Gà Xé Trứng Non</h3>
            <div class="menu-card-price">47.000₫</div>
            <p class="menu-card-desc">Cơm nghệ vàng óng thơm ngậy mỡ gà ta, thịt gà xé phay giòn ngọt chấm mắm gừng cay nồng, chùm trứng non vàng ngậy ấm bụng.</p>
            <a href="order.html" class="menu-card-cta">ĐẶT MÓN</a>
          </div>
        </article>'''

if old_card_1 in content:
    content = content.replace(old_card_1, new_card_1)
    print("Replaced Card 1 exactly!")
else:
    # Pattern replace if whitespace differs
    pattern = re.compile(
        r'<!-- Card 1: CƠM GÀ XÉ -->\s*<article class="menu-card[^"]*"[^>]*data-dish-id="com-goi-xe-trung-non"[\s\S]*?</article>',
        re.MULTILINE
    )
    if pattern.search(content):
        content = pattern.sub(new_card_1, content)
        print("Replaced Card 1 via regex pattern!")
    else:
        print("Could not find Card 1 pattern in index.html!")
        sys.exit(1)

# Also check menu dot aria-label
content = content.replace('aria-label="Xem Cơm Gà Xé"', 'aria-label="Xem Cơm Gà Xé Trứng Non"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")
