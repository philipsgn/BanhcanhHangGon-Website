import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update HTML: Remove the 2 arrow buttons
old_html_arrows = """    <!-- Stage Focus Carousel -->
    <div class="menu-stage-wrapper">
      <!-- Navigation Arrow Buttons -->
      <button class="menu-nav-arrow menu-nav-arrow--prev" id="menuPrevBtn" aria-label="Món trước đó">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>
      <button class="menu-nav-arrow menu-nav-arrow--next" id="menuNextBtn" aria-label="Món kế tiếp">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>

      <!-- Carousel Track with 4 Dishes -->"""

new_html_arrows = """    <!-- Stage Focus Carousel (Drag & Swipe Navigation) -->
    <div class="menu-stage-wrapper">
      <!-- Carousel Track with 4 Dishes -->"""

assert old_html_arrows in text, "old_html_arrows not found in HTML!"
text = text.replace(old_html_arrows, new_html_arrows)
print("Removed arrow buttons from HTML!")

# 2. Update CSS: Position mascot at far left edge, widen stage track, lock hover on inactive cards
old_css_part = """    /* Menu Hero Header: Chef Rooster with ropes touching ceiling (Shifted Left) */
    .menu-hero-header {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      max-width: 980px;
      margin: 0 auto clamp(6px, 1.2vw, 14px);
      padding: 0 clamp(16px, 4vw, 40px);
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      position: relative;
      margin-top: 0;
      width: auto;
    }

    /* Ropes reach y=0 to touch the ceiling of #menu */
    .menu-rooster-img {
      width: 100%;
      max-width: clamp(220px, 24vw, 320px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 14px 28px rgba(45, 26, 18, 0.18));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.012) translateY(-2px);
    }

    /* ==========================================================================
       SECTION 4: 3D FOCUS SLIDER (STARBUCKS INSPIRATION & ARTISAN IDENTITY)
       ========================================================================== */
    .menu-stage-wrapper {
      position: relative;
      max-width: 980px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 2;
    }

    /* Arrow Navigation Buttons (Borderless, Subtle Opacity) */
    .menu-nav-arrow {
      position: absolute;
      top: 48%;
      transform: translateY(-50%);
      width: 44px;
      height: 44px;
      background: transparent;
      border: none;
      color: #6B5344;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      opacity: 0.45;
      box-shadow: none;
      transition: all 0.28s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-nav-arrow:hover {
      background: transparent;
      color: #1A1410;
      opacity: 0.95;
      transform: translateY(-50%) scale(1.18);
    }

    .menu-nav-arrow:active {
      transform: translateY(-50%) scale(0.96);
    }

    .menu-nav-arrow--prev {
      left: clamp(4px, 2vw, 20px);
    }

    .menu-nav-arrow--next {
      right: clamp(4px, 2vw, 20px);
    }

    /* Carousel 3D Track (Supports Mouse Drag) */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: 520px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1100px;
      margin-top: 20px;
      cursor: grab;
      user-select: none;
    }

    .menu-carousel-track:active {
      cursor: grabbing;
    }

    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(260px, 28vw, 310px);
      padding: 0 24px 28px;
      border-radius: 28px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1),
                  opacity 0.45s ease,
                  background-color 0.45s ease,
                  box-shadow 0.5s ease,
                  border-color 0.45s ease;
      will-change: transform, opacity;
      cursor: pointer;
    }

    /* Active Card: Tone Nâu Cát & Vàng Kem Ấm Nhẹ Nhàng (#EFE8DD) */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: 1.5px solid #C4A482;
      transform: translate3d(0, -18px, 60px) scale(1.04);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 20px 42px rgba(36, 22, 16, 0.16),
                  0 0 0 1px rgba(196, 164, 130, 0.35);
      cursor: default;
    }

    /* Inactive Cards: Kem Sáng (#FAF7F2) */
    .menu-card.is-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(-88%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 3;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
    }

    .menu-card.is-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(88%, 10px, -40px) scale(0.85);
      opacity: 0.65;
      z-index: 3;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
    }"""

