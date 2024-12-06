# blog/admin.py

from django.contrib import admin
from .models import Category, Tag, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')  # Fields displayed in list view
    search_fields = ('name',)  # Searchable by 'name'
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from 'name'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')  # Fields displayed in list view
    search_fields = ('name',)  # Searchable by 'name'
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from 'name'

class TagInline(admin.TabularInline):
    model = Article.tags.through  # Inline Many-to-Many relation for tags
    extra = 1  # Number of empty fields for adding new tags

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_featured', 'created_at', 'modified_at')
    list_filter = ('is_published', 'is_featured', 'category')  # Filters for sidebar
    search_fields = ('title', 'content')  # Searchable by 'title' and 'content'
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from 'title'
    inlines = [TagInline]  # Add tags inline editing
    date_hierarchy = 'created_at'  # Navigation by creation date
    readonly_fields = ('created_at', 'modified_at')  # Prevent manual changes to timestamps
