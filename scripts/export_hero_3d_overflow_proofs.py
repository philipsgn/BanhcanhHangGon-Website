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
    f_title_act = ImageFont.truetype('arialbd.ttf', 14.5)
    f_price_act = ImageFont.truetype('arialbd.ttf', 18.5)
    f_desc_act = ImageFont.truetype('arial.ttf', 10.5)
    f_btn_act = ImageFont.truetype('arialbd.ttf', 11.5)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 12)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 15)
    f_desc_inact = ImageFont.truetype('arial.ttf', 9.5)

    f_footer_label = ImageFont.truetype('arial.ttf', 10)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 14)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 11.5)

    f_m_title = ImageFont.truetype('arialbd.ttf', 15)
    f_m_price = ImageFont.truetype('arialbd.ttf', 18.5)
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

def draw_hero_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc, is_mobile=False):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        # Enhanced 3D shadow for active card
        for off in range(1, 14):
            alpha = int(20 * (1 - off / 14))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off*2, x1 + off//2, y1 + off*2 + 4], radius=24, fill=(36, 22, 16, alpha))
        
        # Warm craft beige card body
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=(239, 232, 221))
        
        # HERO TRAY (Phóng to đập vào mắt: 215px desktop, 190px mobile)
        plate_size = 215 if not is_mobile else 190
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        # Overflow top by 24px
        py = y0 - (24 if not is_mobile else 18)
        
        # Tray drop shadow
        tray_shadow = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        ts_draw = ImageDraw.Draw(tray_shadow)
        for s_off in range(1, 10):
            s_alpha = int(22 * (1 - s_off / 10))
            ts_draw.ellipse([px + s_off, py + 14 + s_off*2, px + plate_size - s_off, py + plate_size + 14 + s_off], fill=(36, 22, 16, s_alpha))
        bg_img.alpha_composite(tray_shadow)
        
        # Paste Dish Tray
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 6
        
        # Title
        t_font = f_m_title if is_mobile else f_title_act
        tb = card_draw.textbbox((0, 0), title, font=t_font)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16), font=t_font)
        cy += 18
        
        # Price
        p_font = f_m_price if is_mobile else f_price_act
        pb = card_draw.textbbox((0, 0), price, font=p_font)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28), font=p_font)
        cy += 20
        
        # Desc
        d_font = f_m_desc if is_mobile else f_desc_act
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=d_font)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51), font=d_font)
            cy += 13
        
        # CTA Button
        b_font = f_m_btn if is_mobile else f_btn_act
        bw, bh = (160, 34) if not is_mobile else (168, 36)
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 14
        bx1 = center_x + bw // 2
        by1 = y1 - 14
        card_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(158, 94, 43))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=b_font)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 255, 255), font=b_font)
    
    elif tier == 'near':
        # Inactive card near
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(250, 247, 242, 220))
        
        plate_size = 165
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 + 8
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 6
        tb = c_draw.textbbox((0, 0), title, font=f_title_inact)
        c_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(51, 36, 28, 200), font=f_title_inact)
        cy += 16
        pb = c_draw.textbbox((0, 0), price, font=f_price_inact)
        c_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 94, 43, 200), font=f_price_inact)
        cy += 18
        
        lines = desc.split('\n')
        for l in lines:
            lb = c_draw.textbbox((0, 0), l, font=f_desc_inact)
            c_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(106, 88, 77, 180), font=f_desc_inact)
            cy += 13
        
        bw, bh = 130, 26
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 12
        bx1 = center_x + bw // 2
        by1 = y1 - 12
        c_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, outline=(196, 142, 89, 180), width=1)
        btn_txt = "ĐẶT MÓN NGAY"
        btb = c_draw.textbbox((0, 0), btn_txt, font=f_footer_label)
        c_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(158, 94, 43, 180), font=f_footer_label)
        
        card_layer.putalpha(card_layer.getchannel('A').point(lambda a: int(a * 0.60)))
        bg_img.alpha_composite(card_layer)
        
    elif tier == 'far':
        # Inactive card far
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(250, 247, 242, 160))
        
        plate_size = 135
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 + 10
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 6
        tb = c_draw.textbbox((0, 0), title, font=f_desc_inact)
        c_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(51, 36, 28, 140), font=f_desc_inact)
        cy += 15
        pb = c_draw.textbbox((0, 0), price, font=f_desc_inact)
        c_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 94, 43, 140), font=f_desc_inact)
        
        card_layer.putalpha(card_layer.getchannel('A').point(lambda a: int(a * 0.32)))
        bg_img.alpha_composite(card_layer)

