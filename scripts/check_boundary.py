import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

lines = c.split('\n')
print("Line 2387-2390:")
for i in range(2386, 2392):
    print(f"{i+1}: {lines[i]}")

print("\nLine 3275-3282:")
for i in range(3274, min(len(lines), 3283)):
    print(f"{i+1}: {lines[i]}")
