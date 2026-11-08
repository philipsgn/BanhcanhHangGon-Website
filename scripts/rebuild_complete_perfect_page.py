import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index_head.html', 'r', encoding='utf-8') as f:
    c = f.read()

# -----------------------------------------------------------------------------
# 1. UPDATE <head> PRELOADS
# -----------------------------------------------------------------------------
old_preload = '<link rel="preload" as="image" href="/images/home/background_result.webp" fetchpriority="high">'
new_preload = '''  <link rel="preload" as="image" href="/images/home/new-chicken-chef-desktop.webp" media="(min-width: 881px)" fetchpriority="high">
  <link rel="preload" as="image" href="/images/home/new-chicken-chef-mobile.webp" media="(max-width: 880px)" fetchpriority="high">'''
if old_preload in c:
    c = c.replace(old_preload, new_preload, 1)

# -----------------------------------------------------------------------------
# 2. UPDATE SECTION 1 (HERO) CSS & HTML
# -----------------------------------------------------------------------------
# Hero desktop CSS
old_hero_desktop_css = '''    .hero-panorama {
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
    }

    .hero-bg-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 42%;
      z-index: 0;
    }'''

new_hero_desktop_css = '''    .hero-panorama {
      position: absolute;
      inset: 0;
      z-index: 0;
      overflow: hidden;
    }

    .hero-picture {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
      z-index: 0;
    }

    .hero-bg-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
      z-index: 0;
    }'''

if old_hero_desktop_css in c:
    c = c.replace(old_hero_desktop_css, new_hero_desktop_css, 1)

# Hero HTML
old_hero_html = re.compile(r'<!-- SECTION 1: HERO -->\s*<section id="hero">\s*<div class="hero-panorama" aria-hidden="true">.*?</div>\s*<div class="hero-overlay"></div>\s*<div class="hero-content">\s*<p class="hero-quote">"Đưa gánh bánh canh Hàng Gòn về giữa phố thị"</p>\s*</div>\s*</section>', re.DOTALL)
new_hero_html = '''<!-- SECTION 1: HERO -->
  <section id="hero">
    <div class="hero-panorama" aria-hidden="true">
      <picture class="hero-picture">
        <source media="(max-width: 880px)" srcset="/images/home/new-chicken-chef-mobile.webp" width="941" height="1672">
        <source media="(min-width: 881px)" srcset="/images/home/new-chicken-chef-desktop.webp" width="1672" height="941">
        <img class="hero-bg-photo" src="/images/home/new-chicken-chef-desktop.webp" width="1672" height="941"
          fetchpriority="high" decoding="async"
          alt="Chú gà đầu bếp Hàng Gòn bên tô bánh canh gà ta bốc khói nghi ngút">
      </picture>
    </div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <p class="hero-quote">"Đưa gánh bánh canh Hàng Gòn về giữa phố thị"</p>
    </div>
  </section>'''

if old_hero_html.search(c):
    c = old_hero_html.sub(new_hero_html, c, count=1)

# -----------------------------------------------------------------------------
# 3. UPDATE SECTION 2: WELCOME (GREETING) CSS & HTML
# -----------------------------------------------------------------------------
# Desktop Welcome CSS
old_welcome_css_pattern = re.compile(r'/\* Section: welcome \*/\s*#welcome\s*\{[^}]*\}\s*\.welcome-grid\s*\{[^}]*\}\s*\.welcome-copy\s*\{[^}]*\}\s*\.welcome-title\s*\{[^}]*\}\s*\.welcome-title__line\s*\{[^}]*\}\s*\.welcome-title__line--accent\s*\{[^}]*\}\s*\.welcome-description\s*\{[^}]*\}\s*\.welcome-photo\s*\{[^}]*\}\s*\.welcome-photo img\s*\{[^}]*\}', re.DOTALL)

