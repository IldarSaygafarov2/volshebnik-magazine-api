# from pprint import pprint

# from slugify import slugify
# from shop.settings import BASE_DIR
# from utils.google_sheets import get_items
# from .models import Product, PublishingHouse, Category, Subcategory, CategoryAge
# import requests
# from bs4 import BeautifulSoup

# from .models import Person
# import requests
# import json
# import time

# celery -A shop worker -l info
# celery -A shop beat -l info


# @app.task  # регистриуем таску
# def get_spreadsheet_items():
#     items = get_items()
#     print(len(items))
#     for item in items:
#         barcode = item.get("Баркод")

#         age = item.get("Возраст")
#         size = item.get("Габариты")
#         publisher = item.get("Издательство")
#         category = item.get("Категория")
#         pages = item.get("Кол-во страниц")
#         title = item.get("Название")
#         description = item.get("Описание")
#         binding = item.get("Переплёт")
#         subcategory = item.get("Под категория")
#         image_url = item.get("Ссылка на фото")
#         host = "//".join(list(filter(lambda x: x, image_url.split("/")[:3])))

#         price = item.get("Цена")

#         soup = BeautifulSoup(requests.get(image_url).text, "html.parser")
#         slider_block = soup.find("div", {"class": "product-pages-slider"})
#         slider_items = [url.get("src") for url in slider_block.find_all("img")]

#         preview = slider_items[0].split("/")[-1]

#         data = requests.get(f"{host}{slider_items[0]}").content

#         with open(f"media/products/{preview}", "wb") as _img:
#             _img.write(data)

#         main_category, main_category_created = Category.objects.get_or_create(
#             name=category
#         )
#         product_subcategory, product_subcategory_created = (
#             Subcategory.objects.get_or_create(
#                 name=subcategory,
#                 slug=slugify(subcategory),
#                 category=main_category,
#             )
#         )
#         publisher_obj, publisher_created = PublishingHouse.objects.get_or_create(
#             name=publisher,
#             slug=slugify(publisher),
#         )
#         age, created_age = CategoryAge.objects.get_or_create(age=age)

#         try:
#             product = Product.objects.get(barcode=int(barcode))

#             product.ages.add(age)
#             product.size = size
#             product.publisher = publisher_obj
#             product.main_category = main_category
#             product.title = title
#             product.slug = slugify(title)
#             product.description = description
#             product.binding = binding
#             product.subcategory = product_subcategory
#             product.price = int(price) if price else 0
#             product.preview = f"products/{preview}"
#             product.pages = pages
#             product.save()
#             print(f"Product updated: {product}")
#         except Product.DoesNotExist:
#             new_product = Product.objects.create(
#                 barcode=int(barcode),
#                 title=title,
#                 size=size,
#                 slug=slugify(title),
#                 price=int(price) if price else 0,
#                 description=description,
#                 binding=binding,
#                 main_category=main_category,
#                 subcategory=product_subcategory,
#                 publisher=publisher_obj,
#                 preview=f"products/{preview}",
#                 pages=pages,
#             )
#             new_product.ages.add(age)
#             print(f"product created: {new_product}")

#     print("FINISHED")
