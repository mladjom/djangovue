# blog/models/tag_model.py
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from .featured_image_model import FeaturedImage
import os

class Tag(FeaturedImage):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
            
        # Check if the image is being replaced or cleared
        if self.pk:
            old_tag = Tag.objects.get(pk=self.pk)
            if old_tag.featured_image and old_tag.featured_image != self.featured_image:
                try:
                    os.remove(old_tag.featured_image.path)
                except FileNotFoundError:
                    pass  # If the file doesn't exist, just skip it           
            
            
        super().save(*args, **kwargs)

        # Process the featured image after the initial save
        if self.featured_image:
            self.process_featured_image()

            # Save again to persist the updated `featured_image` path
            super().save(update_fields=['featured_image'])

    def delete(self, *args, **kwargs):
        """
        Ensure the associated image file is deleted when the tag is deleted.
        """
        if self.featured_image:
            image_path = self.featured_image.path

            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                    print(f"Deleted image: {image_path}")
                except Exception as e:
                    print(f"Error deleting image {image_path}: {e}")
            else:
                print(f"Image file not found: {image_path}")

        super().delete(*args, **kwargs)



    def __str__(self):
        return self.name