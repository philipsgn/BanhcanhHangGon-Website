import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

lines = c.split('\n')
for idx in range(2200, 2300):
    if lines[idx].strip().startswith('/*') or lines[idx].strip().startswith('@media'):
        print(f"{idx+1}: {lines[idx]}")
