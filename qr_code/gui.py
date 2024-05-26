import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox, ttk, simpledialog
from PIL import Image, ImageTk, ImageFont, ImageDraw
from qr_code.qr_code_utils.color_utils import choose_fill_color, choose_bg_color
from qr_code.qr_code_utils.logo_utils import choose_logo, add_logo
from qr_code.qr_code_utils.export_utils import export_to_file
from qr_code.qr_code_utils.round_utils import round_qr_cells
from qr_code.qr_code_utils.watermark_utils import add_watermark
from qr_code.qr_code_utils.gradient_utils import apply_gradient
from qr_code.qr_code_utils.error_correction_utils import get_error_correction_map
from qr_code.qr_code_utils.data_utils import get_default_data
from qr_code.qr_code_utils.border_utils import get_border_width
from qr_code.qr_code_utils.size_utils import get_size
from qr_code.qr_code_utils.shape_utils import get_shape
from qr_code.qr_code_utils.save_settings_utils import save_settings
from qr_code.qr_code_utils.load_settings_utils import load_settings
import qrcode

def create_qr_code(data, fill_color, bg_color, gradient_color, size, border_width, error_correction, transparent_bg, shape, logo_path, watermark, watermark_size):
    error_correction_map = get_error_correction_map()
    
    qr = qrcode.QRCode(version=1, error_correction=error_correction_map[error_correction], box_size=int(size), border=int(border_width))
    qr.add_data(data)
    qr.make(fit=True)
    
    if transparent_bg:
        img = qr.make_image(fill_color=fill_color, back_color=None).convert('RGBA')
        new_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
        new_img.paste(img, (0, 0), img)
        img = new_img
    else:
        img = qr.make_image(fill_color=fill_color, back_color=bg_color).convert('RGBA')
    
    if gradient_color:
        img = apply_gradient(img, fill_color, gradient_color)
    
    if logo_path:
        img = add_logo(img, logo_path)
    
    if watermark:
        img = add_watermark(img, watermark, fill_color, watermark_size)
    
    if shape == 'Round':
        img = round_qr_cells(img)
    
    return img

