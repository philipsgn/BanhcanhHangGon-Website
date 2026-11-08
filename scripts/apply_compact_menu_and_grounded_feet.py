import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update mascot, feet shadows, and board CSS
old_css_block = """    /* Rooster Mascot Body (Layer 1 - Background: Hugging Left Edge) */
    .rooster-mascot-body {
      position: absolute;
      left: 0;
      top: 0;
      width: 590px;
      height: auto;
      z-index: 1;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(4px 14px 26px rgba(0, 0, 0, 0.65));
      transition: all 0.3s ease;
    }

    /* The Wooden Clipboard (Layer 2 - Middle: Unified Single WebP Board, Aspect Ratio Locked) */
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
    }

    /* Menu Resize Handles (Kéo mép phải và mép đáy bottom) */
    .menu-resize-edge-r {
      position: absolute;
      top: 20px;
      bottom: 20px;
      right: -6px;
      width: 14px;
      cursor: ew-resize;
      z-index: 45;
      touch-action: none;
    }

    .menu-resize-edge-b {
      position: absolute;
      left: 20px;
      right: 20px;
      bottom: -6px;
      height: 14px;
      cursor: ns-resize;
      z-index: 45;
      touch-action: none;
    }

    .menu-resize-edge-r:hover::after,
    .menu-resize-edge-r.resizing::after {
      content: '';
      position: absolute;
      top: 15%;
      bottom: 15%;
      left: 6px;
      width: 2px;
      background: rgba(201, 154, 74, 0.85);
      border-radius: 1px;
      box-shadow: 0 0 8px rgba(201, 154, 74, 0.7);
    }

    .menu-resize-edge-b:hover::after,
    .menu-resize-edge-b.resizing::after {
      content: '';
      position: absolute;
      left: 15%;
      right: 15%;
      top: 6px;
      height: 2px;
      background: rgba(201, 154, 74, 0.85);
      border-radius: 1px;
      box-shadow: 0 0 8px rgba(201, 154, 74, 0.7);
    }"""

new_css_block = """    /* Rooster Mascot Body (Layer 1 - Grounded on wooden table) */
    .rooster-mascot-body {
      position: absolute;
      left: 0;
      top: 15px;
      width: 620px;
      height: auto;
      z-index: 1;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(4px 14px 26px rgba(0, 0, 0, 0.65));
      transition: all 0.3s ease;
    }

    /* The Wooden Clipboard (Layer 2 - Middle: Compact Horizontal 720x520 WebP Board) */
    .clipboard-wrapper {
      position: relative;
      width: var(--menu-width, 720px);
      aspect-ratio: 720 / 520;
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

    /* Subtle Menu Corner Resize Handle (Chỉ 1 tay nắm nhỏ ở góc dưới phải) */
    .menu-resize-corner-br {
      position: absolute;
      right: 0;
      bottom: 0;
      width: 18px;
      height: 18px;
      cursor: nwse-resize;
      z-index: 45;
      border-bottom: 2.5px solid rgba(201, 154, 74, 0.7);
      border-right: 2.5px solid rgba(201, 154, 74, 0.7);
      border-radius: 0 0 6px 0;
      touch-action: none;
      transition: all 0.2s ease;
    }

    .menu-resize-corner-br:hover,
    .menu-resize-corner-br.resizing {
      border-color: var(--gold);
      box-shadow: 2px 2px 8px rgba(201, 154, 74, 0.6);
    }

    /* Ambient Occlusion Arm Shadow (Bóng đổ mềm giữa cánh gà & mép trái bảng menu) */
    .rooster-arm-shadow {
      position: absolute;
      left: 0;
      top: 72px;
      width: 32px;
      height: 180px;
      background: linear-gradient(to right, rgba(20, 10, 5, 0.45) 0%, rgba(20, 10, 5, 0.15) 50%, transparent 100%);
      pointer-events: none;
      z-index: 15;
      border-radius: 12px 0 0 0;
    }

    /* Feet Contact Shadows (Bóng tiếp xúc dính sát ngay dưới móng chân gà tiếp đất) */
    .rooster-feet-shadows {
      position: absolute;
      left: 0;
      top: 15px;
      width: 620px;
      height: 780px;
      pointer-events: none;
      z-index: 0;
    }

    .foot-shadow-l {
      position: absolute;
      left: 55px;
      top: 765px;
      width: 110px;
      height: 20px;
      background: radial-gradient(ellipse at center, rgba(10, 5, 2, 0.88) 0%, rgba(18, 9, 4, 0.5) 45%, transparent 75%);
      filter: blur(2px);
      transform: rotate(-3deg);
    }

    .foot-shadow-r {
      position: absolute;
      left: 195px;
      top: 765px;
      width: 110px;
      height: 20px;
      background: radial-gradient(ellipse at center, rgba(10, 5, 2, 0.88) 0%, rgba(18, 9, 4, 0.5) 45%, transparent 75%);
      filter: blur(2px);
      transform: rotate(2deg);
    }"""

