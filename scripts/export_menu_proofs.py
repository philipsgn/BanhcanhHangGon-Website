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

# 1. Desktop Render (1200 x 1560) - Compact & Centered
DW, DH = 1200, 1560
desk_bg = Image.new('RGB', (DW, DH), (250, 248, 245))
draw = ImageDraw.Draw(desk_bg)

try:
    f_dish_title = ImageFont.truetype('arialbd.ttf', 21)
    f_dish_desc = ImageFont.truetype('arial.ttf', 13)
    f_price = ImageFont.truetype('arialbd.ttf', 14)
    f_btn = ImageFont.truetype('arialbd.ttf', 12)
    f_footer_label = ImageFont.truetype('arial.ttf', 12)
    f_footer_phone = ImageFont.truetype('arialbd.ttf', 16)
    f_footer_btn = ImageFont.truetype('arialbd.ttf', 13.5)
except:
    f_dish_title = f_dish_desc = f_price = f_btn = f_footer_label = f_footer_phone = f_footer_btn = ImageFont.load_default()

# --- HERO HEADER: CENTERED ROOSTER + BOARD (NO EXTERNAL TEXT) ---
# Ropes reach y=0 directly!
rw = 480
rh = int(rw * im_rooster.height / im_rooster.width)
rooster_s = im_rooster.resize((rw, rh), Image.Resampling.LANCZOS)
rx = (DW - rw) // 2
desk_bg.paste(rooster_s, (rx, 0), rooster_s)

# --- 4 ZIGZAG DISHES (COMPACT 940px CONTAINER) ---
dishes = [
    {
        'title': 'BÁNH CANH GÀ ĐẶC BIỆT',
        'price': '70K',
        'desc': 'Tô bánh canh đầy đặn với từng lát thịt gà ta da vàng ươm mọng nước,\ntrứng non lòng đào béo ngậy, tim mề giòn sần sật. Nước dùng ninh từ xương gà tươi\nngọt thanh, thơm nồng tiêu sọ rang và hành phi giòn rụm.',
        'img': im_dish1,
        'reverse': False
    },
    {
        'title': 'CƠM GỎI GÀ XÉ',
        'price': '52K',
        'desc': 'Hạt cơm vàng óng ánh màu nghệ tươi nấu từ nước luộc gà béo ngọt, ăn cùng\nđĩa gỏi gà xé chua ngọt bắp cải giòn sần sật, rau răm cay the. Kèm chén nước mắm gừng\ngia truyền thơm lừng và súp gà nóng hổi.',
        'img': im_dish2,
        'reverse': True
    },
    {
        'title': 'GỎI GÀ TA BẮP CHUỐI',
        'price': '50K',
        'desc': 'Thịt gà ta thả vườn dai ngọt xé phay trộn cùng bắp chuối bào giòn sần sật,\nhành tây thanh mát, rau răm và đậu phộng rang củi béo bùi. Nước sốt chua ngọt\nđậm đà đánh thức mọi giác quan.',
        'img': im_dish3,
        'reverse': False
    },
    {
        'title': 'XÔI GÀ TRỨNG NON',
        'price': '40K',
        'desc': 'Xôi nếp nương đồ chín dẻo quánh, thoang thoảng mỡ gà thơm phức, đẫy đà\nthịt gà xé chắc ngọt, chùm trứng non vàng ngậy béo bùi và hành phi giòn tan.\nĐậm đà từng thìa xôi quê ấm bụng.',
        'img': im_dish4,
        'reverse': True
    }
]

container_w = 940
cx_start = (DW - container_w) // 2
start_y = rh + 16
row_gap = 210

plate_size = 230

for idx, d in enumerate(dishes):
    y_pos = start_y + idx * row_gap
    
    # Scale plate image
    p_img = d['img'].resize((plate_size, plate_size), Image.Resampling.LANCZOS)
    
    if not d['reverse']:
        # Text on Left, Plate on Right
        tx = cx_start
        # Title + Price Badge
        draw.text((tx, y_pos), d['title'], fill=(17, 17, 17), font=f_dish_title)
        tb = draw.textbbox((tx, y_pos), d['title'], font=f_dish_title)
        # Price badge circle
        bx = tb[2] + 14
        by = y_pos + 1
        draw.ellipse([bx, by, bx + 36, by + 36], fill=(17, 17, 17))
        draw.text((bx + 6, by + 9), d['price'], fill=(255, 255, 255), font=f_price)
        
        # Desc
        draw.text((tx, y_pos + 38), d['desc'], fill=(85, 68, 59), font=f_dish_desc)
        
        # Accent line
        draw.line([(tx, y_pos + 104), (tx + 220, y_pos + 104)], fill=(34, 34, 34), width=1)
        
        # Order button pill
        draw.rounded_rectangle([tx, y_pos + 116, tx + 120, y_pos + 146], radius=15, outline=(196, 142, 89), width=1)
        draw.text((tx + 16, y_pos + 123), "+ Đặt Món Ngay", fill=(158, 94, 43), font=f_btn)
        
        # Plate visual
        px = cx_start + container_w - plate_size
        desk_bg.paste(p_img, (px, y_pos - 15), p_img)
    else:
        # Plate on Left, Text on Right (Reverse)
        px = cx_start
        desk_bg.paste(p_img, (px, y_pos - 15), p_img)
        
        tx = cx_start + plate_size + 38
        # Title + Price Badge
        draw.text((tx, y_pos), d['title'], fill=(17, 17, 17), font=f_dish_title)
        tb = draw.textbbox((tx, y_pos), d['title'], font=f_dish_title)
        # Price badge circle
        bx = tb[2] + 14
        by = y_pos + 1
        draw.ellipse([bx, by, bx + 36, by + 36], fill=(17, 17, 17))
        draw.text((bx + 6, by + 9), d['price'], fill=(255, 255, 255), font=f_price)
        
        # Desc
        draw.text((tx, y_pos + 38), d['desc'], fill=(85, 68, 59), font=f_dish_desc)
        
        # Accent line
        draw.line([(tx, y_pos + 104), (tx + 220, y_pos + 104)], fill=(34, 34, 34), width=1)
        
        # Order button pill
        draw.rounded_rectangle([tx, y_pos + 116, tx + 120, y_pos + 146], radius=15, outline=(196, 142, 89), width=1)
        draw.text((tx + 16, y_pos + 123), "+ Đặt Món Ngay", fill=(158, 94, 43), font=f_btn)

# --- FOOTER BAR ---
fy = start_y + 4 * row_gap + 20
draw.line([(cx_start, fy), (cx_start + container_w, fy)], fill=(225, 218, 210), width=1)
draw.text((cx_start, fy + 18), "Đặt Giao Tận Nơi • Hotline", fill=(136, 136, 136), font=f_footer_label)
draw.text((cx_start, fy + 36), "090 642 79 38", fill=(17, 17, 17), font=f_footer_phone)
draw.text((cx_start, fy + 60), "Phục vụ: 06:00 – 23:00 hàng ngày", fill=(102, 102, 102), font=f_footer_label)

# View all button
btn_w, btn_h = 240, 48
bx = cx_start + container_w - btn_w
draw.rounded_rectangle([bx, fy + 24, bx + btn_w, fy + 24 + btn_h], radius=24, fill=(17, 17, 17))
draw.text((bx + 34, fy + 38), "Xem Toàn Bộ Thực Đơn  →", fill=(255, 255, 255), font=f_footer_btn)

out_desk = os.path.join(ARTIFACT_DIR, 'proof_menu_compact_centered_desktop.png')
desk_bg.save(out_desk)
print(f'Saved proof: {out_desk}')
