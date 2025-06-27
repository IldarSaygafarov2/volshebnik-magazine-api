from django.http import HttpRequest
from ninja import Router

from core.api.schemas.product import ProductPaginatedSchema
from core.apps.main.models import Product

router = Router(tags=["Subcategories"])


@router.get("/subcategories/{slug}/", response=ProductPaginatedSchema)
def get_products_by_subcategory_slug(
    request: HttpRequest,
    slug: str,
    offset: int = 0,
    limit: int = 10,
):
    products = Product.objects.filter(subcategory__slug=slug)
    total_products = products.count()

    return ProductPaginatedSchema(
        total=total_products,
        offset=offset,
        limit=limit,
        products=products[offset:limit],
    )
