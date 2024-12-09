from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_quill.fields import QuillField

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    class Meta:
        verbose_name = _('Category')  # Translated singular name
        verbose_name_plural = _('Categories')  # Translated plural name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = QuillField(verbose_name=_('Content'))  # Assuming QuillField handles translation internally or needs additional processing
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name=_('Category'))
    tags = models.ManyToManyField(Tag, related_name='articles', verbose_name=_('Tags'))
    is_published = models.BooleanField(default=False, verbose_name=_('Is Published'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Is Featured'))
    created_at = models.DateTimeField(default=now, verbose_name=_('Created At'))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_('Modified At'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
