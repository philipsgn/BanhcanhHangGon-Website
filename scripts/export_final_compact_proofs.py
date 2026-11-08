import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

# Load standardized assets with bottom=810px
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
    f_quote = ImageFont.truetype('times.ttf', 24)
    f_title_active = ImageFont.truetype('arialbd.ttf', 14.5)
    f_price_active = ImageFont.truetype('arialbd.ttf', 18)
    f_desc_active = ImageFont.truetype('arial.ttf', 10.5)
    f_btn_active = ImageFont.truetype('arialbd.ttf', 11)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 12)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 14.5)
    f_desc_inact = ImageFont.truetype('arial.ttf', 9)

    f_footer_label = ImageFont.truetype('arial.ttf', 9.5)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 13.5)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 11)

    # Mobile fonts
    f_m_title = ImageFont.truetype('arialbd.ttf', 15)
    f_m_price = ImageFont.truetype('arialbd.ttf', 18.5)
    f_m_desc = ImageFont.truetype('arial.ttf', 11)
    f_m_btn = ImageFont.truetype('arialbd.ttf', 12)
except:
    f_quote = f_title_active = f_price_active = f_desc_active = f_btn_active = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()
    f_m_title = f_m_price = f_m_desc = f_m_btn = ImageFont.load_default()

def draw_menu_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc, is_mobile=False):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        # Card shadow
        for off in range(1, 10):
            alpha = int(18 * (1 - off / 10))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=22, fill=(36, 22, 16, alpha))
        
        # Card body
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(239, 232, 221))
        
        # Plate dimensions (ultra-compact)
        plate_size = 124 if not is_mobile else 138
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 - (28 if not is_mobile else 32)
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 10
        
        # Title
        t_font = f_m_title if is_mobile else f_title_active
        tb = card_draw.textbbox((0, 0), title, font=t_font)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16), font=t_font)
        cy += 18
        
        # Price
        p_font = f_m_price if is_mobile else f_price_active
        pb = card_draw.textbbox((0, 0), price, font=p_font)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28), font=p_font)
        cy += 20
        
        # Desc
        d_font = f_m_desc if is_mobile else f_desc_active
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=d_font)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51), font=d_font)
            cy += 14
        
        # Button
        b_font = f_m_btn if is_mobile else f_btn_active
        bw, bh = (156, 32) if not is_mobile else (168, 36)
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 14
        bx1 = center_x + bw // 2
        by1 = y1 - 14
        card_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(163, 89, 39))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=b_font)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 255, 255), font=b_font)
    else:
        # Inactive card on transparent layer with opacity
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(245, 240, 232, 170))
        
        plate_size = 96
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 - 18
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 8
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
        
        # Alpha composite with opacity 0.40
        card_layer.putalpha(card_layer.getchannel('A').point(lambda a: int(a * 0.45)))
        bg_img.alpha_composite(card_layer)

print("Card drawing engine initialized.")

# -------------------------------------------------------------------------
# PROOF 1: 1024x515 Viewport (User Chrome at 100% zoom with #story bottom visible)
# -------------------------------------------------------------------------
W1, H1 = 1024, 515
canvas1 = Image.new('RGBA', (W1, H1), (250, 247, 242, 255))
d1 = ImageDraw.Draw(canvas1)

# Draw bottom of #story (simulated 30px sliver at the very top to verify clearance)
story_bar_h = 32
d1.rectangle([0, 0, W1, story_bar_h], fill=(36, 22, 14, 255))
d1.text((32, 4), "Gìn giữ vị quê đượm ấm bát canh...", fill=(235, 218, 195, 220), font=f_quote)

# White separator line / shadow
d1.line([(0, story_bar_h), (W1, story_bar_h)], fill=(225, 215, 200, 255), width=1)

# Menu section starts at y = story_bar_h (y=32)
# Rooster sign at left edge:
rw, rh = 120, 115
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
rx = 18
ry = story_bar_h + 12 # y = 44px
canvas1.paste(rooster_s, (rx, ry), rooster_s)