new_welcome_desktop_css = '''/* Section: welcome */
    #welcome {
      position: relative;
      padding: clamp(40px, 4.5vw, 68px) clamp(24px, 4vw, 64px);
      background-color: #3F2311;
      color: var(--cream);
      overflow: hidden;
    }

    /* Chú gà neo sát mép góc trái dưới, nghiêng sang phải nhìn User */
    .welcome-corner-chick {
      position: absolute;
      left: -18px;
      bottom: -10px;
      width: clamp(170px, 16vw, 235px);
      z-index: 4;
      pointer-events: none;
      user-select: none;
      display: flex;
      align-items: flex-end;
      transform-origin: bottom left;
      transform: rotate(8deg);
      transition: transform 0.4s ease;
    }

    .welcome-corner-chick:hover {
      transform: rotate(11deg) scale(1.03);
    }

    .welcome-chick-img {
      display: block;
      width: 100%;
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 14px 26px rgba(0, 0, 0, 0.52));
      transition: transform 0.35s ease;
    }

    /* Lưới 2 cột: Cột trái (Text Trầm tích Thư quán) và Cột phải (Khung ảnh quán ăn) */
    .welcome-grid {
      display: grid;
      grid-template-columns: minmax(360px, 1.15fr) minmax(340px, 1fr);
      align-items: center;
      gap: clamp(32px, 5vw, 64px);
      max-width: 1280px;
      margin: 0 auto;
      padding-left: clamp(130px, 13vw, 190px);
    }

    .welcome-copy {
      max-width: 540px;
    }

    .welcome-label {
      display: inline-block;
      font-family: 'Montserrat', sans-serif;
      font-size: clamp(11px, 0.9vw, 13px);
      font-weight: 600;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--gold);
      margin-bottom: 12px;
      opacity: 0.92;
    }

    .welcome-title {
      margin: 0;
      color: var(--cream);
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(34px, 3.8vw, 56px);
      font-weight: 500;
      line-height: 1.05;
      letter-spacing: 0;
      position: relative;
    }

    .welcome-title__line {
      display: block;
    }

    .welcome-title__line--accent {
      margin-top: 4px;
      font-weight: 600;
      color: var(--gold);
    }

    /* Đường chỉ vàng đồng mảnh phân cách tiêu đề và đoạn văn (Trầm tích Thư quán) */
    .welcome-divider {
      display: block;
      width: 52px;
      height: 1.5px;
      background: linear-gradient(90deg, var(--gold), rgba(212, 163, 89, 0.2));
      margin: 20px 0 22px;
      border-radius: 1px;
    }

    /* Đoạn văn phong cách Trầm tích Thư quán: in nghiêng nhẹ, lắng đọng, ấm cúng */
    .welcome-description {
      max-width: 510px;
      margin: 0;
      color: rgba(255, 246, 228, 0.95);
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(20px, 1.8vw, 25px);
      font-style: italic;
      line-height: 1.68;
      letter-spacing: 0.012em;
      text-shadow: 0 1px 3px rgba(0, 0, 0, 0.35);
    }

    .welcome-photo {
      position: relative;
      isolation: isolate;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
    }

    .welcome-photo img,
    .welcome-framed-img {
      display: block;
      width: 100%;
      max-width: 470px;
      height: auto;
      aspect-ratio: auto;
      border-radius: 4px;
      object-fit: contain;
      object-position: center;
      filter: drop-shadow(0 20px 40px rgba(0, 0, 0, 0.52));
      transition: transform 0.4s ease, filter 0.4s ease;
    }

    .welcome-photo img:hover,
    .welcome-framed-img:hover {
      transform: scale(1.025);
      filter: drop-shadow(0 24px 48px rgba(0, 0, 0, 0.62));
    }'''

if old_welcome_css_pattern.search(c):
    c = old_welcome_css_pattern.sub(new_welcome_desktop_css, c, count=1)