assert old_css_block in content, "old_css_block not found in content"
content = content.replace(old_css_block, new_css_block, 1)

# 2. Update .rooster-claw-top and .rooster-claw-mid CSS
old_claws = """    .rooster-claw-top {
      position: absolute;
      left: 105px;
      top: -16px;
      width: 85px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.6));
    }

    .rooster-claw-mid {
      position: absolute;
      left: -8px;
      top: 135px;
      width: 40px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(2px 2px 5px rgba(0, 0, 0, 0.55));
    }"""

new_claws = """    .rooster-claw-top {
      position: absolute;
      left: 115px;
      top: -14px;
      width: 85px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.6));
    }

    .rooster-claw-mid {
      position: absolute;
      left: -8px;
      top: 125px;
      width: 40px;
      height: auto;
      z-index: 35;
      pointer-events: none;
      user-select: none;
      filter: drop-shadow(2px 2px 5px rgba(0, 0, 0, 0.55));
    }"""

assert old_claws in content, "old_claws not found in content"
content = content.replace(old_claws, new_claws, 1)

# 3. Update .single-menu-sheet and .menu-two-col-grid CSS
old_sheet = """/* Single-Page 2-Column Menu Sheet (Seamlessly Overlaying Natural Paper of WebP Board) */
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

new_sheet = """/* Single-Page 2-Column Menu Sheet (Fitted Perfectly Inside 720x520 Horizontal Board) */
    .single-menu-sheet {
      position: absolute;
      top: 72px;      /* Starts right below the wood top clamp */
      bottom: 24px;   /* Sits comfortably above the bottom wood border */
      left: 20px;     /* Inset from left wood border */
      right: 20px;    /* Inset from right wood border */
      width: auto;
      height: auto;
      background: transparent;
      box-shadow: none;
      color: var(--ink-dark);
      padding: 4px 14px 4px;
      border-radius: 0;
      display: flex;
      flex-direction: column;
      z-index: 10;
    }"""

assert old_sheet in content, "old_sheet not found in content"
content = content.replace(old_sheet, new_sheet, 1)

# 4. Update gap in .menu-two-col-grid
old_grid = """    /* 2-Column Grid (Spacious 28px gap) */
    .menu-two-col-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 28px;
      position: relative;
      flex: 1;
    }"""

new_grid = """    /* 2-Column Grid (Spacious 36px gap for wide horizontal layout) */
    .menu-two-col-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 36px;
      position: relative;
      flex: 1;
    }"""

assert old_grid in content, "old_grid not found in content"
content = content.replace(old_grid, new_grid, 1)

# 5. Update HTML: Replace menu-resize-edge-r and menu-resize-edge-b with menu-resize-corner-br
old_html_handles = """          <!-- Menu Resize Handles (Kéo mép phải & mép đáy) -->
          <div class="menu-resize-edge-r" id="menuResizeEdgeR" title="Kéo mép phải để giãn độ rộng Menu"></div>
          <div class="menu-resize-edge-b" id="menuResizeEdgeB" title="Kéo mép đáy để giãn chiều dài Menu"></div>"""

new_html_handles = """          <!-- Subtle Corner Handle (Kéo góc dưới phải để phóng to/thu nhỏ đồng tỷ lệ) -->
          <div class="menu-resize-corner-br" id="menuResizeCornerBR" title="Kéo góc để thu phóng tỷ lệ Menu"></div>"""

assert old_html_handles in content, "old_html_handles not found in content"
content = content.replace(old_html_handles, new_html_handles, 1)

# 6. Update setupMenuEdgeResize in JS to listen to menuResizeCornerBR with 720:520 ratio
old_js_menu = """    // 4. Kéo giãn Bảng Menu Cố Định Tỷ Lệ Vàng (Aspect Ratio 678:872 Locked)
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

