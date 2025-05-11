from datetime import datetime
from typing import Optional

from ninja import Schema

from .ages import CategoryAgeSchema
from .category import CategorySchema
from .publisher import PublisherSchema
from .subcategory import SubcategorySchema


class ProductSchema(Schema):
    id: int
    title: str
    slug: str
    price: float | str
    description: str
    ages: list[CategoryAgeSchema]
    size: str
    pages: str
    binding: str
    publisher: PublisherSchema
    main_category: CategorySchema
    subcategory: SubcategorySchema


class ProductResultSchema(Schema):
    is_updated: Optional[bool]
    is_created: Optional[bool]
    product: ProductSchema


class ProductCreateSchema(Schema):
    title: str
    description: Optional[str] = ""
    barcode: str
    price: Optional[str] = ""
    size: Optional[str] = ""
    pages: Optional[str] = None
    binding: Optional[str] = ""
    publisher: str
    main_category: str
    subcategory: str
    age: str
    preview: str


class ProductListSchema(Schema):
    id: int
    title: str
    slug: str
    price: str
    preview: Optional[str]
    subcategory: Optional[SubcategorySchema]


class ProductPaginatedSchema(Schema):
    total: int
    limit: int
    offset: int
    products: list[ProductListSchema]


class ProductImageSchema(Schema):
    id: int
    image: str


class ProductPublisherSchema(Schema):
    id: int
    name: str
    slug: str
    created_at: datetime


class ProductCategoryAgeSchema(Schema):
    id: int
    age: str


class ProductDetailSchema(Schema):
    id: int
    title: str
    description: Optional[str]
    price: Optional[str]
    barcode: Optional[str]
    size: Optional[str]
    pages: Optional[str]
    binding: Optional[str]

    publisher: Optional[ProductPublisherSchema]
    ages: Optional[list[CategoryAgeSchema]]
    images: list[ProductImageSchema]
