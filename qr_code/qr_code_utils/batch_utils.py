 
def save_batch_qr_codes(simpledialog, entry_data, update_qr_preview, save_qr_code):
    batch_data = simpledialog.askstring("Batch Data", "Enter data for each QR code separated by commas:")
    if batch_data:
        data_list = batch_data.split(',')
        for data in data_list:
            entry_data.delete(0, tk.END)
            entry_data.insert(0, data)
            update_qr_preview()
            save_qr_code()
