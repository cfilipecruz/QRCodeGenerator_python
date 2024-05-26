 
import json

def load_settings(filedialog, entry_data, fill_color_var, bg_color_var, logo_path_var, transparent_bg_var, file_type_var, shape_var, error_correction_var, size_var, border_width_var, update_qr_preview):
    settings_file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if settings_file:
        with open(settings_file, 'r') as f:
            settings = json.load(f)
            entry_data.delete(0, tk.END)
            entry_data.insert(0, settings.get("data", ""))
            fill_color_var.set(settings.get("fill_color", "black"))
            bg_color_var.set(settings.get("bg_color", "white"))
            logo_path_var.set(settings.get("logo_path", ""))
            transparent_bg_var.set(settings.get("transparent_bg", False))
            file_type_var.set(settings.get("file_type", "PNG"))
            shape_var.set(settings.get("shape", "Square"))
            error_correction_var.set(settings.get("error_correction", "L"))
            size_var.set(settings.get("size", 10))
            border_width_var.set(settings.get("border_width", 4))
            update_qr_preview()