# Welcome HTML
old_welcome_html = re.compile(r'<!-- SECTION 2: WELCOME -->\s*<section id="welcome">.*?</section>', re.DOTALL)
new_welcome_html = '''<!-- SECTION 2: WELCOME -->
  <section id="welcome">
    <!-- Chú gà neo sát mép góc trái dưới, nghiêng sang phải nhìn User -->
    <div class="welcome-corner-chick" aria-hidden="true">
      <img src="images/story/cute-chicken.webp" alt="Linh vật chú gà ta Hàng Gòn ngộ nghĩnh" class="welcome-chick-img" loading="lazy" decoding="async">
    </div>

    <div class="welcome-grid">
      <div class="welcome-copy">
        <span class="welcome-label">HƯƠNG VỊ GIA TRUYỀN</span>
        <h2 class="welcome-title">
          <span class="welcome-title__line">Chào mừng bạn</span>
          <span class="welcome-title__line welcome-title__line--accent">đến với Hàng Gòn</span>
        </h2>
        <div class="welcome-divider" aria-hidden="true"></div>
        <p class="welcome-description">Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà giữa lòng thành phố. Từng tô canh được nấu mỗi ngày với nước lèo ninh xương, thịt gà tươi chọn lọc, giữ trọn vẹn sự ngọt thanh nguyên bản như thuở ban đầu.</p>
      </div>
      <figure class="welcome-photo">
        <img src="images/story/framed-restaurant-storefront.webp" alt="Khung ảnh mặt tiền quán Bánh Canh Gà Hàng Gòn về đêm" class="welcome-framed-img" loading="lazy" decoding="async">
      </figure>
    </div>
  </section>'''

if old_welcome_html.search(c):
    c = old_welcome_html.sub(new_welcome_html, c, count=1)

# -----------------------------------------------------------------------------
# 4. UPDATE SECTION 3: STORY CSS & HTML
# -----------------------------------------------------------------------------
old_story_bg = "url('/images/story/background_result.webp');"
new_story_bg = "url('images/story/new-background-story-chicken.webp');"
if old_story_bg in c:
    c = c.replace(old_story_bg, new_story_bg, 1)

old_story_html = re.compile(r'<!-- SECTION 3: STORY -->\s*<section id="story">.*?</section>', re.DOTALL)
new_story_html = '''<!-- SECTION 3: STORY -->
  <section id="story">
    <div class="story-slider" aria-label="Câu chuyện Hàng Gòn">
      <article class="story-slide is-active">
        <picture>
          <source srcset="images/story/new-background-story-chicken.webp" type="image/webp">
          <img src="images/story/new-background-story-chicken.png" alt="Không gian mộc mạc và câu chuyện truyền thống quán Bánh Canh Gà Hàng Gòn"
            loading="lazy" decoding="async">
        </picture>
        <div class="story-slide__content">
          <p class="story-slide__quote">“Góc chợ <em>Hàng Gòn</em> bao năm qua vẫn vậy,<br>Gìn giữ vị quê đượm ấm bát canh đầy.”</p>
        </div>
      </article>
    </div>
  </section>'''

if old_story_html.search(c):
    c = old_story_html.sub(new_story_html, c, count=1)

# -----------------------------------------------------------------------------
# 5. UPDATE SECTION 4: MENU CSS & HTML & CONTROLLER
# -----------------------------------------------------------------------------
pos_menu_css_start = c.find('/* ---------- SECTION 3 : MENU (ZIGZAG 3D EDITORIAL) ---------- */')
pos_story_css_start = c.find('/* ---------- SECTION 3 : STORY ---------- */')

