from pprint import pprint

from django.core.management.base import BaseCommand
from main.models import PublishingHouse, Product, Category
import json
from slugify import slugify


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('products.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)

        categories_objects = []
        for item in data:
            publishing_house, created = PublishingHouse.objects.get_or_create(
                name=item['publishing_house'],
                slug=slugify(item['publishing_house']),
            )
            obj = Product.objects.create(
                name=item['name'],
                slug=item['slug'],
                description=item['description'],
                price=int(item['price']) * 25.70,
                publishing_house=publishing_house,
                barcode=item['barcode']

            )
            print(f'[INFO] - added {obj}')


