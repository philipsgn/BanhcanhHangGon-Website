import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

# Load newly normalized assets (all 740px diameter, 155px padding)
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
    f_price_act = ImageFont.truetype('arialbd.ttf', 18)
    f_desc_act = ImageFont.truetype('arial.ttf', 10.5)
    f_btn_act = ImageFont.truetype('arialbd.ttf', 11)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 12)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 14.5)
    f_desc_inact = ImageFont.truetype('arial.ttf', 9)

    f_footer_label = ImageFont.truetype('arial.ttf', 9.5)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 13.5)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 11)

    f_m_title = ImageFont.truetype('arialbd.ttf', 15)
    f_m_price = ImageFont.truetype('arialbd.ttf', 18.5)
    f_m_desc = ImageFont.truetype('arial.ttf', 11)
    f_m_btn = ImageFont.truetype('arialbd.ttf', 12)
except:
    f_quote = f_title_act = f_price_act = f_desc_act = f_btn_act = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()
    f_m_title = f_m_price = f_m_desc = f_m_btn = ImageFont.load_default()

dishes = [
    (im_dish0, "BÁNH CANH GÀ ĐẶC BIỆT", "70.000đ", "Thịt gà ta da vàng mọng nước, trứng\nnon béo ngậy. Nước dùng ninh xương..."),
    (im_dish1, "CƠM GÀ XÉ", "52.000đ", "Cơm nghệ vàng óng nấu từ nước luộc gà\nbéo ngọt, thịt gà ta xé phay đậm vị..."),
    (im_dish2, "GỎI GÀ TA", "50.000đ", "Thịt gà thả vườn xé phay giòn sần sật,\nrau răm thơm nồng và sốt trộn đậm đà."),
    (im_dish3, "XÔI GÀ TRỨNG NON", "40.000đ", "Xôi nếp nương dẻo quánh thoang thoảng\nmỡ gà, chùm trứng non vàng ngậy..."),
    (im_dish4, "MÌ GÀ TA TRUYỀN THỐNG", "55.000đ", "Sợi mì trứng dai vàng óng, thịt gà ta\nxé ngọt mềm, trứng non béo bùi...")
]

def draw_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc, is_mobile=False):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        # Card shadow
        for off in range(1, 12):
            alpha = int(18 * (1 - off / 12))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=22, fill=(36, 22, 16, alpha))
        
        # Card body
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(239, 232, 221))
        
        # Plate image (Natural inside card: margin-top: 0)
        plate_size = 126 if not is_mobile else 138
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 + (8 if not is_mobile else 10)  # Sits naturally at top of card, 0 negative margin!
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
            cy += 14
        
        # CTA Button
        b_font = f_m_btn if is_mobile else f_btn_act
        bw, bh = (156, 32) if not is_mobile else (168, 36)
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 14
        bx1 = center_x + bw // 2
        by1 = y1 - 14
        card_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(158, 94, 43))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=b_font)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 255, 255), font=b_font)
    else:
        # Inactive card on transparent layer with opacity
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(245, 240, 232, 180))
        
        plate_size = 100
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 + 6
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 6
        tb = c_draw.textbbox((0, 0), title, font=f_title_inact)
        c_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16, 170), font=f_title_inact)
        cy += 16
        pb = c_draw.textbbox((0, 0), price, font=f_price_inact)
        c_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28, 170), font=f_price_inact)
        cy += 18
        
        lines = desc.split('\n')
        for l in lines:
            lb = c_draw.textbbox((0, 0), l, font=f_desc_inact)
            c_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51, 150), font=f_desc_inact)
            cy += 12
        
        bw, bh = 120, 26
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 10
        bx1 = center_x + bw // 2
        by1 = y1 - 10
        c_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, outline=(184, 153, 126, 120), width=1)
        btn_txt = "ĐẶT MÓN NGAY"
        btb = c_draw.textbbox((0, 0), btn_txt, font=f_footer_label)
        c_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(138, 74, 28, 140), font=f_footer_label)
        
        # Alpha composite with opacity 0.50
        card_layer.putalpha(card_layer.getchannel('A').point(lambda a: int(a * 0.55)))
        bg_img.alpha_composite(card_layer)

# -------------------------------------------------------------------------
# PROOF 1: 1024x515 Viewport (User Chrome at 100% zoom with #story bottom visible)
# -------------------------------------------------------------------------
W1, H1 = 1024, 515
canvas1 = Image.new('RGBA', (W1, H1), (250, 247, 242, 255))
d1 = ImageDraw.Draw(canvas1)

# Draw bottom of #story (simulated 28px sliver at the very top to verify clearance)
story_bar_h = 28
d1.rectangle([0, 0, W1, story_bar_h], fill=(36, 22, 14, 255))
d1.text((32, 4), "Gìn giữ vị quê đượm ấm bát canh đầy...", fill=(235, 218, 195, 220), font=f_quote)
d1.line([(0, story_bar_h), (W1, story_bar_h)], fill=(225, 215, 200, 255), width=1)

# Rooster sign: sits at x=20, y=story_bar_h + 12 = 40px
rw, rh = 115, 110
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
canvas1.paste(rooster_s, (20, story_bar_h + 12), rooster_s)

# Body Section: Stage is centered vertically in the body!
cx = 512
card_cy = 245
c_w_act, c_h_act = 236, 280
c_w_inact, c_h_inact = 195, 250
gap = 210

