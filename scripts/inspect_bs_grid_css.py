import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'\.bs-grid[\s\S]*?(?=@media|\n\s*\.review|\n\s*#customer)', text)
if m:
    print(m.group(0)[:1200])

# Also check mobile queries for .bs-grid
m_media = re.findall(r'@media[^{]*\{[\s\S]*?\.bs-[^}]*\}', text)
for mm in m_media:
    print("--- MEDIA QUERY ---")
    print(mm)
