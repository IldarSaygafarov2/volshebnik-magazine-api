from api.schemas.product import ProductCreateSchema
from main import models
from slugify import slugify


class ProductService:
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
            # product.preview = f"products/{preview}"
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
                # preview=f"products/{preview}",
                pages=data.pages,
            )
            product.ages.add(age)
            print(f"product created: {product}")
        return product
