import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(os.listdir('scripts')):
    if 'story' in f or 'welcome' in f:
        print(f"--- {f} ---")
        try:
            with open(os.path.join('scripts', f), 'r', encoding='utf-8') as fp:
                print(fp.read()[:800])
        except Exception as e:
            print(f"Error: {e}")
        print("="*60)