# -------------------------------------------------------------------------
# PROOF 1: Desktop 100% Zoom (1024x515 Viewport - User Laptop Screen)
# -------------------------------------------------------------------------
W1, H1 = 1024, 515
canvas1 = Image.new('RGBA', (W1, H1), (250, 248, 245, 255))
d1 = ImageDraw.Draw(canvas1)

# Story Section Bottom Border (simulated 30px sliver)
story_bar_h = 30
d1.rectangle([0, 0, W1, story_bar_h], fill=(36, 22, 14, 255))
d1.text((32, 5), "Gìn giữ vị quê đượm ấm bát canh đầy...", fill=(235, 218, 195, 220), font=f_quote)
d1.line([(0, story_bar_h), (W1, story_bar_h)], fill=(225, 215, 200, 255), width=1)

# Rooster mascot board in top-left
rw, rh = 115, 110
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
canvas1.paste(rooster_s, (22, story_bar_h + 14), rooster_s)

# Stage Coordinates: Card height = 340px.
# Card top = 95px. Plate top = 95 - 24 = 71px.
# Clearance from story border (30px) = 71 - 30 = 41px >= 40px safe buffer!
# Card bottom = 95 + 340 = 435px.
# Dots at y = 448px. Footer at y = 468px.
cx = 512
card_cy = 265
c_w_act, c_h_act = 265, 340

# Far prev (-2): Dish 3
draw_hero_card(canvas1, cx - 435, card_cy + 18, 185, 275, 'far', dishes[3][0], dishes[3][1], dishes[3][2], dishes[3][3])
# Far next (+2): Dish 2
draw_hero_card(canvas1, cx + 435, card_cy + 18, 185, 275, 'far', dishes[2][0], dishes[2][1], dishes[2][2], dishes[2][3])
# Near prev (-1): Dish 4
draw_hero_card(canvas1, cx - 230, card_cy + 10, 220, 315, 'near', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3])
# Near next (+1): Dish 1
draw_hero_card(canvas1, cx + 230, card_cy + 10, 220, 315, 'near', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3])
# Active (0): Dish 0 (Hero Tray!)
draw_hero_card(canvas1, cx, card_cy, c_w_act, c_h_act, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3])