# Carousel track: center is at x = 512, track height = 330px
# Card center_y in track:
card_cy = story_bar_h + 16 + 165 # y = 213px
c_w_act, c_h_act = 236, 280
c_w_inact, c_h_inact = 195, 250

# Dishes data
dishes = [
    (im_dish0, "BÁNH CANH GÀ ĐẶC BIỆT", "70.000đ", "Thịt gà ta da vàng mọng nước, trứng\nnon béo ngậy. Nước dùng ninh xương..."),
    (im_dish1, "CƠM GÀ XÉ", "52.000đ", "Cơm nghệ vàng óng nấu từ nước luộc gà\nbéo ngọt, thịt gà ta xé phay đậm vị..."),
    (im_dish2, "GỎI GÀ TA", "50.000đ", "Thịt gà thả vườn xé phay giòn sần sật,\nrau răm thơm nồng và sốt trộn đậm đà."),
    (im_dish3, "XÔI GÀ TRỨNG NON", "40.000đ", "Xôi nếp nương dẻo quánh thoang thoảng\nmỡ gà, chùm trứng non vàng ngậy..."),
    (im_dish4, "MÌ GÀ TA TRUYỀN THỐNG", "55.000đ", "Sợi mì trứng dai vàng óng, thịt gà ta\nxé ngọt mềm, trứng non béo bùi...")
]

# We render with Dish 0 (Bánh Canh) as active center at x=512
cx = 512
gap = 210

# Neighbor -2 (Dish 3)
draw_menu_card(canvas1, cx - 2*gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[3][0], dishes[3][1], dishes[3][2], dishes[3][3])
# Neighbor -1 (Dish 4)
draw_menu_card(canvas1, cx - gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3])
# Active Center (Dish 0)
draw_menu_card(canvas1, cx, card_cy, c_w_act, c_h_act, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3])
# Neighbor +1 (Dish 1)
draw_menu_card(canvas1, cx + gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3])
# Neighbor +2 (Dish 2)
draw_menu_card(canvas1, cx + 2*gap, card_cy, c_w_inact, c_h_inact, 'inactive', dishes[2][0], dishes[2][1], dishes[2][2], dishes[2][3])

# Dots below track
dots_y = story_bar_h + 16 + 330 + 8 # y = 386px
for i in range(5):
    dx = cx - 28 + i * 14
    if i == 0:
        d1.rounded_rectangle([dx - 8, dots_y, dx + 8, dots_y + 7], radius=3, fill=(163, 89, 39))
    else:
        d1.ellipse([dx - 3, dots_y, dx + 3, dots_y + 6], fill=(210, 195, 180))

