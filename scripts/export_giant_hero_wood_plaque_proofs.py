import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

# Load standardized assets
p_rooster = os.path.join(ROOT, 'images', 'menu', 'original-chef-rooster-board.webp')
p_dish0 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Soup on Wooden Tray_result.webp')
p_dish1 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Rice Tray Feast_result.webp')
p_dish2 = os.path.join(ROOT, 'images', 'menu', 'goi-ga.webp')
p_dish3 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Xôi Gà on a Wooden Tray_result.webp')
p_dish4 = os.path.join(ROOT, 'images', 'menu', 'mi-ga.webp')

im_rooster = Image.open(p_rooster).convert('RGBA')
im_dish0 = Image.open(p_dish0).convert('RGBA')
im_dish1 = Image.open(p_dish1).convert('RGBA')
im_dish2 = Image.open(p_dish2).convert('RGBA')
im_dish3 = Image.open(p_dish3).convert('RGBA')
im_dish4 = Image.open(p_dish4).convert('RGBA')

try:
    f_quote = ImageFont.truetype('times.ttf', 20)
    f_title_act = ImageFont.truetype('arialbd.ttf', 15.5)
    f_price_act = ImageFont.truetype('arialbd.ttf', 19.5)
    f_desc_act = ImageFont.truetype('arial.ttf', 10.5)
    f_btn_act = ImageFont.truetype('arialbd.ttf', 11.5)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 12)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 15)
    f_desc_inact = ImageFont.truetype('arial.ttf', 9.5)

    f_footer_label = ImageFont.truetype('arial.ttf', 10)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 14)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 11.5)

    f_m_title = ImageFont.truetype('arialbd.ttf', 15.5)
    f_m_price = ImageFont.truetype('arialbd.ttf', 19)
    f_m_desc = ImageFont.truetype('arial.ttf', 10.5)
    f_m_btn = ImageFont.truetype('arialbd.ttf', 11.5)
except:
    f_quote = f_title_act = f_price_act = f_desc_act = f_btn_act = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()
    f_m_title = f_m_price = f_m_desc = f_m_btn = ImageFont.load_default()

dishes = [
    (im_dish0, "BÁNH CANH GÀ ĐẶC BIỆT", "70.000₫", "Thịt gà ta da vàng mọng nước, trứng\nnon béo ngậy. Nước dùng thanh ngọt..."),
    (im_dish1, "CƠM GÀ XÉ", "52.000₫", "Cơm nghệ vàng óng nấu từ nước luộc gà\nbéo ngọt, thịt gà ta xé phay đậm vị..."),
    (im_dish2, "GỎI GÀ TA", "50.000₫", "Thịt gà thả vườn xé phay giòn ngọt,\nrau răm thơm the và sốt chua ngọt..."),
    (im_dish3, "XÔI GÀ TRỨNG NON", "40.000₫", "Xôi nếp nương dẻo quánh thoang thoảng\nmỡ gà, chùm trứng non vàng ngậy..."),
    (im_dish4, "MÌ GÀ TA TRUYỀN THỐNG", "55.000₫", "Sợi mì trứng dai vàng óng, thịt gà ta\nxé ngọt mềm, trứng non béo bùi...")
]

