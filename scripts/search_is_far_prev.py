import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

matches = [m.start() for m in re.finditer(r'is-far-prev', c)]
print(f"Total is-far-prev occurrences: {len(matches)}")
for idx, pos in enumerate(matches):
    start = max(0, pos - 80)
    end = min(len(c), pos + 120)
    print(f"\n--- Match {idx+1} at {pos} ---")
    print(c[start:end])
