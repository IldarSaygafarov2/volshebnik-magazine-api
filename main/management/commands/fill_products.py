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
        with open("json_data/final_result.json", "r", encoding="utf-8") as file:
            content = json.load(file)

        with open("json_data/photos.json", "r", encoding="utf-8") as photos:
            photos_content = json.load(photos)

        _ages = []
        _categories = []

        for item in content:
            sku = item.get("Артикул:", "")
            price = int(item.get("price")) * 24.70
            slug = item.get("url").split("/")[-2]
            product_code = item.get("Код товара:")

            photos_content_item = photos_content.get(slug)

            preview_path = os.path.join("products", photos_content_item.get("preview"))

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

            product, created = models.Product.objects.get_or_create(
                barcode=item.get("barcode"),
                title=item.get("title"),
                slug=slug,
                price=price,
                description=item.get("description"),
                sku=sku,
                preview=preview_path,
                product_code=int(product_code),
                pages=item.get("Количество страниц:", "0"),
                size=item.get("Размер:", ""),
                publisher=publisher,
            )
            print(product)

            for img in photos_content.get(slug).get("gallery"):
                gallery_image_path = os.path.join("products", "gallery", img)
                gallery_obj = models.ProductImage.objects.get_or_create(
                    product=product, image=gallery_image_path
                )
                print(gallery_obj)

            if category_names is not None:
                for category_name in category_names.split(","):
                    obj = models.ProductBaseCategory.objects.get(name=category_name)
                    product.base_category.add(obj)
                    print(product.base_category)

            for age in ages.split(","):
                _age, created = models.CategoryAge.objects.get_or_create(age=age)
                product.ages.add(_age)
                # print("age", _age)
        # print(count)
