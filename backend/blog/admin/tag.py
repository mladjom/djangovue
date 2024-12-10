from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _
from blog.models.tag import Tag
from blog.models.article import Article
from .mixins import ArticleCountMixin

@admin.register(Tag)
class TagAdmin( ArticleCountMixin, admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at', 'article_count')  # Fields displayed in list view
    search_fields = ('name',)  # Searchable by 'name'
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from 'name'

    
class TagInline(admin.TabularInline):
    model = Article.tags.through  # Inline Many-to-Many relation for tags
    extra = 1  # Number of empty fields for adding new tags