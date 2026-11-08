import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect CSS boundary
css_menu_start = html.find('#menu {')
css_menu_end = html.find('/* ---------- SECTION 3 : STORY ---------- */')
print(f"CSS #menu found from {css_menu_start} to {css_menu_end}")

# Let's inspect HTML boundary
html_menu_start = html.find('<section id="menu">')
html_menu_end = html.find('</section>', html_menu_start) + len('</section>')
print(f"HTML Section 4 found from {html_menu_start} to {html_menu_end}")
