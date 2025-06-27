import json

from django.core.management.base import BaseCommand

from core.apps.main.models import Category, Subcategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('json_data/categories.json', mode='r', encoding='utf-8') as f:
            categories = json.load(f)

        for category, subcategories in categories.items():
            category_obj = Category.objects.create(name=category)
            print(f'[CATEGORY - {category_obj.name}]')

            for subcategory in subcategories:
                subcategory_obj = Subcategory.objects.create(
                    name=subcategory['title'],
                    slug=subcategory['slug'],
                    category=category_obj
                )
                print(f'[SUBCATEGORY - {subcategory_obj.name}]')
