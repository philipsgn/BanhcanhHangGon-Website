import os
import sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
ARTIFACT_DIR = r'C:\Users\TanPhat\.gemini\antigravity\brain\6b7037e5-7059-4367-a02f-fa92707708bf'

# Load assets
p_rooster = os.path.join(ROOT, 'images', 'menu', 'chef-rooster-board.webp')
p_dish1 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Soup on Wooden Tray_result.webp')
p_dish2 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Rice Tray Feast_result.webp')
p_dish3 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Chicken Salad on Wooden Tray_result.webp')
p_dish4 = os.path.join(ROOT, 'images', 'menu', 'Vietnamese Xôi Gà on a Wooden Tray_result.webp')

im_rooster = Image.open(p_rooster).convert('RGBA')
im_dish1 = Image.open(p_dish1).convert('RGBA')
im_dish2 = Image.open(p_dish2).convert('RGBA')
im_dish3 = Image.open(p_dish3).convert('RGBA')
im_dish4 = Image.open(p_dish4).convert('RGBA')

# Canvas: 1200 x 980 (Compact, Screen-Fit Stage)
DW, DH = 1200, 980
desk_bg = Image.new('RGB', (DW, DH), (250, 248, 245))
draw = ImageDraw.Draw(desk_bg)

# Background subtle motif & radial warm lighting
draw.ellipse([DW//2 - 350, 150, DW//2 + 350, 850], fill=(255, 255, 255))

try:
    f_title_active = ImageFont.truetype('arialbd.ttf', 17)
    f_price_active = ImageFont.truetype('arialbd.ttf', 24)
    f_desc_active = ImageFont.truetype('arial.ttf', 12.5)
    f_btn_active = ImageFont.truetype('arialbd.ttf', 12.5)

    f_title_inact = ImageFont.truetype('arialbd.ttf', 14.5)
    f_price_inact = ImageFont.truetype('arialbd.ttf', 18)
    f_desc_inact = ImageFont.truetype('arial.ttf', 11)

    f_footer_label = ImageFont.truetype('arial.ttf', 11.5)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 16)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 13)
except:
    f_title_active = f_price_active = f_desc_active = f_btn_active = ImageFont.load_default()
    f_title_inact = f_price_inact = f_desc_inact = ImageFont.load_default()
    f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()

# 1. HERO HEADER: ROOSTER + BOARD (ROPES TOUCH CEILING y=0)
rw = 310
rh = int(rw * im_rooster.height / im_rooster.width)
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
rx = (DW - rw) // 2
desk_bg.paste(rooster_s, (rx, 0), rooster_s)

# 2. 3D STAGE CARDS
stage_center_x = DW // 2
stage_center_y = rh + 280

