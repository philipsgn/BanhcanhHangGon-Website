import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
fonts = re.findall(r'<link[^>]*fonts\.googleapis\.com[^>]*>', text)
for f in fonts:
    print(f)
