import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

menu_match = re.search(r'<section id="menu".*?</section>', c, re.DOTALL)
if menu_match:
    print("Found #menu, length:", len(menu_match.group(0)))
    print(menu_match.group(0))
else:
    print("No #menu section found!")
