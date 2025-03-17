from PIL import Image
import os

images = ['AG20brn1.tif',
 'AG20flw1_a.tif',
 'AG20flw2_r.tif',
 'AG20frt3_a.tif',
 'AG20lef2_a.tif',
 'AG20brn2.tif',
 'AG20flw1_r.tif',
 'AG20frt1.tif',
 'AG20lef1.tif',
 'AG20lef3.tif',
 'AG20brn3.tif',
 'AG20flw2.tif',
 'AG20frt2.tif',
 'AG20lef1_a.tif',
 'AG20lef3_a.tif',
 'AG20flw1.tif',
 'AG20flw2_a.tif',
 'AG20frt3.tif',
 'AG20lef2.tif'
]

for image_png in images:
    im = Image.open(image_png)
    print(im.mode)
    fig = im.convert('RGB')
    fig.save(os.path.splitext(image_png)[0]+'.bmp')