import os
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.conf import settings
from blog.utils.image_utils import resize_and_compress_image

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

        # Check if the image is being replaced
        if self.pk:
            old_category = Category.objects.get(pk=self.pk)
            if old_category.featured_image != self.featured_image:
                # Delete the old image if it's being replaced
                if old_category.featured_image:
                    try:
                        os.remove(old_category.featured_image.path)
                    except FileNotFoundError:
                        pass  # If the file doesn't exist, just skip it

        # Process the featured image if it exists
        if self.featured_image:
            original_image_path = self.featured_image.path
            extension = 'webp'
            new_image_path = category_image_upload_path(self, self.featured_image.name)
            
            # Generate the new filename based on the category name
            new_filename = f"{slugify(self.name)}.{extension}"
            new_image_path = os.path.join(os.path.dirname(original_image_path), new_filename)

            resize_and_compress_image(original_image_path, os.path.join(settings.MEDIA_ROOT, new_image_path))
        
            # Update the featured_image field with the new file path
            self.featured_image.name = os.path.relpath(new_image_path, settings.MEDIA_ROOT)

        # Save the category instance
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Retrieve the full instance from the database
        category = Category.objects.get(pk=self.pk)
        print(category)
        # Check if there's a featured_image
        if category.featured_image:
            print(category.featured_image)
            # Get the full path to the image
            image_path = os.path.join(settings.MEDIA_ROOT, str(category.featured_image))

            if os.path.exists(image_path):
                try:
                    os.remove(image_path)  # Delete the image file
                    print(f"Deleted image: {image_path}")
                except Exception as e:
                    print(f"Error deleting image {image_path}: {e}")
            else:
                print(f"Image not found: {image_path}")

        # Call the parent delete method to delete the database record
        super().delete(*args, **kwargs)
            
    def __str__(self):
        return self.name