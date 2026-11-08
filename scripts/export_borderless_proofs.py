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
p_dish2 = os.path.join(ROOT, 'images', 'menu', 'goi-ga.webp')  # NEW GỎI GÀ XÉ
p_dish3 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Xôi Gà on a Wooden Tray_result.webp')
p_dish4 = os.path.join(ROOT, 'images', 'menu', 'mi-ga.webp')

im_rooster = Image.open(p_rooster).convert('RGBA')
im_dish0 = Image.open(p_dish0).convert('RGBA')
im_dish1 = Image.open(p_dish1).convert('RGBA')
im_dish2 = Image.open(p_dish2).convert('RGBA')
im_dish3 = Image.open(p_dish3).convert('RGBA')
im_dish4 = Image.open(p_dish4).convert('RGBA')

try:
    f_title_active = ImageFont.truetype('arialbd.ttf', 16)
    f_price_active = ImageFont.truetype('arialbd.ttf', 21)
    f_desc_active = ImageFont.truetype('arial.ttf', 11.5)
    f_btn_active = ImageFont.truetype('arialbd.ttf', 12)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 13)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 16)
    f_desc_inact = ImageFont.truetype('arial.ttf', 10)

    f_footer_label = ImageFont.truetype('arial.ttf', 11)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 15)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 12.5)
except:
    f_title_active = f_price_active = f_desc_active = f_btn_active = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()

def draw_clean_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        # Soft ambient shadow beneath card body (NO BORDER LINE)
        for off in range(1, 16):
            alpha = int(24 * (1 - off / 16))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=26, fill=(36, 22, 16, alpha))
        
        # Active Card Background (#EFE8DD) - 100% borderless
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=(239, 232, 221))
        
        # Plate pops OUT of the top of the card by 60px (Free upper hemisphere in open space!)
        plate_size = 154
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        px = center_x - plate_size // 2
        py = y0 - 62  # Plate top sits at y0 - 62, card starts at y0 -> ZERO top frame or rabbit ears!
        bg_img.paste(dish_s, (px, py), dish_s)
        
        # Body Content: ample clear gap (26px) between plate bottom and title
        cy = py + plate_size + 16
        
        # Title (Deep Coal Brown #1A1410)
        tb = card_draw.textbbox((0, 0), title, font=f_title_active)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16), font=f_title_active)
        cy += 23
        
        # Price (Warm Reddish Wood #8A4A1C)
        pb = card_draw.textbbox((0, 0), price, font=f_price_active)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(138, 74, 28), font=f_price_active)
        cy += 26
        
        # Desc
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_active)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(74, 60, 51), font=f_desc_active)
            cy += 16
        
        # CTA Button
        cy = y1 - 42
        btn_w, btn_h = 175, 36
        bx0 = center_x - btn_w // 2
        by0 = cy
        bx1 = bx0 + btn_w
        by1 = by0 + btn_h
        card_draw.rounded_rectangle([bx0, by0, bx1, by1], radius=18, fill=(158, 94, 43))
        btn_text = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_text, font=f_btn_active)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + (btn_h - (btb[3]-btb[1]))//2 - 1), btn_text, fill=(255, 255, 255), font=f_btn_active)

    elif tier == 'near':
        # Near Card (scale 0.85, opacity ~65%, NO BORDER LINE)
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=(250, 247, 242))
        
        plate_size = 126
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        r, g, b, a = dish_s.split()
        a = a.point(lambda p: int(p * 0.75))
        dish_s.putalpha(a)
        
        px = center_x - plate_size // 2
        py = y0 - 52
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 14
        tb = card_draw.textbbox((0, 0), title, font=f_title_inact)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(80, 65, 55), font=f_title_inact)
        cy += 20
        pb = card_draw.textbbox((0, 0), price, font=f_price_inact)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 100, 50), font=f_price_inact)
        cy += 22
        lines = desc.split('\n')
        for l in lines[:2]:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_inact)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(110, 95, 85), font=f_desc_inact)
            cy += 14
        
        btn_w, btn_h = 100, 26
        bx0 = center_x - btn_w // 2
        by0 = y1 - 32
        card_draw.rounded_rectangle([bx0, by0, bx0 + btn_w, by0 + btn_h], radius=13, fill=(245, 238, 228))
        btn_text = "XEM MÓN"
        btb = card_draw.textbbox((0, 0), btn_text, font=f_desc_inact)
        card_draw.text((center_x - (btb[2]-btb[0])//2, by0 + 6), btn_text, fill=(158, 94, 43), font=f_desc_inact)

    elif tier == 'far':
        # Far Card (scale 0.72, opacity ~40%, NO BORDER LINE)
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(250, 247, 242))
        plate_size = 105
        dish_s = dish_img.resize((plate_size, plate_size), Image.Resampling.LANCZOS)
        r, g, b, a = dish_s.split()
        a = a.point(lambda p: int(p * 0.45))
        dish_s.putalpha(a)
        
        px = center_x - plate_size // 2
        py = y0 - 44
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_size + 12
        tb = card_draw.textbbox((0, 0), title, font=f_desc_inact)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(110, 95, 85), font=f_desc_inact)
        cy += 16
        pb = card_draw.textbbox((0, 0), price, font=f_desc_inact)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(140, 110, 85), font=f_desc_inact)

