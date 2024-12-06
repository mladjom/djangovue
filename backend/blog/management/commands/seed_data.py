# blog/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Category, Tag, Article
import random
import json

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Categories
        self.stdout.write("Creating Categories...")
        categories = []
        for _ in range(5):  # Create 5 categories
            category = Category.objects.create(
                name=fake.unique.word().capitalize(),
                description=fake.sentence(),
                slug=fake.unique.slug()
            )
            categories.append(category)

        # Create Tags
        self.stdout.write("Creating Tags...")
        tags = []
        for _ in range(10):  # Create 10 tags
            tag = Tag.objects.create(
                name=fake.unique.word().capitalize(),
                description=fake.sentence(),
                slug=fake.unique.slug()
            )
            tags.append(tag)

        # Create Articles
        self.stdout.write("Creating Articles...")
        for _ in range(20):  # Create 20 articles
            article = Article.objects.create(
                title=fake.sentence(),
                # content={
                #     "delta": {  # Ensures QuillField is properly formatted
                #         "ops": [
                #             {"insert": "International only heart write vote let...\n"}
                #             ]
                #         }
                #     },
                # slug=fake.unique.slug(),
                category=random.choice(categories),
                is_published=random.choice([True, False]),
                is_featured=random.choice([True, False]),
            )
            # Add random tags to each article
            article.tags.set(random.sample(tags, random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
