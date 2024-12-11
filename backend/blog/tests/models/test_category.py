import pytest
from blog.models import Category
from django.utils.text import slugify
from django.conf import settings

@pytest.mark.django_db
def test_create_category():
    """Test the creation of a Category object."""
    category = Category.objects.create(
        name="Technology",
        description="Category for technology articles",
        slug="technology"
    )
    assert category.name == "Technology"
    assert category.slug == "technology"
    assert category.description == "Category for technology articles"


@pytest.mark.django_db
def test_slug_auto_generation():
    """Test that the slug is auto-generated if not provided."""
    category = Category.objects.create(
        name="Artificial Intelligence",
        description="Category for AI articles"
    )
    assert category.slug == "artificial-intelligence"
    assert category.name == "Artificial Intelligence"


@pytest.mark.django_db
def test_category_ordering():
    """Test if categories are ordered by name."""
    Category.objects.create(name="Zebra")
    Category.objects.create(name="Apple")
    categories = list(Category.objects.all())
    assert [cat.name for cat in categories] == ["Apple", "Zebra"]

@pytest.mark.django_db
def test_category_slug_generation():
    category = Category.objects.create(name="Test Category")
    assert category.slug == slugify(category.name)