# ==========================================
# 1. RENDER DESKTOP PANORAMA (1350 x 980) WITH GỎI GÀ XÉ AS ACTIVE
# ==========================================
DW, DH = 1350, 980
desk_bg = Image.new('RGB', (DW, DH), (250, 248, 245))
draw = ImageDraw.Draw(desk_bg)
draw.ellipse([DW//2 - 460, 140, DW//2 + 460, 900], fill=(255, 255, 255))

# Rooster Board FAR LEFT (rx=32, y=0)
rw = 220
rh = int(rw * im_rooster.height / im_rooster.width)
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
desk_bg.paste(rooster_s, (32, 0), rooster_s)

# Stage Center
stage_center_x = DW // 2
stage_center_y = 540

# Far Left (4): Mì Gà
draw_clean_card(desk_bg, stage_center_x - 480, stage_center_y + 16, 210, 310, 'far', im_dish4, 'MÌ GÀ TA', '55.000₫', '')
# Near Left (1): Cơm Gỏi Gà
draw_clean_card(desk_bg, stage_center_x - 265, stage_center_y + 8, 245, 360, 'near', im_dish1, 'CƠM GỎI GÀ XÉ', '52.000₫', 'Cơm nghệ thơm béo nước luộc gà,\ngỏi bắp cải chua ngọt cay nồng.')
# Far Right (3): Xôi Gà
draw_clean_card(desk_bg, stage_center_x + 480, stage_center_y + 16, 210, 310, 'far', im_dish3, 'XÔI GÀ TRỨNG NON', '40.000₫', '')
# Near Right (0): Bánh Canh Gà
draw_clean_card(desk_bg, stage_center_x + 265, stage_center_y + 8, 245, 360, 'near', im_dish0, 'BÁNH CANH GÀ', '70.000₫', 'Thịt gà da vàng mọng nước,\ntrứng non ngậy, nước hầm ngọt thanh.')
# Center Active (2): GỎI GÀ XÉ (NEW IMAGE & NAME!)
draw_clean_card(desk_bg, stage_center_x, stage_center_y - 8, 280, 420, 'active', im_dish2, 'GỎI GÀ XÉ', '50.000₫', 'Thịt gà thả vườn xé phay bắp cải cà rốt\ngiòn mát, rau răm cay the và sốt chua ngọt.')

# Dots
dot_y = stage_center_y + 225
for i in range(5):
    dx = stage_center_x - 40 + i * 20
    if i == 2:
        draw.rounded_rectangle([dx - 8, dot_y, dx + 16, dot_y + 8], radius=4, fill=(158, 94, 43))
    else:
        draw.ellipse([dx, dot_y, dx + 8, dot_y + 8], fill=(216, 195, 165))

# Footer bar
draw.line([DW//2 - 380, dot_y + 36, DW//2 + 380, dot_y + 36], fill=(201, 154, 74, 100), width=1)
draw.text((DW//2 - 380, dot_y + 48), "Đặt Giao Tận Nơi • Hotline", fill=(140, 122, 112), font=f_footer_label)
draw.text((DW//2 - 380, dot_y + 64), "090 642 79 38", fill=(17, 17, 17), font=f_footer_phone)
draw.text((DW//2 - 380, dot_y + 86), "Phục vụ: 06:00 – 23:00 hàng ngày", fill=(102, 85, 77), font=f_footer_label)

draw.rounded_rectangle([DW//2 + 200, dot_y + 54, DW//2 + 380, dot_y + 90], radius=18, fill=(17, 17, 17))
draw.text((DW//2 + 225, dot_y + 64), "Xem Toàn Bộ Thực Đơn →", fill=(255, 255, 255), font=f_footer_btn)

proof_main = os.path.join(ARTIFACT_DIR, 'proof_menu_borderless_clean.png')
desk_bg.save(proof_main, 'PNG')
print(f'Saved proof: {proof_main}')

# ==========================================
# 2. RENDER CLOSE-UP PROOF OF CARD TOP (600 x 450)
# ==========================================
# Crop center active card top to prove 0 top frame and 0 border stroke
crop_box = [stage_center_x - 170, stage_center_y - 250, stage_center_x + 170, stage_center_y + 100]
closeup = desk_bg.crop(crop_box)
proof_closeup = os.path.join(ARTIFACT_DIR, 'proof_menu_card_top_closeup.png')
closeup.save(proof_closeup, 'PNG')
print(f'Saved closeup: {proof_closeup}')
