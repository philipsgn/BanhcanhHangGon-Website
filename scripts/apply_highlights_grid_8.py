import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()

def apply_update():
    path = os.path.join(ROOT, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update HTML in #backstage
    old_html_block = '''      <div class="bs-grid">
        <figure class="bs-item bs-hero">
          <img src="images/behind-scenes/trung-non-nuoc-cham_result.webp" alt="Trứng non chấm nước mắm" loading="lazy"
            decoding="async">
          <figcaption class="bs-caption">Vị chấm không thể thiếu</figcaption>
        </figure>
        <figure class="bs-item bs-vert1">
          <img src="images/behind-scenes/chan-nuoc-leo_result.webp" alt="Chan nước lèo nóng hổi" loading="lazy"
            decoding="async">
          <figcaption class="bs-caption">Nước lèo ngọt thanh</figcaption>
        </figure>
        <figure class="bs-item bs-vert2">
          <img src="images/behind-scenes/ga-luoc-quan_result.webp" alt="Gà luộc tại quán" loading="lazy"
            decoding="async">
          <figcaption class="bs-caption">Gà tuyển chọn mỗi sáng</figcaption>
        </figure>
        <figure class="bs-item bs-wide1 bs-fit-full">
          <img src="images/behind-scenes/mot-goc-nho-cua-quan_result.webp" alt="Một góc nhỏ của quán" loading="lazy"
            decoding="async">
          <figcaption class="bs-caption">Góc quán mỗi trưa</figcaption>
        </figure>
        <figure class="bs-item bs-wide2 bs-fit-full">
          <img src="images/behind-scenes/khong-gian-quan_result.webp" alt="Không gian quán" loading="lazy"
            decoding="async">
          <figcaption class="bs-caption">Mặt tiền Hàng Gòn</figcaption>
        </figure>
      </div>'''

    new_html_block = '''      <div class="bs-grid-8">
        <!-- 1. Chan nước lèo -->
        <figure class="bs-card">
          <img src="images/behind-scenes/chan-nuoc-leo_result.webp" alt="Chan nước lèo nóng hổi" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Nước lèo ngọt thanh</figcaption>
        </figure>

        <!-- 2. Gà luộc tại quán -->
        <figure class="bs-card">
          <img src="images/behind-scenes/ga-luoc-quan_result.webp" alt="Gà luộc tại quán" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Gà tuyển chọn mỗi sáng</figcaption>
        </figure>

        <!-- 3. Trứng non nước chấm -->
        <figure class="bs-card">
          <img src="images/behind-scenes/trung-non-nuoc-cham_result.webp" alt="Trứng non chấm nước mắm" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Vị chấm không thể thiếu</figcaption>
        </figure>

        <!-- 4. Highlights 4: Mẹt thức ăn và tô bánh canh -->
        <figure class="bs-card">
          <img src="images/highlights/highlights-4.webp" alt="Mẹt thức ăn đậm vị" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Hương vị trọn vẹn</figcaption>
        </figure>

        <!-- 5. Highlights 1: Góc bàn ăn quán -->
        <figure class="bs-card">
          <img src="images/highlights/highlights-1.webp" alt="Góc bàn ăn ấm cúng" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Góc quán thân thuộc</figcaption>
        </figure>

        <!-- 6. Highlights: Không gian quán sáng sủa -->
        <figure class="bs-card">
          <img src="images/highlights/hightlights.webp" alt="Không gian quán" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Không gian ấm cúng</figcaption>
        </figure>

        <!-- 7. Highlights 3: Khoảnh khắc chuẩn bị món -->
        <figure class="bs-card">
          <img src="images/highlights/higlights-3.webp" alt="Khoảnh khắc chuẩn bị món" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Khoảnh khắc Hàng Gòn</figcaption>
        </figure>

        <!-- 8. Không gian mặt tiền quán phố -->
        <figure class="bs-card">
          <img src="images/behind-scenes/khong-gian-quan_result.webp" alt="Mặt tiền Hàng Gòn" loading="lazy" decoding="async">
          <figcaption class="bs-card-caption">Mặt tiền quán phố</figcaption>
        </figure>
      </div>'''

    if old_html_block in content:
        content = content.replace(old_html_block, new_html_block)
        print("Updated HTML structure for #backstage grid 8!")
    else:
        # Regex replacement
        pattern = re.compile(r'<div class="bs-grid">[\s\S]*?</div>\s*(?=</div>\s*</section>)')
        if pattern.search(content):
            content = pattern.sub(new_html_block, content)
            print("Updated HTML structure via pattern for #backstage grid 8!")
        else:
            print("Error: Could not find old HTML block in index.html")
            sys.exit(1)

    # 2. Update CSS for .bs-grid-8
    old_css_grid = '''.bs-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-template-rows: 180px 180px clamp(320px, 28vw, 430px);
      gap: 14px;
      grid-template-areas:
        "hero hero vert1 vert2"
        "hero hero vert1 vert2"
        "wide1 wide1 wide2 wide2";
    }

    .bs-item {
      position: relative;
      overflow: hidden;
      border-radius: 18px;
      background: #1a0f0a;
      cursor: pointer;
    }

    .bs-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.7s cubic-bezier(.2, .7, .2, 1);
    }

    .bs-item.bs-fit-full {
      background:
        radial-gradient(ellipse at center, rgba(201, 154, 74, 0.08), transparent 62%),
        #241610;
    }

    .bs-item.bs-fit-full img {
      object-fit: contain;
    }

    .bs-item::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(20, 10, 6, 0.85) 0%, rgba(20, 10, 6, 0.25) 40%, transparent 65%);
      opacity: 0;
      transition: opacity 0.5s ease;
      pointer-events: none;
    }

    .bs-caption {
      position: absolute;
      left: 20px;
      right: 20px;
      bottom: 18px;
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 17px;
      color: var(--cream);
      opacity: 0;
      transform: translateY(8px);
      transition: opacity 0.45s ease, transform 0.45s ease;
      z-index: 2;
      letter-spacing: 0.01em;
    }

    .bs-item:hover img {
      transform: scale(1.05);
    }

    .bs-item.bs-fit-full:hover img {
      transform: none;
    }

    .bs-item:hover::after {
      opacity: 1;
    }

    .bs-item:hover .bs-caption {
      opacity: 1;
      transform: translateY(0);
    }

    .bs-hero {
      grid-area: hero;
    }

    .bs-vert1 {
      grid-area: vert1;
    }

    .bs-vert2 {
      grid-area: vert2;
    }

    .bs-wide1 {
      grid-area: wide1;
    }

    .bs-wide2 {
      grid-area: wide2;
    }'''

    new_css_grid = '''.bs-grid-8 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: clamp(12px, 1.4vw, 18px);
      width: 100%;
    }

    .bs-card {
      position: relative;
      overflow: hidden;
      border-radius: 12px;
      height: clamp(230px, 20vw, 290px);
      background: #1A0F0A;
      margin: 0;
      cursor: pointer;
    }

    .bs-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
      display: block;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .bs-card:hover img {
      transform: scale(1.04);
    }

    .bs-card::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(20, 10, 6, 0.88) 0%, rgba(20, 10, 6, 0.20) 45%, transparent 70%);
      pointer-events: none;
      transition: opacity 0.35s ease;
    }

    .bs-card-caption {
      position: absolute;
      left: 14px;
      right: 14px;
      bottom: 12px;
      margin: 0;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12px, 1.05vw, 13.5px);
      font-weight: 400;
      letter-spacing: 0.5px;
      color: #F7EBD2;
      z-index: 2;
      text-shadow: 0 1px 4px rgba(0, 0, 0, 0.6);
      transition: color 0.3s ease;
    }

    .bs-card:hover .bs-card-caption {
      color: var(--gold);
    }'''

    if old_css_grid in content:
        content = content.replace(old_css_grid, new_css_grid)
        print("Updated main CSS for .bs-grid-8!")
    else:
        # Regex replacement if needed
        pattern_css = re.compile(r'\.bs-grid\s*\{[\s\S]*?\.bs-wide2\s*\{\s*grid-area:\s*wide2;\s*\}')
        if pattern_css.search(content):
            content = pattern_css.sub(new_css_grid, content)
            print("Updated main CSS via pattern for .bs-grid-8!")
        else:
            print("Warning: Could not match exact old_css_grid")

    # 3. Update media queries in index.html for .bs-grid-8
    old_mq_960 = '''    @media (max-width: 960px) {
      .bs-grid {
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 200px 200px 220px clamp(360px, 58vw, 520px) clamp(360px, 58vw, 520px);
        grid-template-areas:
          "hero hero"
          "hero hero"
          "vert1 vert2"
          "wide1 wide1"
          "wide2 wide2";
      }
    }'''

    new_mq_960 = '''    @media (max-width: 960px) {
      .bs-grid-8 {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
      }
      .bs-card {
        height: clamp(210px, 28vw, 260px);
      }
    }'''

    if old_mq_960 in content:
        content = content.replace(old_mq_960, new_mq_960)
        print("Updated media query 960px for .bs-grid-8!")
    else:
        pattern_mq960 = re.compile(r'@media\s*\(max-width:\s*960px\)\s*\{\s*\.bs-grid\s*\{[\s\S]*?\}\s*\}')
        if pattern_mq960.search(content):
            content = pattern_mq960.sub(new_mq_960, content)
            print("Updated media query 960px via pattern!")

    # 4. Update media query 620px for .bs-grid-8
    old_mq_620 = '''      .bs-grid {
        grid-template-columns: 1fr;
        grid-template-rows:
          240px clamp(280px, 72vw, 430px) 240px 240px clamp(280px, 72vw, 430px);
        grid-template-areas:
          "hero"
          "wide1"
          "vert1"
          "vert2"
          "wide2";
      }

      .bs-caption {
        opacity: 1;
        transform: translateY(0);
      }

      .bs-item::after {
        opacity: 1;
      }'''

    new_mq_620 = '''      .bs-grid-8 {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
      }

      .bs-card {
        height: clamp(165px, 23vh, 205px);
        border-radius: 10px;
      }

      .bs-card-caption {
        font-size: 11.5px;
        left: 10px;
        right: 10px;
        bottom: 8px;
      }'''

    if old_mq_620 in content:
        content = content.replace(old_mq_620, new_mq_620)
        print("Updated media query 620px for .bs-grid-8!")
    else:
        pattern_mq620 = re.compile(r'\.bs-grid\s*\{[\s\S]*?\.bs-item::after\s*\{\s*opacity:\s*1;\s*\}')
        if pattern_mq620.search(content):
            content = pattern_mq620.sub(new_mq_620, content)
            print("Updated media query 620px via pattern!")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully with 8-photo layout!")

if __name__ == '__main__':
    apply_update()
