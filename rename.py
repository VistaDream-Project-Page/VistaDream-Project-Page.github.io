import os
import numpy as np
from PIL import Image
from glob import glob

files = ['bathroom','lavender','kitchen','fall','kitchen1','seaside','barn','sd_bedroom','sd_livingroom',
         'sd_readingroom','sd_garden','anstronaut','living_room','victorian','steampunk','bedroom1','bedroom3','bathroom1',
         'computer','piano','dragon','sd_babyroom','tunnel','sd_garage',
         'conference','car','wukong','bear','ocean','bust']

# for file in files:
#     fn = str.split(file,'/')[-1]
#     fn = str.split(fn,'.')[0]
#     image = np.array(Image.open(f'visual/thumbnails/{fn}.png'))
#     H,W = image.shape[0:2]
#     W = int(W*72/H)
#     format1 = f'<span class="pill scene-pill" data-value="{fn}" onclick="selectCompVideo(activeMethodPill, this, 3)">'
#     format2 = f'    <img class="thumbnail-img" src="visual/thumbnails/{fn}.png" alt="{fn}" width="{W}">'
#     format3 = f'</span>'
#     print(format1)
#     print(format2)
#     print(format3)

# for file in files:
#     fn = str.split(file,'/')[-1]
#     fn = str.split(fn,'.')[0]
#     image = np.array(Image.open(f'visual/thumbnails/{fn}.png'))
#     H,W = image.shape[0:2]
#     W = int(W*72/H)
#     format1 = f'<span class="pill scene-pill" data-value="{fn}" onclick="selectC2Fvideos(activeMethodPill, this, 3)">'
#     format2 = f'    <img class="thumbnail-img" src="visual/thumbnails/{fn}.png" alt=fn width="{W}">'
#     format3 = f'</span>'
#     print(format1)
#     print(format2)
#     print(format3)   

for file in files:
    fn = str.split(file,'/')[-1]
    fn = str.split(fn,'.')[0]
    image = np.array(Image.open(f'visual/thumbnails/{fn}.png'))
    H,W = image.shape[0:2]
    W = int(W*72/H)
    format1 = f'<span class="pill scene-pill" data-value="{fn}" onclick="selectRGBDvideos(activeMethodPill, this, 3)">'
    format2 = f'    <img class="thumbnail-img" src="visual/thumbnails/{fn}.png" alt=fn width="{W}">'
    format3 = f'</span>'
    print(format1)
    print(format2)
    print(format3)   


# files = ['bathroom','lavender','kitchen','fall','kitchen1','seaside','barn','sd_bedroom','sd_livingroom',
#          'sd_readingroom','sd_garden','anstronaut','living_room','victorian','steampunk','bedroom1','bedroom3','bathroom1',
#          'computer','piano','dragon','sd_babyroom','tunnel','sd_garage',
#          'conference','car','wukong','bear','ocean','bust']
# print(len(files))
# for i,file in enumerate(files):
#     fn = str.split(file,'/')[-1]
#     fn = str.split(fn,'.')[0]
    
#     image = np.array(Image.open(f'visual/thumbnails/{fn}.png'))
#     H,W = image.shape[0:2]
#     W = int(W*72/H)
    
#     print(f'<span class="pill scene-pill" data-value="{fn}" onclick="selectiframe(this)">')
#     print(f'    <img class="thumbnail-img" src="visual/thumbnails/{fn}.png" alt="{fn}" width="{W}">')
#     print(f'</span>')
 