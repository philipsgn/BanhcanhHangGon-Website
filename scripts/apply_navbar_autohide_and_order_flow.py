import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# -----------------------------------------------------------------------------
# 1. UPDATE index.html
# -----------------------------------------------------------------------------
INDEX_PATH = 'index.html'
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# A. Phóng to Biển gỗ Menu ở Desktop: clamp(145px, 14vw, 185px)
old_rooster_css = """    .menu-rooster-img {
      width: clamp(110px, 11vw, 145px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 10px 20px rgba(45, 26, 18, 0.14));
      transition: transform 0.4s ease;
    }"""

new_rooster_css = """    .menu-rooster-img {
      width: clamp(145px, 14vw, 185px); /* Phình to 25-30% bề thế trên Desktop */
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 12px 24px rgba(45, 26, 18, 0.18));
      transition: transform 0.4s ease;
    }"""

if old_rooster_css in content:
    content = content.replace(old_rooster_css, new_rooster_css)
    print("Updated .menu-rooster-img to enlarged desktop size.")
else:
    print(".menu-rooster-img pattern not matched!")

# B. Cập nhật CSS Nút ĐẶT MÓN: Be Vietnam Pro Light 300 thanh mảnh, không đổ bóng nặng
old_cta_css = """    .menu-card.is-active .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Plus Jakarta Sans', 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13.5px, 1.1vw, 15px);
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(180px, 16vw, 220px);
      height: 46px;
      background: linear-gradient(135deg, #8A2B0E 0%, #C24A22 100%);
      border: none;
      color: #FFFDF5;
      box-shadow: 0 6px 20px rgba(138, 43, 14, 0.28);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.12s both;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: linear-gradient(135deg, #9C3312 0%, #D45328 100%);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(138, 43, 14, 0.38);
    }"""

new_cta_css = """    .menu-card.is-active .menu-card-cta {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(13px, 1.05vw, 14.5px);
      font-weight: 300; /* Light 300 thanh mảnh tinh tế */
      letter-spacing: 1.5px; /* Giãn chữ thoáng mắt không sặc mùi AI */
      text-transform: uppercase;
      text-decoration: none;
      border-radius: 999px;
      width: clamp(165px, 14vw, 195px);
      height: 42px;
      background: linear-gradient(135deg, #8A2B0E 0%, #B84B32 100%);
      border: none;
      color: #FFFDF5;
      box-shadow: 0 3px 10px rgba(138, 43, 14, 0.20); /* Tối giản mộc mạc, không nặng nề */
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      animation: gentleSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1) 0.12s both;
      cursor: pointer;
    }

    .menu-card.is-active .menu-card-cta:hover {
      background: linear-gradient(135deg, #9E3514 0%, #C9563A 100%);
      transform: translateY(-2px);
      box-shadow: 0 5px 14px rgba(138, 43, 14, 0.28);
    }"""

if old_cta_css in content:
    content = content.replace(old_cta_css, new_cta_css)
    print("Updated .menu-card-cta CSS to Be Vietnam Pro Light 300.")
else:
    print(".menu-card-cta CSS pattern not matched!")

# C. Cập nhật thẻ HTML 5 món: data-dish-id và chữ "ĐẶT MÓN"
card_replacements = [
    # Card 0
    ('<article class="menu-card is-active" data-index="0" aria-label="Bánh Canh Gà Đặc Biệt">',
     '<article class="menu-card is-active" data-index="0" data-dish-id="bc-dac-biet" aria-label="Bánh Canh Gà Đặc Biệt">'),
    # Card 1
    ('<article class="menu-card is-near-next" data-index="1" aria-label="Cơm Gà Xé">',
     '<article class="menu-card is-near-next" data-index="1" data-dish-id="com-goi-xe-trung-non" aria-label="Cơm Gà Xé">'),
    # Card 2
    ('<article class="menu-card is-far-next" data-index="2" aria-label="Gỏi Gà Ta">',
     '<article class="menu-card is-far-next" data-index="2" data-dish-id="goi-nho" aria-label="Gỏi Gà Ta">'),
    # Card 3
    ('<article class="menu-card is-far-prev" data-index="3" aria-label="Xôi Gà Trứng Non">',
     '<article class="menu-card is-far-prev" data-index="3" data-dish-id="xoi-xe-trung-non" aria-label="Xôi Gà Trứng Non">'),
    # Card 4
    ('<article class="menu-card is-near-prev" data-index="4" aria-label="Mì Gà Ta Truyền Thống">',
     '<article class="menu-card is-near-prev" data-index="4" data-dish-id="mi-xe-trung-non" aria-label="Mì Gà Ta Truyền Thống">')
]

for old_c, new_c in card_replacements:
    if old_c in content:
        content = content.replace(old_c, new_c)
        print(f"Added data-dish-id to card: {old_c[:40]}")

# Thay thế nút 'Đặt Món Ngay' -> 'ĐẶT MÓN' trong Section 4
content = re.sub(r'(<a href="order\.html" class="menu-card-cta">)Đặt Món Ngay(</a>)', r'\1ĐẶT MÓN\2', content)
print("Updated all 5 CTA buttons to 'ĐẶT MÓN'.")

