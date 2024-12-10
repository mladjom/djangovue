from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from blog.models.article import Article
from blog.models.category import Category
from blog.admin.tag import TagInline


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('is_published', 'is_featured', 'category')  # Filters for sidebar
    search_fields = ('title', 'content')  # Searchable by 'title' and 'content'
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from 'title'
    inlines = [TagInline]  # Add tags inline editing
    date_hierarchy = 'created_at'  # Navigation by creation date
    readonly_fields = ('created_at', 'updated_at')  # Prevent manual changes to timestamps