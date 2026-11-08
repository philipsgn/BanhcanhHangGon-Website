import os
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

src = 'images/menu/Gà trống mặc trang phục bên bảng gỗ.png'
im = Image.open(src).convert('RGBA')
arr = np.array(im)

# Let's inspect the rooster's left wing/claw:
# In the image:
# The rooster's white sleeve is around x=500..650, y=300..450
# The feathers/wing extend from x=630 to x=830, y=360 to y=600!
# Below the wing is the wooden board.
# The wooden board surface is around x=650..1450, y=320..950.
# Notice: the wing hangs over the top-left portion of the wooden board!
print('Image size:', im.size)

# If we place "THỰC ĐƠN" centered on the wooden board:
# What is the center of the wooden board?
# Board horizontal span: from x ≈ 630 to x ≈ 1470 -> Center x ≈ 1050!
# Board vertical span: from y ≈ 340 to y ≈ 940 -> Center y ≈ 640!
# If text "THỰC ĐƠN" is centered at cx = 1050, cy = 640:
# The text width is ~300px -> x from 900 to 1200!
# Notice that x=900..1200 is completely to the right of the wing (wing ends at x=830)!
# BUT to be 100% compliant with "nằm sau lớp Layer của cánh của gà":
# We can extract the entire rooster (everything that is rooster feathers, head, body, wing) into a foreground layer!
# How?
# In the original image `im`:
# If we keep the rooster's pixels in a separate layer, and paste the text ON the board, and then paste the rooster's wing back ON TOP of the text,
# any overlap will be 100% behind the wing!
print('Testing layer separation...')
