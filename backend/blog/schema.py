# blog/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from .models import Category, Tag, Article

# Define GraphQL types for each model
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "description", "slug")  # Expose these fields

class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ("id", "name", "description", "slug")

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        interfaces = (Node,)
        filter_fields = ['title']
        fields = (
            "id",
            "title",
            "content",
            "slug",
            "category",
            "tags",
            "is_published",
            "is_featured",
            "created_at",
            "modified_at",
        )

# Define Query class
class Query(graphene.ObjectType):
    # Add fields to query
    all_categories = graphene.List(CategoryType)
    all_tags = graphene.List(TagType)
    #all_articles = graphene.List(ArticleType)
    all_articles = DjangoFilterConnectionField(ArticleType)
    article_by_slug = graphene.Field(ArticleType, slug=graphene.String(required=True))

    # Resolvers
    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_tags(root, info):
        return Tag.objects.all()

    def resolve_all_articles(root, info):
        return Article.objects.all()

    def resolve_article_by_slug(root, info, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            return None

# Define the schema
schema = graphene.Schema(query=Query)