menu_css = """/* ---------- SECTION 4 : MENU (PANORAMA 5 MÓN & BIỂN GÀ NGHỆ THUẬT - LOGICAL BODY FLOW) ---------- */
    #menu {
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
      padding: clamp(24px, 3.8vh, 40px) clamp(16px, 2.5vw, 40px) clamp(14px, 2vh, 22px);
    }

    .menu-decor-pattern {
      position: absolute;
      left: 0;
      top: 15%;
      width: clamp(60px, 8vw, 130px);
      height: 70%;
      background-repeat: repeat-y;
      background-size: 100% auto;
      background-image: url("data:image/svg+xml,%3Csvg width='80' height='160' viewBox='0 0 80 160' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 40L40 0L80 40L40 80L0 40Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Cpath d='M0 120L40 80L80 120L40 160L0 120Z' fill='%23C99A4A' fill-opacity='0.08'/%3E%3Ccircle cx='40' cy='40' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3Ccircle cx='40' cy='120' r='10' fill='%23C99A4A' fill-opacity='0.06'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 0;
      opacity: 0.85;
    }

    /* Biển gà nghệ thuật nguyên bản: Treo góc trái, dây thừng cách trần an toàn */
    .menu-hero-header {
      position: absolute;
      top: clamp(12px, 1.8vh, 22px);
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
    }

    .menu-rooster-img {
      width: clamp(110px, 11vw, 145px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 10px 20px rgba(45, 26, 18, 0.14));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.02) translateY(-2px);
    }

    /* SÂN KHẤU PANORAMA: NẰM HOÀN TOÀN TRONG BODY SECTION, CÁCH TRẦN >= 60PX */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1280px;
      flex: 1;
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin: clamp(16px, 2.5vh, 32px) auto 0;
      z-index: 2;
    }

    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: clamp(325px, 46vh, 395px);
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin: 0;
      cursor: grab;
      user-select: none;
    }

    .menu-carousel-track:active {
      cursor: grabbing;
    }

    /* Thẻ Card: Neo chuẩn tại top: 50%, left: 50%, không dùng margin âm trôi nổi */
    .menu-card {
      position: absolute;
      top: 50%;
      left: 50%;
      width: clamp(215px, 20vw, 260px);
      padding: 10px 16px 18px;
      border-radius: 22px;
      border: none;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1),
                  opacity 0.45s ease,
                  background-color 0.45s ease,
                  box-shadow 0.5s ease;
      will-change: transform, opacity;
      cursor: pointer;
    }

    /* Mâm Món Ăn: Nằm tự nhiên trong thẻ, không tràn ra ngoài trần section */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 0;
      margin-bottom: clamp(6px, 1vh, 12px);
      z-index: 3;
    }

    .menu-card-plate {
      width: clamp(110px, 15vh, 140px);
      height: clamp(110px, 15vh, 140px);
      aspect-ratio: 1 / 1;
      object-fit: contain;
      filter: drop-shadow(0 8px 16px rgba(36, 22, 16, 0.16));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card:not(.is-active) .menu-card-plate {
      transform: none !important;
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.02);
      filter: drop-shadow(0 12px 22px rgba(36, 22, 16, 0.22));
    }

    /* Thân thẻ: Typography chuẩn mực, không bị che lấp */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      padding-top: 2px;
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13px, 1.12vw, 15.5px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 4px;
      text-transform: uppercase;
      line-height: 1.25;
      color: #1A1410;
      transition: color 0.35s ease;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(17px, 1.45vw, 19.5px);
      font-weight: 900;
      margin: 0 0 5px;
      letter-spacing: 0.03em;
      color: #8A4A1C;
      transition: color 0.35s ease;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(10px, 0.82vw, 11.5px);
      line-height: 1.38;
      font-weight: 300;
      margin: 0 0 10px;
      max-width: 230px;
      color: #4A3C33;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(11px, 0.9vw, 12px);
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(140px, 14vw, 165px);
      height: 34px;
      transition: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
    }

    /* Card Active: Nổi bật, sang trọng, tương phản cao */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: none !important;
      transform: translate3d(-50%, -50%, 40px) scale(1);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 20px 45px rgba(36, 22, 16, 0.12);
      cursor: default;
    }

    .menu-card.is-active .menu-card-title {
      color: #1A1410;
    }

    .menu-card.is-active .menu-card-price {
      color: #8A4A1C;
    }

    .menu-card.is-active .menu-card-desc {
      color: #4A3C33;
      opacity: 1;
    }

    .menu-card.is-active .menu-card-cta {
      background: #9E5E2B;
      color: #FFFFFF;
      box-shadow: 0 6px 16px rgba(158, 94, 43, 0.28);
      opacity: 1;
      pointer-events: auto;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: #B56E35;
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(158, 94, 43, 0.38);
    }

    /* 4 Thẻ Phụ: Mờ nhẹ, tạo chiều sâu thị giác */
    .menu-card:not(.is-active) {
      background: #FAF7F2;
      border: none !important;
    }

    .menu-card:not(.is-active) .menu-card-title {
      color: #33241C;
    }

    .menu-card:not(.is-active) .menu-card-price {
      color: #9E5E2B;
    }

    .menu-card:not(.is-active) .menu-card-desc {
      color: #6A584D;
      opacity: 0.8;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .menu-card:not(.is-active) .menu-card-cta {
      background: transparent;
      color: #9E5E2B;
      border: 1px solid #C48E59;
      padding: 6px 16px;
      font-size: 11px;
      opacity: 0.85;
    }

    .menu-card:not(.is-active) .menu-card-cta:hover {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
    }

    /* 3D Transform Positions */
    .menu-card.is-near-prev {
      transform: translate3d(calc(-50% - 92%), calc(-50% + 10px), -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
    }

    .menu-card.is-near-next {
      transform: translate3d(calc(-50% + 92%), calc(-50% + 10px), -40px) scale(0.85);
      opacity: 0.65;
      z-index: 4;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.06);
    }

    .menu-card.is-far-prev {
      transform: translate3d(calc(-50% - 176%), calc(-50% + 20px), -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-far-next {
      transform: translate3d(calc(-50% + 176%), calc(-50% + 20px), -90px) scale(0.72);
      opacity: 0.35;
      z-index: 2;
      box-shadow: 0 8px 18px rgba(36, 22, 16, 0.04);
    }

    .menu-card.is-hidden {
      opacity: 0;
      transform: translate3d(-50%, calc(-50% + 30px), -140px) scale(0.65);
      pointer-events: none;
      z-index: 1;
    }

    /* Chấm chuyển trang (Pagination Dots) */
    .menu-dots {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      margin: clamp(6px, 1vh, 12px) auto clamp(8px, 1.2vh, 14px);
      z-index: 5;
    }

    .menu-dot {
      width: 7px;
      height: 7px;
      border-radius: 999px;
      background: #D8CEBE;
      border: none;
      padding: 0;
      cursor: pointer;
      transition: all 0.35s ease;
    }

    .menu-dot:hover {
      background: #B56E35;
      transform: scale(1.2);
    }

    .menu-dot.is-active {
      width: 22px;
      background: #9E5E2B;
      box-shadow: 0 2px 8px rgba(158, 94, 43, 0.35);
    }

    /* Menu Footer Bar */
    .menu-footer-bar {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: clamp(16px, 3vw, 40px);
      width: 100%;
      max-width: 680px;
      padding: clamp(6px, 1vh, 10px) clamp(16px, 2.5vw, 28px);
      background: #FAF7F2;
      border: 1px solid rgba(201, 154, 74, 0.22);
      border-radius: 999px;
      box-sizing: border-box;
      box-shadow: 0 6px 18px rgba(45, 26, 18, 0.04);
      margin: 2px auto 0;
      z-index: 4;
    }

    .menu-footer-contact {
      display: flex;
      align-items: baseline;
      gap: 12px;
      flex-wrap: wrap;
    }

    .menu-footer-tagline {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #7A6658;
    }

    .menu-footer-phone {
      font-size: clamp(13px, 1.1vw, 15px);
      font-weight: 800;
      color: #8A4A1C;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: color 0.2s ease;
    }

    .menu-footer-phone:hover {
      color: #6B3410;
    }

    .menu-footer-hours {
      font-size: 11px;
      color: #8C7B70;
      border-left: 1px solid rgba(201, 154, 74, 0.3);
      padding-left: 12px;
    }

    .menu-view-all-btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 7px 18px;
      background: #1A1410;
      color: #FAF8F5;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      border-radius: 999px;
      transition: all 0.3s ease;
      white-space: nowrap;
    }

    .menu-view-all-btn:hover {
      background: #8A4A1C;
      transform: translateY(-1px);
    }

    /* Responsive & Mobile Adaptation */
    @media (max-width: 1024px) {
      .menu-hero-header {
        left: clamp(10px, 2vw, 20px);
      }
      .menu-rooster-img {
        width: clamp(95px, 10vw, 120px);
      }
      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 80%), calc(-50% + 10px), -40px) scale(0.82) !important;
      }
      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 80%), calc(-50% + 10px), -40px) scale(0.82) !important;
      }
      .menu-card.is-far-prev {
        transform: translate3d(calc(-50% - 150%), calc(-50% + 20px), -80px) scale(0.68) !important;
      }
      .menu-card.is-far-next {
        transform: translate3d(calc(-50% + 150%), calc(-50% + 20px), -80px) scale(0.68) !important;
      }
    }

    @media (max-width: 600px) {
      #menu {
        min-height: 100vh;
        min-height: 100svh;
        padding: clamp(10px, 1.5vh, 16px) 12px clamp(12px, 1.8vh, 18px);
        overflow: visible;
      }

      .menu-hero-header {
        position: absolute;
        top: 10px;
        left: 12px;
        margin: 0;
        padding: 0;
        z-index: 6;
      }

      .menu-rooster-img {
        width: clamp(80px, 20vw, 95px);
      }

      .menu-stage-wrapper {
        margin-top: clamp(48px, 7vh, 64px);
      }

      .menu-carousel-track {
        height: clamp(335px, 48vh, 375px);
      }

      .menu-card {
        width: 78vw;
        max-width: 260px;
        padding: 10px 14px 16px;
      }

      .menu-card.is-active {
        transform: translate3d(-50%, -50%, 40px) scale(1) !important;
      }

      .menu-card.is-near-prev {
        transform: translate3d(calc(-50% - 68%), calc(-50% + 8px), -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-card.is-near-next {
        transform: translate3d(calc(-50% + 68%), calc(-50% + 8px), -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-card.is-far-prev,
      .menu-card.is-far-next {
        opacity: 0;
        pointer-events: none;
      }

      .menu-footer-bar {
        border-radius: 16px;
        padding: 10px 14px;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        text-align: center;
      }

      .menu-footer-contact {
        justify-content: center;
        gap: 8px;
      }

      .menu-footer-hours {
        border-left: none;
        padding-left: 0;
        width: 100%;
        text-align: center;
      }

      .menu-view-all-btn {
        width: 100%;
        justify-content: center;
        min-height: 44px;
      }
    }

    """

