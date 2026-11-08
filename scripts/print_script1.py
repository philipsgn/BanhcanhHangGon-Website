import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', c, re.DOTALL)
print("=== SCRIPT 1 CONTENT ===")
print(scripts[1])
