import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index_head.html', 'r', encoding='utf-8') as f:
    c = f.read()

sections = re.findall(r'<section\b[^>]*id="([^"]+)"', c)
print("Sections in index_head.html:", sections)

comments = re.findall(r'/\* ---------- (SECTION [0-9]+ [^\*]+) ---------- \*/', c)
print("CSS Sections in index_head.html:", comments)
