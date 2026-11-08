import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

# Load standardized assets (740px diameter, 155px padding)
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
except:
    f_quote = f_title_act = f_price_act = f_desc_act = f_btn_act = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()

dishes = [
    (im_dish0, "BÁNH CANH GÀ ĐẶC BIỆT", "70.000đ", "Thịt gà ta da vàng mọng nước, trứng\nnon béo ngậy. Nước dùng ninh xương..."),
    (im_dish1, "CƠM GÀ XÉ", "52.000đ", "Cơm nghệ vàng óng nấu từ nước luộc gà\nbéo ngọt, thịt gà ta xé phay đậm vị..."),
    (im_dish2, "GỎI GÀ TA", "50.000đ", "Thịt gà thả vườn xé phay giòn sần sật,\nrau răm thơm nồng và sốt trộn đậm đà."),
    (im_dish3, "XÔI GÀ TRỨNG NON", "40.000đ", "Xôi nếp nương dẻo quánh thoang thoảng\nmỡ gà, chùm trứng non vàng ngậy..."),
    (im_dish4, "MÌ GÀ TA TRUYỀN THỐNG", "55.000đ", "Sợi mì trứng dai vàng óng, thịt gà ta\nxé ngọt mềm, trứng non béo bùi...")
]

def draw_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc, is_hovered=False):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        for off in range(1, 12):
            alpha = int(18 * (1 - off / 12))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=22, fill=(36, 22, 16, alpha))
        
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(239, 232, 221))
        
        plate_size = 126
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 + 8
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 6
        tb = card_draw.textbbox((0, 0), title, font=f_title_act)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16), font=f_title_act)
        cy += 18
        pb = card_draw.textbbox((0, 0), price, font=f_price_act)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28), font=f_price_act)
        cy += 20
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_act)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51), font=f_desc_act)
            cy += 14
        
        bw, bh = 156, 32
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 14
        bx1 = center_x + bw // 2
        by1 = y1 - 14
        card_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(158, 94, 43))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=f_btn_act)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 255, 255), font=f_btn_act)
    else:
        # Inactive card
        opacity_mult = 0.88 if is_hovered else (0.60 if tier == 'near' else 0.30)
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        
        # Soft shadow if hovered
        if is_hovered:
            for off in range(1, 8):
                alpha = int(14 * (1 - off / 8))
                c_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=20, fill=(36, 22, 16, alpha))
        
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(245, 240, 232, 255))
        
        plate_size = 100 if not is_hovered else 104
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 + 6
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 6
        tb = c_draw.textbbox((0, 0), title, font=f_title_inact)
        c_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16, 255), font=f_title_inact)
        cy += 16
        pb = c_draw.textbbox((0, 0), price, font=f_price_inact)
        c_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28, 255), font=f_price_inact)
        cy += 18
        lines = desc.split('\n')
        for l in lines:
            lb = c_draw.textbbox((0, 0), l, font=f_desc_inact)
            c_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51, 230), font=f_desc_inact)
            cy += 12
        
        bw, bh = 120, 26
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 10
        bx1 = center_x + bw // 2
        by1 = y1 - 10
        c_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, outline=(184, 153, 126, 200), width=1)
        btn_txt = "ĐẶT MÓN NGAY"
        btb = c_draw.textbbox((0, 0), btn_txt, font=f_footer_label)
        c_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(138, 74, 28, 220), font=f_footer_label)
        
        # Apply unified opacity
        card_layer.putalpha(card_layer.getchannel('A').point(lambda a: int(a * opacity_mult)))
        bg_img.alpha_composite(card_layer)

# -------------------------------------------------------------------------
# PROOF: Hovering on Near Card (Dish 1 - Cơm Gà Xé)
# -------------------------------------------------------------------------
W1, H1 = 1024, 515
canvas = Image.new('RGBA', (W1, H1), (250, 247, 242, 255))
d = ImageDraw.Draw(canvas)

