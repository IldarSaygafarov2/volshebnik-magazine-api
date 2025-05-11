from django.http import HttpRequest
from ninja import Router

from api.schemas.product import (
    ProductCreateSchema,
    ProductListSchema,
    ProductPaginatedSchema,
    ProductResultSchema,
)
from api.services.product import ProductService
from main.models import Product

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


@router.get("/products/all/", response=list[ProductListSchema])
def get_all_products(request: HttpRequest):
    return Product.objects.all()


@router.get("/products/", response=ProductPaginatedSchema)
def get_paginated_products(request: HttpRequest, limit: int = 5, offset: int = 0):
    products = Product.objects.all()
    total_products = products.count()
    paginated_products = products[offset:limit]
    return ProductPaginatedSchema(
        total=total_products,
        limit=limit,
        offset=offset,
        products=paginated_products,
    )
