import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'@media[^{]*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\.bs-[^}]*\}', text)
for m in matches:
    print("MATCH:")
    print(m)

# Find any other mention of .bs-grid
for i, line in enumerate(text.split('\n')):
    if 'bs-grid' in line or 'bs-item' in line or 'bs-hero' in line or 'bs-wide' in line:
        print(f'{i+1}: {line.strip()[:80]}')