# Story divider sliver at top
story_bar_h = 28
d.rectangle([0, 0, W1, story_bar_h], fill=(36, 22, 14, 255))
d.text((32, 4), "Gìn giữ vị quê đượm ấm bát canh đầy...", fill=(235, 218, 195, 220), font=f_quote)
d.line([(0, story_bar_h), (W1, story_bar_h)], fill=(225, 215, 200, 255), width=1)

# Rooster sign at left edge
rw, rh = 115, 110
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
canvas.paste(rooster_s, (20, story_bar_h + 12), rooster_s)

cx = 512
card_cy = 245
c_w_act, c_h_act = 236, 280
c_w_inact, c_h_inact = 195, 250
gap = 210

# Draw cards in order (far to near to active)
# Dish 3 (Far Prev)
draw_card(canvas, cx - 2*gap, card_cy, c_w_inact, c_h_inact, 'far', dishes[3][0], dishes[3][1], dishes[3][2], dishes[3][3])
# Dish 2 (Far Next)
draw_card(canvas, cx + 2*gap, card_cy, c_w_inact, c_h_inact, 'far', dishes[2][0], dishes[2][1], dishes[2][2], dishes[2][3])
# Dish 4 (Near Prev)
draw_card(canvas, cx - gap, card_cy, c_w_inact, c_h_inact, 'near', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3])
# Dish 1 (Near Next - HOVERED! Stays at cx + gap = 722px, lifts +4px in Y, brightens opacity to 0.88!)
draw_card(canvas, cx + gap, card_cy - 4, c_w_inact + 6, c_h_inact + 6, 'near', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3], is_hovered=True)
# Dish 0 (Active Center)
draw_card(canvas, cx, card_cy, c_w_act, c_h_act, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3])

# Dots
dots_y = card_cy + c_h_act // 2 + 16
for i in range(5):
    dx = cx - 28 + i * 14
    if i == 0:
        d.rounded_rectangle([dx - 8, dots_y, dx + 8, dots_y + 7], radius=3, fill=(158, 94, 43))
    else:
        d.ellipse([dx - 3, dots_y, dx + 3, dots_y + 6], fill=(210, 195, 180))

# Footer bar
fw, fh = 620, 44
fx0 = cx - fw // 2
fy0 = dots_y + 16
fx1 = cx + fw // 2
fy1 = fy0 + fh
d.rounded_rectangle([fx0, fy0, fx1, fy1], radius=fh//2, fill=(244, 238, 230), outline=(225, 215, 200), width=1)
d.text((fx0 + 24, fy0 + 8), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(120, 100, 90), font=f_footer_label)
d.text((fx0 + 24, fy0 + 20), "090 642 79 38", fill=(138, 74, 28), font=f_footer_phone)
d.text((fx0 + 155, fy0 + 22), "Phục vụ: 06:00 – 23:00 hàng ngày", fill=(140, 123, 112), font=f_footer_label)
fbw, fbh = 145, 28
fbx0 = fx1 - fbw - 8
fby0 = fy0 + (fh - fbh) // 2
fbx1 = fx1 - 8
fby1 = fby0 + fbh
d.rounded_rectangle([fbx0, fby0, fbx1, fby1], radius=fbh//2, fill=(26, 20, 16))
d.text((fbx0 + 14, fby0 + 7), "Xem Toàn Bộ Thực Đơn →", fill=(250, 248, 245), font=f_footer_btn)

# Social buttons
for idx, icon in enumerate(["📞", "f", "♪", "🛍️", "🛵"]):
    sy = 160 + idx * 42
    d.ellipse([W1 - 38, sy, W1 - 10, sy + 28], fill=(42, 28, 22))

out_path = os.path.join(ARTIFACT_DIR, 'proof_harmonized_hover_interaction.png')
canvas.convert('RGB').save(out_path, 'PNG')
print(f"Saved Hover Verification Proof: {out_path}")
