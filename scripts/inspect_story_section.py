import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<!-- SECTION 3: STORY -->.*?(?=<!-- SECTION|\Z)', text, re.DOTALL)
if m:
    print("Found Section 3:")
    print(m.group(0))
else:
    print("Section 3 not found!")
