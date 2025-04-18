from ninja import Router

from api.schemas.product import ProductCreateSchema, ProductSchema
from api.services.product import ProductService


router = Router(tags=["Products"])
product_service = ProductService()


@router.post("/products/", response=ProductSchema)
def create_product(request, data: ProductCreateSchema):
    return product_service.create_or_update(data)
