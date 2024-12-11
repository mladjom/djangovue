# utils/image_utils.py

from PIL import Image
from django.conf import settings

def resize_and_compress_image(image_path, new_image_path, max_size=(800, 800), quality=85):
    """
    Resizes, compresses, renames, and converts an image to WebP format.

    Args:
        image_path (str): Path to the original image file.
        new_image_path (str): Path where the new image will be saved.
        max_size (tuple): Maximum dimensions for resizing (width, height).
        quality (int): Quality for compression (1-100).
    """
    try:
        print(f"Processing image: {image_path}")  # Debug print

        # Open the image file from the path
        with Image.open(image_path) as img:
            # Debug original dimensions
            print(f"Original dimensions: {img.size}")

            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Resize the image while maintaining the aspect ratio
            img.thumbnail(max_size, Image.LANCZOS)

            # Debug resized dimensions
            print(f"Resized dimensions: {img.size}")

            # Save as WebP format with the specified quality
            img.save(new_image_path, format='WEBP', quality=quality)
            print(f"Image saved successfully: {new_image_path}")

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
