import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

lines = c.split('\n')
for idx in range(1800, 2500):
    l = lines[idx].strip()
    if l.startswith('/*') or l.startswith('#') or l.startswith('@media'):
        print(f"{idx+1}: {l[:80]}")
