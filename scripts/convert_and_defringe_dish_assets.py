import os
import sys
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()

def defringe_and_convert_com_ga_xe():
    src_p = os.path.join(ROOT, 'images', 'menu', 'cơm-gà-xé.png')
    out_webp_ascii = os.path.join(ROOT, 'images', 'menu', 'com-ga-xe.webp')
    out_webp_utf8 = os.path.join(ROOT, 'images', 'menu', 'cơm-gà-xé.webp')
    
    if not os.path.exists(src_p):
        print(f"Error: {src_p} does not exist!")
        return False
        
    print(f"Reading {src_p}...")
    im = Image.open(src_p).convert('RGBA')
    w, h = im.size
    print(f"Original size: {w}x{h}")
    
    # Anti-AI Slop: Defringe / Alpha thresholding
    # Remove semi-transparent fringe pixels that contain white or grey halos
    r, g, b, a = im.split()
    
    # Clean edge alpha
    # For pixels where alpha is low (< 15), make completely transparent
    # For pixels with 15 <= alpha < 255, ensure color isn't contaminated by pure white background
    clean_im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pixels_src = im.load()
    pixels_clean = clean_im.load()
    
    for y in range(h):
        for x in range(w):
            pr, pg, pb, pa = pixels_src[x, y]
            if pa < 15:
                pixels_clean[x, y] = (0, 0, 0, 0)
            elif pa < 240 and (pr > 240 and pg > 240 and pb > 240):
                # White halo fringe pixel: blend towards nearest darker or suppress alpha
                pixels_clean[x, y] = (pr, pg, pb, int(pa * 0.4))
            else:
                pixels_clean[x, y] = (pr, pg, pb, pa)
                
    # Save as high-quality WebP (quality 92, method 6 for maximum detail retention)
    clean_im.save(out_webp_ascii, format='WEBP', quality=92, method=6)
    clean_im.save(out_webp_utf8, format='WEBP', quality=92, method=6)
    
    sz_src = os.path.getsize(src_p) / 1024
    sz_out = os.path.getsize(out_webp_ascii) / 1024
    print(f"com-ga-xe.webp created: {sz_out:.1f} KB (Reduced from {sz_src:.1f} KB, -{(1 - sz_out/sz_src)*100:.1f}%)")
    return True

def convert_other_heavy_assets_to_webp():
    targets = [
        # images/order
        ('images/order/7up.png', 'images/order/7up.webp'),
        ('images/order/pepsi.png', 'images/order/pepsi.webp'),
        ('images/order/aquafina.png', 'images/order/aquafina.webp'),
        ('images/order/sting.png', 'images/order/sting.webp'),
        ('images/order/sam-rong-bien.png', 'images/order/sam-rong-bien.webp'),
        ('images/order/sam-thao-moc.png', 'images/order/sam-thao-moc.webp'),
        ('images/order/nhadam-mutrom.png', 'images/order/nhadam-mutrom.webp'),
        ('images/order/mutrom-hatchia.png', 'images/order/mutrom-hatchia.webp'),
        ('images/order/khung-go-menu.png', 'images/order/khung-go-menu.webp'),
        ('images/order/khung-go.png', 'images/order/khung-go.webp'),
        ('images/order/phieu-don-order.png', 'images/order/phieu-don-order.webp'),
        ('images/order/rooster_menu_option1_viewer_gaze_3000px.png', 'images/order/rooster_menu_option1_viewer_gaze_3000px.webp'),
        # images/menu
        ('images/menu/gỏi-gà.png', 'images/menu/gỏi-gà.webp'),
        ('images/menu/mì-gà.png', 'images/menu/mì-gà.webp'),
        ('images/menu/background.png', 'images/menu/background.webp'),
        ('images/menu/Gà trống mặc trang phục bên bảng gỗ.png', 'images/menu/Gà trống mặc trang phục bên bảng gỗ.webp'),
        # images/story
        ('images/story/new-background-story-chicken.png', 'images/story/new-background-story-chicken.webp'),
        ('images/story/cute-chicken.png', 'images/story/cute-chicken.webp'),
        ('images/story/frame-for-restaurant.png', 'images/story/frame-for-restaurant.webp'),
        ('images/story/mattien-quan-dem.png', 'images/story/mattien-quan-dem.webp'),
        ('images/story/story-scene-v3.png', 'images/story/story-scene-v3.webp'),
        ('images/story/greeting-background.jpg', 'images/story/greeting-background.webp'),
        # images/highlights
        ('images/highlights/4-mon-an.jpg', 'images/highlights/4-mon-an.webp'),
        ('images/highlights/highlights-1.jpg', 'images/highlights/highlights-1.webp'),
        ('images/highlights/highlights-2.jpg', 'images/highlights/highlights-2.webp'),
        ('images/highlights/highlights-4.jpg', 'images/highlights/highlights-4.webp'),
        ('images/highlights/hightlights.jpg', 'images/highlights/hightlights.webp'),
        ('images/highlights/higlights-3.jpg', 'images/highlights/higlights-3.webp'),
        ('images/behind-scenes/4-mon-an.jpg', 'images/behind-scenes/4-mon-an.webp')
    ]
    
    total_orig = 0
    total_webp = 0
    
    for src_rel, dst_rel in targets:
        src_path = os.path.join(ROOT, src_rel)
        dst_path = os.path.join(ROOT, dst_rel)
        
        if os.path.exists(src_path):
            orig_sz = os.path.getsize(src_path) / 1024
            total_orig += orig_sz
            
            # If destination webp doesn't exist or is older, convert
            if not os.path.exists(dst_path) or os.path.getsize(dst_path) == 0:
                try:
                    im = Image.open(src_path)
                    im.save(dst_path, format='WEBP', quality=90, method=5)
                    new_sz = os.path.getsize(dst_path) / 1024
                    total_webp += new_sz
                    print(f"Converted: {src_rel} ({orig_sz:.1f} KB) -> {dst_rel} ({new_sz:.1f} KB, -{(1-new_sz/orig_sz)*100:.1f}%)")
                except Exception as e:
                    print(f"Error converting {src_rel}: {e}")
            else:
                new_sz = os.path.getsize(dst_path) / 1024
                total_webp += new_sz
                print(f"Already exists: {dst_rel} ({new_sz:.1f} KB)")
                
    saved_kb = total_orig - total_webp
    print(f"\nTotal scanned: {total_orig/1024:.2f} MB -> WebP: {total_webp/1024:.2f} MB. Saved: {saved_kb/1024:.2f} MB!")

if __name__ == '__main__':
    print("=== STEP 1: DEFRINGE & CONVERT CƠM GÀ XÉ ===")
    defringe_and_convert_com_ga_xe()
    print("\n=== STEP 2: CONVERT ALL REMAINING DISH & BACKGROUND IMAGES TO WEBP ===")
    convert_other_heavy_assets_to_webp()
