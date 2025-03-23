from pprint import pprint

from main.models import Catalog, Category
from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            catalog_item = Catalog.objects.create(name=item.get('name'))
            print(f'added {catalog_item.name}')
            links = []
            inner_items = item.get('inner_items', [])
            for idx, inner_item in enumerate(inner_items):
                link = ''.join(inner_item.get('link').split('/')[-2])
                links.append(inner_item.get('name'))

                category_item = Category.objects.create(
                    name=inner_item.get('name'),
                    slug=''.join(inner_item.get('link').split('/')[-2]),
                    catalog=catalog_item
                )
                print(f'added {category_item.name} for {catalog_item.name}')
