import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '#menu {' in l or '#menu{' in l:
        print(f"Line {i+1}:")
        for j in range(i, i + 40):
            print(f"  {j+1}: {lines[j].rstrip()}")
        break