new_css_part = """    /* Menu Hero Header: Chef Rooster Welcoming Guests at Far Left Edge (Treo sát rìa trái) */
    .menu-hero-header {
      position: absolute;
      top: 0;
      left: clamp(12px, 2.8vw, 36px);
      z-index: 8;
      pointer-events: none;
      margin: 0;
      padding: 0;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      position: relative;
      margin-top: 0;
      width: auto;
      pointer-events: auto;
    }

    /* Ropes reach y=0 to touch the ceiling of #menu */
    .menu-rooster-img {
      width: clamp(190px, 19vw, 260px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 14px 28px rgba(45, 26, 18, 0.18));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.015) translateY(-2px);
    }

    /* ==========================================================================
       SECTION 4: 3D FOCUS SLIDER (EXPANDED STAGE & DRAG/SWIPE NAVIGATION)
       ========================================================================== */
    .menu-stage-wrapper {
      position: relative;
      max-width: 1140px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 2;
      padding-top: clamp(16px, 2.5vw, 36px);
    }

    /* Carousel 3D Track (Supports Mouse Drag) */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: 530px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1200px;
      margin-top: 10px;
      cursor: grab;
      user-select: none;
    }

    .menu-carousel-track:active {
      cursor: grabbing;
    }

    /* Individual Card Base */
    .menu-card {
      position: absolute;
      width: clamp(260px, 28vw, 310px);
      padding: 0 24px 28px;
      border-radius: 28px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1),
                  opacity 0.45s ease,
                  background-color 0.45s ease,
                  box-shadow 0.5s ease,
                  border-color 0.45s ease;
      will-change: transform, opacity;
      cursor: grab;
    }

    /* Active Card: Tone Nâu Cát & Vàng Kem Ấm Nhẹ Nhàng (#EFE8DD) */
    .menu-card.is-active {
      background: #EFE8DD;
      color: #1A1410;
      border: 1.5px solid #C4A482;
      transform: translate3d(0, -18px, 60px) scale(1.04);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 20px 42px rgba(36, 22, 16, 0.16),
                  0 0 0 1px rgba(196, 164, 130, 0.35);
      cursor: default;
    }

    /* Inactive Cards: Kem Sáng (#FAF7F2) - Mở rộng cự ly ±108% tạo khoảng thở */
    .menu-card.is-prev {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(-108%, 10px, -45px) scale(0.85);
      opacity: 0.62;
      z-index: 3;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
      cursor: grab;
    }

    .menu-card.is-next {
      background: #FAF7F2;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.2);
      transform: translate3d(108%, 10px, -45px) scale(0.85);
      opacity: 0.62;
      z-index: 3;
      box-shadow: 0 10px 24px rgba(36, 22, 16, 0.08);
      cursor: grab;
    }

    /* KHÓA CỨNG: Tuyệt đối không cho thẻ mờ bị dịch chuyển hay rung lắc khi chạm hờ/hover */
    .menu-card.is-prev:hover {
      transform: translate3d(-108%, 10px, -45px) scale(0.85) !important;
    }

    .menu-card.is-next:hover {
      transform: translate3d(108%, 10px, -45px) scale(0.85) !important;
    }

    .menu-card:not(.is-active) .menu-card-plate {
      transform: none !important;
    }"""

assert old_css_part in text, "old_css_part not found!"
text = text.replace(old_css_part, new_css_part)
print("Updated CSS with left-anchored mascot, 1140px stage, and locked inactive card hover!")

# 3. Update Responsive CSS at max-width: 960px and 600px
old_resp_css = """    /* Responsive adjustments */
    @media (max-width: 960px) {
      .menu-hero-header {
        margin-bottom: 12px;
      }

      .menu-hero-mascot {
        max-width: 280px;
        margin: 0 auto;
      }

      .menu-carousel-track {
        height: 480px;
      }

      .menu-card.is-prev {
        transform: translate3d(-78%, 10px, -40px) scale(0.82);
      }

      .menu-card.is-next {
        transform: translate3d(78%, 10px, -40px) scale(0.82);
      }
    }

    @media (max-width: 600px) {
      #menu {
        padding: 0 12px 36px;
      }

      .menu-carousel-track {
        height: 470px;
        margin-top: 20px;
      }

      .menu-card {
        width: 82vw;
        max-width: 290px;
        padding: 0 18px 24px;
      }

      .menu-card.is-active {
        transform: translate3d(0, -12px, 40px) scale(1);
      }

      .menu-card.is-prev {
        transform: translate3d(-68%, 8px, -40px) scale(0.78);
        opacity: 0.35;
      }

      .menu-card.is-next {
        transform: translate3d(68%, 8px, -40px) scale(0.78);
        opacity: 0.35;
      }

      .menu-nav-arrow {
        width: 38px;
        height: 38px;
      }

      .menu-footer-bar {
        flex-direction: column;
        text-align: center;
        gap: 16px;
      }

      .menu-footer-contact {
        align-items: center;
        text-align: center;
      }
    }"""

