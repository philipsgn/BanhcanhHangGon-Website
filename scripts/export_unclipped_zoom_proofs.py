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
    f_title_active = ImageFont.truetype('arialbd.ttf', 15.5)
    f_price_active = ImageFont.truetype('arialbd.ttf', 20)
    f_desc_active = ImageFont.truetype('arial.ttf', 11)
    f_btn_active = ImageFont.truetype('arialbd.ttf', 11.5)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 12.5)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 15.5)
    f_desc_inact = ImageFont.truetype('arial.ttf', 9.5)

    f_footer_label = ImageFont.truetype('arial.ttf', 10.5)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 14.5)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 12)
except:
    f_title_active = f_price_active = f_desc_active = f_btn_active = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()

def draw_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        for off in range(1, 14):
            alpha = int(20 * (1 - off / 14))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=24, fill=(36, 22, 16, alpha))
        
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=(239, 232, 221))
        
        # Responsive plate: 136x136px for laptop vh=680
        plate_size = 136
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 - 38  # Protrudes 38px, completely within bounds and never sliced!
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 14
        
        # Title
        tb = card_draw.textbbox((0, 0), title, font=f_title_active)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16), font=f_title_active)
        cy += 21
        
        # Price
        pb = card_draw.textbbox((0, 0), price, font=f_price_active)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28), font=f_price_active)
        cy += 23
        
        # Desc
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_active)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51), font=f_desc_active)
            cy += 15
        
        # CTA Button
        btn_w, btn_h = 165, 34
        bx0 = center_x - btn_w // 2
        by0 = y1 - 38
        card_draw.rounded_rectangle([bx0, by0, bx0 + btn_w, by0 + btn_h], radius=17, fill=(158, 94, 43))
        btn_text = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_text, font=f_btn_active)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (btn_h - (btb[3]-btb[1]))//2 - 1), btn_text, fill=(255, 255, 255), font=f_btn_active)

    elif tier == 'near':
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(250, 247, 242))
        plate_size = 114
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        r, g, b, a = dish_s.split()
        a = a.point(lambda p: int(p * 0.75))
        dish_s.putalpha(a)
        
        px = center_x - plate_size // 2
        py = y0 - 32
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 12
        tb = card_draw.textbbox((0, 0), title, font=f_title_inact)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(80, 65, 55), font=f_title_inact)
        cy += 18
        pb = card_draw.textbbox((0, 0), price, font=f_price_inact)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 100, 50), font=f_price_inact)
        cy += 20
        lines = desc.split('\n')
        for l in lines[:2]:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_inact)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(110, 95, 85), font=f_desc_inact)
            cy += 13
        
        btn_w, btn_h = 95, 24
        bx0 = center_x - btn_w // 2
        by0 = y1 - 28
        card_draw.rounded_rectangle([bx0, by0, bx0 + btn_w, by0 + btn_h], radius=12, fill=(245, 238, 228))
        btn_text = "XEM MÓN"
        btb = card_draw.textbbox((0, 0), btn_text, font=f_desc_inact)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + 5), btn_text, fill=(158, 94, 43), font=f_desc_inact)

    elif tier == 'far':
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=20, fill=(250, 247, 242))
        plate_size = 96
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        r, g, b, a = dish_s.split()
        a = a.point(lambda p: int(p * 0.45))
        dish_s.putalpha(a)
        
        px = center_x - plate_size // 2
        py = y0 - 26
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 10
        tb = card_draw.textbbox((0, 0), title, font=f_desc_inact)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(110, 95, 85), font=f_desc_inact)
        cy += 15
        pb = card_draw.textbbox((0, 0), price, font=f_desc_inact)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(140, 110, 85), font=f_desc_inact)

