import os

import requests
from bs4 import BeautifulSoup
from slugify import slugify

from api.schemas.product import ProductCreateSchema
from shop.settings import BASE_DIR
from main import models


class ProductService:
    IMAGE_HOST = "https://robins.ru"

    def download_images_by_preview_url(self, preview_url: str):

        soup = BeautifulSoup(requests.get(preview_url).text, "html.parser")
        wrapper = soup.find("div", {"class": "flexslider-big"})
        images = [i.get("src") for i in wrapper.find_all("img")]
        previews_dir = BASE_DIR / "media/products"
        gallery_dir = previews_dir / "gallery"
        preview = images[0] if len(images) > 0 else ""
        preview_name = preview.split("/")[-1]

        preview_content = requests.get(f"{self.IMAGE_HOST}/{preview}").content
        with open(f"{previews_dir}/{preview_name}", mode="wb") as f:
            f.write(preview_content)

        return preview_name

    def create_or_update(self, data: ProductCreateSchema):
        main_category, main_category_created = models.Category.objects.get_or_create(
            name=data.main_category
        )

        product_subcategory, product_subcategory_created = (
            models.Subcategory.objects.get_or_create(
                name=data.subcategory,
                slug=slugify(data.subcategory),
                category=main_category,
            )
        )
        publisher_obj, publisher_created = models.PublishingHouse.objects.get_or_create(
            name=data.publisher,
            slug=slugify(data.publisher),
        )
        age, created_age = models.CategoryAge.objects.get_or_create(age=data.age)

        preview_name = self.download_images_by_preview_url(preview_url=data.preview)

        try:
            product = models.Product.objects.get(barcode=int(data.barcode))

            product.ages.add(age)
            product.size = data.size
            product.publisher = publisher_obj
            product.main_category = main_category
            product.title = data.title
            product.slug = slugify(data.title)
            product.description = data.description
            product.binding = data.binding
            product.subcategory = product_subcategory
            product.price = int(data.price) if data.price else 0
            product.preview = f"products/{preview_name}"
            product.pages = data.pages
            product.save()
            print(f"Product updated: {product}")
        except models.Product.DoesNotExist:
            product = models.Product.objects.create(
                barcode=int(data.barcode),
                title=data.title,
                size=data.size,
                slug=slugify(data.title),
                price=int(data.price) if data.price else 0,
                description=data.description,
                binding=data.binding,
                main_category=main_category,
                subcategory=product_subcategory,
                publisher=publisher_obj,
                preview=f"products/{preview_name}",
                pages=data.pages,
            )
            product.ages.add(age)
            print(f"product created: {product}")
        return product