new_resp_css = """    /* Responsive adjustments */
    @media (max-width: 960px) {
      .menu-hero-header {
        position: relative;
        left: 0;
        margin: 0 auto 8px;
        justify-content: center;
      }

      .menu-hero-mascot {
        max-width: 240px;
        margin: 0 auto;
      }

      .menu-carousel-track {
        height: 500px;
      }

      .menu-card.is-prev {
        transform: translate3d(-85%, 10px, -40px) scale(0.82) !important;
      }

      .menu-card.is-next {
        transform: translate3d(85%, 10px, -40px) scale(0.82) !important;
      }
    }

    @media (max-width: 600px) {
      #menu {
        padding: 0 12px 36px;
      }

      .menu-hero-header {
        position: relative;
        left: 0;
        margin: 0 auto 6px;
        justify-content: center;
      }

      .menu-hero-mascot {
        max-width: 200px;
        margin: 0 auto;
      }

      .menu-carousel-track {
        height: 480px;
        margin-top: 10px;
      }

      .menu-card {
        width: 82vw;
        max-width: 290px;
        padding: 0 18px 24px;
      }

      .menu-card.is-active {
        transform: translate3d(0, -12px, 40px) scale(1) !important;
      }

      .menu-card.is-prev {
        transform: translate3d(-70%, 8px, -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-card.is-next {
        transform: translate3d(70%, 8px, -40px) scale(0.78) !important;
        opacity: 0.35;
      }

      .menu-footer-bar {
        flex-direction: column;
        text-align: center;
        gap: 16px;
      }

      .menu-footer-contact {
        align-items: center;
        text-align: center;
      }
    }"""

assert old_resp_css in text, "old_resp_css not found!"
text = text.replace(old_resp_css, new_resp_css)
print("Updated responsive CSS!")

