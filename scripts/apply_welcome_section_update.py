import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for #welcome in Desktop CSS (lines 838 to 905)
old_welcome_css = re.compile(r'/\* Section: welcome \*/\s*#welcome\s*\{[^}]*\}\s*\.welcome-grid\s*\{[^}]*\}\s*\.welcome-copy\s*\{[^}]*\}\s*\.welcome-title\s*\{[^}]*\}\s*\.welcome-title__line\s*\{[^}]*\}\s*\.welcome-title__line--accent\s*\{[^}]*\}\s*\.welcome-description\s*\{[^}]*\}\s*\.welcome-photo\s*\{[^}]*\}\s*\.welcome-photo img\s*\{[^}]*\}', re.DOTALL)

new_welcome_css = '''/* Section: welcome */
    #welcome {
      position: relative;
      padding: clamp(34px, 4vw, 58px) clamp(24px, 5vw, 80px);
      background-color: #3F2311;
      color: var(--cream);
      overflow: hidden;
    }

    .welcome-grid {
      display: grid;
      grid-template-columns: clamp(160px, 16vw, 240px) minmax(300px, 1fr) minmax(320px, 1.05fr);
      align-items: center;
      gap: clamp(24px, 3.5vw, 56px);
      max-width: 1280px;
      margin: 0 auto;
    }

    .welcome-mascot-col {
      align-self: end;
      display: flex;
      justify-content: center;
      margin-bottom: -6px;
    }

    .welcome-chick-mascot {
      display: block;
      width: 100%;
      max-width: 240px;
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 14px 24px rgba(0, 0, 0, 0.45));
      transition: transform 0.35s ease;
    }

    .welcome-chick-mascot:hover {
      transform: translateY(-4px) scale(1.03);
    }

    .welcome-copy {
      max-width: 520px;
    }

    .welcome-title {
      margin: 0 0 16px;
      color: var(--cream);
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(32px, 3.5vw, 54px);
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
      max-width: 440px;
      height: auto;
      aspect-ratio: auto;
      border-radius: 4px;
      object-fit: contain;
      object-position: center;
      filter: drop-shadow(0 18px 36px rgba(0, 0, 0, 0.48));
      transition: transform 0.4s ease, filter 0.4s ease;
    }

    .welcome-photo img:hover,
    .welcome-framed-img:hover {
      transform: scale(1.025);
      filter: drop-shadow(0 22px 42px rgba(0, 0, 0, 0.58));
    }'''

assert old_welcome_css.search(content), "old_welcome_css not found"
content = old_welcome_css.sub(new_welcome_css, content, count=1)
print("1. Desktop CSS for #welcome updated")

# 2. Update Mobile Media Query for #welcome (around line 906-938)
old_welcome_mobile_css = re.compile(r'@media\s*\(max-width:\s*880px\)\s*\{\s*#welcome\s*\{[^}]*\}\s*\.welcome-grid\s*\{[^}]*\}\s*\.welcome-photo\s*\{[^}]*\}\s*\.welcome-copy,\s*\.welcome-description\s*\{[^}]*\}\s*\.welcome-title\s*\{[^}]*\}\s*\.welcome-description\s*\{[^}]*\}', re.DOTALL)

new_welcome_mobile_css = '''@media (max-width: 880px) {
      #welcome {
        padding: 36px 20px 42px;
      }

      .welcome-grid {
        grid-template-columns: 1fr;
        gap: 28px;
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

      .welcome-mascot-col {
        order: 3;
        align-self: center;
        justify-content: center;
        margin-top: 4px;
        margin-bottom: 0;
      }

      .welcome-chick-mascot {
        max-width: 180px;
        margin: 0 auto;
      }

      .welcome-title {
        margin-bottom: 14px;
        font-size: clamp(30px, 8.5vw, 42px);
      }

      .welcome-description {
        font-size: clamp(18px, 5.2vw, 22px);
        line-height: 1.45;
      }'''

assert old_welcome_mobile_css.search(content), "old_welcome_mobile_css not found"
content = old_welcome_mobile_css.sub(new_welcome_mobile_css, content, count=1)
print("2. Mobile CSS for #welcome updated")

# 3. Update Section 2 HTML Markup (around line 3108-3125)
old_welcome_html = re.compile(r'<!-- SECTION 2: WELCOME -->\s*<section id="welcome">\s*<div class="welcome-grid">\s*<div class="welcome-copy">.*?</div>\s*<figure class="welcome-photo">\s*<img src="images/story/mattien-quan-dem_result\.webp".*?</figure>\s*</div>\s*</section>', re.DOTALL)

new_welcome_html = '''<!-- SECTION 2: WELCOME -->
  <section id="welcome">
    <div class="welcome-grid">
      <div class="welcome-mascot-col">
        <img src="images/story/cute-chicken.webp" alt="Linh vật chú gà ta Hàng Gòn ngộ nghĩnh" class="welcome-chick-mascot" loading="lazy" decoding="async">
      </div>
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

assert old_welcome_html.search(content), "old_welcome_html not found"
content = old_welcome_html.sub(new_welcome_html, content, count=1)
print("3. HTML Markup for Section 2 updated")

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print("-> index.html successfully updated!")
