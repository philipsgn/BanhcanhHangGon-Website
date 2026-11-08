import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Make card 0 image loading eager for fastest render
c = c.replace(
    'alt="Mẹt Bánh Canh Gà Đặc Biệt Hàng Gòn" class="menu-card-plate" loading="lazy"',
    'alt="Mẹt Bánh Canh Gà Đặc Biệt Hàng Gòn" class="menu-card-plate" loading="eager"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Card 0 set to loading eager successfully!")
