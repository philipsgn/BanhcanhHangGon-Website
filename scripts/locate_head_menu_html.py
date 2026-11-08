import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index_head.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_menu_sec = c.find('<section id="menu"')
pos_next_sec = c.find('</section>', pos_menu_sec)
print(f"HTML menu section: {pos_menu_sec} to {pos_next_sec + 10}")
print(c[pos_menu_sec:pos_menu_sec+300])
