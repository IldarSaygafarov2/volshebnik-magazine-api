from pprint import pprint
import json
from main import models
from django.core.management.base import BaseCommand
from slugify import slugify


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("final_result.json", "r", encoding="utf-8") as file:
            content = json.load(file)
        count = 0
        for item in content:
            publisher_name = item.get("Издательство:")
            if publisher_name is not None:
                publisher, created = models.PublishingHouse.objects.get_or_create(
                    name=publisher_name,
                    slug=slugify(publisher_name),
                )

            category_names = item.get("Категория:")
            if category_names is not None:
                for category_name in category_names.split(","):
                    base_category, created = (
                        models.ProductBaseCategory.objects.get_or_create(
                            name=category_name, slug=slugify(category_name)
                        )
                    )

                    print(base_category)

        # print(count)