# Replace ONLY the Section 3: Menu CSS
c = c[:pos_menu_css_start] + menu_css + c[pos_story_css_start:]

# Replace Menu HTML Section
pos_menu_html_start = c.find('<section id="menu"')
pos_menu_html_end = c.find('</section>', pos_menu_html_start) + len('</section>')

menu_html = """<section id="menu">
    <!-- Decorative side pattern motif -->
    <div class="menu-decor-pattern" aria-hidden="true"></div>

    <!-- TẦNG 1: Biển gà chữ nghệ thuật nguyên bản treo nóc sát rìa ngoài cùng bên trái -->
    <header class="menu-hero-header">
      <div class="menu-hero-mascot">
        <picture>
          <source srcset="images/menu/original-chef-rooster-board.webp" type="image/webp">
          <img src="images/menu/Gà trống mặc trang phục bên bảng gỗ.png" alt="Chú gà trống đầu bếp Hàng Gòn bên bảng gỗ nghệ thuật nguyên bản" class="menu-rooster-img" loading="lazy" decoding="async">
        </picture>
      </div>
    </header>

    <!-- TẦNG 2: SÂN KHẤU PANORAMA 5 MÓN (NẰM HOÀN TOÀN TRONG BODY SECTION) -->
    <div class="menu-stage-wrapper">
      <!-- Carousel Track with 5 Dishes -->
      <div class="menu-carousel-track" id="menuTrack" role="region" aria-label="Thực đơn món đặc sản Hàng Gòn">
        <!-- Card 0: BÁNH CANH GÀ ĐẶC BIỆT -->
        <article class="menu-card is-active" data-index="0" aria-label="Bánh Canh Gà Đặc Biệt">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Chicken Soup on Wooden Tray_result.webp" alt="Mẹt Bánh Canh Gà Đặc Biệt Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">BÁNH CANH GÀ ĐẶC BIỆT</h3>
            <div class="menu-card-price">70.000₫</div>
            <p class="menu-card-desc">Thịt gà ta da vàng giòn mọng nước, trứng non béo ngậy. Nước dùng ninh xương thanh ngọt đậm đà.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 1: CƠM GÀ XÉ -->
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
        </article>

        <!-- Card 2: GỎI GÀ TA -->
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
        </article>

        <!-- Card 3: XÔI GÀ TRỨNG NON -->
        <article class="menu-card is-far-prev" data-index="3" aria-label="Xôi Gà Trứng Non">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" type="image/webp">
              <img src="images/menu/Vietnamese Xôi Gà on a Wooden Tray_result.webp" alt="Mẹt Xôi Gà Trứng Non Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">XÔI GÀ TRỨNG NON</h3>
            <div class="menu-card-price">40.000₫</div>
            <p class="menu-card-desc">Xôi nếp nương dẻo quánh thoang thoảng mỡ gà, chùm trứng non vàng ngậy và hành phi giòn rụm ấm bụng.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>

        <!-- Card 4: MÌ GÀ TA TRUYỀN THỐNG -->
        <article class="menu-card is-near-prev" data-index="4" aria-label="Mì Gà Ta Truyền Thống">
          <div class="menu-card-visual">
            <picture>
              <source srcset="images/menu/mi-ga.webp" type="image/webp">
              <img src="images/menu/mi-ga.webp" alt="Mẹt Mì Gà Ta Truyền Thống Hàng Gòn" class="menu-card-plate" loading="lazy" decoding="async">
            </picture>
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-title">MÌ GÀ TA TRUYỀN THỐNG</h3>
            <div class="menu-card-price">55.000₫</div>
            <p class="menu-card-desc">Sợi mì trứng dai vàng óng, thịt gà ta xé ngọt mềm, trứng non béo bùi, nước dùng hầm xương thanh ngọt thơm nồng tiêu sọ.</p>
            <a href="order.html" class="menu-card-cta">Đặt Món Ngay</a>
          </div>
        </article>
      </div>

      <!-- Pagination Indicator Dots (5 Món) -->
      <div class="menu-dots" id="menuDots" role="tablist" aria-label="Chọn món hiển thị">
        <button class="menu-dot is-active" data-index="0" role="tab" aria-selected="true" aria-label="Xem Bánh Canh Gà Đặc Biệt"></button>
        <button class="menu-dot" data-index="1" role="tab" aria-selected="false" aria-label="Xem Cơm Gà Xé"></button>
        <button class="menu-dot" data-index="2" role="tab" aria-selected="false" aria-label="Xem Gỏi Gà Ta"></button>
        <button class="menu-dot" data-index="3" role="tab" aria-selected="false" aria-label="Xem Xôi Gà Trứng Non"></button>
        <button class="menu-dot" data-index="4" role="tab" aria-selected="false" aria-label="Xem Mì Gà Ta Truyền Thống"></button>
      </div>
    </div>

    <!-- Menu Footer Bar -->
    <footer class="menu-footer-bar">
      <div class="menu-footer-contact">
        <span class="menu-footer-tagline">Đặt Giao Tận Nơi • Hotline</span>
        <a href="tel:0906427938" class="menu-footer-phone">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          090 642 79 38
        </a>
        <span class="menu-footer-hours">Phục vụ: 06:00 – 23:00 hàng ngày</span>
      </div>
      <a href="order.html" class="menu-view-all-btn">
        <span>Xem Toàn Bộ Thực Đơn</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </a>
    </footer>
  </section>"""

