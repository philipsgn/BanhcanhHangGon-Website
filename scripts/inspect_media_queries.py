import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'(@media[^{]+\{(?:[^{}]+|\{[^{}]*\})*\})', c)
for m in matches:
    if 'menu-card' in m:
        print("=== MEDIA QUERY WITH MENU-CARD ===")
        print(m[:1000])
