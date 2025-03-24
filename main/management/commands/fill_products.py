from django.core.management.base import BaseCommand
from main.models import PublishingHouse, Product, Category
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('products.json', mode='r', encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
            print(item)

