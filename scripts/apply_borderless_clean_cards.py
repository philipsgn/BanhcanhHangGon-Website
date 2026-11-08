import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Card CSS: Remove borders and elevate plate to eliminate top frame
old_card_css = """    /* 1. Active Card: 1 Món Tâm Điểm (100% sắc nét, tone Nâu Cát Gỗ Ấm) */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: 1.5px solid #C4A482;
      transform: translate3d(0, -14px, 50px) scale(1.04);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 20px 42px rgba(36, 22, 16, 0.16),
                  0 0 0 1px rgba(196, 164, 130, 0.35);
      cursor: default;
    }

    /* 2. Near Inactive Cards: 2 Món Mờ Cận Tâm (Scale 0.85, Opacity 65%) */
    .menu-card.is-near-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(-92%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
      cursor: pointer;
    }

    .menu-card.is-near-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(92%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
      cursor: pointer;
    }

    /* 3. Far Inactive Cards: 2 Món Mờ Rìa Xa (Scale 0.72, Opacity 35%) */
    .menu-card.is-far-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.15);
      transform: translate3d(-178%, 20px, -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.06);
      cursor: pointer;
    }

    .menu-card.is-far-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.15);
      transform: translate3d(178%, 20px, -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.06);
      cursor: pointer;
    }"""

new_card_css = """    /* 1. Active Card: 1 Món Tâm Điểm (Khử 100% viền bo cứng, nền Nâu Cát ấm áp) */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: none !important;
      transform: translate3d(0, -10px, 50px) scale(1.04);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 22px 48px rgba(36, 22, 16, 0.14);
      cursor: default;
    }

    /* 2. Near Inactive Cards: 2 Món Mờ Cận Tâm (Không viền stroke) */
    .menu-card.is-near-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: none !important;
      transform: translate3d(-92%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
      cursor: pointer;
    }

    .menu-card.is-near-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: none !important;
      transform: translate3d(92%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
      cursor: pointer;
    }

    /* 3. Far Inactive Cards: 2 Món Mờ Rìa Xa (Không viền stroke) */
    .menu-card.is-far-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: none !important;
      transform: translate3d(-178%, 20px, -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
      cursor: pointer;
    }

    .menu-card.is-far-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: none !important;
      transform: translate3d(178%, 20px, -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
      cursor: pointer;
    }"""

assert old_card_css in content, 'old_card_css not found!'
content = content.replace(old_card_css, new_card_css)

# 2. Update .menu-card-visual: Elevate plate so 0 top frame sticks out behind
old_visual_css = """    /* Card Plate Visual: Đĩa vuông 1:1 chuẩn hóa, khoảng cách an toàn tuyệt đối với chữ */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -12px;
      margin-bottom: 24px;
      z-index: 2;
    }"""

new_visual_css = """    /* Card Plate Visual: Mâm đĩa vươn đỉnh tự do, triệt tiêu 100% khung thừa phía sau */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -62px;
      margin-bottom: 18px;
      z-index: 3;
    }"""

assert old_visual_css in content, 'old_visual_css not found!'
content = content.replace(old_visual_css, new_visual_css)

# Also ensure .menu-card has border: none in base definition
content = re.sub(
    r'(\.menu-card\s*\{[^}]*?)(border-radius:\s*26px;)',
    r'\1border-radius: 26px;\n      border: none;',
    content,
    count=1
)

# 3. Update Card 2 HTML: New image goi-ga.webp, Title: GỎI GÀ XÉ, remove "bắp chuối"
old_card2_html = """        <!-- Card 2: GỎI GÀ TA BẮP CHUỐI -->
        <article class="menu-card is-far-next" data-index="2" aria-label="Gỏi Gà Ta Bắp Chuối">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Salad on Wooden Tray_result.webp" alt="Mẹt Gỏi Gà Ta Bắp Chuối Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">GỎI GÀ TA BẮP CHUỐI</h3>
            <div class="menu-card-price">50.000₫</div>
            <p class="menu-card-desc">Thịt gà thả vườn xé phay bắp chuối giòn sần sật, rau răm cay the và sốt chua ngọt béo bùi đậu phộng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>"""

new_card2_html = """        <!-- Card 2: GỎI GÀ XÉ -->
        <article class="menu-card is-far-next" data-index="2" aria-label="Gỏi Gà Xé">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/goi-ga.webp" type="image/webp">
              <img src="images/menu/goi-ga.webp" alt="Mẹt Gỏi Gà Xé Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">GỎI GÀ XÉ</h3>
            <div class="menu-card-price">50.000₫</div>
            <p class="menu-card-desc">Thịt gà thả vườn xé phay bắp cải cà rốt giòn mát, rau răm cay the và sốt chua ngọt béo bùi đậu phộng rang.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>"""

assert old_card2_html in content, 'old_card2_html not found!'
content = content.replace(old_card2_html, new_card2_html)

# Update pagination dot 2 aria-label
content = content.replace(
    'aria-label="Xem Gỏi Gà Ta Bắp Chuối"',
    'aria-label="Xem Gỏi Gà Xé"'
)

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print('Updated index.html with borderless cards and Gỏi Gà Xé successfully!')
