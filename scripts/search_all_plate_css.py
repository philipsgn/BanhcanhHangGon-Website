import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = [m.start() for m in re.finditer(r'\.menu-card-plate', c)]
print(f"Found {len(matches)} occurrences of .menu-card-plate:")
for pos in matches:
    print(c[pos-50:pos+250])
    print("-" * 50)
