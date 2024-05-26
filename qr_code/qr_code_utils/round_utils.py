 
from PIL import Image, ImageDraw

def round_qr_cells(img):
    width, height = img.size
    new_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(new_img)

    for x in range(0, width, 10):
        for y in range(0, height, 10):
            bbox = (x, y, x + 10, y + 10)
            cell = img.crop(bbox)
            if cell.getbbox():
                draw.ellipse(bbox, fill=cell.getpixel((5, 5)))

    return new_img
