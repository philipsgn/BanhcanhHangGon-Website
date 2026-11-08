import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Desktop CSS for #welcome
old_css_re = re.compile(
    r'/\* Section: welcome \*/\s*'
    r'#welcome\s*\{[^}]*\}\s*'
    r'/\* Chú gà neo sát mép góc trái dưới chỉa ra nhìn User \*/\s*'
    r'\.welcome-corner-chick\s*\{[^}]*\}\s*'
    r'\.welcome-chick-img\s*\{[^}]*\}\s*'
    r'/\* Lưới 2 cột: Cột trái \(Text lệch trái\) và Cột phải \(Khung ảnh quán ăn\) \*/\s*'
    r'\.welcome-grid\s*\{[^}]*\}\s*'
    r'\.welcome-copy\s*\{[^}]*\}\s*'
    r'\.welcome-title\s*\{[^}]*\}\s*'
    r'\.welcome-title__line\s*\{[^}]*\}\s*'
    r'\.welcome-title__line--accent\s*\{[^}]*\}\s*'
    r'\.welcome-description\s*\{[^}]*\}\s*'
    r'\.welcome-photo\s*\{[^}]*\}\s*'
    r'\.welcome-photo img,\s*\.welcome-framed-img\s*\{[^}]*\}\s*'
    r'\.welcome-photo img:hover,\s*\.welcome-framed-img:hover\s*\{[^}]*\}',
    re.DOTALL
)

new_desktop_css = '''/* Section: welcome */
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

assert old_css_re.search(content), "old_css_re pattern not matched"
content = old_css_re.sub(new_desktop_css, content, count=1)
print("1. Desktop CSS for #welcome updated successfully")

# 2. Update Mobile CSS for #welcome
old_mobile_re = re.compile(
    r'@media\s*\(max-width:\s*880px\)\s*\{\s*'
    r'#welcome\s*\{[^}]*\}\s*'
    r'\.welcome-corner-chick\s*\{[^}]*\}\s*'
    r'\.welcome-grid\s*\{[^}]*\}\s*'
    r'\.welcome-photo\s*\{[^}]*\}\s*'
    r'\.welcome-copy\s*\{[^}]*\}\s*'
    r'\.welcome-title\s*\{[^}]*\}\s*'
    r'\.welcome-description\s*\{[^}]*\}',
    re.DOTALL
)

new_mobile_css = '''@media (max-width: 880px) {
      #welcome {
        padding: 36px 20px 42px;
      }

      .welcome-corner-chick {
        position: relative;
        left: auto;
        bottom: auto;
        width: 145px;
        margin: 20px auto 0;
        order: 3;
        display: flex;
        justify-content: center;
        transform: rotate(5deg);
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

      .welcome-divider {
        margin: 16px auto 18px;
      }

      .welcome-title {
        margin-bottom: 0;
        font-size: clamp(30px, 8.5vw, 42px);
      }

      .welcome-description {
        font-size: clamp(19px, 5.2vw, 23px);
        line-height: 1.6;
      }'''

assert old_mobile_re.search(content), "old_mobile_re pattern not matched"
content = old_mobile_re.sub(new_mobile_css, content, count=1)
print("2. Mobile CSS for #welcome updated successfully")

# 3. Update HTML Markup for Section 2
old_html_re = re.compile(
    r'<!-- SECTION 2: WELCOME -->\s*'
    r'<section id="welcome">.*?'
    r'</section>',
    re.DOTALL
)

new_html = '''<!-- SECTION 2: WELCOME -->
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

assert old_html_re.search(content), "old_html_re pattern not matched"
content = old_html_re.sub(new_html, content, count=1)
print("3. HTML Markup for Section 2 updated successfully")

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)
print("-> index.html successfully updated!")
