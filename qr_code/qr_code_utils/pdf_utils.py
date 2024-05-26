 
from reportlab.pdfgen import canvas
import os

def save_pdf_with_qr_code(filedialog, entry_data, fill_color_var, bg_color_var, logo_path_var, transparent_bg_var, shape_var, error_correction_var, size_var, border_width_var, watermark_var, gradient_color_var, create_qr_code):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        data = entry_data.get()
        if not data:
            data = "www.myskillhub.pt"

        fill_color = fill_color_var.get()
        bg_color = bg_color_var.get()
        logo_path = logo_path_var.get()
        transparent_bg = transparent_bg_var.get()
        shape = shape_var.get()
        error_correction = error_correction_var.get()
        size = size_var.get()
        border_width = border_width_var.get()
        watermark = watermark_var.get()
        gradient_color = gradient_color_var.get()

        img = create_qr_code(data, fill_color, bg_color, size, border_width, error_correction, transparent_bg, gradient_color, shape, logo_path, watermark)

        c = canvas.Canvas(file_path)
        img.save("temp_qr.png")
        c.drawImage("temp_qr.png", 100, 500, width=200, height=200)
        c.save()
        os.remove("temp_qr.png")