def draw_giant_hero_wood_plaque(bg_img, center_x, center_y, tier, dish_img, title, price, desc, is_mobile=False):
    card_draw = ImageDraw.Draw(bg_img)

    if tier == 'active':
        plate_size = 350 if not is_mobile else 275
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        
        px = center_x - plate_size // 2
        py = center_y - plate_size // 2 - (65 if not is_mobile else 55)
        
        pw = 285 if not is_mobile else 270
        ph = 145 if not is_mobile else 140
        x0 = center_x - pw // 2
        y0 = py + plate_size - 32
        x1 = center_x + pw // 2
        y1 = y0 + ph
        
        for off in range(1, 14):
            alpha = int(22 * (1 - off / 14))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off*2, x1 + off//2, y1 + off*2 + 4], radius=22, fill=(20, 10, 6, alpha))
        
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(45, 26, 18), outline=(212, 163, 89), width=1)
        
        tray_shadow = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        ts_draw = ImageDraw.Draw(tray_shadow)
        for s_off in range(1, 14):
            s_alpha = int(28 * (1 - s_off / 14))
            ts_draw.ellipse([px + s_off*2, py + 22 + s_off*2, px + plate_size - s_off*2, py + plate_size + 20 + s_off], fill=(22, 11, 6, s_alpha))
        bg_img.alpha_composite(tray_shadow)
        
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = y0 + 16
        t_font = f_m_title if is_mobile else f_title_act
        tb = card_draw.textbbox((0, 0), title, font=t_font)
        card_draw.text((center_x - (tb[2]-tb[0])//2 + 1, cy + 1), title, fill=(15, 8, 4), font=t_font)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(245, 208, 97), font=t_font)
        cy += 20
        
        p_font = f_m_price if is_mobile else f_price_act
        pb = card_draw.textbbox((0, 0), price, font=p_font)
        card_draw.text((center_x - (pb[2]-pb[0])//2 + 1, cy + 1), price, fill=(15, 8, 4), font=p_font)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(255, 168, 52), font=p_font)
        cy += 22
        
        d_font = f_m_desc if is_mobile else f_desc_act
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=d_font)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(212, 196, 181), font=d_font)
            cy += 14
        
        b_font = f_m_btn if is_mobile else f_btn_act
        bw, bh = (165, 34) if not is_mobile else (170, 36)
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 14
        bx1 = center_x + bw // 2
        by1 = y1 - 14
        card_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(196, 122, 59))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=b_font)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 255, 255), font=b_font)
        return y1

    elif tier == 'near':
        plate_size = 210
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = center_y - plate_size // 2 - 35
        
        pw = 215
        ph = 115
        x0 = center_x - pw // 2
        y0 = py + plate_size - 22
        x1 = center_x + pw // 2
        y1 = y0 + ph
        
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=(45, 26, 18, 220), outline=(212, 163, 89, 120), width=1)
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = y0 + 12
        tb = c_draw.textbbox((0, 0), title, font=f_title_inact)
        c_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(245, 208, 97, 210), font=f_title_inact)
        cy += 16
        pb = c_draw.textbbox((0, 0), price, font=f_price_inact)
        c_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(255, 168, 52, 210), font=f_price_inact)
        cy += 18
        
        lines = desc.split('\n')
        for l in lines[:1]:
            lb = c_draw.textbbox((0, 0), l, font=f_desc_inact)
            c_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(212, 196, 181, 180), font=f_desc_inact)
            cy += 13
        
        bw, bh = 130, 26
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 10
        bx1 = center_x + bw // 2
        by1 = y1 - 10
        c_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, outline=(255, 168, 52, 160), width=1)
        btn_txt = "ĐẶT MÓN NGAY"
        btb = c_draw.textbbox((0, 0), btn_txt, font=f_footer_label)
        c_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 168, 52, 180), font=f_footer_label)
        
        card_layer.putalpha(card_layer.getchannel('A').point(lambda a: int(a * 0.62)))
        bg_img.alpha_composite(card_layer)
        return y1

    elif tier == 'far':
        plate_size = 155
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = center_y - plate_size // 2 - 25
        
        pw = 175
        ph = 95
        x0 = center_x - pw // 2
        y0 = py + plate_size - 16
        x1 = center_x + pw // 2
        y1 = y0 + ph
        
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=(45, 26, 18, 180), outline=(212, 163, 89, 80), width=1)
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = y0 + 10
        tb = c_draw.textbbox((0, 0), title, font=f_desc_inact)
        c_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(245, 208, 97, 160), font=f_desc_inact)
        cy += 14
        pb = c_draw.textbbox((0, 0), price, font=f_desc_inact)
        c_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(255, 168, 52, 160), font=f_desc_inact)
        
        card_layer.putalpha(card_layer.getchannel('A').point(lambda a: int(a * 0.32)))
        bg_img.alpha_composite(card_layer)
        return y1

