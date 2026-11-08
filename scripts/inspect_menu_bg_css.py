import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'/\* ---------- SECTION 2 : MENU[\s\S]*?(?=/\* ---------- SECTION 3|$)', text)
if m:
    print(m.group(0)[:1500])
