import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.findall(r'(\.menu-card\.is-far-prev[^{]*\{[^}]+\})', c)
for m in matches:
    print(m)

matches2 = re.findall(r'(\.menu-card\.is-far-next[^{]*\{[^}]+\})', c)
for m in matches2:
    print(m)
