import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('order.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for MENU or items in JS
m = re.findall(r'(name:\s*[\'\"].*?[\'\"])', text)
print("Found name matches:", len(m))
for item in m[:25]:
    print(item)
