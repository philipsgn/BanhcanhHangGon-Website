import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Desktop CSS for #welcome
old_css_re = re.compile(r'/\* Section: welcome \*/\s*#welcome\s*\{[^}]*\}\s*\.welcome-grid\s*\{[^}]*\}\s*\.welcome-mascot-col\s*\{[^}]*\}\s*\.welcome-chick-mascot\s*\{[^}]*\}\s*\.welcome-chick-mascot:hover\s*\{[^}]*\}\s*\.welcome-copy\s*\{[^}]*\}\s*\.welcome-title\s*\{[^}]*\}\s*\.welcome-title__line\s*\{[^}]*\}\s*\.welcome-title__line--accent\s*\{[^}]*\}\s*\.welcome-description\s*\{[^}]*\}\s*\.welcome-photo\s*\{[^}]*\}\s*\.welcome-photo img,\s*\.welcome-framed-img\s*\{[^}]*\}\s*\.welcome-photo img:hover,\s*\.welcome-framed-img:hover\s*\{[^}]*\}', re.DOTALL)

new_desktop_css = '''/* Section: welcome */
    #welcome {
      position: relative;
      padding: clamp(40px, 4.5vw, 68px) clamp(24px, 4vw, 64px);
      background-color: #3F2311;
      color: var(--cream);
      overflow: hidden;
    }

    /* Chú gà neo sát mép góc trái dưới chỉa ra nhìn User */
    .welcome-corner-chick {
      position: absolute;
      left: 0;
      bottom: 0;
      width: clamp(210px, 20vw, 290px);
      z-index: 4;
      pointer-events: none;
      user-select: none;
      display: flex;
      align-items: flex-end;
    }

    .welcome-chick-img {
      display: block;
      width: 100%;
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 16px 28px rgba(0, 0, 0, 0.55));
      transition: transform 0.35s ease;
    }

    /* Lưới 2 cột: Cột trái (Text lệch trái) và Cột phải (Khung ảnh quán ăn) */
    .welcome-grid {
      display: grid;
      grid-template-columns: minmax(360px, 1.1fr) minmax(360px, 1fr);
      align-items: center;
      gap: clamp(32px, 5vw, 64px);
      max-width: 1280px;
      margin: 0 auto;
      padding-left: clamp(160px, 16vw, 240px);
    }

    .welcome-copy {
      max-width: 540px;
    }

    .welcome-title {
      margin: 0 0 16px;
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

    .welcome-description {
      max-width: 500px;
      margin: 0;
      color: rgba(255, 244, 220, 0.92);
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(19px, 1.7vw, 24px);
      line-height: 1.55;
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

assert old_css_re.search(content), "old_css_re not found"
content = old_css_re.sub(new_desktop_css, content, count=1)
print("1. Desktop CSS for #welcome updated")

# 2. Update Mobile CSS for #welcome
old_mobile_re = re.compile(r'@media\s*\(max-width:\s*880px\)\s*\{\s*#welcome\s*\{[^}]*\}\s*\.welcome-grid\s*\{[^}]*\}\s*\.welcome-photo\s*\{[^}]*\}\s*\.welcome-copy\s*\{[^}]*\}\s*\.welcome-mascot-col\s*\{[^}]*\}\s*\.welcome-chick-mascot\s*\{[^}]*\}\s*\.welcome-title\s*\{[^}]*\}\s*\.welcome-description\s*\{[^}]*\}', re.DOTALL)

new_mobile_css = '''@media (max-width: 880px) {
      #welcome {
        padding: 36px 20px 42px;
      }

      .welcome-corner-chick {
        position: relative;
        left: auto;
        bottom: auto;
        width: 170px;
        margin: 16px auto 0;
        order: 3;
        display: flex;
        justify-content: center;
      }

      .welcome-grid {
        grid-template-columns: 1fr;
        gap: 28px;
        padding-left: 0;
        text-align: center;
      }

      .welcome-photo {
        order: 1;
        width: min(100%, 380px);
        margin: 0 auto;
      }

      .welcome-copy {
        order: 2;
        max-width: 100%;
      }

      .welcome-title {
        margin-bottom: 14px;
        font-size: clamp(30px, 8.5vw, 42px);
      }

      .welcome-description {
        font-size: clamp(18px, 5.2vw, 22px);
        line-height: 1.45;
      }'''

assert old_mobile_re.search(content), "old_mobile_re not found"
content = old_mobile_re.sub(new_mobile_css, content, count=1)
print("2. Mobile CSS for #welcome updated")

# 3. Update HTML Markup for Section 2
old_html_re = re.compile(r'<!-- SECTION 2: WELCOME -->\s*<section id="welcome">\s*<div class="welcome-grid">\s*<div class="welcome-mascot-col">.*?</div>\s*<div class="welcome-copy">.*?</div>\s*<figure class="welcome-photo">.*?</figure>\s*</div>\s*</section>', re.DOTALL)

new_html = '''<!-- SECTION 2: WELCOME -->
  <section id="welcome">
    <!-- Chú gà neo sát mép góc trái dưới chỉa ra nhìn User -->
    <div class="welcome-corner-chick" aria-hidden="true">
      <img src="images/story/cute-chicken.webp" alt="Linh vật chú gà ta Hàng Gòn ngộ nghĩnh" class="welcome-chick-img" loading="lazy" decoding="async">
    </div>

    <div class="welcome-grid">
      <div class="welcome-copy">
        <h2 class="welcome-title">
          <span class="welcome-title__line">Chào mừng bạn</span>
          <span class="welcome-title__line welcome-title__line--accent">đến với Hàng Gòn</span>
        </h2>
        <p class="welcome-description">Hàng Gòn tự hào mang đến hương vị bánh canh gà đậm đà giữa lòng thành phố. Từng
          tô canh được nấu mỗi ngày với nước lèo ninh xương, thịt gà tươi chọn lọc — phục vụ ngay khi bạn vừa gọi món.
        </p>
      </div>
      <figure class="welcome-photo">
        <img src="images/story/framed-restaurant-storefront.webp" alt="Khung ảnh mặt tiền quán Bánh Canh Gà Hàng Gòn về đêm" class="welcome-framed-img" loading="lazy" decoding="async">
      </figure>
    </div>
  </section>'''

assert old_html_re.search(content), "old_html_re not found"
content = old_html_re.sub(new_html, content, count=1)
print("3. HTML Markup for Section 2 updated")

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print("-> index.html successfully updated!")
