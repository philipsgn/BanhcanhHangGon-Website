import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .clipboard-wrapper CSS and related classes
old_cb_css = """    /* The Wooden Clipboard (Layer 2 - Middle: Elevated & Widened 680px, Resizable) */
    .clipboard-wrapper {
      position: relative;
      width: var(--menu-width, 680px);
      min-height: var(--menu-height, 530px);
      margin-top: 175px;
      background: url('images/order/clipboard_board_only.png') center/cover no-repeat;
      border-radius: 8px;
      box-shadow: var(--shadow-board);
      display: flex;
      flex-direction: column;
      align-items: center;
      user-select: none;
      z-index: 2;
      transition: width 0.05s ease-out, min-height 0.05s ease-out;
    }"""

new_cb_css = """    /* The Wooden Clipboard (Layer 2 - Middle: Unified Single WebP Board, Aspect Ratio Locked) */
    .clipboard-wrapper {
      position: relative;
      width: var(--menu-width, 640px);
      aspect-ratio: 678 / 872;
      height: auto;
      margin-top: 175px;
      background: url('images/order/clipboard_board_only.webp') center/100% 100% no-repeat;
      display: flex;
      flex-direction: column;
      align-items: center;
      user-select: none;
      z-index: 2;
      filter: drop-shadow(0 16px 36px rgba(0, 0, 0, 0.52));
      transition: width 0.05s ease-out;
    }

    /* Ambient Occlusion Arm Shadow (Bóng đổ mềm giữa cánh gà & mép trái bảng menu) */
    .rooster-arm-shadow {
      position: absolute;
      left: 0;
      top: 10%;
      width: 32px;
      height: 38%;
      background: linear-gradient(to right, rgba(20, 10, 5, 0.45) 0%, rgba(20, 10, 5, 0.15) 50%, transparent 100%);
      pointer-events: none;
      z-index: 15;
      border-radius: 12px 0 0 0;
    }

    /* Feet Contact Shadows (Bóng tiếp xúc 2 bàn chân gà bám chặt thớt gỗ) */
    .rooster-feet-shadows {
      position: absolute;
      left: 0;
      top: 10px;
      width: 590px;
      height: 740px;
      pointer-events: none;
      z-index: 0;
    }

    .foot-shadow-l {
      position: absolute;
      left: 65px;
      top: 725px;
      width: 95px;
      height: 22px;
      background: radial-gradient(ellipse at center, rgba(12, 6, 3, 0.85) 0%, rgba(18, 9, 4, 0.45) 50%, transparent 75%);
      filter: blur(2.5px);
      transform: rotate(-3deg);
    }

    .foot-shadow-r {
      position: absolute;
      left: 185px;
      top: 725px;
      width: 95px;
      height: 22px;
      background: radial-gradient(ellipse at center, rgba(12, 6, 3, 0.85) 0%, rgba(18, 9, 4, 0.45) 50%, transparent 75%);
      filter: blur(2.5px);
      transform: rotate(2deg);
    }"""

assert old_cb_css in content, "old_cb_css not found in content"
content = content.replace(old_cb_css, new_cb_css, 1)

# 2. Update .single-menu-sheet CSS: Remove white/cream gradient background and lock inside natural paper area
old_sms_css = """/* Single-Page 2-Column Menu Sheet (Dynamic Stretch & Seamless Bottom Fit) */
    .single-menu-sheet {
      position: absolute;
      top: 48px;
      bottom: 16px;
      left: 18px;
      right: 18px;
      width: auto;
      height: calc(100% - 64px);
      background-color: var(--paper-cream);
      background-image: 
        radial-gradient(ellipse at 50% 15%, rgba(255, 255, 255, 0.5) 0%, transparent 80%),
        linear-gradient(to bottom, #fdfbf7 0%, #f4ece0 100%);
      color: var(--ink-dark);
      padding: 14px 24px 12px;
      border-radius: 2px;
      box-shadow: 0 4px 16px rgba(40, 25, 15, 0.14);
      display: flex;
      flex-direction: column;
      z-index: 10;
    }"""

new_sms_css = """/* Single-Page 2-Column Menu Sheet (Seamlessly Overlaying Natural Paper of WebP Board) */
    .single-menu-sheet {
      position: absolute;
      top: 9.5%;     /* Starts right below the real wood top clamp */
      bottom: 4.5%;  /* Sits comfortably above the bottom wood border */
      left: 3.5%;    /* Inset from left wood border */
      right: 3.5%;   /* Inset from right wood border */
      width: auto;
      height: auto;
      background: transparent;
      box-shadow: none;
      color: var(--ink-dark);
      padding: 10px 18px 8px;
      border-radius: 0;
      display: flex;
      flex-direction: column;
      z-index: 10;
    }"""

