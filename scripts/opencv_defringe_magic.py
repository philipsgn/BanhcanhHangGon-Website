import sys
sys.stdout.reconfigure(encoding='utf-8')
import cv2
import numpy as np
from PIL import Image

# ==========================================
# 1. PROCESS ROOSTER FOOT BLOCK (THỚT GỖ)
# ==========================================
print('--- 1. Processing Foot Block with OpenCV Defringe ---')
src_pil = Image.open(r'images/order/kê-chân gà.jpg').convert('RGB')
src_rgb = np.array(src_pil)
src_bgr = cv2.cvtColor(src_rgb, cv2.COLOR_RGB2BGR)
H, W = src_bgr.shape[:2]

# Detect background (light grey/white > 215)
b, g, r = src_bgr[:, :, 0], src_bgr[:, :, 1], src_bgr[:, :, 2]
is_bg = (r > 215) & (g > 215) & (b > 215)

raw_mask = np.zeros((H, W), dtype=np.uint8)
raw_mask[~is_bg] = 255

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
closed_mask = cv2.morphologyEx(raw_mask, cv2.MORPH_CLOSE, kernel)

# ERODE 2.5 pixels to strip all white fringe / halo pixels
eroded_mask = cv2.erode(closed_mask, kernel, iterations=2)

# Color Decontamination via Inpainting / Color Bleed:
inpaint_mask = cv2.dilate(eroded_mask, kernel, iterations=4) - eroded_mask
decontaminated_bgr = cv2.inpaint(src_bgr, inpaint_mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)

# Also decontaminate near-edge bright pixels inside eroded_mask using distance transform
dist_block = cv2.distanceTransform(eroded_mask, cv2.DIST_L2, 3)
decontaminated_rgb = cv2.cvtColor(decontaminated_bgr, cv2.COLOR_BGR2RGB)
near_edge_bright_block = (dist_block <= 4) & (np.max(decontaminated_rgb, axis=2) > 180)
# Fill with deep oak wood color
decontaminated_rgb[near_edge_bright_block] = [115, 80, 45]

# Smooth alpha edge
alpha_smooth = cv2.GaussianBlur(eroded_mask, (3, 3), 0.6)
rgba = np.dstack((decontaminated_rgb, alpha_smooth))

coords = np.argwhere(alpha_smooth > 10)
y_min, x_min = coords.min(axis=0)
y_max, x_max = coords.max(axis=0)

cropped_block = rgba[y_min:y_max+1, x_min:x_max+1]
block_pil = Image.fromarray(cropped_block)
block_pil.save('images/order/rooster_foot_block.webp', 'WEBP', quality=95)
print('Foot block saved! Size:', block_pil.size)

# Verify no white halo at the borders
outer_ring = (cropped_block[:, :, 3] > 10) & (cropped_block[:, :, 3] < 240)
if np.any(outer_ring):
    ring_pixels = cropped_block[outer_ring]
    max_brightness = np.max(ring_pixels[:, :3], axis=1)
    white_halo_count = np.sum(max_brightness > 190)
    print(f'Foot block transition pixels: {len(ring_pixels)}, White fringe count: {white_halo_count}')
    assert white_halo_count == 0, 'White halo still detected in foot block!'
print('VERIFIED: 0 white fringe pixels in foot block!')

# ==========================================
# 2. PROCESS CLIPBOARD MENU (720x520)
# ==========================================
print('--- 2. Processing Clipboard Menu with OpenCV Defringe ---')
orig_cb = Image.open('images/order/clipboard_board_only.png').convert('RGBA')

TW, TH = 720, 520

# Top clamp: Y=7 to Y=88
top_clamp_src = orig_cb.crop((7, 7, 685, 88))
top_clamp = top_clamp_src.resize((TW, 75), Image.Resampling.LANCZOS)

# Bottom wood border: Y=850 to Y=868 (pure wood)
bottom_border_src = orig_cb.crop((7, 850, 685, 868))
bottom_border = bottom_border_src.resize((TW, 24), Image.Resampling.LANCZOS)

