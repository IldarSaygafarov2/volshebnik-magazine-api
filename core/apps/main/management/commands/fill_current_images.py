import os
from typing import Any

from django.core.management.base import BaseCommand

from core.apps.main.models import Product, ProductImage
from core.shop.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        products = Product.objects.all()
        products_dir_path = BASE_DIR / "media/products"
        product_images_dirs = os.listdir(products_dir_path)
        product_gallery_images = {
            i: os.listdir(products_dir_path / i / "gallery")
            for i in product_images_dirs
        }
        product_preview_images = {
            i: os.listdir(products_dir_path / i / "previews")[0]
            for i in product_images_dirs
        }

        print(product_preview_images)

        for db_product in products:
            product_images = product_gallery_images.get(db_product.slug)
            preview = product_preview_images.get(db_product.slug)

            if preview is not None:
                db_product.preview = f"products/{db_product.slug}/previews/{preview}"
                db_product.save()

            if product_images is not None:
                for image in product_images:
                    obj = ProductImage.objects.create(
                        product=db_product,
                        image=f"products/{db_product.slug}/gallery/{image}",
                    )