assert old_sms_css in content, "old_sms_css not found in content"
content = content.replace(old_sms_css, new_sms_css, 1)

# 3. Remove .clipboard-clamp CSS rule completely
old_clamp_css = """    /* Top Clamp */
    .clipboard-clamp {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 58px;
      background: url('images/order/clipboard_top_clamp.png') top center/cover no-repeat;
      z-index: 30;
      pointer-events: none;
      filter: drop-shadow(0 5px 7px rgba(0, 0, 0, 0.45));
    }"""

new_clamp_css = """    /* Top Clamp is now integrated 100% seamlessly in clipboard_board_only.webp */"""

assert old_clamp_css in content, "old_clamp_css not found in content"
content = content.replace(old_clamp_css, new_clamp_css, 1)

# 4. Update HTML in rooster-menu-holder: Add feet shadows, remove clipboard-clamp, add arm shadow
old_holder_html = """      <div class="rooster-menu-holder" id="roosterMenuHolder">
                <!-- 1. Background Mascot Layer: Thân & Chân Chú Gà Trống Đầu Bếp (z-index: 1) -->
        <img src="images/order/rooster_mascot_body_opt.webp"
             alt="Mascot Gà Trống Đầu Bếp Hàng Gòn"
             class="rooster-mascot-body"
             id="roosterMascotBody" />

        <!-- 2. Middle Layer: The Wooden Clipboard (z-index: 2) -->
        <div class="clipboard-wrapper" id="clipboardWrapper">
          <!-- Top Clamp Graphic Overlay -->
          <div class="clipboard-clamp"></div>"""

new_holder_html = """      <div class="rooster-menu-holder" id="roosterMenuHolder">
        <!-- 0. Feet Contact Shadows: Bóng tiếp xúc 2 bàn chân gà chạm mặt thớt gỗ (z-index: 0) -->
        <div class="rooster-feet-shadows">
          <div class="foot-shadow-l"></div>
          <div class="foot-shadow-r"></div>
        </div>

        <!-- 1. Background Mascot Layer: Thân & Chân Chú Gà Trống Đầu Bếp (z-index: 1) -->
        <img src="images/order/rooster_mascot_body_opt.webp"
             alt="Mascot Gà Trống Đầu Bếp Hàng Gòn"
             class="rooster-mascot-body"
             id="roosterMascotBody" />

        <!-- 2. Middle Layer: The Wooden Clipboard (z-index: 2, 100% Unified WebP Board) -->
        <div class="clipboard-wrapper" id="clipboardWrapper">
          <!-- Ambient Occlusion Arm Shadow (Bóng đổ cánh gà lên mép bảng) -->
          <div class="rooster-arm-shadow"></div>"""

assert old_holder_html in content, "old_holder_html not found in content"
content = content.replace(old_holder_html, new_holder_html, 1)

# 5. Update setupMenuEdgeResize in JS to enforce Aspect Ratio Locking (678 / 872)
old_menu_js = """    // 4. Kéo giãn Bảng Menu ở mép phải (Width) và mép đáy bottom (Height)
    let currentMenuWidth = 680;
    let currentMenuHeight = 530;
    function setupMenuEdgeResize() {
      const menu = document.getElementById('clipboardWrapper');
      const edgeR = document.getElementById('menuResizeEdgeR');
      const edgeB = document.getElementById('menuResizeEdgeB');
      if (!menu || !edgeR || !edgeB) return;

      let isResizing = false;
      let activeDir = null;
      let startX = 0, startY = 0;
      let startW = 680, startH = 530;

      const minW = 640, maxW = 820;
      const minH = 480, maxH = 650; // Giới hạn an toàn giữ khoảng cách món đẹp

      function startResize(dir, clientX, clientY, targetEl) {
        isResizing = true;
        activeDir = dir;
        startX = clientX;
        startY = clientY;
        startW = currentMenuWidth;
        startH = currentMenuHeight;
        targetEl.classList.add('resizing');
      }

      edgeR.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        e.preventDefault();
        startResize('width', e.clientX, e.clientY, edgeR);
        document.addEventListener('mousemove', onMenuMove);
        document.addEventListener('mouseup', onMenuUp);
      });

      edgeB.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        e.preventDefault();
        startResize('height', e.clientX, e.clientY, edgeB);
        document.addEventListener('mousemove', onMenuMove);
        document.addEventListener('mouseup', onMenuUp);
      });

      edgeR.addEventListener('touchstart', (e) => {
        e.stopPropagation();
        const t = e.touches[0];
        startResize('width', t.clientX, t.clientY, edgeR);
      }, { passive: false });

      edgeB.addEventListener('touchstart', (e) => {
        e.stopPropagation();
        const t = e.touches[0];
        startResize('height', t.clientX, t.clientY, edgeB);
      }, { passive: false });

      function onMenuMove(e) {
        if (!isResizing) return;
        applyDelta(e.clientX - startX, e.clientY - startY);
      }

      function onMenuUp() {
        if (!isResizing) return;
        isResizing = false;
        edgeR.classList.remove('resizing');
        edgeB.classList.remove('resizing');
        document.removeEventListener('mousemove', onMenuMove);
        document.removeEventListener('mouseup', onMenuUp);
      }

      window.addEventListener('touchmove', (e) => {
        if (!isResizing) return;
        const t = e.touches[0];
        applyDelta(t.clientX - startX, t.clientY - startY);
      }, { passive: false });

      window.addEventListener('touchend', () => {
        if (!isResizing) return;
        isResizing = false;
        edgeR.classList.remove('resizing');
        edgeB.classList.remove('resizing');
      });

      function applyDelta(dx, dy) {
        if (activeDir === 'width') {
          const nw = Math.min(Math.max(startW + dx, minW), maxW);
          currentMenuWidth = nw;
          menu.style.setProperty('--menu-width', nw + 'px');
        } else if (activeDir === 'height') {
          const nh = Math.min(Math.max(startH + dy, minH), maxH);
          currentMenuHeight = nh;
          menu.style.setProperty('--menu-height', nh + 'px');
        }
      }
    }"""

