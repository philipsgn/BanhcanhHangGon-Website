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
    f_title_act = ImageFont.truetype('arialbd.ttf', 15)
    f_price_act = ImageFont.truetype('arialbd.ttf', 19)
    f_desc_act = ImageFont.truetype('arial.ttf', 10.5)
    f_btn_act = ImageFont.truetype('arialbd.ttf', 11.5)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 12)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 15)
    f_desc_inact = ImageFont.truetype('arial.ttf', 9.5)

    f_footer_label = ImageFont.truetype('arial.ttf', 10)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 14)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 11.5)
except:
    f_quote = f_title_act = f_price_act = f_desc_act = f_btn_act = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()

dishes = [
    (im_dish0, "BÁNH CANH GÀ ĐẶC BIỆT", "70.000₫", "Thịt gà ta da vàng mọng nước, trứng\nnon béo ngậy. Nước dùng thanh ngọt..."),
    (im_dish1, "CƠM GÀ XÉ", "52.000₫", "Cơm nghệ vàng óng nấu từ nước luộc gà\nbéo ngọt, thịt gà ta xé phay đậm vị..."),
    (im_dish2, "GỎI GÀ TA", "50.000₫", "Thịt gà thả vườn xé phay giòn ngọt,\nrau răm thơm the và sốt chua ngọt..."),
    (im_dish3, "XÔI GÀ TRỨNG NON", "40.000₫", "Xôi nếp nương dẻo quánh thoang thoảng\nmỡ gà, chùm trứng non vàng ngậy..."),
    (im_dish4, "MÌ GÀ TA TRUYỀN THỐNG", "55.000₫", "Sợi mì trứng dai vàng óng, thịt gà ta\nxé ngọt mềm, trứng non béo bùi...")
]

