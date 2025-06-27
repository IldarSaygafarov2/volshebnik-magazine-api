from slugify import slugify

from core.api.schemas.product import ProductCreateSchema
from core.api.services.image import image_service
from core.apps.main import models


class ProductService:
    IMAGES_DATA = {
        "robins.ru": "https://robins.ru",
        "kristall-kanc.ru": "https://kristall-kanc.ru",
        "moy-lvenok.ru": "https://moy-lvenok.ru",
        "chitatel.by": "https://chitatel.by",
        "www.detmir.ru": "https://www.detmir.ru",
        "shkola7gnomov.ru": "https://shkola7gnomov.ru",
        "childrensmarket.ru": "https://childrensmarket.ru",
        "maguss.ru": "https://maguss.ru",
    }

    def create_or_update(self, data: ProductCreateSchema):
        images = image_service.get_images_from_dir()
        print(images.get(data.title))

        if data.main_category is not None:
            main_category, main_category_created = (
                models.Category.objects.get_or_create(name=data.main_category)
            )
        else:
            main_category = None

        if data.subcategory is not None:
            product_subcategory, product_subcategory_created = (
                models.Subcategory.objects.get_or_create(
                    name=data.subcategory,
                    slug=slugify(data.subcategory),
                    category=main_category,
                )
            )
        else:
            product_subcategory = None

        publisher_obj, publisher_created = models.PublishingHouse.objects.get_or_create(
            name=data.publisher,
            slug=slugify(data.publisher),
        )
        age, created_age = models.CategoryAge.objects.get_or_create(age=data.age)

        is_updated, is_created = None, None

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
            product.pages = data.pages
            product.save()
            is_updated = True
        except models.Product.DoesNotExist:
            product = models.Product.objects.create(
                barcode=int(data.barcode),
                title=data.title,
                size=data.size,
                slug=slugify(data.title),
                price=data.price,
                description=data.description,
                binding=data.binding,
                main_category=main_category,
                subcategory=product_subcategory,
                publisher=publisher_obj,
                pages=data.pages,
            )
            product.ages.add(age)
            is_created = True

        return product, is_updated, is_created
