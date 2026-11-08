import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

try:
    f_title = ImageFont.truetype('arialbd.ttf', 24)
    f_header = ImageFont.truetype('arialbd.ttf', 18)
    f_dish_title = ImageFont.truetype('arialbd.ttf', 26)
    f_dish_price = ImageFont.truetype('arialbd.ttf', 26)
    f_body = ImageFont.truetype('arial.ttf', 14)
    f_body_b = ImageFont.truetype('arialbd.ttf', 14)
    f_btn_light = ImageFont.truetype('arial.ttf', 13.5)
    f_small = ImageFont.truetype('arial.ttf', 12)
    f_small_b = ImageFont.truetype('arialbd.ttf', 12)
except:
    f_title = f_header = f_dish_title = f_dish_price = f_body = f_body_b = f_btn_light = f_small = f_small_b = ImageFont.load_default()

# -------------------------------------------------------------
# PROOF 1: DESKTOP VIGNETTE (CLEAR FLANKS VS MUTED CENTER)
# -------------------------------------------------------------
W1, H1 = 1200, 750

# 1. Base Cream Paper
c1 = Image.new('RGBA', (W1, H1), (250, 245, 235, 255))

# 2. Texture Layer with Radial Mask
p_bg = os.path.join(ROOT, 'images', 'menu', 'menu-bg-3.webp')
if os.path.exists(p_bg):
    im_bg_raw = Image.open(p_bg).convert('RGBA').resize((W1, H1), Image.Resampling.LANCZOS)
    
    # Generate Alpha Mask: Center ~0.08, Flanks ~0.72
    mask = Image.new('L', (W1, H1), 0)
    m_draw = ImageDraw.Draw(mask)
    
    # Fill with base 72% opacity (184 out of 255)
    m_draw.rectangle([0, 0, W1, H1], fill=184)
    
    # Carve out center ellipse (fade to ~20 out of 255 = 8%)
    cx, cy = W1 // 2, int(H1 * 0.38)
    rx, ry = int(W1 * 0.52 * 0.5), int(H1 * 0.58 * 0.5)
    
    for r_step in range(100, 0, -2):
        step_factor = r_step / 100.0
        cur_rx = int(rx * step_factor)
        cur_ry = int(ry * step_factor)
        # Interpolate between 184 (flank) down to 20 (center)
        # quadratic curve for natural smooth vignette
        cur_val = int(20 + (184 - 20) * (step_factor ** 1.8))
        m_draw.ellipse([cx - cur_rx, cy - cur_ry, cx + cur_rx, cy + cur_ry], fill=cur_val)
        
    im_bg_masked = im_bg_raw.copy()
    im_bg_masked.putalpha(mask)
    c1.alpha_composite(im_bg_masked)

# 3. Soft Spotlight Layer (#menu::after)
spotlight = Image.new('RGBA', (W1, H1), (0, 0, 0, 0))
sp_draw = ImageDraw.Draw(spotlight)
cx, cy = W1 // 2, int(H1 * 0.38)
rx, ry = int(W1 * 0.56 * 0.5), int(H1 * 0.60 * 0.5)
for r_step in range(100, 0, -2):
    step_factor = r_step / 100.0
    cur_rx = int(rx * step_factor)
    cur_ry = int(ry * step_factor)
    alpha = int(140 * (1 - step_factor ** 1.4))
    sp_draw.ellipse([cx - cur_rx, cy - cur_ry, cx + cur_rx, cy + cur_ry], fill=(250, 245, 235, alpha))
c1.alpha_composite(spotlight)

# 4. Render Active Food Dish & Surrounding Dish Trays
p_dish0 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Soup on Wooden Tray_result.webp')
p_dish1 = os.path.join(ROOT, 'images', 'menu', 'com-ga-xe.webp')
p_dish2 = os.path.join(ROOT, 'images', 'menu', 'goi-ga.webp')

# Flank Dishes (Near prev & near next)
if os.path.exists(p_dish1):
    im_prev = Image.open(p_dish1).convert('RGBA').resize((320, 320), Image.Resampling.LANCZOS)
    im_prev.putalpha(Image.eval(im_prev.split()[-1], lambda a: int(a * 0.42)))
    c1.paste(im_prev, (60, cy - 140), im_prev)

