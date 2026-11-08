import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update #menu CSS for fixed 100vh screen
old_menu_css = """    #menu {
      position: relative;
      background-color: #FAF8F5;
      background-image:
        radial-gradient(circle at 12% 18%, rgba(201, 154, 74, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 88% 82%, rgba(181, 118, 42, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.6) 0%, transparent 100%);
      color: #1A1410;
      overflow: hidden;
      isolation: isolate;
      /* padding-top: 0 allows the 2 hanging ropes to physically touch the top ceiling */
      padding: 0 clamp(16px, 2.5vw, 40px) clamp(36px, 4vw, 56px);
    }"""

new_menu_css = """    #menu {
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

assert old_menu_css in content, 'old_menu_css not found!'
content = content.replace(old_menu_css, new_menu_css)

# 2. Update .menu-hero-header (Absolute top-left, doesn't take vertical flow)
old_header_css = """    .menu-hero-header {
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
    }"""

new_header_css = """    .menu-hero-header {
      position: absolute;
      top: 0;
      left: clamp(16px, 3.5vw, 48px);
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      width: auto;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      z-index: 10;
      pointer-events: none;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      position: relative;
      margin: 0;
      width: auto;
      pointer-events: auto;
    }"""

assert old_header_css in content, 'old_header_css not found!'
content = content.replace(old_header_css, new_header_css)

# 3. Update .menu-stage-wrapper (flex: 1, centers vertically in screen)
old_stage_css = """    .menu-stage-wrapper {
      position: relative;
      max-width: 1260px;
      margin: clamp(14px, 2vw, 28px) auto 0;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 2;
    }

    /* Carousel 3D Track */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: 520px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin-top: 4px;
      cursor: grab;
      user-select: none;
    }"""

new_stage_css = """    .menu-stage-wrapper {
      position: relative;
      max-width: 1260px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: 0 auto;
      z-index: 2;
    }

    /* Carousel 3D Track - Món ăn hiển thị nổi là Dead Center của Screen */
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

assert old_stage_css in content, 'old_stage_css not found!'
content = content.replace(old_stage_css, new_stage_css)

# 4. Update .menu-card-visual & .menu-card-body for zero text overlap
old_visual_block = """    /* Card Plate Visual: Mâm đĩa vươn đỉnh tự do, triệt tiêu 100% khung thừa phía sau */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -62px;
      margin-bottom: 18px;
      z-index: 3;
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

new_visual_block = """    /* Card Plate Visual: Mâm đĩa vươn đỉnh tự do, triệt tiêu 100% khung thừa phía sau */
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
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.03) translateY(-2px);
      filter: drop-shadow(0 14px 22px rgba(36, 22, 16, 0.24));
    }

    /* Card Content Typography - Khoảng cách an toàn tuyệt đối > 55px từ đáy đĩa */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      padding-top: 10px;
    }"""

assert old_visual_block in content, 'old_visual_block not found!'
content = content.replace(old_visual_block, new_visual_block)

# 5. Update Responsive Media Queries for 100vh
old_mq = """    @media (max-width: 960px) {
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
      }

      .menu-carousel-track {
        height: 500px;
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
        width: clamp(140px, 18vw, 180px);
      }

      .menu-carousel-track {
        height: 460px;
      }"""

assert old_mq in content, 'old_mq not found!'
content = content.replace(old_mq, new_mq)

old_mq600 = """    @media (max-width: 600px) {
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
      }

      .menu-carousel-track {
        height: 480px;
        margin-top: 10px;
      }"""

new_mq600 = """    @media (max-width: 600px) {
      #menu {
        height: 100vh;
        min-height: 100svh;
        max-height: 100vh;
        padding: 0 12px 18px;
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
      }"""

assert old_mq600 in content, 'old_mq600 not found!'
content = content.replace(old_mq600, new_mq600)

# 6. Update Card 1: Cơm gà xé (bỏ bắp cải)
old_card1 = """        <!-- Card 1: CƠM GỎI GÀ XÉ -->
        <article class="menu-card is-near-next" data-index="1" aria-label="Cơm Gỏi Gà Xé">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" alt="Mẹt Cơm Gỏi Gà Xé Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">CƠM GỎI GÀ XÉ</h3>
            <div class="menu-card-price">52.000₫</div>
            <p class="menu-card-desc">Cơm nghệ thơm béo nấu từ nước luộc gà, ăn cùng gỏi gà bắp cải chua ngọt và chén mắm gừng cay nồng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>"""

new_card1 = """        <!-- Card 1: CƠM GÀ XÉ -->
        <article class="menu-card is-near-next" data-index="1" aria-label="Cơm Gà Xé">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Rice Tray Feast_result.webp" alt="Mẹt Cơm Gà Xé Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">CƠM GÀ XÉ</h3>
            <div class="menu-card-price">52.000₫</div>
            <p class="menu-card-desc">Cơm nghệ vàng óng nấu từ nước luộc gà béo ngọt, thịt gà ta xé phay đậm vị ăn kèm dưa chua thanh mát và chén mắm gừng cay nồng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>"""

assert old_card1 in content, 'old_card1 not found!'
content = content.replace(old_card1, new_card1)

# 7. Update Card 2: GỎI GÀ TA (bỏ triệt để từ bắp chuối)
old_card2 = """        <!-- Card 2: GỎI GÀ XÉ -->
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

new_card2 = """        <!-- Card 2: GỎI GÀ TA -->
        <article class="menu-card is-far-next" data-index="2" aria-label="Gỏi Gà Ta">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/goi-ga.webp" type="image/webp">
              <img src="images/menu/goi-ga.webp" alt="Mẹt Gỏi Gà Ta Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">GỎI GÀ TA</h3>
            <div class="menu-card-price">50.000₫</div>
            <p class="menu-card-desc">Thịt gà ta thả vườn xé phay trộn cùng hành tây giòn ngọt, rau răm thơm the nồng nàn và sốt mắm chua ngọt béo bùi đậu phộng rang.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>"""

assert old_card2 in content, 'old_card2 not found!'
content = content.replace(old_card2, new_card2)

# 8. Update pagination dots
content = content.replace('aria-label="Xem Cơm Gỏi Gà Xé"', 'aria-label="Xem Cơm Gà Xé"')
content = content.replace('aria-label="Xem Gỏi Gà Xé"', 'aria-label="Xem Gỏi Gà Ta"')

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print('Updated index.html successfully with fixed 100vh centering and copy!')