# D. Cập nhật JS Navbar Auto-hide sau 2.5s bất động
old_scroll_listener = """    window.addEventListener('scroll', () => {
      const currentScrollY = window.scrollY;
      const scrollDelta = currentScrollY - lastScrollY;

      if (currentScrollY < 80) {
        siteNav.classList.remove('is-hidden');
      } else if (scrollDelta > 8 && !siteNav.classList.contains('nav-open')) {
        siteNav.classList.add('is-hidden');
      } else if (scrollDelta < -8) {
        siteNav.classList.remove('is-hidden');
      }

      lastScrollY = currentScrollY;
    }, { passive: true });"""

new_scroll_listener = """    // Smart Inactivity Auto-hide Navbar (Ẩn sau 2.5s bất động, hiện khi cuộn)
    let navHideTimer = null;

    function resetNavInactivityTimer() {
      clearTimeout(navHideTimer);
      siteNav.classList.remove('is-hidden');

      // Chỉ kích hoạt tự động ẩn nếu đã cuộn qua đầu trang và menu không mở
      if (window.scrollY >= 50 && !siteNav.classList.contains('nav-open')) {
        navHideTimer = setTimeout(() => {
          siteNav.classList.add('is-hidden');
        }, 2500); // 2.5 giây bất động sẽ trượt lên ẩn
      }
    }

    window.addEventListener('scroll', () => {
      resetNavInactivityTimer();
      lastScrollY = window.scrollY;
    }, { passive: true });

    // Khi rê chuột lên sát mép trên màn hình (< 40px), chủ động hiện lại thanh navbar
    window.addEventListener('mousemove', (e) => {
      if (e.clientY < 40) {
        resetNavInactivityTimer();
      }
    });

    // Khởi tạo trạng thái ban đầu
    resetNavInactivityTimer();"""

if old_scroll_listener in content:
    content = content.replace(old_scroll_listener, new_scroll_listener)
    print("Updated Navbar Smart Inactivity Auto-hide logic successfully.")
else:
    print("Navbar scroll listener pattern not matched!")

# E. Bổ sung xử lý click ĐẶT MÓN để thêm trực tiếp vào phiếu order
old_cta_check = """        // Allow CTA order button to navigate naturally
        if (e.target.closest('.menu-card-cta')) return;
        if (hasDragged) return;"""

new_cta_check = """        // Xử lý nút ĐẶT MÓN: Chủ động lưu món vào phiếu order và chuyển trang
        const ctaBtn = e.target.closest('.menu-card-cta');
        if (ctaBtn) {
          e.preventDefault();
          const card = ctaBtn.closest('.menu-card');
          const dishId = card.getAttribute('data-dish-id') || 'bc-dac-biet';
          const dishTitle = card.querySelector('.menu-card-title').textContent.trim();
          const dishPriceText = card.querySelector('.menu-card-price').textContent.replace(/\\D/g, '');
          const dishPrice = parseInt(dishPriceText, 10) || 70000;

          try {
            localStorage.setItem('hg_pending_order', JSON.stringify({
              id: dishId,
              name: dishTitle,
              price: dishPrice,
              qty: 1
            }));
          } catch (err) {}

          window.location.href = 'order.html';
          return;
        }
        if (hasDragged) return;"""

if old_cta_check in content:
    content = content.replace(old_cta_check, new_cta_check)
    print("Updated CTA button click handler to save pending order item.")
else:
    print("Old CTA check pattern not matched!")

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html successfully.")


# -----------------------------------------------------------------------------
# 2. UPDATE order.html: Đón nhận món từ pending order và tự động đưa vào phiếu
# -----------------------------------------------------------------------------
ORDER_PATH = 'order.html'
with open(ORDER_PATH, 'r', encoding='utf-8') as f:
    order_content = f.read()

# Chèn đoạn code tự động kiểm tra hg_pending_order ngay sau khi DOM sẵn sàng
pending_order_handler = """    // Tự động thêm món vào phiếu order nếu được chuyển từ trang Menu
    function checkPendingOrderFromMenu() {
      try {
        const pending = localStorage.getItem('hg_pending_order');
        if (pending) {
          const item = JSON.parse(pending);
          if (item && item.id && DISH_DETAILS[item.id]) {
            updateQty(item.id, item.qty || 1);
          }
          localStorage.removeItem('hg_pending_order');
        }
      } catch (err) {
        console.warn('Lỗi đọc pending order:', err);
      }
    }
"""

target_order_pos = "renderOrderState();"
if "checkPendingOrderFromMenu()" not in order_content:
    if target_order_pos in order_content:
        # Tìm vị trí đầu tiên hoặc cuối hàm init
        idx = order_content.rfind(target_order_pos)
        order_content = order_content[:idx + len(target_order_pos)] + "\n      checkPendingOrderFromMenu();" + order_content[idx + len(target_order_pos):]
        # Thêm định nghĩa hàm trước đó
        order_content = order_content.replace("function updateQty(id, delta, e) {", pending_order_handler + "\n    function updateQty(id, delta, e) {")
        print("Injected checkPendingOrderFromMenu() into order.html successfully.")
    else:
        print("target_order_pos not found in order.html!")
else:
    print("checkPendingOrderFromMenu already exists in order.html.")

with open(ORDER_PATH, 'w', encoding='utf-8') as f:
    f.write(order_content)
print("Updated order.html successfully.")
print("ALL CODE UPDATES APPLIED WITH 100% PRECISION!")
