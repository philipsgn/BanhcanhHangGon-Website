import re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

cards = re.findall(r'<div class="menu-card[^"]*"[\s\S]*?(?=<div class="menu-card|<!-- END OF CARDS|\s*</section>)', text)
print(f'Total cards found: {len(cards)}')
for i, card in enumerate(cards):
    print(f'=== CARD {i} ===')
    lines = [l.strip() for l in card.split('\n') if l.strip()]
    for l in lines[:10]:
        print(' ', l)
