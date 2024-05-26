 
def get_default_data(entry_data):
    data = entry_data.get()
    if not data:
        data = "www.myskillhub.pt"
    return data
