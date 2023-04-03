#!/usr/bin/env python3

"""
Generate images with less opacity from the original image.
"""

from PIL import Image, ImageOps

STEP = 5

path = "subpacks/{}/textures/misc/pumpkinblur.png"
solid = Image.open(path.format(100))

images = []
for _ in range(STEP):
	images.append(Image.new("RGBA", solid.size))


width, height = solid.size
for w in range(width):
	for h in range(height):
		r, g, b, a = solid.getpixel((w, h))
		for n, image in enumerate(images):
			image.putpixel(
				(w, h),
				(
					r,
					g,
					b,
					round(a * (n / STEP))
				)
			)

for n, image in enumerate(images):
	image.save(path.format(round(n / STEP * 100)))

