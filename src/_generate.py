#!/usr/bin/env python3

"""
Generate images with less opacity from the original image.
"""

from PIL import Image

path = "subpacks/{}/textures/misc/pumpkinblur.png"
solid = Image.open(path.format(100))

for opacity in range(0, 100, 20):
    opacity /= 100
    print(f"generating image for {opacity:.0%} opacity")
    im = solid.copy()
    im.putalpha(round(255 * opacity))
    im.save(path.format(round(opacity * 100)))

