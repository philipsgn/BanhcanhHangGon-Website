import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('order.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<nav id="siteNav"' in l:
        for j in range(i, i + 30):
            print(f'{j+1}: {lines[j].rstrip()}')
        break
