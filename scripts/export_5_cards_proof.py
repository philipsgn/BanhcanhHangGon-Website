import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

# Load assets
p_rooster = os.path.join(ROOT, 'images', 'menu', 'original-chef-rooster-board.webp')
p_dish0 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Soup on Wooden Tray_result.webp')
p_dish1 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Rice Tray Feast_result.webp')
p_dish2 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Salad on Wooden Tray_result.webp')
p_dish3 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Xôi Gà on a Wooden Tray_result.webp')
p_dish4 = os.path.join(ROOT, 'images', 'menu', 'mi-ga.webp')

im_rooster = Image.open(p_rooster).convert('RGBA')
im_dish0 = Image.open(p_dish0).convert('RGBA')
im_dish1 = Image.open(p_dish1).convert('RGBA')
im_dish2 = Image.open(p_dish2).convert('RGBA')
im_dish3 = Image.open(p_dish3).convert('RGBA')
im_dish4 = Image.open(p_dish4).convert('RGBA')

# Canvas: 1300 x 980 (Wide Panorama Stage)
DW, DH = 1300, 980
desk_bg = Image.new('RGB', (DW, DH), (250, 248, 245))
draw = ImageDraw.Draw(desk_bg)

# Background subtle motif & radial warm lighting
draw.ellipse([DW//2 - 460, 140, DW//2 + 460, 900], fill=(255, 255, 255))

try:
    f_title_active = ImageFont.truetype('arialbd.ttf', 16.5)
    f_price_active = ImageFont.truetype('arialbd.ttf', 22)
    f_desc_active = ImageFont.truetype('arial.ttf', 12)
    f_btn_active = ImageFont.truetype('arialbd.ttf', 12)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 13.5)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 17)
    f_desc_inact = ImageFont.truetype('arial.ttf', 10.5)

    f_footer_label = ImageFont.truetype('arial.ttf', 11.5)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 16)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 13)
except:
    f_title_active = f_price_active = f_desc_active = f_btn_active = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()

# 1. TIER 1: ORIGINAL ROOSTER BOARD AT FAR LEFT (x=24, y=0)
rw = 230
rh = int(rw * im_rooster.height / im_rooster.width)
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
rx = 24
desk_bg.paste(rooster_s, (rx, 0), rooster_s)

# 2. TIER 2: 3D PANORAMA 5 CARDS (Stage Center below the bottom of the wooden board!)
# Bottom of wooden board is at rh = 130px. Stage center is at y=520px -> Complete 100% vertical clearance!
stage_center_x = DW // 2
stage_center_y = 510

def draw_card(bg_img, center_x, center_y, width, height, tier, dish_img, title, price, desc):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if tier == 'active':
        # Soft ambient shadow
        for off in range(1, 14):
            alpha = int(32 * (1 - off / 14))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=26, fill=(36, 22, 16, alpha))
        
        # Active Card: Nâu Cát Gỗ Ấm (#EFE8DD)
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=(239, 232, 221), outline=(196, 164, 130), width=2)
        
        # Pop-out Plate (Elevated naturally, 0% clipped at top, 0% overlapping title)
        plate_w = 165
        plate_h = int(plate_w * dish_img.height / dish_img.width)
        dish_s = dish_img.resize((plate_w, plate_h), Image.Resampling.LANCZOS)
        px = center_x - plate_w // 2
        py = y0 - 15  # Natural placement inside top of card
        bg_img.paste(dish_s, (px, py), dish_s)
        
        # Body Content: ample clear gap (24px) between plate bottom and title
        cy = py + plate_h + 20
        # Title (Deep Coal Brown #1A1410)
        tb = card_draw.textbbox((0, 0), title, font=f_title_active)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(26, 20, 16), font=f_title_active)
        cy += 22
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
        cy += 10
        # Button: ĐẶT MÓN NGAY (#9E5E2B)
        bw, bh = 170, 36
        bx = center_x - bw // 2
        card_draw.rounded_rectangle([bx, cy, bx + bw, cy + bh], radius=18, fill=(158, 94, 43))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=f_btn_active)
        card_draw.text((center_x - (btb[2]-btb[0])//2, cy + 9), btn_txt, fill=(255, 255, 255), font=f_btn_active)

    elif tier == 'near':
        # Inactive Near Card: Kem Sáng (#FAF7F2)
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=22, fill=(250, 247, 242), outline=(216, 195, 165), width=1)
        
        # Pop-out Plate
        plate_w = 135
        plate_h = int(plate_w * dish_img.height / dish_img.width)
        dish_s = dish_img.resize((plate_w, plate_h), Image.Resampling.LANCZOS)
        px = center_x - plate_w // 2
        py = y0 - 10
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_h + 16
        tb = card_draw.textbbox((0, 0), title, font=f_title_inact)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(51, 36, 28), font=f_title_inact)
        cy += 18
        pb = card_draw.textbbox((0, 0), price, font=f_price_inact)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 94, 43), font=f_price_inact)
        cy += 22
        lines = desc.split('\n')[:2]
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_inact)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(106, 88, 77), font=f_desc_inact)
            cy += 15
        cy += 6
        bw, bh = 120, 28
        bx = center_x - bw // 2
        card_draw.rounded_rectangle([bx, cy, bx + bw, cy + bh], radius=14, outline=(196, 142, 89), width=1)
        btn_txt = "XEM MÓN"
        btb = card_draw.textbbox((0, 0), btn_txt, font=f_desc_inact)
        card_draw.text((center_x - (btb[2]-btb[0])//2, cy + 7), btn_txt, fill=(158, 94, 43), font=f_desc_inact)

    elif tier == 'far':
        # Far Card: Mờ 35% (#FAF7F2 mờ)
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=(250, 247, 242), outline=(225, 210, 190), width=1)
        plate_w = 110
        plate_h = int(plate_w * dish_img.height / dish_img.width)
        dish_s = dish_img.resize((plate_w, plate_h), Image.Resampling.LANCZOS)
        px = center_x - plate_w // 2
        py = y0 - 5
        bg_img.paste(dish_s, (px, py), dish_s)
        
        cy = py + plate_h + 12
        tb = card_draw.textbbox((0, 0), title, font=f_desc_inact)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(85, 68, 59), font=f_desc_inact)
        cy += 16
        pb = card_draw.textbbox((0, 0), price, font=f_desc_inact)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 94, 43), font=f_desc_inact)

