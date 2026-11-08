import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'index.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Typography CSS in Section 4 (.menu-card.is-active .menu-card-title, .menu-card-desc, etc.)
old_typo_css = """    .menu-card.is-active .menu-card-title {
      font-family: 'Playfair Display', 'Cormorant Garamond', Georgia, serif;
      font-size: clamp(26px, 2.3vw, 34px);
      font-weight: 700;
      letter-spacing: 0.015em;
      margin: 0 0 6px;
      line-height: 1.22;
      color: #24120A;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    .menu-card.is-active .menu-card-price {
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(26px, 2.4vw, 34px);
      font-weight: 800;
      margin: 0 0 8px;
      letter-spacing: 0.01em;
      color: #BD3C0D;
      text-shadow: 0 1px 2px rgba(255, 255, 255, 0.7);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.04s both;
    }

    .menu-card.is-active .menu-card-desc {
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14px, 1.05vw, 16px);
      line-height: 1.55;
      font-weight: 400;
      margin: 0 0 18px;
      max-width: 440px;
      color: #4A3528;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.08s both;
    }"""

new_typo_css = """    .menu-card.is-active .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(25px, 2.2vw, 33px);
      font-weight: 800;
      letter-spacing: -0.015em;
      margin: 0 0 6px;
      line-height: 1.24;
      color: #1A0F08;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) both;
    }

    .menu-card.is-active .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(24px, 2.2vw, 32px);
      font-weight: 800;
      margin: 0 0 8px;
      letter-spacing: -0.01em;
      color: #BD3C0D;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.04s both;
    }

    .menu-card.is-active .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(14px, 1.05vw, 15.5px);
      line-height: 1.6;
      font-weight: 400;
      margin: 0 0 18px;
      max-width: 440px;
      color: #38251B;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.08s both;
    }"""

if old_typo_css in content:
    content = content.replace(old_typo_css, new_typo_css)
    print("Updated Typography to Be Vietnam Pro successfully.")
else:
    print("Old Typography block not matched exactly!")

# 2. Replace Footer CSS (.menu-footer-bar and sub-elements) with .menu-footer-clean & .menu-all-dishes-gold-link
old_footer_css_pattern = r'/\* Thanh Footer Menu \*/\s*\.menu-footer-bar\s*\{.*?(?=/\* RESPONSIVE QUERIES)'
match_footer_css = re.search(old_footer_css_pattern, content, re.DOTALL)

new_footer_css = """/* Thanh Footer Menu: Nền trơn không viền, Chữ vàng kim với 2 gạch trên dưới */
    .menu-footer-clean {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      margin-top: clamp(14px, 2.2vh, 24px);
      padding: 0;
      background: transparent !important;
      border: none !important;
      box-shadow: none !important;
      z-index: 5;
    }

    .menu-all-dishes-gold-link {
      position: relative;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 0;
      padding: 8px 24px 9px;
      color: #ffd978;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(15px, 1.3vw, 18px);
      font-weight: 600;
      letter-spacing: 2.8px;
      line-height: 1;
      text-transform: uppercase;
      text-decoration: none;
      text-shadow:
        0 1px 0 rgba(255, 246, 204, 0.42),
        0 0 10px rgba(255, 187, 58, 0.42),
        0 0 22px rgba(201, 112, 26, 0.28);
      background:
        linear-gradient(90deg, transparent 0%, rgba(144, 91, 28, 0.42) 18%, rgba(255, 218, 105, 0.92) 50%, rgba(144, 91, 28, 0.42) 82%, transparent 100%) center top / 100% 1.5px no-repeat,
        linear-gradient(90deg, transparent 0%, rgba(144, 91, 28, 0.45) 18%, rgba(255, 218, 105, 0.95) 50%, rgba(144, 91, 28, 0.45) 82%, transparent 100%) center bottom / 100% 1.5px no-repeat;
      transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-all-dishes-gold-link:hover,
    .menu-all-dishes-gold-link:focus-visible {
      color: #fff0b8;
      transform: translateY(-2px);
      text-shadow:
        0 1px 0 rgba(255, 246, 204, 0.65),
        0 0 14px rgba(255, 200, 70, 0.65),
        0 0 28px rgba(201, 112, 26, 0.45);
    }

    """

if match_footer_css:
    content = content[:match_footer_css.start()] + new_footer_css + content[match_footer_css.end():]
    print("Updated Footer CSS successfully.")
else:
    print("Footer CSS regex pattern not matched!")

# 3. Clean up mobile media query footer rules
old_mob_footer = """      .menu-footer-bar {
        border-radius: 16px;
        padding: 10px 14px;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        text-align: center;
      }

      .menu-footer-contact {
        align-items: center;
      }"""