# Left and right borders:
left_border_src = orig_cb.crop((7, 88, 24, 850))
right_border_src = orig_cb.crop((668, 88, 685, 850))

middle_h = TH - 75 - 24 # 421px
left_border = left_border_src.resize((18, middle_h), Image.Resampling.LANCZOS)
right_border = right_border_src.resize((18, middle_h), Image.Resampling.LANCZOS)

# Paper interior: pure cream
paper_color = (235, 228, 209, 255)
paper = Image.new('RGBA', (TW - 36, middle_h), paper_color)

# Assemble board
new_board = Image.new('RGBA', (TW, TH), (0, 0, 0, 0))
new_board.paste(top_clamp, (0, 0))
new_board.paste(left_border, (0, 75))
new_board.paste(paper, (18, 75))
new_board.paste(right_border, (TW - 18, 75))
new_board.paste(bottom_border, (0, TH - 24))

nb_arr = np.array(new_board)

# High precision rounded corner mask using cv2 (radius 16)
mask_cv = np.zeros((TH, TW), dtype=np.uint8)
cv2.rectangle(mask_cv, (16, 0), (TW - 16, TH), 255, -1)
cv2.rectangle(mask_cv, (0, 16), (TW, TH - 16), 255, -1)
cv2.circle(mask_cv, (16, 16), 16, 255, -1)
cv2.circle(mask_cv, (TW - 16, 16), 16, 255, -1)
cv2.circle(mask_cv, (16, TH - 16), 16, 255, -1)
cv2.circle(mask_cv, (TW - 16, TH - 16), 16, 255, -1)

# Erode mask 2 pixels to strip any outer white fringe
eroded_menu_mask = cv2.erode(mask_cv, kernel, iterations=2)

# Distance transform edge decontamination
dist_menu = cv2.distanceTransform(eroded_menu_mask, cv2.DIST_L2, 3)

wood_rgb = np.array([125, 85, 45], dtype=np.uint8)
# All pixels outside eroded mask:
nb_arr[eroded_menu_mask < 255, :3] = wood_rgb
# All pixels within 6px of boundary that are bright:
near_edge_bright_menu = (dist_menu <= 6) & (np.max(nb_arr[:, :, :3], axis=2) > 170)
nb_arr[near_edge_bright_menu, :3] = wood_rgb

# Top 4 rows, bottom 4 rows, left 4 cols, right 4 cols forced to wood_rgb
nb_arr[:4, :, :3] = wood_rgb
nb_arr[-4:, :, :3] = wood_rgb
nb_arr[:, :4, :3] = wood_rgb
nb_arr[:, -4:, :3] = wood_rgb

# Smooth alpha on the eroded mask
mask_cv_smooth = cv2.GaussianBlur(eroded_menu_mask, (3, 3), 0.6)
nb_arr[:, :, 3] = mask_cv_smooth

final_board = Image.fromarray(nb_arr)
final_board.save('images/order/clipboard_board_only.webp', 'WEBP', quality=95)
print('Clipboard menu saved! Size:', final_board.size)

# Verify no white halo on menu
outer_ring_cb = (nb_arr[:, :, 3] > 10) & (nb_arr[:, :, 3] < 240)
if np.any(outer_ring_cb):
    ring_pixels_cb = nb_arr[outer_ring_cb]
    max_b_cb = np.max(ring_pixels_cb[:, :3], axis=1)
    white_halo_cb = np.sum(max_b_cb > 190) # strict threshold: no bright pixel > 190
    print(f'Menu edge transition pixels: {len(ring_pixels_cb)}, White fringe count: {white_halo_cb}')
    assert white_halo_cb == 0, f'{white_halo_cb} white fringe pixels detected!'
print('VERIFIED: 0 white fringe pixels in clipboard menu!')
print('=====================================================')
print('SUCCESS: ALL OPENCV DEFRINGE TASKS ACHIEVED 100% CLEAN!')
print('=====================================================')