# Draw 1: Far Left Card (Card 3: Xôi Gà Trứng Non)
draw_card(desk_bg, stage_center_x - 470, stage_center_y + 20, 210, 310, 'far',
          im_dish3, "XÔI GÀ TRỨNG NON", "40.000₫", "Nếp nương dẻo thơm mỡ gà,\ntrứng non ngậy bùi.")

# Draw 2: Far Right Card (Card 2: Gỏi Gà Ta Bắp Chuối)
draw_card(desk_bg, stage_center_x + 470, stage_center_y + 20, 210, 310, 'far',
          im_dish2, "GỎI GÀ TA BẮP CHUỐI", "50.000₫", "Bắp chuối giòn sần sật,\ngà ta thả vườn ngọt dai.")

# Draw 3: Near Left Card (Card 4: Mì Gà Ta Truyền Thống - MỚI)
draw_card(desk_bg, stage_center_x - 250, stage_center_y + 10, 250, 370, 'near',
          im_dish4, "MÌ GÀ TA TRUYỀN THỐNG", "55.000₫", "Mì trứng vàng óng dai giòn,\ngà xé ngọt mềm thanh tao.")

# Draw 4: Near Right Card (Card 1: Cơm Gỏi Gà Xé)
draw_card(desk_bg, stage_center_x + 250, stage_center_y + 10, 250, 370, 'near',
          im_dish1, "CƠM GỎI GÀ XÉ", "52.000₫", "Cơm nghệ thơm ngọt nước luộc gà,\ngỏi gà xé chua ngọt bắp cải.")

# Draw 5: ACTIVE Center Card (Card 0: Bánh Canh Gà Đặc Biệt)
draw_card(desk_bg, stage_center_x, stage_center_y - 14, 290, 420, 'active',
          im_dish0, "BÁNH CANH GÀ ĐẶC BIỆT", "70.000₫", "Thịt gà da vàng giòn mọng nước,\ntrứng non béo ngậy lòng đào.\nNước dùng ninh xương thanh ngọt.")

# 3. PAGINATION DOTS (5 Món)
dot_y = stage_center_y + 225
dots_w = 5 * 14 + 18
start_dot_x = stage_center_x - dots_w // 2

# Dot 0: active
draw.rounded_rectangle([start_dot_x, dot_y, start_dot_x + 26, dot_y + 9], radius=5, fill=(158, 94, 43))
# Dots 1, 2, 3, 4: inactive
for i in range(1, 5):
    dx = start_dot_x + 26 + 10 + (i - 1) * 18
    draw.ellipse([dx, dot_y, dx + 9, dot_y + 9], fill=(216, 195, 165))

# 4. FOOTER BAR
fy = DH - 70
draw.line([(stage_center_x - 440, fy), (stage_center_x + 440, fy)], fill=(225, 218, 210), width=1)
draw.text((stage_center_x - 440, fy + 12), "Đặt Giao Tận Nơi • Hotline", fill=(140, 122, 112), font=f_footer_label)
draw.text((stage_center_x - 440, fy + 26), "090 642 79 38", fill=(17, 17, 17), font=f_footer_phone)
draw.text((stage_center_x - 440, fy + 48), "Phục vụ: 06:00 – 23:00 hàng ngày", fill=(102, 85, 77), font=f_footer_label)

btn_w, btn_h = 220, 40
bx = stage_center_x + 440 - btn_w
draw.rounded_rectangle([bx, fy + 18, bx + btn_w, fy + 18 + btn_h], radius=20, fill=(17, 17, 17))
draw.text((bx + 26, fy + 30), "Xem Toàn Bộ Thực Đơn  →", fill=(255, 255, 255), font=f_footer_btn)

out_path = os.path.join(ARTIFACT_DIR, 'proof_menu_original_board_5_cards.png')
desk_bg.save(out_path)
print(f'Saved proof: {out_path}')
