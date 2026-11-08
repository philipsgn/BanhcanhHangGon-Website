import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

for cls in ['.welcome-grid', '.welcome-copy', '.welcome-title', '.welcome-photo']:
    print(f"{cls} in index.html: {cls in c}")