new_menu_js = """    // 4. Kéo giãn Bảng Menu Cố Định Tỷ Lệ Vàng (Aspect Ratio 678:872 Locked)
    let currentMenuWidth = 640;
    const MENU_ASPECT_RATIO = 678 / 872; // ~0.7775
    function setupMenuEdgeResize() {
      const menu = document.getElementById('clipboardWrapper');
      const edgeR = document.getElementById('menuResizeEdgeR');
      const edgeB = document.getElementById('menuResizeEdgeB');
      if (!menu || !edgeR || !edgeB) return;

      let isResizing = false;
      let activeDir = null;
      let startX = 0, startY = 0;
      let startW = 640;

      const minW = 560; // Ngưỡng tối thiểu đẹp mắt
      const maxW = 740; // Ngưỡng tối đa vừa vặn khung hình 1080p

      function startResize(dir, clientX, clientY, targetEl) {
        isResizing = true;
        activeDir = dir;
        startX = clientX;
        startY = clientY;
        startW = currentMenuWidth;
        targetEl.classList.add('resizing');
      }

      edgeR.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        e.preventDefault();
        startResize('width', e.clientX, e.clientY, edgeR);
        document.addEventListener('mousemove', onMenuMove);
        document.addEventListener('mouseup', onMenuUp);
      });

      edgeB.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        e.preventDefault();
        startResize('height', e.clientX, e.clientY, edgeB);
        document.addEventListener('mousemove', onMenuMove);
        document.addEventListener('mouseup', onMenuUp);
      });

      edgeR.addEventListener('touchstart', (e) => {
        e.stopPropagation();
        const t = e.touches[0];
        startResize('width', t.clientX, t.clientY, edgeR);
      }, { passive: false });

      edgeB.addEventListener('touchstart', (e) => {
        e.stopPropagation();
        const t = e.touches[0];
        startResize('height', t.clientX, t.clientY, edgeB);
      }, { passive: false });

      function onMenuMove(e) {
        if (!isResizing) return;
        applyDelta(e.clientX - startX, e.clientY - startY);
      }

      function onMenuUp() {
        if (!isResizing) return;
        isResizing = false;
        edgeR.classList.remove('resizing');
        edgeB.classList.remove('resizing');
        document.removeEventListener('mousemove', onMenuMove);
        document.removeEventListener('mouseup', onMenuUp);
      }

      window.addEventListener('touchmove', (e) => {
        if (!isResizing) return;
        const t = e.touches[0];
        applyDelta(t.clientX - startX, t.clientY - startY);
      }, { passive: false });

      window.addEventListener('touchend', () => {
        if (!isResizing) return;
        isResizing = false;
        edgeR.classList.remove('resizing');
        edgeB.classList.remove('resizing');
      });

      function applyDelta(dx, dy) {
        let nw = startW;
        if (activeDir === 'width') {
          nw = startW + dx;
        } else if (activeDir === 'height') {
          // Tính width tương ứng từ delta Y theo tỷ lệ vàng
          nw = startW + (dy * MENU_ASPECT_RATIO);
        }
        nw = Math.min(Math.max(nw, minW), maxW);
        currentMenuWidth = nw;
        menu.style.setProperty('--menu-width', nw + 'px');
      }
    }"""

assert old_menu_js in content, "old_menu_js not found in content"
content = content.replace(old_menu_js, new_menu_js, 1)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: order.html successfully updated with unified clipboard and realistic rooster layering!")