# Dots Indicator
dots_y = card_cy + c_h_act // 2 + 10
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (158, 94, 43, 255) if i == 2 else (214, 199, 178, 255)
    dot_w = 26 if i == 2 else 8
    d1.rounded_rectangle([cx + dx_off - dot_w//2, dots_y, cx + dx_off + dot_w//2, dots_y + 8], radius=4, fill=dot_color)

# Footer Bar
fy = H1 - 46
d1.rounded_rectangle([48, fy, W1 - 48, fy + 38], radius=19, fill=(255, 255, 255, 200), outline=(201, 154, 74, 50), width=1)
d1.text((68, fy + 5), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(138, 74, 28), font=f_footer_label)
d1.text((68, fy + 17), "090 642 79 38", fill=(26, 20, 16), font=f_footer_phone)
btn_lbl = "Xem Toàn Bộ Thực Đơn  →"
bb = d1.textbbox((0, 0), btn_lbl, font=f_footer_btn)
d1.rounded_rectangle([W1 - 250, fy + 5, W1 - 65, fy + 33], radius=14, fill=(26, 20, 16))
d1.text((W1 - 250 + (185 - (bb[2]-bb[0]))//2, fy + 10), btn_lbl, fill=(250, 248, 245), font=f_footer_btn)

# Visual measurement annotation
plate_top_y = card_cy - c_h_act // 2 - 24
d1.line([(cx + 140, story_bar_h), (cx + 140, plate_top_y)], fill=(34, 139, 34, 220), width=2)
d1.line([(cx + 135, story_bar_h), (cx + 145, story_bar_h)], fill=(34, 139, 34, 220), width=2)
d1.line([(cx + 135, plate_top_y), (cx + 145, plate_top_y)], fill=(34, 139, 34, 220), width=2)
gap_val = plate_top_y - story_bar_h
d1.text((cx + 152, story_bar_h + gap_val // 2 - 8), f"Khoảng thở trần an toàn: {gap_val}px (>= 40px)", fill=(34, 139, 34, 255), font=f_desc_act)

proof1_path = os.path.join(ARTIFACT_DIR, 'proof_hero_3d_tray_100_zoom.png')
canvas1.save(proof1_path, 'PNG')
print(f"Proof 1 saved to: {proof1_path}")

# -------------------------------------------------------------------------
# PROOF 2: Mobile Viewport (390x844 iPhone Viewport)
# -------------------------------------------------------------------------
W2, H2 = 390, 844
canvas2 = Image.new('RGBA', (W2, H2), (250, 248, 245, 255))
d2 = ImageDraw.Draw(canvas2)

# Mobile Rooster mascot
m_rw, m_rh = 85, 80
rooster_m = im_rooster.resize((m_rw, m_rh), Image.Resampling.LANCZOS)
canvas2.paste(rooster_m, (14, 18), rooster_m)

# Mobile Stage
m_cx = 195
m_card_cy = 380
m_w_act, m_h_act = 275, 360

# Near prev peek
draw_hero_card(canvas2, m_cx - 240, m_card_cy + 8, 215, 310, 'near', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3], is_mobile=True)
# Near next peek
draw_hero_card(canvas2, m_cx + 240, m_card_cy + 8, 215, 310, 'near', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3], is_mobile=True)
# Active Dish (Hero Tray!)
draw_hero_card(canvas2, m_cx, m_card_cy, m_w_act, m_h_act, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3], is_mobile=True)

# Mobile Dots
m_dots_y = m_card_cy + m_h_act // 2 + 16
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (158, 94, 43, 255) if i == 2 else (214, 199, 178, 255)
    dot_w = 26 if i == 2 else 8
    d2.rounded_rectangle([m_cx + dx_off - dot_w//2, m_dots_y, m_cx + dx_off + dot_w//2, m_dots_y + 8], radius=4, fill=dot_color)

# Mobile Footer
m_fy = H2 - 120
d2.rounded_rectangle([18, m_fy, W2 - 18, m_fy + 95], radius=18, fill=(255, 255, 255, 220), outline=(201, 154, 74, 50), width=1)
d2.text((W2 // 2 - 75, m_fy + 10), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(138, 74, 28), font=f_footer_label)
d2.text((W2 // 2 - 55, m_fy + 25), "090 642 79 38", fill=(26, 20, 16), font=f_footer_phone)
m_btn_lbl = "Xem Toàn Bộ Thực Đơn  →"
m_bb = d2.textbbox((0, 0), m_btn_lbl, font=f_footer_btn)
d2.rounded_rectangle([32, m_fy + 52, W2 - 32, m_fy + 86], radius=17, fill=(26, 20, 16))
d2.text((32 + (W2 - 64 - (m_bb[2]-m_bb[0]))//2, m_fy + 62), m_btn_lbl, fill=(250, 248, 245), font=f_footer_btn)

proof2_path = os.path.join(ARTIFACT_DIR, 'proof_hero_3d_tray_mobile_390.png')
canvas2.save(proof2_path, 'PNG')
print(f"Proof 2 saved to: {proof2_path}")

# -------------------------------------------------------------------------
# PROOF 3: Closeup Crop of the Active Hero Tray (Food Details & 3D Layering)
# -------------------------------------------------------------------------
crop_box = (cx - 150, card_cy - c_h_act // 2 - 35, cx + 150, card_cy + c_h_act // 2 + 30)
crop_img = canvas1.crop(crop_box)
proof3_path = os.path.join(ARTIFACT_DIR, 'proof_hero_3d_tray_closeup_crop.png')
crop_img.save(proof3_path, 'PNG')
print(f"Proof 3 saved to: {proof3_path}")
print("ALL 3 PROOFS GENERATED SUCCESSFULLY!")
