import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.findall(r'(\.menu-card\.is-[a-z-]+[^{]*\{[^}]+\})', c)
for r in m:
    print("TRANSFORM RULE:", r)