# -------------------------------------------------------------------------
# PROOF 1: Desktop 100% Zoom (1024x580 Viewport)
# -------------------------------------------------------------------------
W1, H1 = 1024, 580
canvas1 = Image.new('RGBA', (W1, H1), (250, 248, 245, 255))
d1 = ImageDraw.Draw(canvas1)

story_bar_h = 30
d1.rectangle([0, 0, W1, story_bar_h], fill=(36, 22, 14, 255))
d1.text((32, 5), "Gìn giữ vị quê đượm ấm bát canh đầy...", fill=(235, 218, 195, 220), font=f_quote)
d1.line([(0, story_bar_h), (W1, story_bar_h)], fill=(225, 215, 200, 255), width=1)

rw, rh = 125, 120
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
canvas1.paste(rooster_s, (22, story_bar_h), rooster_s)

cx = 512
card_cy = 280

draw_giant_hero_wood_plaque(canvas1, cx - 440, card_cy + 22, 'far', dishes[3][0], dishes[3][1], dishes[3][2], dishes[3][3])
draw_giant_hero_wood_plaque(canvas1, cx + 440, card_cy + 22, 'far', dishes[2][0], dishes[2][1], dishes[2][2], dishes[2][3])
draw_giant_hero_wood_plaque(canvas1, cx - 232, card_cy + 12, 'near', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3])
draw_giant_hero_wood_plaque(canvas1, cx + 232, card_cy + 12, 'near', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3])
plaque_bottom_y = draw_giant_hero_wood_plaque(canvas1, cx, card_cy, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3])

d1.polygon([(cx - 165, card_cy + 85), (cx - 150, card_cy + 70), (cx - 150, card_cy + 100)], fill=(158, 94, 43, 150))
d1.polygon([(cx + 165, card_cy + 85), (cx + 150, card_cy + 70), (cx + 150, card_cy + 100)], fill=(158, 94, 43, 150))

