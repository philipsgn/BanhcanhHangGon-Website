import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['index.html', 'order.html']:
    print(f'=== NAVBAR IN {fname} ===')
    with open(fname, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    nav = soup.find('nav', id='siteNav')
    if nav:
        for a in nav.find_all('a'):
            txt = a.get_text(strip=True)
            href = a.get('href')
            cls = a.get('class')
            print(f"  text: '{txt}' | href: '{href}' | class: {cls}")