new_mob_footer = """      .menu-footer-clean {
        margin-top: 14px;
      }"""

if old_mob_footer in content:
    content = content.replace(old_mob_footer, new_mob_footer)
    print("Updated mobile footer CSS successfully.")
else:
    print("Mobile footer block not matched directly!")

# 4. Replace HTML footer block in Section 4
old_html_footer = """    <!-- Menu Footer Bar -->
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
    </footer>"""

new_html_footer = """    <!-- Menu Footer: Nền trơn không viền, chữ vàng kim Toàn Bộ Thực Đơn với 2 gạch trên dưới như ĐẶT HÀNG -->
    <footer class="menu-footer-clean">
      <a href="order.html" class="menu-all-dishes-gold-link">TOÀN BỘ THỰC ĐƠN</a>
    </footer>"""

if old_html_footer in content:
    content = content.replace(old_html_footer, new_html_footer)
    print("Updated HTML Footer to clean gold link successfully.")
else:
    print("HTML Footer block not matched!")

# 5. Update JavaScript carousel controller: Active Viewport Centering on tap/click
old_js_click = """        // If clicked specifically on any inactive card
        const clickedCard = e.target.closest('.menu-card');
        if (clickedCard) {
          const idx = Number(clickedCard.dataset.index);
          if (!isNaN(idx) && idx !== currentIndex) {
            e.preventDefault();
            updateCarousel(idx);
            return;
          }
        }

        // Smart hit testing: click left half -> prev, right half -> next
        const rect = track.getBoundingClientRect();
        const clickX = e.clientX;
        const centerX = rect.left + rect.width / 2;
        const deadZone = 55; // safe center buffer on the active card body
        if (clickX < centerX - deadZone) {
          e.preventDefault();
          updateCarousel(currentIndex - 1);
        } else if (clickX > centerX + deadZone) {
          e.preventDefault();
          updateCarousel(currentIndex + 1);
        }"""

new_js_click = """        function centerMenuInViewport() {
          const menuSec = document.getElementById('menu');
          if (menuSec) {
            const rect = menuSec.getBoundingClientRect();
            const targetY = window.pageYOffset + rect.top + (rect.height / 2) - (window.innerHeight / 2);
            window.scrollTo({
              top: targetY,
              behavior: 'smooth'
            });
          }
        }

        // Khi người dùng chạm vào món ăn, chủ động chuyển món về Center và canh giữa viewport
        const clickedCard = e.target.closest('.menu-card');
        if (clickedCard) {
          const idx = Number(clickedCard.dataset.index);
          if (!isNaN(idx)) {
            e.preventDefault();
            updateCarousel(idx);
            centerMenuInViewport();
            return;
          }
        }

        // Smart hit testing: click left half -> prev, right half -> next
        const rect = track.getBoundingClientRect();
        const clickX = e.clientX;
        const centerX = rect.left + rect.width / 2;
        const deadZone = 55; // safe center buffer on the active card body
        if (clickX < centerX - deadZone) {
          e.preventDefault();
          updateCarousel(currentIndex - 1);
          centerMenuInViewport();
        } else if (clickX > centerX + deadZone) {
          e.preventDefault();
          updateCarousel(currentIndex + 1);
          centerMenuInViewport();
        }"""

if old_js_click in content:
    content = content.replace(old_js_click, new_js_click)
    print("Updated JavaScript click & active viewport centering successfully.")
else:
    print("JavaScript click block not matched!")

# Also update touch end event to call centerMenuInViewport if needed
old_touch = """        if (touchEndX < touchStartX - threshold) {
          updateCarousel(currentIndex + 1);
        } else if (touchEndX > touchStartX + threshold) {
          updateCarousel(currentIndex - 1);
        }"""

new_touch = """        if (touchEndX < touchStartX - threshold) {
          updateCarousel(currentIndex + 1);
          centerMenuInViewport();
        } else if (touchEndX > touchStartX + threshold) {
          updateCarousel(currentIndex - 1);
          centerMenuInViewport();
        }"""

if old_touch in content:
    content = content.replace(old_touch, new_touch)
    print("Updated touch event with centerMenuInViewport.")

# Also update dots click
old_dots = """      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => updateCarousel(idx));
      });"""

new_dots = """      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => {
          updateCarousel(idx);
          centerMenuInViewport();
        });
      });"""

if old_dots in content:
    content = content.replace(old_dots, new_dots)
    print("Updated dots click with centerMenuInViewport.")

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("ALL CHANGES WRITTEN TO index.html SUCCESSFULLY!")
