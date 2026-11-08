import re

with open('index.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Normalize all line endings to simple \n
clean = raw.replace('\r\n', '\n').replace('\r', '\n')
# Collapse any triple or more consecutive newlines down to double newlines
clean = re.sub(r'\n{3,}', '\n\n', clean)

print("Line count after normalizing newlines:", len(clean.split('\n')))

# Now let's find the section between /* SECTION 4: MENU */ or .menu-editorial-container
# Let's inspect where .menu-editorial-container is
pos = clean.find('.menu-editorial-container {')
print("Position of .menu-editorial-container:", pos)

# Find where .menu-footer-bar starts
pos_footer = clean.find('.menu-footer-bar {')
print("Position of .menu-footer-bar:", pos_footer)

# Replace the block from .menu-editorial-container { to .menu-footer-bar {
menu_block_replacement = """    .menu-editorial-container {
      position: relative;
      z-index: 1;
      max-width: 740px;
      margin: 0 auto;
      width: 100%;
    }

    /* Menu Hero Header: Chef Rooster with ropes touching ceiling */
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
    }

    /* Ropes reach y=0 to touch the ceiling of #menu */
    .menu-rooster-img {
      width: 100%;
      max-width: clamp(220px, 24vw, 340px);
      height: auto;
      object-fit: contain;
      display: block;
      filter: drop-shadow(0 14px 28px rgba(45, 26, 18, 0.18));
      transition: transform 0.4s ease;
    }

    .menu-hero-mascot:hover .menu-rooster-img {
      transform: scale(1.012) translateY(-2px);
    }

    /* Tightened Zigzag Dish Rows (Snug 24-28px gap, Zero bloat) */
    .menu-dish-row {
      display: grid;
      grid-template-columns: minmax(0, 1.35fr) minmax(0, 1fr);
      align-items: center;
      gap: clamp(14px, 2.2vw, 28px);
      margin-bottom: clamp(6px, 1vw, 12px);
      position: relative;
    }

    .menu-dish-row:last-of-type {
      margin-bottom: clamp(8px, 1.2vw, 14px);
    }

    /* Reverse variant for Zigzag */
    .menu-dish-row--reverse {
      grid-template-columns: minmax(0, 1fr) minmax(0, 1.35fr);
    }

    .menu-dish-row--reverse .menu-dish-visual {
      order: 1;
    }

    .menu-dish-row--reverse .menu-dish-info {
      order: 2;
    }

    /* Dish Info Box (Text side) */
    .menu-dish-info {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      text-align: left;
      padding: 0;
      position: relative;
      z-index: 2;
    }

    .menu-dish-header-row {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 3px;
      flex-wrap: wrap;
    }

    .menu-dish-name {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(17px, 1.6vw, 21px);
      font-weight: 800;
      letter-spacing: 0.02em;
      color: #111111;
      margin: 0;
      text-transform: uppercase;
      line-height: 1.15;
    }

    /* Black Circular Price Badge */
    .menu-price-circle {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
      background: #111111;
      color: #FFFFFF;
      border-radius: 50%;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 13px;
      font-weight: 800;
      flex-shrink: 0;
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.18);
      user-select: none;
    }

    .menu-dish-desc {
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: clamp(12px, 0.88vw, 13px);
      line-height: 1.45;
      font-weight: 300;
      color: #55443B;
      margin: 0 0 4px;
      max-width: 440px;
    }

    /* Thin Horizontal Accent Line */
    .menu-accent-line {
      width: min(200px, 70%);
      height: 1.5px;
      background: #222222;
      opacity: 0.8;
      margin: 2px 0 6px;
    }

    /* Action order button */
    .menu-order-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 4px 14px;
      background: transparent;
      color: #9E5E2B;
      border: 1.5px solid #C48E59;
      border-radius: 999px;
      font-family: 'Be Vietnam Pro', sans-serif;
      font-size: 11.5px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.28s ease;
      cursor: pointer;
    }

    .menu-order-btn:hover,
    .menu-order-btn:focus-visible {
      background: #9E5E2B;
      color: #FFFFFF;
      border-color: #9E5E2B;
      transform: translateY(-2px);
      box-shadow: 0 5px 14px rgba(158, 94, 43, 0.24);
    }

    /* Dish Visual (Snug compact plate presentation) */
    .menu-dish-visual {
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      z-index: 1;
    }

    .menu-dish-img {
      width: 100%;
      max-width: clamp(160px, 18vw, 190px);
      height: auto;
      object-fit: contain;
      filter: drop-shadow(0 12px 22px rgba(36, 22, 16, 0.2));
      transition: transform 0.35s ease;
    }

    .menu-dish-img:hover {
      transform: scale(1.02);
    }
"""

if pos != -1 and pos_footer != -1:
    clean = clean[:pos] + menu_block_replacement + "\n\n" + clean[pos_footer:]
    print("Replaced menu CSS block successfully!")
else:
    print("Could not find markers for replacement!")

# Also update responsive media query for 960px and 600px
clean = re.sub(
    r'\.menu-hero-mascot\s*\{\s*max-width:\s*\d+px;\s*margin:\s*0 auto;\s*\}',
    '.menu-hero-mascot {\n        max-width: 280px;\n        margin: 0 auto;\n      }',
    clean
)

clean = re.sub(
    r'\.menu-dish-visual \.menu-dish-img\s*\{\s*max-height:\s*\d+px;\s*\}',
    '.menu-dish-visual .menu-dish-img {\n        max-height: 170px;\n      }',
    clean
)

# Write out using newline='' to prevent auto-conversion to \r\r\n
with open('index.html', 'w', encoding='utf-8', newline='') as f:
    f.write(clean)

print("Wrote clean index.html successfully!")
