import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update opening hours in HTML
old_hours = "Hotline: 090 123 4567 • Mở cửa: 06:30 - 22:00"
new_hours = "Hotline: 090 123 4567 • Mở cửa: 06:00 - 23:00"

assert old_hours in content, "old_hours not found in content"
content = content.replace(old_hours, new_hours, 1)

# 2. Update CSS for .single-menu-sheet and its inner elements
old_sheet_css = """    /* Single-Page 2-Column Menu Sheet (Fitted Perfectly Inside 720x520 Horizontal Board) */
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
    }

    /* Header: menu. (lowercase bold with subtle dot & underline) */
    .single-menu-header {
      padding-bottom: 4px;
      border-bottom: 1.5px solid var(--ink-dark);
      margin-bottom: 8px;
    }"""

new_sheet_css = """    /* Single-Page 2-Column Menu Sheet (Responsive % Sizing, Zero Bottom Overflow) */
    .single-menu-sheet {
      position: absolute;
      top: 13.5%;     /* Starts right below the wood top clamp */
      bottom: 4%;      /* Sits comfortably above the bottom wood border */
      left: 2.8%;     /* Inset from left wood border */
      right: 2.8%;    /* Inset from right wood border */
      width: auto;
      height: auto;
      background: transparent;
      box-shadow: none;
      color: var(--ink-dark);
      padding: 2px 14px 2px;
      border-radius: 0;
      display: flex;
      flex-direction: column;
      z-index: 10;
      overflow: hidden; /* Prevents text overflow on zoom / shrink */
    }

    /* Header: menu. (lowercase bold with subtle dot & underline) */
    .single-menu-header {
      padding-bottom: 2px;
      border-bottom: 1.5px solid var(--ink-dark);
      margin-bottom: 4px;
    }"""

assert old_sheet_css in content, "old_sheet_css not found in content"
content = content.replace(old_sheet_css, new_sheet_css, 1)

# 3. Update column gap, item padding, and footer CSS
old_cols_css = """    .menu-col-left {
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding-right: 14px;
      border-right: 1px solid rgba(60, 40, 25, 0.16);
    }

    .menu-col-right {
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding-left: 2px;
    }

    /* Category Block */
    .menu-category-block {
      display: flex;
      flex-direction: column;
    }

    .menu-category-heading {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--ink-dark);
      text-transform: uppercase;
      padding-bottom: 3px;
      border-bottom: 1px solid rgba(60, 40, 25, 0.22);
      margin-bottom: 4px;
    }

    /* Dish List & Compact Items */
    .compact-dish-list {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    .compact-dish-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 5px 4px;
      border-radius: 4px;
      transition: all 0.18s ease;
      cursor: pointer;
      position: relative;
    }"""

new_cols_css = """    .menu-col-left {
      display: flex;
      flex-direction: column;
      gap: 5px;
      padding-right: 14px;
      border-right: 1px solid rgba(60, 40, 25, 0.16);
    }

    .menu-col-right {
      display: flex;
      flex-direction: column;
      gap: 5px;
      padding-left: 2px;
    }

    /* Category Block */
    .menu-category-block {
      display: flex;
      flex-direction: column;
    }

    .menu-category-heading {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--ink-dark);
      text-transform: uppercase;
      padding-bottom: 2px;
      border-bottom: 1px solid rgba(60, 40, 25, 0.22);
      margin-bottom: 2px;
    }

    /* Dish List & Compact Items */
    .compact-dish-list {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }

    .compact-dish-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 3.5px 4px;
      border-radius: 4px;
      transition: all 0.18s ease;
      cursor: pointer;
      position: relative;
    }"""

assert old_cols_css in content, "old_cols_css not found in content"
content = content.replace(old_cols_css, new_cols_css, 1)

# 4. Update .single-menu-footer CSS to flex-shrink: 0
old_footer_css = """    /* Footer: address and note */
    .single-menu-footer {
      border-top: 1px solid rgba(60, 40, 25, 0.18);
      padding-top: 5px;
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.66rem;
      color: var(--ink-light);
      letter-spacing: 0.02em;
    }"""

new_footer_css = """    /* Footer: address and note */
    .single-menu-footer {
      border-top: 1px solid rgba(60, 40, 25, 0.18);
      padding-top: 4px;
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.65rem;
      color: var(--ink-light);
      letter-spacing: 0.02em;
      flex-shrink: 0;
    }"""

assert old_footer_css in content, "old_footer_css not found in content"
content = content.replace(old_footer_css, new_footer_css, 1)

# 5. Update minW in setupMenuEdgeResize to 660 for safe aspect ratio height
old_min_w = "const minW = 640; // Ngưỡng tối thiểu đẹp mắt"
new_min_w = "const minW = 660; // Ngưỡng tối thiểu an toàn, bảo đảm không tràn đáy"

assert old_min_w in content, "old_min_w not found in content"
content = content.replace(old_min_w, new_min_w, 1)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: order.html successfully updated with safe menu padding and new opening hours!")

