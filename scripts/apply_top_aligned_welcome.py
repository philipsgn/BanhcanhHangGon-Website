import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

INDEX_HTML = 'index.html'
with open(INDEX_HTML, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Desktop CSS for #welcome
# Replace .welcome-grid and .welcome-copy / .welcome-label
old_css_re = re.compile(
    r'/\* Lưới 2 cột: Cột trái \(Text Trầm tích Thư quán\) và Cột phải \(Khung ảnh quán ăn\) \*/\s*'
    r'\.welcome-grid\s*\{[^}]*\}\s*'
    r'\.welcome-copy\s*\{[^}]*\}\s*'
    r'\.welcome-label\s*\{[^}]*\}\s*'
    r'\.welcome-title\s*\{',
    re.DOTALL
)

new_desktop_grid_css = '''/* Lưới 2 cột: Cột trái (Text Trầm tích Thư quán) và Cột phải (Khung ảnh quán ăn) */
    .welcome-grid {
      display: grid;
      grid-template-columns: minmax(360px, 1.15fr) minmax(340px, 1fr);
      align-items: start;
      gap: clamp(32px, 5vw, 64px);
      max-width: 1280px;
      margin: 0 auto;
      padding-left: clamp(130px, 13vw, 190px);
    }

    .welcome-copy {
      max-width: 540px;
      padding-top: clamp(2px, 0.4vw, 6px);
    }

    .welcome-title {'''

assert old_css_re.search(content), "old_css_re not matched"
content = old_css_re.sub(new_desktop_grid_css, content, count=1)
print("1. Desktop CSS updated: align-items: start, welcome-label removed")

# 2. Update HTML Markup for Section 2
# Remove <span class="welcome-label">HƯƠNG VỊ GIA TRUYỀN</span>
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

assert old_html_re.search(content), "old_html_re not matched"
content = old_html_re.sub(new_html, content, count=1)
print("2. HTML Markup updated: welcome-label removed, title is top element")

with open(INDEX_HTML, 'w', encoding='utf-8') as f:
    f.write(content)

print("-> index.html successfully updated!")
