 
from PIL import Image

def apply_gradient(img, fill_color, bg_color):
    width, height = img.size
    base = Image.new('RGBA', img.size, bg_color)
    for y in range(height):
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            base.putpixel((x, y), (int(r * y / height), int(g * y / height), int(b * y / height), a))
    return base
