 
from reportlab.pdfgen import canvas
import os

def export_to_file(img, file_path, file_type):
    if file_type == 'PNG':
        img.save(file_path)
    elif file_type == 'JPEG':
        img.convert('RGB').save(file_path, 'JPEG')
    elif file_type == 'BMP':
        img.convert('RGB').save(file_path, 'BMP')
    elif file_type == 'PDF':
        c = canvas.Canvas(file_path)
        img.save("temp_qr.png")
        c.drawImage("temp_qr.png", 100, 500, width=200, height=200)
        c.save()
        os.remove("temp_qr.png")
