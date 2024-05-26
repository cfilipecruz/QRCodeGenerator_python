 
import json

def save_settings(entry_data, fill_color_var, bg_color_var, logo_path_var, transparent_bg_var, file_type_var, shape_var, error_correction_var, size_var, border_width_var):
    settings = {
        "data": entry_data.get(),
        "fill_color": fill_color_var.get(),
        "bg_color": bg_color_var.get(),
        "logo_path": logo_path_var.get(),
        "transparent_bg": transparent_bg_var.get(),
        "file_type": file_type_var.get(),
        "shape": shape_var.get(),
        "error_correction": error_correction_var.get(),
        "size": size_var.get(),
        "border_width": border_width_var.get()
    }
    settings_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if settings_file:
        with open(settings_file, 'w') as f:
            json.dump(settings, f)