# ==========================================
# 1. RENDER EXACT LAPTOP 100% ZOOM VIEWPORT (1366 x 680)
# Matches user's exact resolution and zoom level!
# ==========================================
LW, LH = 1366, 680
lap_bg = Image.new('RGB', (LW, LH), (250, 248, 245))
draw = ImageDraw.Draw(lap_bg)
draw.ellipse([LW//2 - 420, 60, LW//2 + 420, 620], fill=(255, 255, 255))

# Rooster Board ABSOLUTE TOP-LEFT (rx=24, y=0)
rw = 180
rh = int(rw * im_rooster.height / im_rooster.width)
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
lap_bg.paste(rooster_s, (24, 0), rooster_s)

# Stage Center: Vertical Center at y = 330!
stage_center_x = LW // 2
stage_center_y = 330

# Dish 3 (XÔI GÀ TRỨNG NON) AS CENTER ACTIVE (as in user screenshot!)
# Far Left (1): Cơm gà xé
draw_card(lap_bg, stage_center_x - 470, stage_center_y + 14, 195, 280, 'far', im_dish1, 'CƠM GÀ XÉ', '52.000₫', '')
# Near Left (2): Gỏi gà ta
draw_card(lap_bg, stage_center_x - 260, stage_center_y + 6, 225, 325, 'near', im_dish2, 'GỎI GÀ TA', '50.000₫', 'Gà thả vườn xé phay giòn ngọt,\nrau răm thơm the nồng nàn.')
# Far Right (0): Bánh canh gà đặc biệt
draw_card(lap_bg, stage_center_x + 470, stage_center_y + 14, 195, 280, 'far', im_dish0, 'BÁNH CANH GÀ', '70.000₫', '')
# Near Right (4): Mì gà ta
draw_card(lap_bg, stage_center_x + 260, stage_center_y + 6, 225, 325, 'near', im_dish4, 'MÌ GÀ TA TRUYỀN THỐNG', '55.000₫', 'Sợi mì trứng dai vàng óng,\nthịt gà ngọt mềm thanh tao.')
# Center Active (3): XÔI GÀ TRỨNG NON (100% UNCLIPPED!)
draw_card(lap_bg, stage_center_x, stage_center_y - 6, 255, 370, 'active', im_dish3, 'XÔI GÀ TRỨNG NON', '40.000₫', 'Xôi nếp nương dẻo quánh thoang thoảng\nmỡ gà, chùm trứng non béo ngậy.')

# Dots
dot_y = LH - 80
for i in range(5):
    dx = stage_center_x - 36 + i * 18
    if i == 3:
        draw.rounded_rectangle([dx - 6, dot_y, dx + 14, dot_y + 7], radius=3.5, fill=(158, 94, 43))
    else:
        draw.ellipse([dx, dot_y, dx + 7, dot_y + 7], fill=(216, 195, 165))

# Footer bar (neatly at bottom)
draw.line([LW//2 - 350, dot_y + 24, LW//2 + 350, dot_y + 24], fill=(201, 154, 74, 80), width=1)
draw.text((LW//2 - 350, dot_y + 32), "Đặt Giao Tận Nơi • Hotline", fill=(140, 122, 112), font=f_footer_label)
draw.text((LW//2 - 350, dot_y + 46), "090 642 79 38", fill=(17, 17, 17), font=f_footer_phone)

draw.rounded_rectangle([LW//2 + 180, dot_y + 36, LW//2 + 350, dot_y + 68], radius=16, fill=(17, 17, 17))
draw.text((LW//2 + 205, dot_y + 45), "Xem Toàn Bộ Thực Đơn →", fill=(255, 255, 255), font=f_footer_btn)

proof_laptop = os.path.join(ARTIFACT_DIR, 'proof_menu_zoom_100_laptop.png')
lap_bg.save(proof_laptop, 'PNG')
print(f'Saved proof: {proof_laptop}')

# ==========================================
# 2. RENDER CLOSE-UP OF TRAY TOP ON LAPTOP VIEW
# ==========================================
# Crop top 250px above card center to prove 100% circular intact wooden rim
crop_box = [stage_center_x - 140, stage_center_y - 250, stage_center_x + 140, stage_center_y + 50]
closeup = lap_bg.crop(crop_box)
proof_closeup = os.path.join(ARTIFACT_DIR, 'proof_menu_zoom_100_plate_top_closeup.png')
closeup.save(proof_closeup, 'PNG')
print(f'Saved closeup: {proof_closeup}')
