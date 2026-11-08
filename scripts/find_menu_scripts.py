import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# search for menuTrack or menuDots in script tags
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', c, re.DOTALL)
print(f"Total script tags: {len(scripts)}")
for i, s in enumerate(scripts):
    if 'menuTrack' in s or 'menu-card' in s or 'menuDots' in s or 'menu' in s:
        print(f"\n--- Script {i} has menu references (length {len(s)}) ---")
        lines = [line for line in s.split('\n') if any(k in line for k in ['menu', 'card', 'track', 'dot', 'carousel'])]
        print('\n'.join(lines[:30]))