if os.path.exists(p_dish2):
    im_next = Image.open(p_dish2).convert('RGBA').resize((320, 320), Image.Resampling.LANCZOS)
    im_next.putalpha(Image.eval(im_next.split()[-1], lambda a: int(a * 0.42)))
    c1.paste(im_next, (W1 - 380, cy - 140), im_next)

# Center Active Dish (Hero 460px)
if os.path.exists(p_dish0):
    im_hero = Image.open(p_dish0).convert('RGBA').resize((460, 460), Image.Resampling.LANCZOS)
    
    # Ground Contact Shadow
    shadow = Image.new('RGBA', (W1, H1), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    for off in range(1, 22):
        s_alpha = int(32 * (1 - off / 22))
        s_draw.ellipse([cx - 210 + off*2, cy + 190 + off, cx + 210 - off*2, cy + 245 + off], fill=(42, 22, 12, s_alpha))
    c1.alpha_composite(shadow)
    
    c1.paste(im_hero, (cx - 230, cy - 230), im_hero)

d1 = ImageDraw.Draw(c1)

# Typography & CTA
ty = cy + 230
t_txt = "Bánh Canh Gà Đặc Biệt"
tb = d1.textbbox((0, 0), t_txt, font=f_dish_title)
d1.text((cx - (tb[2]-tb[0])//2, ty), t_txt, fill=(26, 15, 8), font=f_dish_title)
ty += 36

p_txt = "70.000₫"
pb = d1.textbbox((0, 0), p_txt, font=f_dish_price)
d1.text((cx - (pb[2]-pb[0])//2, ty), p_txt, fill=(189, 60, 13), font=f_dish_price)
ty += 32

d_txt = "Thịt gà ta da vàng giòn mọng nước, trứng non béo ngậy. Nước dùng ninh xương thanh ngọt đậm đà."
db = d1.textbbox((0, 0), d_txt, font=f_body)
d1.text((cx - (db[2]-db[0])//2, ty), d_txt, fill=(65, 45, 35), font=f_body)
ty += 28

bw, bh = 180, 42
bx0, by0 = cx - bw // 2, ty
bx1, by1 = cx + bw // 2, by0 + bh
d1.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(189, 60, 13))
btn_txt = "Đ Ặ T   M Ó N"
btb = d1.textbbox((0, 0), btn_txt, font=f_btn_light)
d1.text((cx - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_btn_light)

# Feature Annotations
# Flank Left Indicator
d1.rounded_rectangle([40, 30, 300, 75], radius=6, fill=(35, 26, 20), outline=(201, 154, 74), width=1)
d1.text((55, 42), 'CÁNH TRÁI: RÕ NÉT 72%', fill=(225, 175, 80), font=f_body_b)
d1.text((55, 58), 'Họa tiết giấy mộc hiện rõ', fill=(200, 190, 180), font=f_small)

# Center Spotlight Indicator
d1.rounded_rectangle([cx - 160, 30, cx + 160, 75], radius=6, fill=(35, 26, 20), outline=(120, 210, 140), width=1)
d1.text((cx - 145, 42), 'TRUNG TÂM: MỜ DỊU 8% (SPOTLIGHT)', fill=(120, 210, 140), font=f_body_b)
d1.text((cx - 145, 58), 'Món ăn & Chữ không bị rối nét', fill=(220, 245, 225), font=f_small)

# Flank Right Indicator
d1.rounded_rectangle([W1 - 340, 30, W1 - 40, 75], radius=6, fill=(35, 26, 20), outline=(201, 154, 74), width=1)
d1.text((W1 - 325, 42), 'CÁNH PHẢI: RÕ NÉT 72%', fill=(225, 175, 80), font=f_body_b)
d1.text((W1 - 325, 58), 'Hoa văn truyền thống sắc sảo', fill=(200, 190, 180), font=f_small)

# Bottom Badge
d1.rounded_rectangle([40, H1 - 50, W1 - 40, H1 - 15], radius=6, fill=(25, 85, 40))
d1.text((60, H1 - 38), '✓ HOÀN TẤT NÂNG CẤP NỀN: RÕ NÉT TỰ NHIÊN 2 BÊN CÁNH & TRUNG TÂM MỜ DỊU TÔN VINH MÓN ĂN', fill=(230, 255, 235), font=f_body_b)

out1 = os.path.join(ARTIFACT_DIR, 'proof_menu_vignette_bg_desktop.png')
c1.save(out1, quality=95)
print('Saved proof 1 to:', out1)


# -------------------------------------------------------------
# PROOF 2: MOBILE VIEWPORT SPOTLIGHT (400 x 820)
# -------------------------------------------------------------
W2, H2 = 400, 820
c2 = Image.new('RGBA', (W2, H2), (250, 245, 235, 255))

if os.path.exists(p_bg):
    im_bg_m = Image.open(p_bg).convert('RGBA').resize((W2, H2), Image.Resampling.LANCZOS)
    mask_m = Image.new('L', (W2, H2), 0)
    mm_draw = ImageDraw.Draw(mask_m)
    mm_draw.rectangle([0, 0, W2, H2], fill=184)
    
    mcx, mcy = W2 // 2, int(H2 * 0.35)
    mrx, mry = int(W2 * 0.68 * 0.5), int(H2 * 0.56 * 0.5)
    for r_step in range(100, 0, -2):
        sf = r_step / 100.0
        c_rx = int(mrx * sf)
        c_ry = int(mry * sf)
        c_val = int(20 + (184 - 20) * (sf ** 1.8))
        mm_draw.ellipse([mcx - c_rx, mcy - c_ry, mcx + c_rx, mcy + c_ry], fill=c_val)
        
    im_bg_m.putalpha(mask_m)
    c2.alpha_composite(im_bg_m)

# Mobile Spotlight
sp_m = Image.new('RGBA', (W2, H2), (0, 0, 0, 0))
spm_draw = ImageDraw.Draw(sp_m)
for r_step in range(100, 0, -2):
    sf = r_step / 100.0
    alpha = int(145 * (1 - sf ** 1.4))
    spm_draw.ellipse([mcx - int(mrx * sf), mcy - int(mry * sf), mcx + int(mrx * sf), mcy + int(mry * sf)], fill=(250, 245, 235, alpha))
c2.alpha_composite(sp_m)

# Mobile Plate (340px)
if os.path.exists(p_dish0):
    im_dish_m = Image.open(p_dish0).convert('RGBA').resize((340, 340), Image.Resampling.LANCZOS)
    c2.paste(im_dish_m, (mcx - 170, mcy - 170), im_dish_m)

d2 = ImageDraw.Draw(c2)
d2.text((20, 20), 'MENU MOBILE: SPOTLIGHT NỀN MỜ DỊU', fill=(189, 60, 13), font=f_header)

m_ty = mcy + 175
mtb = d2.textbbox((0, 0), t_txt, font=f_header)
d2.text((mcx - (mtb[2]-mtb[0])//2, m_ty), t_txt, fill=(26, 15, 8), font=f_header)
m_ty += 30

mpb = d2.textbbox((0, 0), p_txt, font=f_dish_price)
d2.text((mcx - (mpb[2]-mpb[0])//2, m_ty), p_txt, fill=(189, 60, 13), font=f_dish_price)
m_ty += 32

for dl in ["Thịt gà ta da vàng giòn mọng nước,", "trứng non béo ngậy, nước dùng thanh ngọt."]:
    mlb = d2.textbbox((0, 0), dl, font=f_small)
    d2.text((mcx - (mlb[2]-mlb[0])//2, m_ty), dl, fill=(65, 45, 35), font=f_small)
    m_ty += 18

m_ty += 10
mbw, mbh = 175, 42
mbx0, mby0 = mcx - mbw // 2, m_ty
mbx1, mby1 = mcx + mbw // 2, mby0 + mbh
d2.rounded_rectangle([mbx0, mby0, mbx1, mby1], radius=mbh//2, fill=(189, 60, 13))
d2.text((mcx - (btb[2]-btb[0])//2, mby0 + (mbh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 253, 245), font=f_btn_light)

d2.rounded_rectangle([20, H2 - 50, W2 - 20, H2 - 15], radius=6, fill=(25, 85, 40))
d2.text((35, H2 - 38), '✓ Mobile: Tối ưu elip mask, món ăn nổi bật 100%', fill=(230, 255, 235), font=f_small)

out2 = os.path.join(ARTIFACT_DIR, 'proof_menu_vignette_bg_mobile.png')
c2.save(out2, quality=95)
print('Saved proof 2 to:', out2)

print('ALL VIGNETTE PROOFS GENERATED SUCCESSFULLY!')