def draw_borderless_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        for off in range(1, 16):
            alpha = int(22 * (1 - off / 16))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off*2, x1 + off//2, y1 + off*2 + 6], radius=26, fill=(36, 22, 16, alpha))
        
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=(239, 232, 221))
        
        plate_size = 255
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 - 28
        
        tray_shadow = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        ts_draw = ImageDraw.Draw(tray_shadow)
        for s_off in range(1, 12):
            s_alpha = int(26 * (1 - s_off / 12))
            ts_draw.ellipse([px + s_off, py + 16 + s_off*2, px + plate_size - s_off, py + plate_size + 16 + s_off], fill=(36, 22, 16, s_alpha))
        bg_img.alpha_composite(tray_shadow)
        
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 8
        tb = card_draw.textbbox((0, 0), title, font=f_title_act)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16), font=f_title_act)
        cy += 19
        
        pb = card_draw.textbbox((0, 0), price, font=f_price_act)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28), font=f_price_act)
        cy += 21
        
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=d_font if 'd_font' in locals() else f_desc_act)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51), font=f_desc_act)
            cy += 14
        
        bw, bh = 165, 36
        bx0 = center_x - bw // 2
        by0 = y1 - bh - 14
        bx1 = center_x + bw // 2
        by1 = y1 - 14
        card_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=bh//2, fill=(158, 94, 43))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=f_btn_act)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (bh - (btb[3]-btb[1]))//2), btn_txt, fill=(255, 255, 255), font=f_btn_act)
    
    elif tier == 'near':
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=(250, 247, 242, 220))
        
        plate_size = 175
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 + 10
        card_layer.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 8
        tb = c_draw.textbbox((0, 0), title, font=f_title_inact)
        c_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(51, 36, 28, 200), font=f_title_inact)
        cy += 17
        pb = c_draw.textbbox((0, 0), price, font=f_price_inact)
        c_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 94, 43, 200), font=f_price_inact)
        cy += 19
        
        lines = desc.split('\n')
        for l in lines:
            lb = c_draw.textbbox((0, 0), l, font=f_desc_inact)
            c_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(106, 88, 77, 180), font=f_desc_inact)
            cy += 13
        
        bw, bh = 135, 28
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
        card_layer = Image.new('RGBA', bg_img.size, (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(card_layer)
        c_draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(250, 247, 242, 160))
        
        plate_size = 140
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

W1, H1 = 1024, 530
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
card_cy = 278
c_w_act, c_h_act = 275, 355

draw_borderless_card(canvas1, cx - 440, card_cy + 18, 185, 280, 'far', dishes[3][0], dishes[3][1], dishes[3][2], dishes[3][3])
draw_borderless_card(canvas1, cx + 440, card_cy + 18, 185, 280, 'far', dishes[2][0], dishes[2][1], dishes[2][2], dishes[2][3])
draw_borderless_card(canvas1, cx - 232, card_cy + 10, 225, 325, 'near', dishes[4][0], dishes[4][1], dishes[4][2], dishes[4][3])
draw_borderless_card(canvas1, cx + 232, card_cy + 10, 225, 325, 'near', dishes[1][0], dishes[1][1], dishes[1][2], dishes[1][3])
draw_borderless_card(canvas1, cx, card_cy, c_w_act, c_h_act, 'active', dishes[0][0], dishes[0][1], dishes[0][2], dishes[0][3])

d1.polygon([(cx - 165, card_cy), (cx - 150, card_cy - 16), (cx - 150, card_cy + 16)], fill=(158, 94, 43, 140))
d1.polygon([(cx + 165, card_cy), (cx + 150, card_cy - 16), (cx + 150, card_cy + 16)], fill=(158, 94, 43, 140))

dots_y = card_cy + c_h_act // 2 + 10
for i, dx_off in enumerate([-28, -14, 0, 14, 28]):
    dot_color = (158, 94, 43, 255) if i == 2 else (214, 199, 178, 255)
    dot_w = 26 if i == 2 else 8
    d1.rounded_rectangle([cx + dx_off - dot_w//2, dots_y, cx + dx_off + dot_w//2, dots_y + 8], radius=4, fill=dot_color)

fy = H1 - 44
d1.rounded_rectangle([48, fy, W1 - 48, fy + 36], radius=18, fill=(255, 255, 255, 200), outline=(201, 154, 74, 50), width=1)
d1.text((68, fy + 5), "ĐẶT GIAO TẬN NƠI • HOTLINE", fill=(138, 74, 28), font=f_footer_label)
d1.text((68, fy + 17), "090 642 79 38", fill=(26, 20, 16), font=f_footer_phone)
btn_lbl = "Xem Toàn Bộ Thực Đơn  →"
bb = d1.textbbox((0, 0), btn_lbl, font=f_footer_btn)
d1.rounded_rectangle([W1 - 250, fy + 4, W1 - 65, fy + 32], radius=14, fill=(26, 20, 16))
d1.text((W1 - 250 + (185 - (bb[2]-bb[0]))//2, fy + 9), btn_lbl, fill=(250, 248, 245), font=f_footer_btn)

plate_top_y = card_cy - c_h_act // 2 - 28
d1.line([(cx + 150, story_bar_h), (cx + 150, plate_top_y)], fill=(34, 139, 34, 220), width=2)
gap_val = plate_top_y - story_bar_h
d1.text((cx + 158, story_bar_h + gap_val // 2 - 8), f"Khoảng thở trần an toàn: {gap_val}px (>= 42px)", fill=(34, 139, 34, 255), font=f_desc_act)

d1.line([(32, story_bar_h), (50, story_bar_h + 12)], fill=(196, 78, 32, 255), width=2)
d1.text((54, story_bar_h + 4), "2 dây thừng chạm trần (0 gap)", fill=(196, 78, 32, 255), font=f_desc_act)

proof1_path = os.path.join(ARTIFACT_DIR, 'proof_borderless_hero_100_zoom.png')
canvas1.save(proof1_path, 'PNG')
print(f"Proof 1 re-saved with clearance = {gap_val}px: {proof1_path}")
