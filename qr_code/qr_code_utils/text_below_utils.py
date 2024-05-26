from PIL import ImageDraw

def add_text_below(img, text, fill_color):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    bbox = draw.textbbox((0, 0), text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = height - text_height - 10
    draw.text((x, y), text, fill=fill_color)
    return img
