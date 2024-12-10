from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from PIL import Image
from datetime import datetime


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

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

        # Process the featured image if it exists
        if self.featured_image:
            self.resize_and_compress_image()

    def resize_and_compress_image(self):
        """
        Resize and compress the featured image to save storage space.
        """
        image_path = self.featured_image.path
        with Image.open(image_path) as img:
            # Convert image to RGB if it's in a different mode (e.g., RGBA)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            # Resize image if it's too large
            max_size = (800, 800)  # Maximum width and height
            img.thumbnail(max_size, Image.ANTIALIAS)

            # Save image with compression
            img.save(image_path, format='JPEG', quality=85)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name