new_js_menu = """    // 4. Kéo giãn Bảng Menu Cố Định Tỷ Lệ Vàng (720 : 520 Ratio Locked)
    let currentMenuWidth = 720;
    const MENU_ASPECT_RATIO = 720 / 520; // ~1.3846
    function setupMenuEdgeResize() {
      const menu = document.getElementById('clipboardWrapper');
      const corner = document.getElementById('menuResizeCornerBR');
      if (!menu || !corner) return;

      let isResizing = false;
      let startX = 0, startY = 0;
      let startW = 720;

      const minW = 640; // Ngưỡng tối thiểu đẹp mắt
      const maxW = 800; // Ngưỡng tối đa vừa vặn khung hình 1080p

      corner.addEventListener('mousedown', (e) => {
        e.stopPropagation();
        e.preventDefault();
        isResizing = true;
        startX = e.clientX;
        startY = e.clientY;
        startW = currentMenuWidth;
        corner.classList.add('resizing');
        document.addEventListener('mousemove', onMenuMove);
        document.addEventListener('mouseup', onMenuUp);
      });

      corner.addEventListener('touchstart', (e) => {
        e.stopPropagation();
        const t = e.touches[0];
        isResizing = true;
        startX = t.clientX;
        startY = t.clientY;
        startW = currentMenuWidth;
        corner.classList.add('resizing');
      }, { passive: false });

      function onMenuMove(e) {
        if (!isResizing) return;
        const dx = e.clientX - startX;
        const dy = e.clientY - startY;
        // Dùng delta trung bình để co giãn đồng tỷ lệ mượt mà
        const delta = (dx + dy * MENU_ASPECT_RATIO) / 2;
        let nw = Math.min(Math.max(startW + delta, minW), maxW);
        currentMenuWidth = nw;
        menu.style.setProperty('--menu-width', nw + 'px');
      }

      function onMenuUp() {
        if (!isResizing) return;
        isResizing = false;
        corner.classList.remove('resizing');
        document.removeEventListener('mousemove', onMenuMove);
        document.removeEventListener('mouseup', onMenuUp);
      }

      window.addEventListener('touchmove', (e) => {
        if (!isResizing) return;
        const t = e.touches[0];
        const dx = t.clientX - startX;
        const dy = t.clientY - startY;
        const delta = (dx + dy * MENU_ASPECT_RATIO) / 2;
        let nw = Math.min(Math.max(startW + delta, minW), maxW);
        currentMenuWidth = nw;
        menu.style.setProperty('--menu-width', nw + 'px');
      }, { passive: false });

      window.addEventListener('touchend', () => {
        if (!isResizing) return;
        isResizing = false;
        corner.classList.remove('resizing');
      });
    }"""

assert old_js_menu in content, "old_js_menu not found in content"
content = content.replace(old_js_menu, new_js_menu, 1)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: order.html successfully updated with compact horizontal menu and grounded feet!")

