import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Menu Hero Header CSS to align left
old_hero_header = """    /* Menu Hero Header: Chef Rooster with ropes touching ceiling */
    .menu-hero-header {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      max-width: 100%;
      margin: 0 auto clamp(6px, 1.2vw, 14px);
      padding: 0;
    }

    .menu-hero-mascot {
      display: flex;
      justify-content: center;
      align-items: flex-start;
      position: relative;
      margin-top: 0;
      width: 100%;
    }"""

new_hero_header = """    /* Menu Hero Header: Chef Rooster with ropes touching ceiling (Shifted Left) */
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
    }"""

assert old_hero_header in text, "old_hero_header not found!"
text = text.replace(old_hero_header, new_hero_header)
print("Updated hero header alignment to Left!")

# 2. Update Nav Arrows CSS (borderless, subtle opacity)
old_arrows = """    /* Arrow Navigation Buttons */
    .menu-nav-arrow {
      position: absolute;
      top: 48%;
      transform: translateY(-50%);
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 1.5px solid #D8C3A5;
      color: #241610;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 10;
      box-shadow: 0 6px 18px rgba(36, 22, 16, 0.16);
      transition: all 0.28s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-nav-arrow:hover {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
      transform: translateY(-50%) scale(1.08);
      box-shadow: 0 8px 22px rgba(158, 94, 43, 0.3);
    }

    .menu-nav-arrow:active {
      transform: translateY(-50%) scale(0.96);
    }"""

new_arrows = """    /* Arrow Navigation Buttons (Borderless, Subtle Opacity) */
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
    }"""

assert old_arrows in text, "old_arrows not found!"
text = text.replace(old_arrows, new_arrows)
print("Updated Nav Arrows to borderless & subtle opacity!")

# 3. Update Carousel Track height & grab cursor
old_track = """    /* Carousel 3D Track */
    .menu-carousel-track {
      position: relative;
      width: 100%;
      height: 490px;
      display: flex;
      align-items: center;
      justify-content: center;
      perspective: 1100px;
      margin-top: 24px;
    }"""

new_track = """    /* Carousel 3D Track (Supports Mouse Drag) */
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
    }"""

assert old_track in text, "old_track not found!"
text = text.replace(old_track, new_track)
print("Updated Track height to 520px and added grab cursor!")

# 4. Update Cards styling: Nâu Cát & Vàng Kem nhẹ nhàng, tách đĩa không chạm tiêu đề
old_cards = """    /* Active Card: Gỗ Mun Sơn Mài & Vàng Hoàng Kim */
    .menu-card.is-active {
      background: #241610;
      color: #FAF7F2;
      border: 1.5px solid rgba(201, 154, 74, 0.45);
      transform: translate3d(0, -18px, 60px) scale(1.04);
      opacity: 1;
      z-index: 6;
      box-shadow: 0 26px 52px rgba(28, 16, 10, 0.38),
                  0 0 0 1px rgba(201, 154, 74, 0.2);
      cursor: default;
    }

    /* Inactive Cards: Kem Giấy Dó */
    .menu-card.is-prev {
      background: #F4EFEB;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.22);
      transform: translate3d(-88%, 10px, -40px) scale(0.85);
      opacity: 0.62;
      z-index: 3;
      box-shadow: 0 12px 28px rgba(36, 22, 16, 0.1);
    }

    .menu-card.is-next {
      background: #F4EFEB;
      color: #4A3B32;
      border: 1px solid rgba(201, 154, 74, 0.22);
      transform: translate3d(88%, 10px, -40px) scale(0.85);
      opacity: 0.62;
      z-index: 3;
      box-shadow: 0 12px 28px rgba(36, 22, 16, 0.1);
    }

    .menu-card.is-hidden {
      opacity: 0;
      transform: translate3d(0, 30px, -120px) scale(0.7);
      pointer-events: none;
      z-index: 1;
    }

    /* Card Plate Visual (Pop-out 3D Effect) */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -64px;
      margin-bottom: 12px;
      z-index: 2;
    }

    .menu-card-plate {
      width: clamp(170px, 20vw, 205px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 16px 28px rgba(24, 12, 6, 0.35));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.04) translateY(-4px);
      filter: drop-shadow(0 20px 32px rgba(0, 0, 0, 0.45));
    }

    /* Authentic Contact Shadow under plate */
    .menu-card-contact-shadow {
      position: absolute;
      bottom: -6px;
      width: 65%;
      height: 14px;
      background: radial-gradient(ellipse at center, rgba(16, 8, 4, 0.6) 0%, rgba(16, 8, 4, 0) 70%);
      border-radius: 50%;
      z-index: -1;
      pointer-events: none;
    }

    /* Card Content Typography */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(16px, 1.5vw, 19px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 6px;
      text-transform: uppercase;
      line-height: 1.25;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-title {
      color: #F6E2B6;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-title {
      color: #241610;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(21px, 2vw, 25px);
      font-weight: 900;
      margin: 0 0 8px;
      letter-spacing: 0.03em;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-price {
      color: #FFFFFF;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-price {
      color: #9E5E2B;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12px, 0.88vw, 13px);
      line-height: 1.48;
      font-weight: 300;
      margin: 0 0 16px;
      max-width: 250px;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card.is-active .menu-card-desc {
      color: #E2D9D2;
      opacity: 0.95;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-desc {
      color: #6A584D;
      opacity: 0.75;
      /* keep concise on inactive cards */
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* CTA Button */
    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 200px;
      padding: 9px 20px;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      transition: all 0.28s ease;
      cursor: pointer;
    }

    .menu-card.is-active .menu-card-cta {
      background: #C99A4A;
      color: #1A1009;
      box-shadow: 0 6px 16px rgba(201, 154, 74, 0.35);
      opacity: 1;
      pointer-events: auto;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: #DFB469;
      transform: translateY(-2px);
      box-shadow: 0 8px 22px rgba(201, 154, 74, 0.45);
    }"""

