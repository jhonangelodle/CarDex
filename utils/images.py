import os
from PIL import Image
from datetime import datetime

IMG_DIR = "saved_cars"


# -----------------------------
# Image Directory Setup
# -----------------------------
def init_img_dir():
    """Create the image directory if it doesn't exist."""
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)


# -----------------------------
# Save Uploaded Image
# -----------------------------
def save_uploaded_image(uploaded_file):
    """
    Saves an uploaded image to the saved_cars directory.
    Automatically resizes large images and preserves file extension.
    """
    init_img_dir()

    # Get extension
    ext = uploaded_file.name.split(".")[-1].lower()
    if ext not in ["jpg", "jpeg", "png"]:
        ext = "jpg"

    # Create unique filename
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.{ext}"
    path = os.path.join(IMG_DIR, filename)

    # Resize and save
    img = Image.open(uploaded_file)
    img.thumbnail((1400, 1400))  # Prevent huge files
    img.save(path)

    return path


# -----------------------------
# Delete Image
# -----------------------------
def delete_image(path):
    """Deletes an image file if it exists."""
    if path and os.path.exists(path):
        os.remove(path)
