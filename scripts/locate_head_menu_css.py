import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index_head.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_menu = c.find('/* ---------- SECTION 3 : MENU (ZIGZAG 3D EDITORIAL) ---------- */')
pos_story = c.find('/* ---------- SECTION 3 : STORY ---------- */')
print(f"pos_menu: {pos_menu}, pos_story: {pos_story}")
print("MENU CSS START IN HEAD:")
print(c[pos_menu:pos_menu+400])
