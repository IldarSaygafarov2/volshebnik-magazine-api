from pprint import pprint

from slugify import slugify
from shop.celery import app
from shop.settings import BASE_DIR
from utils.google_sheets import get_items
from .models import Product, PublishingHouse, Category, Subcategory, CategoryAge
import requests


# from .models import Person
# import requests
# import json
# import time

# celery -A shop worker -l info
# celery -A shop beat -l info


@app.task  # регистриуем таску
def get_spreadsheet_items():
    print(BASE_DIR)
    items = get_items()
    for item in items:
        barcode = item.get("Баркод")

        age = item.get("Возраст")
        size = item.get("Габариты")
        publisher = item.get("Издательство")
        category = item.get("Категория")
        pages = item.get("Кол-во страниц")
        title = item.get("Название")
        description = item.get("Описание")
        binding = item.get("Переплёт")
        subcategory = item.get("Под категория")
        image_url = item.get("Ссылка на фото")
        price = item.get("Цена")

        file_name = image_url.split("/")[-2]
        data = requests.get(image_url).content

        with open(f"media/products/{file_name}", "wb") as _img:
            _img.write(data)

        main_category, main_category_created = Category.objects.get_or_create(
            name=category
        )
        product_subcategory, product_subcategory_created = (
            Subcategory.objects.get_or_create(
                name=subcategory,
                slug=slugify(subcategory),
                category=main_category,
            )
        )
        publisher_obj, publisher_created = PublishingHouse.objects.get_or_create(
            name=publisher,
            slug=slugify(publisher),
        )
        age, created_age = CategoryAge.objects.get_or_create(age=age)

        try:
            product = Product.objects.get(barcode=int(barcode))

            product.ages.add(age)
            product.size = size
            product.publisher = publisher_obj
            product.main_category = main_category
            product.title = title
            product.slug = slugify(title)
            product.description = description
            product.binding = binding
            product.subcategory = product_subcategory
            product.price = int(price) if price else 0
            product.preview = f"products/{file_name}"
            product.save()
            print(f"Product updated: {product}")
        except Product.DoesNotExist:
            new_product = Product.objects.create(
                barcode=int(barcode),
                title=title,
                size=size,
                slug=slugify(title),
                price=int(price) if price else 0,
                description=description,
                binding=binding,
                main_category=main_category,
                subcategory=product_subcategory,
                publisher=publisher_obj,
                preview=f"products/{file_name}",
            )
            new_product.ages.add(age)
            print(f"product created: {new_product}")
