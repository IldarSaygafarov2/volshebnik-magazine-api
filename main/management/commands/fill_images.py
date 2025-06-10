import os
import shutil
from pprint import pprint
from typing import Any

from django.core.management.base import BaseCommand

from main.models import Product, ProductImage
from shop.settings import BASE_DIR, IMAGES_PATH


class Command(BaseCommand):
    def _get_dir_images_dict(self):
        dir_images = os.listdir(IMAGES_PATH)
        result = {}
        for dir_image in dir_images:
            dir_image_path = os.path.join(IMAGES_PATH, dir_image)  # type: ignore
            if os.path.isdir(dir_image_path):
                result[dir_image] = []
                dir_inner_images = os.listdir(dir_image_path)
                for dir_inner_image in dir_inner_images:
                    dir_inner_image_path = os.path.join(dir_image_path, dir_inner_image)
                    result[dir_image].append(dir_inner_image_path)
        return result

    def handle(self, *args: Any, **options: Any) -> str | None:

        # creating media dir
        media_dir = BASE_DIR / "media"
        media_dir.mkdir(exist_ok=True)

        # creating products dir in media
        products_dir = media_dir / "products"
        products_dir.mkdir(exist_ok=True)

        dir_images = self._get_dir_images_dict()
        db_products = Product.objects.all()

        for db_product in db_products:

            title = db_product.title
            images = dir_images.get(title)
            if images is not None:
                # creating folder for product in media
                product_dir = products_dir / db_product.slug
                product_dir.mkdir(exist_ok=True)

                # creating preview folder for product in media
                product_preview_dir = product_dir / "previews"
                product_preview_dir.mkdir(exist_ok=True)

                product_gallery_dir = product_dir / "gallery"
                product_gallery_dir.mkdir(exist_ok=True)

                preview = images.pop(0)
                preview_name = preview.split("/")[-1]
                db_product.preview = (
                    f"products/{db_product.slug}/previews/{preview_name}"
                )
                db_product.save()

                shutil.copy(preview, product_preview_dir)

                for image in images:
                    image_name = image.split("/")[-1]
                    current_images = ProductImage.objects.filter(product=db_product)
                    current_images_names = [
                        i.image.url.split("/")[-1] for i in current_images
                    ]
                    if image_name not in current_images_names:
                        product_image = ProductImage.objects.create(
                            product=db_product,
                            image=f"products/{db_product.slug}/gallery/{image_name}",
                        )
                        product_image.save()
                    shutil.copy(image, product_gallery_dir)
