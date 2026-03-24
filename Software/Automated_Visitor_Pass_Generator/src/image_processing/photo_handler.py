from PIL import Image

def process_photo(photo_path, size, radius):
    img = Image.open(photo_path).convert("RGBA")
    img = img.resize(size)
    # apply rounded corners
    return img