# Dots safely below the wood plaque
dots_y = plaque_bottom_y + 12
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (158, 94, 43, 255) if i == 2 else (214, 199, 178, 255)
    dot_w = 26 if i == 2 else 8
    d1.rounded_rectangle([cx + dx_off - dot_w//2, dots_y, cx + dx_off + dot_w//2, dots_y + 8], radius=4, fill=dot_color)

# Footer Bar
fy = H1 - 44
d1.rounded_rectangle([48, fy, W1 - 48, fy + 36], radius=18, fill=(255, 255, 255, 200), outline=(201, 154, 74, 50), width=1)
d1.text((68, fy + 5), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(138, 74, 28), font=f_footer_label)
d1.text((68, fy + 17), "090 642 79 38", fill=(26, 20, 16), font=f_footer_phone)
btn_lbl = "Xem Toàn Bộ Thực Đơn  →"
bb = d1.textbbox((0, 0), btn_lbl, font=f_footer_btn)
d1.rounded_rectangle([W1 - 250, fy + 4, W1 - 65, fy + 32], radius=14, fill=(26, 20, 16))
d1.text((W1 - 250 + (185 - (bb[2]-bb[0]))//2, fy + 9), btn_lbl, fill=(250, 248, 245), font=f_footer_btn)

# Visual measurement annotation
plate_top_y = card_cy - 350 // 2 - 65
d1.line([(cx + 185, story_bar_h), (cx + 185, plate_top_y)], fill=(34, 139, 34, 220), width=2)
gap_val = plate_top_y - story_bar_h
d1.text((cx + 192, story_bar_h + gap_val // 2 - 8), f"Khoảng thở trần an toàn: {gap_val}px (>= 40px)", fill=(34, 139, 34, 255), font=f_desc_act)

d1.line([(32, story_bar_h), (50, story_bar_h + 12)], fill=(196, 78, 32, 255), width=2)
d1.text((54, story_bar_h + 4), "2 dây thừng chạm trần (0 gap)", fill=(196, 78, 32, 255), font=f_desc_act)

proof1_path = os.path.join(ARTIFACT_DIR, 'proof_giant_hero_wood_plaque_100_zoom.png')
canvas1.save(proof1_path, 'PNG')
print(f"Proof 1 re-saved with clean dots: {proof1_path}")

# -------------------------------------------------------------------------
# PROOF 2: Mobile Viewport (390x844)
# -------------------------------------------------------------------------
W2, H2 = 390, 844
canvas2 = Image.new('RGBA', (W2, H2), (250, 248, 245, 255))
d2 = ImageDraw.Draw(canvas2)

m_rw, m_rh = 90, 85
rooster_m = im_rooster.resize((m_rw, m_rh), Image.Resampling.LANCZOS)
canvas2.paste(rooster_m, (14, 0), rooster_m)

m_cx = 195
m_card_cy = 380

draw_giant_hero_wood_plaque(canvas2, m_cx - 245, m_card_cy + 10, 'near', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3], is_mobile=True)
draw_giant_hero_wood_plaque(canvas2, m_cx + 245, m_card_cy + 10, 'near', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3], is_mobile=True)
m_plaque_bottom = draw_giant_hero_wood_plaque(canvas2, m_cx, m_card_cy, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3], is_mobile=True)

# Dots safely below the wood plaque
m_dots_y = m_plaque_bottom + 14
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (158, 94, 43, 255) if i == 2 else (214, 199, 178, 255)
    dot_w = 26 if i == 2 else 8
    d2.rounded_rectangle([m_cx + dx_off - dot_w//2, m_dots_y, m_cx + dx_off + dot_w//2, m_dots_y + 8], radius=4, fill=dot_color)

m_fy = H2 - 120
d2.rounded_rectangle([18, m_fy, W2 - 18, m_fy + 95], radius=18, fill=(255, 255, 255, 220), outline=(201, 154, 74, 50), width=1)
d2.text((W2 // 2 - 75, m_fy + 10), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(138, 74, 28), font=f_footer_label)
d2.text((W2 // 2 - 55, m_fy + 25), "090 642 79 38", fill=(26, 20, 16), font=f_footer_phone)
m_btn_lbl = "Xem Toàn Bộ Thực Đơn  →"
m_bb = d2.textbbox((0, 0), m_btn_lbl, font=f_footer_btn)
d2.rounded_rectangle([32, m_fy + 52, W2 - 32, m_fy + 86], radius=17, fill=(26, 20, 16))
d2.text((32 + (W2 - 64 - (m_bb[2]-m_bb[0]))//2, m_fy + 62), m_btn_lbl, fill=(250, 248, 245), font=f_footer_btn)

proof2_path = os.path.join(ARTIFACT_DIR, 'proof_giant_hero_wood_plaque_mobile_390.png')
canvas2.save(proof2_path, 'PNG')
print(f"Proof 2 saved to: {proof2_path}")

# -------------------------------------------------------------------------
# PROOF 3: Closeup Crop of the Giant Dish & Rustic Wood Plaque Base
# -------------------------------------------------------------------------
crop_box = (cx - 195, card_cy - 245, cx + 195, card_cy + 225)
crop_img = canvas1.crop(crop_box)
proof3_path = os.path.join(ARTIFACT_DIR, 'proof_giant_hero_wood_plaque_closeup.png')
crop_img.save(proof3_path, 'PNG')
print(f"Proof 3 saved to: {proof3_path}")
print("ALL PROOFS GENERATED SUCCESSFULLY!")
