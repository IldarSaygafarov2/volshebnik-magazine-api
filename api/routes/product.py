from ninja import Router
from api.schemas.product import ProductCreateSchema


router = Router(tags=["Products"])


@router.post("/products/")
def create_product(request, data: ProductCreateSchema):
    print(data)