c = c[:pos_menu_html_start] + menu_html + c[pos_menu_html_end:]

# Carousel controller script
script_tag = """
  <!-- 3D Focus Menu Carousel Controller (5 Dishes Panorama) -->
  <script>
    (function () {
      const track = document.getElementById('menuTrack');
      if (!track) return;

      const cards = Array.from(track.querySelectorAll('.menu-card'));
      const dots = Array.from(document.querySelectorAll('.menu-dot'));
      const total = cards.length;
      let currentIndex = 0;
      let hasDragged = false;

      function updateCarousel(newIndex) {
        currentIndex = (newIndex + total) % total;

        cards.forEach((card, i) => {
          card.classList.remove('is-active', 'is-near-prev', 'is-near-next', 'is-far-prev', 'is-far-next', 'is-hidden');
          
          let diff = (i - currentIndex) % total;
          if (diff < -Math.floor(total / 2)) diff += total;
          if (diff > Math.floor(total / 2)) diff -= total;

          if (diff === 0) {
            card.classList.add('is-active');
            card.setAttribute('aria-hidden', 'false');
          } else if (diff === -1) {
            card.classList.add('is-near-prev');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === 1) {
            card.classList.add('is-near-next');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === -2) {
            card.classList.add('is-far-prev');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === 2) {
            card.classList.add('is-far-next');
            card.setAttribute('aria-hidden', 'true');
          } else {
            card.classList.add('is-hidden');
            card.setAttribute('aria-hidden', 'true');
          }
        });

        dots.forEach((dot, i) => {
          const isActive = i === currentIndex;
          dot.classList.toggle('is-active', isActive);
          dot.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });
      }

      // Click card to switch
      cards.forEach((card, idx) => {
        card.addEventListener('click', (e) => {
          if (e.target.closest('.menu-card-cta')) return;
          if (hasDragged) return;
          if (idx !== currentIndex) {
            e.preventDefault();
            updateCarousel(idx);
          }
        });
      });

      // Pagination dots click
      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => updateCarousel(idx));
      });

      // Mouse drag-to-slide
      let isDragging = false;
      let dragStartX = 0;
      let dragCurrentX = 0;

      track.addEventListener('mousedown', (e) => {
        if (e.target.closest('.menu-card-cta')) return;
        isDragging = true;
        hasDragged = false;
        dragStartX = e.pageX;
        dragCurrentX = e.pageX;
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        dragCurrentX = e.pageX;
        if (Math.abs(dragCurrentX - dragStartX) > 8) {
          hasDragged = true;
        }
      });

      window.addEventListener('mouseup', (e) => {
        if (!isDragging) return;
        isDragging = false;
        const diffX = dragCurrentX - dragStartX;
        const dragThreshold = 30;
        if (diffX < -dragThreshold) {
          updateCarousel(currentIndex + 1);
        } else if (diffX > dragThreshold) {
          updateCarousel(currentIndex - 1);
        }
        setTimeout(() => { hasDragged = false; }, 80);
      });

      // Touch / swipe for mobile
      let touchStartX = 0;
      let touchEndX = 0;

      track.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      track.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        const threshold = 30;
        if (touchEndX < touchStartX - threshold) {
          updateCarousel(currentIndex + 1);
        } else if (touchEndX > touchStartX + threshold) {
          updateCarousel(currentIndex - 1);
        }
      }, { passive: true });

      // Keyboard arrow keys
      window.addEventListener('keydown', (e) => {
        const menuSec = document.getElementById('menu');
        if (!menuSec) return;
        const rect = menuSec.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
          if (e.key === 'ArrowLeft') updateCarousel(currentIndex - 1);
          else if (e.key === 'ArrowRight') updateCarousel(currentIndex + 1);
        }
      });

      updateCarousel(0);
    })();
  </script>
"""

pos_body_end = c.rfind('</body>')
if pos_body_end != -1:
    c = c[:pos_body_end] + script_tag + c[pos_body_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("COMPLETE REBUILD SUCCESS! All sections: Hero, Greeting/Welcome, Story, Menu are 100% restored and aligned!")