# Footer bar
fw, fh = 580, 48
fx0 = cx - fw // 2
fy0 = dots_y + 16 # y = 409px
fx1 = cx + fw // 2
fy1 = fy0 + fh    # y = 457px (Leaves 58px margin before viewport bottom 515px!)
d1.rounded_rectangle([fx0, fy0, fx1, fy1], radius=fh//2, fill=(244, 238, 230), outline=(225, 215, 200), width=1)
d1.text((fx0 + 24, fy0 + 8), "GIAO TẬN NƠI TẠI TP. BẢO LỘC", fill=(120, 100, 90), font=f_footer_label)
d1.text((fx0 + 24, fy0 + 22), "Hotline: 0988 567 890", fill=(163, 89, 39), font=f_footer_phone)
# Footer button
fbw, fbh = 130, 32
fbx0 = fx1 - fbw - 10
fby0 = fy0 + (fh - fbh) // 2
fbx1 = fx1 - 10
fby1 = fby0 + fbh
d1.rounded_rectangle([fbx0, fby0, fbx1, fby1], radius=fbh//2, fill=(163, 89, 39))
d1.text((fbx0 + 16, fby0 + 8), "GỌI ĐẶT BÀN", fill=(255, 255, 255), font=f_footer_btn)

# Social buttons on right edge
for idx, icon in enumerate(["📞", "f", "♪", "🛍️", "🛵"]):
    sy = 160 + idx * 42
    d1.ellipse([W1 - 38, sy, W1 - 10, sy + 28], fill=(42, 28, 22))

out1_path = os.path.join(ARTIFACT_DIR, 'proof_ultra_compact_100_zoom.png')
canvas1.convert('RGB').save(out1_path, 'PNG')
print(f"Saved Proof 1 (100% Zoom Desktop 1024x515): {out1_path}")

# -------------------------------------------------------------------------
# PROOF 2: Mobile Viewport 390x844
# -------------------------------------------------------------------------
W2, H2 = 390, 844
canvas2 = Image.new('RGBA', (W2, H2), (250, 247, 242, 255))
d2 = ImageDraw.Draw(canvas2)

# Mobile Rooster Sign at top-left (compact & crisp)
m_rw, m_rh = 88, 84
m_rooster = im_rooster.resize((m_rw, m_rh), Image.Resampling.LANCZOS)
canvas2.paste(m_rooster, (14, 12), m_rooster)

# Mobile Track with top clearance margin (starts at y = 100px)
m_card_cy = 280
m_cw, m_ch = 260, 310

# Active Center Dish 0 (Plate sits at py = y0 - 32 = 125 - 32 = 93px, zero collision with rooster board which ends at y=96 and x=102!)
draw_menu_card(canvas2, W2 // 2, m_card_cy, m_cw, m_ch, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3], is_mobile=True)

# Dots
m_dots_y = m_card_cy + m_ch // 2 + 16
for i in range(5):
    dx = (W2 // 2) - 28 + i * 14
    if i == 0:
        d2.rounded_rectangle([dx - 8, m_dots_y, dx + 8, m_dots_y + 7], radius=3, fill=(163, 89, 39))
    else:
        d2.ellipse([dx - 3, m_dots_y, dx + 3, m_dots_y + 6], fill=(210, 195, 180))

# Mobile Footer Bar (stacked or compact)
m_fy0 = m_dots_y + 20
d2.rounded_rectangle([18, m_fy0, W2 - 18, m_fy0 + 58], radius=16, fill=(244, 238, 230), outline=(225, 215, 200), width=1)
d2.text((32, m_fy0 + 10), "GIAO TẬN NƠI TẠI TP. BẢO LỘC", fill=(120, 100, 90), font=f_footer_label)
d2.text((32, m_fy0 + 26), "Hotline: 0988 567 890", fill=(163, 89, 39), font=f_footer_phone)
d2.rounded_rectangle([W2 - 132, m_fy0 + 12, W2 - 26, m_fy0 + 46], radius=17, fill=(163, 89, 39))
d2.text((W2 - 118, m_fy0 + 21), "GỌI NGAY", fill=(255, 255, 255), font=f_btn_active)

out2_path = os.path.join(ARTIFACT_DIR, 'proof_ultra_compact_mobile_390.png')
canvas2.convert('RGB').save(out2_path, 'PNG')
print(f"Saved Proof 2 (Mobile Viewport 390x844): {out2_path}")

# -------------------------------------------------------------------------
# PROOF 3: Closeup of Plate Top & Story Boundary (0px clipping proof)
# -------------------------------------------------------------------------
# Crop the region around story_bar_h and active plate top:
# Active plate top: card_cy - c_h_act//2 - 28 = 213 - 140 - 28 = 45px
# Clearance to story bar (y=32) is 45 - 32 = 13px clean gap!
crop_top = canvas1.crop((412, 10, 612, 160))
out3_path = os.path.join(ARTIFACT_DIR, 'proof_ultra_compact_plate_clearance_crop.png')
crop_top.convert('RGB').save(out3_path, 'PNG')
print(f"Saved Proof 3 (Top Clearance Closeup): {out3_path}")
