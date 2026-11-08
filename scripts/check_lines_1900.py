import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

lines = c.split('\n')
for i in range(1900, 1940):
    print(f"{i+1}: {lines[i]}")
