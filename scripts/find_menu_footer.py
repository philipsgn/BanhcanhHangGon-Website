import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = 0
while True:
    idx = c.find("Xem Toàn Bộ Thực Đơn", pos)
    if idx == -1:
        break
    print(f"Found at {idx}:")
    print(c[max(0, idx-300):idx+300])
    print("="*50)
    pos = idx + 1
