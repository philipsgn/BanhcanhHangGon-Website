import subprocess
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
has_err = False
for idx, s in enumerate(scripts):
    s = s.strip()
    if not s:
        continue
    # encode as utf-8 bytes
    p = subprocess.run(['node', '--input-type=module', '--check'], input=s.encode('utf-8'), capture_output=True)
    if p.returncode != 0:
        p2 = subprocess.run(['node', '--check'], input=s.encode('utf-8'), capture_output=True)
        if p2.returncode != 0:
            print(f"Script {idx} error: {p2.stderr.decode('utf-8', errors='ignore')}")
            has_err = True

if not has_err:
    print("ALL_SCRIPTS_SYNTAX_PASS")
