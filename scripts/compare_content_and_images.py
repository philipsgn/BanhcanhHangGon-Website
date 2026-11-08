import os
import sys
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    soup_idx = BeautifulSoup(f.read(), 'html.parser')

with open('order.html', 'r', encoding='utf-8') as f:
    soup_ord = BeautifulSoup(f.read(), 'html.parser')

print("=== 1. AUDITING PHONE / HOTLINE ===")
phones_idx = soup_idx.find_all(text=re.compile(r'0\d{2,3}[\s\.]?\d{3}[\s\.]?\d{3,4}'))
print("index.html phones:")
for p in set([p.strip() for p in phones_idx if p.strip()]):
    print("  ", p)

phones_ord = soup_ord.find_all(text=re.compile(r'0\d{2,3}[\s\.]?\d{3}[\s\.]?\d{3,4}'))
print("order.html phones:")
for p in set([p.strip() for p in phones_ord if p.strip()]):
    print("  ", p)

print("\n=== 2. AUDITING OPERATING HOURS ===")
hours_idx = soup_idx.find_all(text=re.compile(r'\d{1,2}[:h]\d{2}'))
print("index.html hours:")
for h in set([h.strip() for h in hours_idx if h.strip()]):
    print("  ", h)

hours_ord = soup_ord.find_all(text=re.compile(r'\d{1,2}[:h]\d{2}'))
print("order.html hours:")
for h in set([h.strip() for h in hours_ord if h.strip()]):
    print("  ", h)

print("\n=== 3. AUDITING ADDRESS ===")
addr_idx = soup_idx.find_all(text=re.compile(r'Phan Đăng Lưu|Hàng Gòn|Phú Nhuận'))
print("index.html address mentions:")
for a in set([a.strip() for a in addr_idx if len(a.strip()) < 80]):
    print("  ", a)

addr_ord = soup_ord.find_all(text=re.compile(r'Phan Đăng Lưu|Hàng Gòn|Phú Nhuận'))
print("order.html address mentions:")
for a in set([a.strip() for a in addr_ord if len(a.strip()) < 80]):
    print("  ", a)

print("\n=== 4. AUDITING SOCIAL LINKS ===")
print("index.html social links:")
for a in soup_idx.find_all('a', href=re.compile(r'facebook|tiktok|shopee|grab|maps')):
    print(f"   href: {a.get('href')[:60]}... | class: {a.get('class')}")

print("order.html social links:")
for a in soup_ord.find_all('a', href=re.compile(r'facebook|tiktok|shopee|grab|maps')):
    print(f"   href: {a.get('href')[:60]}... | class: {a.get('class')}")
