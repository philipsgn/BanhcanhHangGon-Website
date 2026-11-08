import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

if os.path.exists('menu_preview.html'):
    with open('menu_preview.html', 'r', encoding='utf-8') as f:
        text = f.read()
    print("menu_preview.html length:", len(text))
    # Print headings or structure
    lines = [l.strip() for l in text.splitlines() if '<h' in l or '<section' in l or 'class="menu' in l]
    for l in lines[:30]:
        print(l[:100])
else:
    print("menu_preview.html does not exist")
