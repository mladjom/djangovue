# blog/tests/utils/test_image.py
import pytest
import os
from django.conf import settings
from blog.models import Category
from blog.utils.image_utils import resize_and_compress_image
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_resize_and_compress_image():
    # Simulate image upload
    image_path = os.path.join(settings.BASE_DIR, 'media', 'categories', '2024', '12', '10', 'test_image.jpg')
    with open(image_path, 'wb') as f:
        f.write(b'fake image data')  # You would replace this with a real image mock if needed
    
    # Get or create the category instance
    category, created = Category.objects.get_or_create(
        name="Test Category", 
        defaults={
            'featured_image': SimpleUploadedFile(
                'test_image.jpg', 
                b'fake image data', 
                content_type='image/jpeg'
            )
        }
    )

    # Paths for original and new image
    original_image_path = os.path.join(settings.MEDIA_ROOT, category.featured_image.name)
    new_image_path = os.path.join(settings.MEDIA_ROOT, 'categories/2024/12/10/test_image.webp')

    # Call the resize and compress function
    resize_and_compress_image(original_image_path, new_image_path)

    # Verify the new image exists and is in the correct format
    assert os.path.exists(new_image_path)
    with Image.open(new_image_path) as img:
        assert img.format == 'WEBP'
        assert img.size[0] <= 800
        assert img.size[1] <= 800

    # Clean up mock files
    os.remove(original_image_path)
    os.remove(new_image_path)
