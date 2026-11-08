import sys

sys.stdout.reconfigure(encoding='utf-8')

for name in ['scripts/apply_welcome_refined.py', 'scripts/apply_welcome_section_update.py', 'scripts/apply_home_hero_update.py']:
    print("="*40, name, "="*40)
    with open(name, 'r', encoding='utf-8') as f:
        print(f.read()[:1500])