# 4. Update JavaScript: Remove button listeners, prevent accidental jumps on light click/hover
old_js_block = """  <!-- 3D Focus Menu Carousel Controller -->
  <script>
    (function () {
      const track = document.getElementById('menuTrack');
      if (!track) return;

      const cards = Array.from(track.querySelectorAll('.menu-card'));
      const dots = Array.from(document.querySelectorAll('.menu-dot'));
      const prevBtn = document.getElementById('menuPrevBtn');
      const nextBtn = document.getElementById('menuNextBtn');
      const total = cards.length;
      let currentIndex = 0;

      function updateCarousel(newIndex) {
        currentIndex = (newIndex + total) % total;

        cards.forEach((card, i) => {
          card.classList.remove('is-active', 'is-prev', 'is-next', 'is-hidden');
          const diff = (i - currentIndex + total) % total;

          if (diff === 0) {
            card.classList.add('is-active');
            card.setAttribute('aria-hidden', 'false');
          } else if (diff === total - 1 || diff === -1) {
            card.classList.add('is-prev');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === 1) {
            card.classList.add('is-next');
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

      if (prevBtn) {
        prevBtn.addEventListener('click', () => updateCarousel(currentIndex - 1));
      }

      if (nextBtn) {
        nextBtn.addEventListener('click', () => updateCarousel(currentIndex + 1));
      }

      cards.forEach((card, idx) => {
        card.addEventListener('click', (e) => {
          // If clicked on CTA button, let navigation happen
          if (e.target.closest('.menu-card-cta')) return;
          if (idx !== currentIndex) {
            e.preventDefault();
            updateCarousel(idx);
          }
        });
      });

      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => updateCarousel(idx));
      });

      // Touch / Swipe Navigation for Mobile
      let touchStartX = 0;
      let touchEndX = 0;

      track.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      track.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      }, { passive: true });

      function handleSwipe() {
        const threshold = 40;
        if (touchEndX < touchStartX - threshold) {
          updateCarousel(currentIndex + 1);
        } else if (touchEndX > touchStartX + threshold) {
          updateCarousel(currentIndex - 1);
        }
      }

      // Mouse Drag-to-Slide for Desktop
      let isDragging = false;
      let dragStartX = 0;
      let dragCurrentX = 0;
      let hasDragged = false;

      track.addEventListener('mousedown', (e) => {
        // If clicking a CTA button or link, let click pass
        if (e.target.closest('a, button')) return;
        isDragging = true;
        hasDragged = false;
        dragStartX = e.pageX;
        dragCurrentX = e.pageX;
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        dragCurrentX = e.pageX;
        if (Math.abs(dragCurrentX - dragStartX) > 10) {
          hasDragged = true;
        }
      });

      window.addEventListener('mouseup', (e) => {
        if (!isDragging) return;
        isDragging = false;
        const diffX = dragCurrentX - dragStartX;
        const dragThreshold = 35;
        if (diffX < -dragThreshold) {
          updateCarousel(currentIndex + 1);
        } else if (diffX > dragThreshold) {
          updateCarousel(currentIndex - 1);
        }
      });

      // Keyboard navigation when track is focused
      window.addEventListener('keydown', (e) => {
        const menuSec = document.getElementById('menu');
        if (!menuSec) return;
        const rect = menuSec.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        if (!isInView) return;

        if (e.key === 'ArrowLeft') {
          updateCarousel(currentIndex - 1);
        } else if (e.key === 'ArrowRight') {
          updateCarousel(currentIndex + 1);
        }
      });

      // Initialize initial state
      updateCarousel(0);
    })();
  </script>"""

new_js_block = """  <!-- 3D Focus Menu Carousel Controller (Pure Mouse Drag & Touch Swipe) -->
  <script>
    (function () {
      const track = document.getElementById('menuTrack');
      if (!track) return;

      const cards = Array.from(track.querySelectorAll('.menu-card'));
      const dots = Array.from(document.querySelectorAll('.menu-dot'));
      const total = cards.length;
      let currentIndex = 0;

      function updateCarousel(newIndex) {
        currentIndex = (newIndex + total) % total;

        cards.forEach((card, i) => {
          card.classList.remove('is-active', 'is-prev', 'is-next', 'is-hidden');
          const diff = (i - currentIndex + total) % total;

          if (diff === 0) {
            card.classList.add('is-active');
            card.setAttribute('aria-hidden', 'false');
          } else if (diff === total - 1 || diff === -1) {
            card.classList.add('is-prev');
            card.setAttribute('aria-hidden', 'true');
          } else if (diff === 1) {
            card.classList.add('is-next');
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

      // Pagination dots click
      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => updateCarousel(idx));
      });

      // Mouse Drag-to-Slide Engine for Desktop (No accidental jump on hover)
      let isDragging = false;
      let dragStartX = 0;
      let dragCurrentX = 0;

      track.addEventListener('mousedown', (e) => {
        // If clicking CTA button, let link navigate
        if (e.target.closest('.menu-card-cta')) return;
        isDragging = true;
        dragStartX = e.pageX;
        dragCurrentX = e.pageX;
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        dragCurrentX = e.pageX;
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
      });

      // Touch / Swipe Navigation for Mobile
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

      // Keyboard navigation
      window.addEventListener('keydown', (e) => {
        const menuSec = document.getElementById('menu');
        if (!menuSec) return;
        const rect = menuSec.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        if (!isInView) return;

        if (e.key === 'ArrowLeft') {
          updateCarousel(currentIndex - 1);
        } else if (e.key === 'ArrowRight') {
          updateCarousel(currentIndex + 1);
        }
      });

      // Initialize initial state
      updateCarousel(0);
    })();
  </script>"""

assert old_js_block in text, "old_js_block not found!"
text = text.replace(old_js_block, new_js_block)
print("Updated JavaScript controller with pure drag & swipe!")

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(text)

print("Applied all changes successfully to index.html!")
