import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<nav' in l:
        print(f'{i+1}: {l.strip()}')
        for j in range(i, i + 35):
            print(f'  {j+1}: {lines[j].rstrip()}')
        break