# --- CARD HELPER FUNCTION ---
def draw_card(bg_img, center_x, center_y, width, height, is_active, dish_img, title, price, desc):
    card_draw = ImageDraw.Draw(bg_img)
    x0 = center_x - width // 2
    y0 = center_y - height // 2
    x1 = center_x + width // 2
    y1 = center_y + height // 2

    if is_active:
        # Deep contact shadow for the active card
        for off in range(1, 16):
            alpha = int(45 * (1 - off / 16))
            card_draw.rounded_rectangle([x0 - off//2, y0 + off, x1 + off//2, y1 + off*2], radius=28, fill=(36, 22, 16, alpha))
        
        # Active Card: Gỗ Mun Sơn Mài
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=28, fill=(36, 22, 16), outline=(201, 154, 74), width=2)
        
        # Pop-out Plate (centered horizontally, shifted upwards)
        plate_w = 195
        plate_h = int(plate_w * dish_img.height / dish_img.width)
        dish_s = dish_img.resize((plate_w, plate_h), Image.Resampling.LANCZOS)
        px = center_x - plate_w // 2
        py = y0 - plate_h // 2 + 15
        
        # Contact shadow under plate
        card_draw.ellipse([px + 20, y0 + 10, px + plate_w - 20, y0 + 26], fill=(16, 8, 4))
        bg_img.paste(dish_s, (px, py), dish_s)
        
        # Body Content
        cy = py + plate_h + 12
        # Title
        tb = card_draw.textbbox((0, 0), title, font=f_title_active)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(246, 226, 182), font=f_title_active)
        cy += 24
        # Price
        pb = card_draw.textbbox((0, 0), price, font=f_price_active)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(255, 255, 255), font=f_price_active)
        cy += 30
        # Desc (multiline center)
        lines = desc.split('\n')
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_active)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(226, 217, 210), font=f_desc_active)
            cy += 18
        cy += 10
        # Button: ĐẶT MÓN NGAY
        bw, bh = 180, 40
        bx = center_x - bw // 2
        card_draw.rounded_rectangle([bx, cy, bx + bw, cy + bh], radius=20, fill=(201, 154, 74))
        btn_txt = "ĐẶT MÓN NGAY"
        btb = card_draw.textbbox((0, 0), btn_txt, font=f_btn_active)
        card_draw.text((center_x - (btb[2]-btb[0])//2, cy + 11), btn_txt, fill=(26, 16, 9), font=f_btn_active)

    else:
        # Inactive Card: Kem Giấy Dó
        card_draw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=(244, 239, 235), outline=(216, 195, 165), width=1)
        
        # Pop-out Plate
        plate_w = 150
        plate_h = int(plate_w * dish_img.height / dish_img.width)
        dish_s = dish_img.resize((plate_w, plate_h), Image.Resampling.LANCZOS)
        px = center_x - plate_w // 2
        py = y0 - plate_h // 2 + 15
        
        # Contact shadow
        card_draw.ellipse([px + 15, y0 + 8, px + plate_w - 15, y0 + 20], fill=(160, 145, 135))
        bg_img.paste(dish_s, (px, py), dish_s)
        
        # Body Content
        cy = py + plate_h + 10
        tb = card_draw.textbbox((0, 0), title, font=f_title_inact)
        card_draw.text((center_x - (tb[2]-tb[0])//2, cy), title, fill=(36, 22, 16), font=f_title_inact)
        cy += 20
        pb = card_draw.textbbox((0, 0), price, font=f_price_inact)
        card_draw.text((center_x - (pb[2]-pb[0])//2, cy), price, fill=(158, 94, 43), font=f_price_inact)
        cy += 24
        lines = desc.split('\n')[:2]
        for l in lines:
            lb = card_draw.textbbox((0, 0), l, font=f_desc_inact)
            card_draw.text((center_x - (lb[2]-lb[0])//2, cy), l, fill=(106, 88, 77), font=f_desc_inact)
            cy += 16
        cy += 6
        # Small pill outline
        bw, bh = 140, 32
        bx = center_x - bw // 2
        card_draw.rounded_rectangle([bx, cy, bx + bw, cy + bh], radius=16, outline=(196, 142, 89), width=1)
        btn_txt = "XEM MÓN"
        btb = card_draw.textbbox((0, 0), btn_txt, font=f_desc_inact)
        card_draw.text((center_x - (btb[2]-btb[0])//2, cy + 9), btn_txt, fill=(158, 94, 43), font=f_desc_inact)

# Draw Inactive Left Card (Card 3: Xôi Gà Trứng Non)
draw_card(desk_bg, stage_center_x - 300, stage_center_y + 15, 260, 370, False,
          im_dish4, "XÔI GÀ TRỨNG NON", "40.000₫", "Nếp nương dẻo thơm mỡ gà,\ntrứng non ngậy và hành phi.")

# Draw Inactive Right Card (Card 1: Cơm Gỏi Gà Xé)
draw_card(desk_bg, stage_center_x + 300, stage_center_y + 15, 260, 370, False,
          im_dish2, "CƠM GỎI GÀ XÉ", "52.000₫", "Cơm nghệ thơm ngọt nước luộc gà,\ngỏi gà xé chua ngọt bắp cải.")

# Draw ACTIVE Center Card (Card 0: Bánh Canh Gà Đặc Biệt)
draw_card(desk_bg, stage_center_x, stage_center_y - 20, 305, 430, True,
          im_dish1, "BÁNH CANH GÀ ĐẶC BIỆT", "70.000₫", "Thịt gà da vàng giòn mọng nước,\ntrứng non béo ngậy lòng đào.\nNước dùng ninh xương thanh ngọt.")

# 3. NAVIGATION ARROWS
arrow_y = stage_center_y - 20
# Left Arrow
ax_l = stage_center_x - 305 // 2 - 45
draw.ellipse([ax_l - 20, arrow_y - 20, ax_l + 20, arrow_y + 20], fill=(255, 255, 255), outline=(216, 195, 165), width=1)
draw.polygon([(ax_l + 4, arrow_y - 8), (ax_l - 6, arrow_y), (ax_l + 4, arrow_y + 8)], fill=(36, 22, 16))

# Right Arrow
ax_r = stage_center_x + 305 // 2 + 45
draw.ellipse([ax_r - 20, arrow_y - 20, ax_r + 20, arrow_y + 20], fill=(255, 255, 255), outline=(216, 195, 165), width=1)
draw.polygon([(ax_r - 4, arrow_y - 8), (ax_r + 6, arrow_y), (ax_r - 4, arrow_y + 8)], fill=(36, 22, 16))

# 4. PAGINATION DOTS
dot_y = stage_center_y + 225
dots_w = 4 * 14 + 16
start_dot_x = stage_center_x - dots_w // 2

# Dot 0: active (wide pill)
draw.rounded_rectangle([start_dot_x, dot_y, start_dot_x + 26, dot_y + 9], radius=5, fill=(158, 94, 43))
# Dots 1, 2, 3: inactive circles
for i in range(1, 4):
    dx = start_dot_x + 26 + 10 + (i - 1) * 18
    draw.ellipse([dx, dot_y, dx + 9, dot_y + 9], fill=(216, 195, 165))

# 5. FOOTER BAR
fy = DH - 85
draw.line([(stage_center_x - 380, fy), (stage_center_x + 380, fy)], fill=(225, 218, 210), width=1)
draw.text((stage_center_x - 380, fy + 14), "Đặt Giao Tận Nơi • Hotline", fill=(140, 122, 112), font=f_footer_label)
draw.text((stage_center_x - 380, fy + 28), "090 642 79 38", fill=(17, 17, 17), font=f_footer_phone)
draw.text((stage_center_x - 380, fy + 50), "Phục vụ: 06:00 – 23:00 hàng ngày", fill=(102, 85, 77), font=f_footer_label)

# View All Button
btn_w, btn_h = 220, 42
bx = stage_center_x + 380 - btn_w
draw.rounded_rectangle([bx, fy + 20, bx + btn_w, fy + 20 + btn_h], radius=21, fill=(17, 17, 17))
draw.text((bx + 26, fy + 32), "Xem Toàn Bộ Thực Đơn  →", fill=(255, 255, 255), font=f_footer_btn)

out_path = os.path.join(ARTIFACT_DIR, 'proof_menu_3d_focus_slider.png')
desk_bg.save(out_path)
print(f'Saved proof: {out_path}')
