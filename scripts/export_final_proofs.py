import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.getcwd()
CLAW_TOP_PATH = os.path.join(ROOT, 'images', 'order', 'rooster_claw_top.webp')
CLAW_MID_PATH = os.path.join(ROOT, 'images', 'order', 'rooster_claw_mid.webp')
BOARD_PATH = os.path.join(ROOT, 'images', 'order', 'clipboard_board_only.webp')
BODY_PATH = os.path.join(ROOT, 'images', 'order', 'rooster_mascot_body_opt.webp')

# 1. Composite of Stage (Rooster + Board + Claws)
body = Image.open(BODY_PATH).convert('RGBA')
board = Image.open(BOARD_PATH).convert('RGBA')
top_claw = Image.open(CLAW_TOP_PATH).convert('RGBA')
mid_claw = Image.open(CLAW_MID_PATH).convert('RGBA')

canvas_w, canvas_h = 1000, 750
stage = Image.new('RGBA', (canvas_w, canvas_h), (245, 240, 232, 255))

# Mascot Body
bw = 550
bh = int(bw * body.height / body.width)
b_sc = body.resize((bw, bh), Image.Resampling.LANCZOS)
stage.paste(b_sc, (0, 10), b_sc)

# Board at left: 190, top: 110
board_w, board_h = 630, 455
board_sc = board.resize((board_w, board_h), Image.Resampling.LANCZOS)
stage.paste(board_sc, (190, 110), board_sc)

# Top Claw at left: 190 + 112 = 302, top: 110 - 14 = 96
cw_t = 62
ch_t = int(cw_t * top_claw.height / top_claw.width)
tc_sc = top_claw.resize((cw_t, ch_t), Image.Resampling.LANCZOS)
stage.paste(tc_sc, (190 + 112, 110 - 14), tc_sc)

# Mid Claw at left: 190 - 12 = 178, top: 110 + 154 = 264
cw_m = 38
ch_m = int(cw_m * mid_claw.height / mid_claw.width)
mc_sc = mid_claw.resize((cw_m, ch_m), Image.Resampling.LANCZOS)
stage.paste(mc_sc, (190 - 12, 110 + 154), mc_sc)

stage.save('proof_stage_full.png')
print('-> Exported proof_stage_full.png')

# 2. Closeups of Both Claws
# Top Claw Closeup
crop_top = stage.crop((190 + 70, 110 - 35, 190 + 220, 110 + 75))
crop_top.save('proof_claw_top_closeup.png')

# Mid Claw Closeup
crop_mid = stage.crop((190 - 45, 110 + 120, 190 + 65, 110 + 250))
crop_mid.save('proof_claw_mid_closeup.png')

print('-> Exported proof_claw_top_closeup.png and proof_claw_mid_closeup.png')