# Draw all 5 cards
# Neighbor -2 (Dish 3)
draw_card(canvas1, cx - 2*gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[3][0], dishes[3][1], dishes[3][2], dishes[3][3])
# Neighbor -1 (Dish 4)
draw_card(canvas1, cx - gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3])
# Active Center (Dish 0 - Bánh Canh)
draw_card(canvas1, cx, card_cy, c_w_act, c_h_act, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3])
# Neighbor +1 (Dish 1 - Cơm Gà)
draw_card(canvas1, cx + gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3])
# Neighbor +2 (Dish 2 - Gỏi Gà)
draw_card(canvas1, cx + 2*gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[2][0], dishes[2][1], dishes[2][2], dishes[2][3])

# Dots
dots_y = card_cy + c_h_act // 2 + 16 # y = 401px
for i in range(5):
    dx = cx - 28 + i * 14
    if i == 0:
        d1.rounded_rectangle([dx - 8, dots_y, dx + 8, dots_y + 7], radius=3, fill=(158, 94, 43))
    else:
        d1.ellipse([dx - 3, dots_y, dx + 3, dots_y + 6], fill=(210, 195, 180))

# Footer bar
fw, fh = 620, 44
fx0 = cx - fw // 2
fy0 = dots_y + 16 # y = 424px
fx1 = cx + fw // 2
fy1 = fy0 + fh    # y = 468px (Leaves 47px margin before viewport bottom 515px!)
d1.rounded_rectangle([fx0, fy0, fx1, fy1], radius=fh//2, fill=(244, 238, 230), outline=(225, 215, 200), width=1)
d1.text((fx0 + 24, fy0 + 8), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(120, 100, 90), font=f_footer_label)
d1.text((fx0 + 24, fy0 + 20), "090 642 79 38", fill=(138, 74, 28), font=f_footer_phone)
d1.text((fx0 + 155, fy0 + 22), "Phục vụ: 06:00 – 23:00 hàng ngày", fill=(140, 123, 112), font=f_footer_label)

fbw, fbh = 145, 28
fbx0 = fx1 - fbw - 8
fby0 = fy0 + (fh - fbh) // 2
fbx1 = fx1 - 8
fby1 = fby0 + fbh
d1.rounded_rectangle([fbx0, fby0, fbx1, fby1], radius=fbh//2, fill=(26, 20, 16))
d1.text((fbx0 + 14, fby0 + 7), "Xem Toàn Bộ Thực Đơn →", fill=(250, 248, 245), font=f_footer_btn)

# Social buttons
for idx, icon in enumerate(["📞", "f", "♪", "🛍️", "🛵"]):
    sy = 160 + idx * 42
    d1.ellipse([W1 - 38, sy, W1 - 10, sy + 28], fill=(42, 28, 22))

out1 = os.path.join(ARTIFACT_DIR, 'proof_body_menu_100_zoom.png')
canvas1.convert('RGB').save(out1, 'PNG')
print(f"Saved Proof 1: {out1}")

# -------------------------------------------------------------------------
# PROOF 2: Mobile Viewport 390x844
# -------------------------------------------------------------------------
W2, H2 = 390, 844
canvas2 = Image.new('RGBA', (W2, H2), (250, 247, 242, 255))
d2 = ImageDraw.Draw(canvas2)

# Mobile Rooster Sign at top-left
m_rw, m_rh = 86, 82
m_rooster = im_rooster.resize((m_rw, m_rh), Image.Resampling.LANCZOS)
canvas2.paste(m_rooster, (14, 12), m_rooster)

# Mobile Track in Body
m_card_cy = 285
m_cw, m_ch = 260, 310

# Active Center Dish 0
draw_card(canvas2, W2 // 2, m_card_cy, m_cw, m_ch, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3], is_mobile=True)

# Dots
m_dots_y = m_card_cy + m_ch // 2 + 18
for i in range(5):
    dx = (W2 // 2) - 28 + i * 14
    if i == 0:
        d2.rounded_rectangle([dx - 8, m_dots_y, dx + 8, m_dots_y + 7], radius=3, fill=(158, 94, 43))
    else:
        d2.ellipse([dx - 3, m_dots_y, dx + 3, m_dots_y + 6], fill=(210, 195, 180))

# Mobile Footer
m_fy0 = m_dots_y + 24
d2.rounded_rectangle([18, m_fy0, W2 - 18, m_fy0 + 64], radius=16, fill=(244, 238, 230), outline=(225, 215, 200), width=1)
d2.text((32, m_fy0 + 12), "ĐẶT GIAO TẬN NƠI • 090 642 79 38", fill=(138, 74, 28), font=f_m_title)
d2.text((32, m_fy0 + 34), "Phục vụ: 06:00 – 23:00 hàng ngày", fill=(140, 123, 112), font=f_desc_act)

out2 = os.path.join(ARTIFACT_DIR, 'proof_body_menu_mobile_390.png')
canvas2.convert('RGB').save(out2, 'PNG')
print(f"Saved Proof 2: {out2}")

# -------------------------------------------------------------------------
# PROOF 3: Closeup of Plate Top & Story Boundary (Massive Safe Gap Proof)
# -------------------------------------------------------------------------
crop_top = canvas1.crop((412, 10, 612, 180))
out3 = os.path.join(ARTIFACT_DIR, 'proof_body_menu_clearance_crop.png')
crop_top.convert('RGB').save(out3, 'PNG')
print(f"Saved Proof 3: {out3}")
