import re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    text_order = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    text_index = f.read()

for name, text in [('order.html', text_order), ('index.html', text_index)]:
    print(f'=== {name} ===')
    matches = re.findall(r'(?:src=|srcset=|url\()["\']?([^"\'\)\s>]+)["\']?', text)
    assets = set([m for m in matches if any(m.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp'])])
    for a in sorted(assets):
        print(f'  {a} (exists: {os.path.exists(a)})')
