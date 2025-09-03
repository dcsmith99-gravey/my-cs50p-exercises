import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

before = sys.argv[1]
after = sys.argv[2]

ext1 = os.path.splitext(before)[1].lower()
ext2 = os.path.splitext(after)[1].lower()

if not before.lower().endswith((".png",".jpg",".jpeg")):
    sys.exit("Invalid input")

if not after.lower().endswith((".png",".jpg",".jpeg")):
    sys.exit("Invalid output")

if ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(before) as photo, Image.open("shirt.png") as shirt:
        photo = ImageOps.fit(photo, shirt.size)
        photo.paste(shirt, shirt)
        photo.save(after)

except FileNotFoundError:
    sys.exit("Input does not exist")
