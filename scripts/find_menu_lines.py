import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '/* SECTION 3: MENU' in l or '/* SECTION: MENU' in l or 'SECTION 4: MENU' in l or '#menu {' in l:
        print(f'{i+1}: {l.strip()[:80]}')
