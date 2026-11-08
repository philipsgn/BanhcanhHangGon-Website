import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<!-- SECTION \d+: MENU.*?-->(.*?)(?=<!-- SECTION|\Z)', text, re.DOTALL)
if m:
    section_text = m.group(0)
    print("Length of section:", len(section_text))
    # Find all articles / dishes
    dishes = re.findall(r'<article class=\"menu-dish-row\".*?</article>', section_text, re.DOTALL)
    print("Found dishes:", len(dishes))
    for i, d in enumerate(dishes):
        name_m = re.search(r'<h3 class=\"menu-dish-name\">(.*?)</h3>', d)
        name = name_m.group(1) if name_m else 'Unknown'
        img_m = re.search(r'<img [^>]*src=[\"\']([^\"\']+)[\"\']', d)
        img = img_m.group(1) if img_m else 'No img'
        price_m = re.search(r'<span class=\"menu-dish-price-value\">(.*?)</span>', d)
        price = price_m.group(1) if price_m else ''
        print(f"Dish {i+1}: {name} | Price: {price} | Image: {img}")
