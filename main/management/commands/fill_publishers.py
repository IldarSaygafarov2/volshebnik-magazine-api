import json

from django.core.management.base import BaseCommand
from slugify import slugify

from main import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('products.json', mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        for publisher in data['publishers']:
            obj = models.PublishingHouse.objects.create(
                name=publisher,
                slug=slugify(publisher),
            )
            print(obj)