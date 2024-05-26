from PIL import Image, ImageDraw, ImageFont

def add_watermark(img, watermark, fill_color, watermark_size):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font_size = int(height * watermark_size)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), watermark, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), watermark, fill=fill_color, font=font)
    return img
