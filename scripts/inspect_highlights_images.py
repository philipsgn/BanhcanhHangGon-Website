import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()

hl_files = [
    'images/highlights/highlights-1.webp',
    'images/highlights/highlights-4.webp',
    'images/highlights/hightlights.webp',
    'images/highlights/higlights-3.webp',
    'images/highlights/4-mon-an.webp'
]

for rel_p in hl_files:
    full_p = os.path.join(ROOT, rel_p)
    if os.path.exists(full_p):
        im = Image.open(full_p)
        sz_kb = os.path.getsize(full_p) / 1024
        print(f"{rel_p}: {im.size} (aspect {im.size[0]/im.size[1]:.2f}) | {sz_kb:.1f} KB | {im.mode}")
    else:
        print(f"{rel_p}: NOT FOUND")
