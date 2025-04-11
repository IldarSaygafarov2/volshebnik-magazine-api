from pprint import pprint
import json
from main import models
from django.core.management.base import BaseCommand
from slugify import slugify
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("final_result.json", "r", encoding="utf-8") as file:
            content = json.load(file)

        _ages = []
        _categories = []
        previews = os.listdir(BASE_DIR / "media/products")

        for item in content:
            sku = item.get("Артикул:", "")
            price = int(item.get("price")) * 24.70
            slug = item.get("url").split("/")[-2]
            product_code = item.get("Код товара:")

            ages = item.get("Возраст:", "")

            for age in ages.split(","):
                _age, created = models.CategoryAge.objects.get_or_create(age=age)
                # print("age", _age)

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

                    # print(base_category)

            # product, created = models.Product.objects.get_or_create(
            #     barcode='',
            #     title=item.get('title'),
            #     slug=slug,
            #     price=price,
            #     description=item.get('description'),
            #     sku=sku,

            # )

        print(_ages)
        # print(count)
