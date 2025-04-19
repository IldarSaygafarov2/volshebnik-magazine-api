from typing import Optional
from ninja import Schema

from .ages import CategoryAgeSchema
from .category import CategorySchema
from .subcategory import SubcategorySchema
from .publisher import PublisherSchema


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
