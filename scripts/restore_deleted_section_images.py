import subprocess, os

files = [
    'images/behind-scenes/4-mon-an.jpg',
    'images/behind-scenes/chan-nuoc-leo_result.webp',
    'images/behind-scenes/ga-luoc-quan_result.webp',
    'images/behind-scenes/khong-gian-quan_result.webp',
    'images/behind-scenes/mot-goc-nho-cua-quan_result.webp',
    'images/behind-scenes/trung-non-nuoc-cham_result.webp',
    'images/testimonials-bg_result.webp',
    'images/icon-grab-food_result.webp',
    'images/icon-shopee_result.webp',
    'images/greeting/background_result.webp',
]

for f in files:
    d = os.path.dirname(f)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    res = subprocess.run(['git', 'show', f'HEAD:{f}'], capture_output=True)
    if res.returncode == 0:
        with open(f, 'wb') as out:
            out.write(res.stdout)
        print(f'Restored {f} ({len(res.stdout)} bytes)')
    else:
        print(f'Failed to restore {f}')