new_cards = """    /* Active Card: Tone Nâu Cát & Vàng Kem Ấm Nhẹ Nhàng (#EFE8DD) */
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
    }

    .menu-card.is-hidden {
      opacity: 0;
      transform: translate3d(0, 30px, -120px) scale(0.7);
      pointer-events: none;
      z-index: 1;
    }

    /* Card Plate Visual (Nhô cao, tạo khoảng cách an toàn không đè tiêu đề) */
    .menu-card-visual {
      position: relative;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: -85px;
      margin-bottom: 24px;
      z-index: 2;
    }

    .menu-card-plate {
      width: clamp(165px, 19vw, 195px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 14px 24px rgba(24, 12, 6, 0.28));
      transition: transform 0.45s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .menu-card.is-active .menu-card-plate {
      transform: scale(1.04) translateY(-4px);
      filter: drop-shadow(0 18px 28px rgba(0, 0, 0, 0.35));
    }

    /* Authentic Contact Shadow under plate */
    .menu-card-contact-shadow {
      position: absolute;
      bottom: -6px;
      width: 65%;
      height: 14px;
      background: radial-gradient(ellipse at center, rgba(16, 8, 4, 0.5) 0%, rgba(16, 8, 4, 0) 70%);
      border-radius: 50%;
      z-index: -1;
      pointer-events: none;
    }

    /* Card Content Typography - Nổi bật, sắc nét, tương phản cao */
    .menu-card-body {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
    }

    .menu-card-title {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(16px, 1.5vw, 19px);
      font-weight: 800;
      letter-spacing: 0.02em;
      margin: 0 0 6px;
      text-transform: uppercase;
      line-height: 1.25;
      color: #1A1410;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-title {
      color: #1A1410;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-title {
      color: #33241C;
    }

    .menu-card-price {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(21px, 2vw, 25px);
      font-weight: 900;
      margin: 0 0 8px;
      letter-spacing: 0.03em;
      color: #8A4A1C;
      transition: color 0.35s ease;
    }

    .menu-card.is-active .menu-card-price {
      color: #8A4A1C;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-price {
      color: #9E5E2B;
    }

    .menu-card-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12px, 0.88vw, 13px);
      line-height: 1.48;
      font-weight: 300;
      margin: 0 0 16px;
      max-width: 250px;
      color: #4A3C33;
      transition: opacity 0.35s ease, color 0.35s ease;
    }

    .menu-card.is-active .menu-card-desc {
      color: #4A3C33;
      opacity: 1;
    }

    .menu-card:not(.menu-card.is-active) .menu-card-desc {
      color: #6A584D;
      opacity: 0.8;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    /* CTA Button */
    .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      max-width: 200px;
      padding: 9px 20px;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      transition: all 0.28s ease;
      cursor: pointer;
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
    }"""

assert old_cards in text, "old_cards not found!"
text = text.replace(old_cards, new_cards)
print("Updated Cards styling to Nâu Cát & Vàng Kem with clear spacing!")

# 5. Update JavaScript Controller for Mouse Drag-to-Slide
old_js = """      // Touch / Swipe Navigation for Mobile
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
      }"""

new_js = """      // Touch / Swipe Navigation for Mobile
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
      });"""

assert old_js in text, "old_js not found!"
text = text.replace(old_js, new_js)
print("Updated JS controller with Mouse Drag-to-Slide!")

with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(text)

print("index.html refined successfully with all requested updates!")
