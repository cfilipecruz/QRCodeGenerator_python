 
def toggle_dark_mode(style, dark_mode_var):
    if dark_mode_var.get():
        style.theme_use('alt')
    else:
        style.theme_use('clam')
