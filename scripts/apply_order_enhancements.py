import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update clipboard-wrapper CSS and add menu resize handles
old_cb = """/* The Wooden Clipboard (Layer 2 - Middle: Elevated & Widened 680px) */
    .clipboard-wrapper {
      position: relative;
      width: 680px;
      min-height: 530px;
      margin-top: 175px;
      background: url('images/order/clipboard_board_only.png') center/cover no-repeat;
      border-radius: 8px;
      box-shadow: var(--shadow-board);
      display: flex;
      flex-direction: column;
      align-items: center;
      user-select: none;
      z-index: 2;
    }"""

new_cb = """/* The Wooden Clipboard (Layer 2 - Middle: Elevated & Widened 680px, Resizable) */
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

assert old_cb in content, "old_cb not found in content"
content = content.replace(old_cb, new_cb, 1)

# 2. Update single-menu-sheet width so it stretches dynamically with clipboard-wrapper
old_sms = """/* Single-Page 2-Column Menu Sheet (Widened 644px & Seamless Bottom Fit) */
    .single-menu-sheet {
      position: absolute;
      top: 48px;
      bottom: 16px;
      width: 644px;
      height: calc(100% - 64px);"""

new_sms = """/* Single-Page 2-Column Menu Sheet (Dynamic Stretch & Seamless Bottom Fit) */
    .single-menu-sheet {
      position: absolute;
      top: 48px;
      bottom: 16px;
      left: 18px;
      right: 18px;
      width: auto;
      height: calc(100% - 64px);"""

assert old_sms in content, "old_sms not found in content"
content = content.replace(old_sms, new_sms, 1)

# 3. Update order-slip-col and guest-check-card CSS
old_slip_css = """    /* ==========================================================================
       3. RIGHT COLUMN: ARTISAN GUEST CHECK (DRAGGABLE & DOCKABLE - 340px)
       ========================================================================== */
    .order-slip-col {
      flex: 0 0 340px;
      position: relative;
      margin-top: 175px;
      align-self: flex-start;
    }

    .guest-check-card {
      width: 340px;"""

new_slip_css = """    /* ==========================================================================
       3. RIGHT COLUMN: ARTISAN GUEST CHECK (DRAGGABLE, DOCKABLE & RESIZABLE)
       ========================================================================== */
    .order-slip-col {
      flex: 0 0 auto;
      width: var(--slip-width, 380px);
      position: relative;
      margin-top: 175px;
      align-self: flex-start;
      transition: width 0.05s ease-out;
    }

    .guest-check-card {
      width: 100%;"""

assert old_slip_css in content, "old_slip_css not found in content"
content = content.replace(old_slip_css, new_slip_css, 1)

# 4. Add CSS for slip resize edges (left and right)
old_corners = """    .resize-corner-br {
      bottom: 0;
      right: 0;
      cursor: nwse-resize;
      border-bottom: 2.5px solid rgba(201, 154, 74, 0.7);
      border-right: 2.5px solid rgba(201, 154, 74, 0.7);
    }"""

new_corners = """    .resize-corner-br {
      bottom: 0;
      right: 0;
      cursor: nwse-resize;
      border-bottom: 2.5px solid rgba(201, 154, 74, 0.7);
      border-right: 2.5px solid rgba(201, 154, 74, 0.7);
    }

    /* Slip Width Resize Handles (Kéo 2 bên trái/phải để mở rộng phiếu) */
    .slip-resize-edge {
      position: absolute;
      top: 0;
      bottom: 0;
      width: 14px;
      z-index: 55;
      cursor: ew-resize;
      touch-action: none;
    }

    .slip-resize-edge-left {
      left: -7px;
    }

    .slip-resize-edge-right {
      right: -7px;
    }

    .slip-resize-edge:hover::after,
    .slip-resize-edge.resizing::after {
      content: '';
      position: absolute;
      top: 10%;
      bottom: 10%;
      left: 6px;
      width: 2px;
      background: rgba(201, 154, 74, 0.85);
      border-radius: 1px;
      box-shadow: 0 0 8px rgba(201, 154, 74, 0.7);
    }"""

assert old_corners in content, "old_corners not found in content"
content = content.replace(old_corners, new_corners, 1)

# 5. Clean scrollbar on check-card-body (Remove grey scrollbar)
old_body_scroll = """    .check-card-body {
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      max-height: calc(100vh - 360px);
      overflow-y: auto;
    }"""

new_body_scroll = """    .check-card-body {
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      max-height: calc(100vh - 360px);
      overflow-y: auto;
      scrollbar-width: none;
      -ms-overflow-style: none;
    }

    .check-card-body::-webkit-scrollbar {
      display: none;
      width: 0;
      height: 0;
    }"""

assert old_body_scroll in content, "old_body_scroll not found in content"
content = content.replace(old_body_scroll, new_body_scroll, 1)

# 6. HTML: Insert menu resize handles in #clipboardWrapper
old_cb_html = """        <!-- 2. Middle Layer: The Wooden Clipboard (z-index: 2) -->
        <div class="clipboard-wrapper" id="clipboardWrapper">
          <!-- Top Clamp Graphic Overlay -->
          <div class="clipboard-clamp"></div>"""

new_cb_html = """        <!-- 2. Middle Layer: The Wooden Clipboard (z-index: 2) -->
        <div class="clipboard-wrapper" id="clipboardWrapper">
          <!-- Top Clamp Graphic Overlay -->
          <div class="clipboard-clamp"></div>

          <!-- Menu Resize Handles (Kéo mép phải & mép đáy) -->
          <div class="menu-resize-edge-r" id="menuResizeEdgeR" title="Kéo mép phải để giãn độ rộng Menu"></div>
          <div class="menu-resize-edge-b" id="menuResizeEdgeB" title="Kéo mép đáy để giãn chiều dài Menu"></div>"""

assert old_cb_html in content, "old_cb_html not found in content"
content = content.replace(old_cb_html, new_cb_html, 1)

# 7. HTML: Insert slip resize handles in #guestCheckCard
old_card_html = """      <aside class="guest-check-card" id="guestCheckCard">
        <!-- 4 Corner Resize Handles (Kéo 4 góc để co giãn tỷ lệ phiếu) -->
        <div class="resize-corner resize-corner-tl" data-corner="tl" title="Kéo để thu phóng phiếu"></div>
        <div class="resize-corner resize-corner-tr" data-corner="tr" title="Kéo để thu phóng phiếu"></div>
        <div class="resize-corner resize-corner-bl" data-corner="bl" title="Kéo để thu phóng phiếu"></div>
        <div class="resize-corner resize-corner-br" data-corner="br" title="Kéo để thu phóng phiếu"></div>"""

new_card_html = """      <aside class="guest-check-card" id="guestCheckCard">
        <!-- 4 Corner Resize Handles (Kéo 4 góc để co giãn tỷ lệ phiếu) -->
        <div class="resize-corner resize-corner-tl" data-corner="tl" title="Kéo để thu phóng phiếu"></div>
        <div class="resize-corner resize-corner-tr" data-corner="tr" title="Kéo để thu phóng phiếu"></div>
        <div class="resize-corner resize-corner-bl" data-corner="bl" title="Kéo để thu phóng phiếu"></div>
        <div class="resize-corner resize-corner-br" data-corner="br" title="Kéo để thu phóng phiếu"></div>

        <!-- Mép kéo giãn chiều rộng 2 bên trái/phải -->
        <div class="slip-resize-edge slip-resize-edge-left" data-edge="left" title="Kéo sang trái để mở rộng phiếu"></div>
        <div class="slip-resize-edge slip-resize-edge-right" data-edge="right" title="Kéo sang phải để mở rộng phiếu"></div>"""

assert old_card_html in content, "old_card_html not found in content"
content = content.replace(old_card_html, new_card_html, 1)

# 8. JS: In card mousedown and touchstart, ignore .slip-resize-edge
old_card_md = "if (e.target.closest('.resize-corner') || e.target.closest('input') || e.target.closest('button') || e.target.closest('table')) return;"
new_card_md = "if (e.target.closest('.resize-corner') || e.target.closest('.slip-resize-edge') || e.target.closest('input') || e.target.closest('button') || e.target.closest('table')) return;"

assert old_card_md in content, "old_card_md not found in content"
content = content.replace(old_card_md, new_card_md) # Replaces both mousedown and touchstart

# 9. JS: Call setupSlipEdgeResize and setupMenuEdgeResize in DOMContentLoaded
old_dom_init = """    document.addEventListener('DOMContentLoaded', () => {
      initLiveClock();
      setInterval(initLiveClock, 1000);
      initOrderCode();
      setupItemClickListeners();
      setupDragDropGuestCheck();
      setupCornerResize();
    });"""

new_dom_init = """    document.addEventListener('DOMContentLoaded', () => {
      initLiveClock();
      setInterval(initLiveClock, 1000);
      initOrderCode();
      setupItemClickListeners();
      setupDragDropGuestCheck();
      setupCornerResize();
      setupSlipEdgeResize();
      setupMenuEdgeResize();
    });"""

assert old_dom_init in content, "old_dom_init not found in content"
content = content.replace(old_dom_init, new_dom_init, 1)

# 10. JS: Add implementations for setupSlipEdgeResize and setupMenuEdgeResize
js_insert_target = """    // Mobile Sheet Toggle
    function toggleMobileSheet(open) {"""

new_js_functions = """    // 3. Kéo giãn chiều ngang 2 bên trái/phải của Phiếu Order (Slip Width Resize)
    let currentSlipWidth = 380;
    function setupSlipEdgeResize() {
      const card = document.getElementById('guestCheckCard');
      const col = document.querySelector('.order-slip-col');
      if (!card || !col) return;

      let isResizing = false;
      let startX = 0;
      let startWidth = 380;
      let activeEdge = null;
      const minW = 320;
      const maxW = 540;

      document.querySelectorAll('.slip-resize-edge').forEach(edge => {
        edge.addEventListener('mousedown', (e) => {
          e.stopPropagation();
          e.preventDefault();
          isResizing = true;
          activeEdge = edge.getAttribute('data-edge');
          startX = e.clientX;
          startWidth = currentSlipWidth;
          edge.classList.add('resizing');

          document.addEventListener('mousemove', onEdgeMove);
          document.addEventListener('mouseup', onEdgeUp);
        });

        edge.addEventListener('touchstart', (e) => {
          e.stopPropagation();
          const t = e.touches[0];
          isResizing = true;
          activeEdge = edge.getAttribute('data-edge');
          startX = t.clientX;
          startWidth = currentSlipWidth;
          edge.classList.add('resizing');
        }, { passive: false });
      });

      function onEdgeMove(e) {
        if (!isResizing) return;
        applyWidthDelta(e.clientX - startX);
      }

      function onEdgeUp() {
        if (!isResizing) return;
        isResizing = false;
        document.querySelectorAll('.slip-resize-edge').forEach(el => el.classList.remove('resizing'));
        document.removeEventListener('mousemove', onEdgeMove);
        document.removeEventListener('mouseup', onEdgeUp);
      }

      window.addEventListener('touchmove', (e) => {
        if (!isResizing) return;
        const t = e.touches[0];
        applyWidthDelta(t.clientX - startX);
      }, { passive: false });

      window.addEventListener('touchend', () => {
        if (!isResizing) return;
        isResizing = false;
        document.querySelectorAll('.slip-resize-edge').forEach(el => el.classList.remove('resizing'));
      });

      function applyWidthDelta(dx) {
        let newWidth = startWidth;
        if (activeEdge === 'right') {
          newWidth = startWidth + dx;
        } else if (activeEdge === 'left') {
          newWidth = startWidth - dx;
        }
        newWidth = Math.min(Math.max(newWidth, minW), maxW);
        currentSlipWidth = newWidth;
        col.style.setProperty('--slip-width', newWidth + 'px');
      }
    }

    // 4. Kéo giãn Bảng Menu ở mép phải (Width) và mép đáy bottom (Height)
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
    }

    // Mobile Sheet Toggle
    function toggleMobileSheet(open) {"""

assert js_insert_target in content, "js_insert_target not found in content"
content = content.replace(js_insert_target, new_js_functions, 1)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: order.html successfully enhanced with bilateral resize and clean order slip!")

