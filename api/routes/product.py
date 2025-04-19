from ninja import Router

from api.schemas.product import ProductCreateSchema, ProductSchema, ProductResultSchema
from api.services.product import ProductService


router = Router(tags=["Products"])
product_service = ProductService()


@router.post("/products/", response=ProductResultSchema)
def create_product(request, data: ProductCreateSchema):
    product, is_updated, is_created = product_service.create_or_update(data)
    return ProductResultSchema(
        is_created=is_created,
        is_updated=is_updated,
        product=product,
    )
