import os
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

bs_section = soup.find('section', id='backstage')
imgs = bs_section.find_all('img')
print(f"Total images in #backstage: {len(imgs)}")
all_exist = True
for im in imgs:
    src = im.get('src')
    cap = im.find_next_sibling('figcaption')
    cap_text = cap.get_text(strip=True) if cap else 'No caption'
    exists = os.path.exists(os.path.join(ROOT, src))
    sz = os.path.getsize(os.path.join(ROOT, src)) / 1024 if exists else 0
    print(f"  src: {src} | exists: {exists} ({sz:.1f} KB) | cap: '{cap_text}'")
    if not exists:
        all_exist = False

print("\nAll 8 images exist on disk:", all_exist)
