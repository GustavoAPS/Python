import numpy as np
from PIL import Image

# load image
image = Image.open('images_to_watermark/lake_in_fall.jpg')
watermark_stamp = Image.open('watermark_stamps/squares_stamp.png')

# converting image to array
pix = np.array(image)
pix_stamp = np.array(watermark_stamp)

# ! this value of 64 ,must be changed according to stamp size
for m in range(0, 64):
    for n in range(0, 64):
        if(pix_stamp[m, n, 0] > 0) or (pix_stamp[m, n, 1] > 0) or (pix_stamp[m, n, 2] > 0):
            pix[m, n, 0] = pix_stamp[m, n, 0]  # 0 accesses the first channel
            pix[m, n, 1] = pix_stamp[m, n, 1]  # 1 accesses the second channel
            pix[m, n, 2] = pix_stamp[m, n, 2]  # 2 accesses the third channel

Image.fromarray(pix).save("images_watermarked/lake_in_fall.jpg")
