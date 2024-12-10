import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from blog.models import Category
from django.conf import settings

class CategoryModelTest(TestCase):
    def setUp(self):
        # Create a temporary image for testing
        self.test_image_path = os.path.join(settings.MEDIA_ROOT, 'test_image.jpg')
        with open(self.test_image_path, 'wb') as f:
            f.write(b'\x00\x00\x00')  # Writing some bytes to simulate an image

        # Create a category instance for testing
        self.category = Category.objects.create(
            name="Test Category",
            description="This is a test category",
            featured_image=SimpleUploadedFile(
                name='test_image.jpg',
                content=open(self.test_image_path, 'rb').read(),
                content_type='image/jpeg'
            )
        )

    def test_image_renaming_and_format_conversion(self):
        """
        Test if the image is renamed to match the category name and converted to WebP format.
        """
        # Check that the image name is updated to the slug format
        expected_filename = f"{self.category.slug}.webp"
        self.assertTrue(self.category.featured_image.name.endswith(expected_filename))

        # Check if the image is saved as WebP
        converted_image_path = os.path.join(settings.MEDIA_ROOT, self.category.featured_image.name)
        self.assertTrue(os.path.exists(converted_image_path))
        self.assertTrue(converted_image_path.endswith('.webp'))

    def test_image_resizing(self):
        """
        Test if the image is resized to the defined maximum dimensions.
        """
        # Load the saved image and check its dimensions
        from PIL import Image
        converted_image_path = os.path.join(settings.MEDIA_ROOT, self.category.featured_image.name)
        with Image.open(converted_image_path) as img:
            self.assertLessEqual(img.width, 800)
            self.assertLessEqual(img.height, 800)

    def tearDown(self):
        """
        Clean up files after tests.
        """
        # Remove the original test image
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

        # Remove the processed image
        processed_image_path = os.path.join(settings.MEDIA_ROOT, self.category.featured_image.name)
        if os.path.exists(processed_image_path):
            os.remove(processed_image_path)