def run_app():
    def update_qr_preview(*args):
        data = entry_data.get()
        fill_color = fill_color_var.get()
        bg_color = bg_color_var.get() if not transparent_bg_var.get() else None
        gradient_color = gradient_color_var.get()
        size = size_var.get()
        border_width = border_width_var.get()
        error_correction = error_correction_var.get()
        transparent_bg = transparent_bg_var.get()
        shape = shape_var.get()
        logo_path = logo_path_var.get()
        watermark = watermark_var.get()
        watermark_size = watermark_size_var.get()
        
        img = create_qr_code(data, fill_color, bg_color, gradient_color, size, border_width, error_correction, transparent_bg, shape, logo_path, watermark, watermark_size)
        
        img_tk = ImageTk.PhotoImage(img)
        qr_preview_label.config(image=img_tk)
        qr_preview_label.image = img_tk

    root = tk.Tk()
    root.title("QR Code Generator")

    left_frame = ttk.Frame(root, padding="10")
    left_frame.grid(row=0, column=0, sticky="nsew")

    right_frame = ttk.Frame(root, padding="10")
    right_frame.grid(row=0, column=1, sticky="nsew")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

    entry_data = ttk.Entry(left_frame)
    entry_data.grid(row=0, column=0, columnspan=2, pady=5)

    fill_color_var = tk.StringVar(value="#000000")
    ttk.Button(left_frame, text="Fill Color", command=lambda: choose_fill_color(fill_color_var)).grid(row=1, column=0, columnspan=2, pady=5)

    bg_color_var = tk.StringVar(value="#FFFFFF")
    ttk.Button(left_frame, text="Background Color", command=lambda: choose_bg_color(bg_color_var)).grid(row=2, column=0, columnspan=2, pady=5)

    transparent_bg_var = tk.BooleanVar()
    ttk.Checkbutton(left_frame, text="Transparent Background", variable=transparent_bg_var, command=update_qr_preview).grid(row=3, column=0, columnspan=2, pady=5)

    gradient_color_var = tk.StringVar(value="")
    ttk.Button(left_frame, text="Gradient Color", command=lambda: colorchooser.askcolor(title="Choose Gradient Color", color=gradient_color_var.get())[1]).grid(row=4, column=0, columnspan=2, pady=5)

    logo_path_var = tk.StringVar(value="")
    ttk.Button(left_frame, text="Choose Logo", command=lambda: choose_logo(logo_path_var)).grid(row=5, column=0, columnspan=2, pady=5)

    watermark_var = tk.StringVar(value="")
    ttk.Button(left_frame, text="Watermark", command=lambda: watermark_var.set(simpledialog.askstring("Watermark", "Enter Watermark Text"))).grid(row=6, column=0, columnspan=2, pady=5)

    watermark_size_var = tk.DoubleVar(value=0.1)
    ttk.Label(left_frame, text="Watermark Size").grid(row=7, column=0, columnspan=2)
    watermark_size_menu = ttk.OptionMenu(left_frame, watermark_size_var, '0.1', '0.1', '0.2', '0.3', '0.4', '0.5')
    watermark_size_menu.grid(row=8, column=0, columnspan=2, pady=5)

    error_correction_var = tk.StringVar(value="L")
    ttk.Label(left_frame, text="Error Correction").grid(row=9, column=0, columnspan=2)
    error_correction_menu = ttk.OptionMenu(left_frame, error_correction_var, 'L', 'L', 'M', 'Q', 'H')
    error_correction_menu.grid(row=10, column=0, columnspan=2, pady=5)

    size_var = tk.DoubleVar(value=10)
    ttk.Label(left_frame, text="Size").grid(row=11, column=0, columnspan=2)
    ttk.Entry(left_frame, textvariable=size_var).grid(row=12, column=0, columnspan=2, pady=5)

    border_width_var = tk.DoubleVar(value=4)
    ttk.Label(left_frame, text="Border Width").grid(row=13, column=0, columnspan=2)
    ttk.Entry(left_frame, textvariable=border_width_var).grid(row=14, column=0, columnspan=2, pady=5)

    shape_var = tk.StringVar(value="Square")
    ttk.Label(left_frame, text="Shape").grid(row=15, column=0, columnspan=2)
    shape_menu = ttk.OptionMenu(left_frame, shape_var, 'Square', 'Square', 'Round')
    shape_menu.grid(row=16, column=0, columnspan=2, pady=5)

    file_type_var = tk.StringVar(value="PNG")
    ttk.Label(left_frame, text="File Type").grid(row=17, column=0, columnspan=2)
    file_type_menu = ttk.OptionMenu(left_frame, file_type_var, 'PNG', 'PNG', 'JPG', 'BMP')
    file_type_menu.grid(row=18, column=0, columnspan=2, pady=5)

    ttk.Button(left_frame, text="Save QR Code", command=save_qr_code).grid(row=19, column=0, columnspan=2, pady=5)
    ttk.Button(left_frame, text="Save Settings", command=lambda: save_settings(entry_data, fill_color_var, bg_color_var, gradient_color_var, logo_path_var, transparent_bg_var, file_type_var, shape_var, error_correction_var, size_var, border_width_var)).grid(row=20, column=0, pady=5, sticky="w")
    ttk.Button(left_frame, text="Load Settings", command=lambda: load_settings(filedialog, entry_data, fill_color_var, bg_color_var, gradient_color_var, logo_path_var, transparent_bg_var, file_type_var, shape_var, error_correction_var, size_var, border_width_var, update_qr_preview)).grid(row=20, column=1, pady=5, sticky="e")

    qr_preview_label = ttk.Label(right_frame, borderwidth=2, relief="groove")
    qr_preview_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    size_label = ttk.Label(right_frame, text="")
    size_label.pack()

    entry_data.bind("<KeyRelease>", update_qr_preview)
    fill_color_var.trace_add("write", update_qr_preview)
    bg_color_var.trace_add("write", update_qr_preview)
    gradient_color_var.trace_add("write", update_qr_preview)
    logo_path_var.trace_add("write", update_qr_preview)
    transparent_bg_var.trace_add("write", update_qr_preview)
    file_type_var.trace_add("write", update_qr_preview)
    shape_var.trace_add("write", update_qr_preview)
    error_correction_var.trace_add("write", update_qr_preview)
    size_var.trace_add("write", update_qr_preview)
    border_width_var.trace_add("write", update_qr_preview)
    watermark_var.trace_add("write", update_qr_preview)
    watermark_size_var.trace_add("write", update_qr_preview)

    update_qr_preview()
    root.mainloop()

if __name__ == "__main__":
    run_app()
