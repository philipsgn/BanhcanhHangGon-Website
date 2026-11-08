import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = [m.start() for m in re.finditer(r'XÔI GÀ TRỨNG NON', c)]
print(f"Found {len(matches)} occurrences of 'XÔI GÀ TRỨNG NON':")
for idx, pos in enumerate(matches):
    start = max(0, pos - 150)
    end = min(len(c), pos + 150)
    print(f"\n--- Match {idx+1} at character {pos} ---")
    print(c[start:end])
