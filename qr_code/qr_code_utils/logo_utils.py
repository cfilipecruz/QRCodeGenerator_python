from PIL import Image

def add_logo(img, logo_path):
    try:
        logo = Image.open(logo_path)
        if logo.format != 'PNG':
            raise ValueError("Only PNG logos are supported.")
        if logo.width > 500 or logo.height > 500:
            raise ValueError("Logo size must be less than 500px.")
        basewidth = img.size[0] // 4
        wpercent = (basewidth / float(logo.size[0]))
        hsize = int((float(logo.size[1]) * float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.LANCZOS)
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos, logo)
    except Exception as e:
        raise Exception(f"Error adding logo: {e}")
    return img

def choose_logo(filedialog, logo_path_var):
    logo_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if logo_path:
        logo_path_var.set(logo_path)
