import os
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from datetime import datetime
from django.conf import settings

def category_image_upload_path(instance, filename):
    """
    Generate a dynamic path for uploading category images.
    Includes date for better file organization.
    """
    today = datetime.now().strftime('%Y/%m/%d')  # Example: 2024/12/10
    return f'categories/{today}/{filename}'


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Name')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Description')
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_('Slug'),
    )
    featured_image = models.ImageField(
        _('Featured Image'),
        upload_to=category_image_upload_path,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        _('Created At'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    @staticmethod
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

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

        # Process the featured image if it exists
        if self.featured_image:
            original_image_path = self.featured_image.path
            extension = 'webp'

            # Generate the new filename based on the category name
            new_filename = f"{slugify(self.name)}.{extension}"
            new_image_path = os.path.join(os.path.dirname(original_image_path), new_filename)

            # Resize and compress image
            self.resize_and_compress_image(original_image_path, new_image_path)

            # Update the featured_image field with the new file path
            self.featured_image.name = os.path.relpath(new_image_path, settings.MEDIA_ROOT)

            # Save the changes
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
