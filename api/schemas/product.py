from datetime import datetime
from typing import Optional

from ninja import Schema

from main.models import Product
from api.schemas.ages import CategoryAgeSchema
from api.schemas.category import CategorySchema
from api.schemas.publisher import PublisherSchema
from api.schemas.subcategory import SubcategorySchema


class ProductSimpleSchema(Schema):
    id: int


class ProductSchema(Schema):
    id: int
    title: Optional[str]
    slug: Optional[str]
    price: Optional[float | str] = ""
    description: Optional[str]
    ages: list[CategoryAgeSchema | None]
    size: Optional[str]
    pages: Optional[str]
    binding: Optional[str]
    publisher: Optional[PublisherSchema]
    main_category: Optional[CategorySchema]
    subcategory: Optional[SubcategorySchema]


class ProductResultSchema(Schema):
    is_updated: Optional[bool]
    is_created: Optional[bool]
    product: ProductSimpleSchema


class ProductCreateSchema(Schema):
    title: Optional[str] = ""
    description: Optional[str] = ""
    barcode: Optional[str] = ""
    price: Optional[str] = ""
    size: Optional[str] = ""
    pages: Optional[str] = None
    binding: Optional[str] = ""
    publisher: Optional[str] = ""
    main_category: Optional[str] = ""
    subcategory: Optional[str] = ""
    age: Optional[str] = ""
    image_url: Optional[str] = ""


class ProductListSchema(Schema):
    id: int
    title: str
    slug: str
    price: Optional[str]
    preview: Optional[str]
    is_on_sale: bool
    is_new: bool
    is_bestseller: bool
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


class ProductBaseCategorySchema(Schema):
    id: int
    name: str
    slug: str


class ProductCharacteristicsSchema(Schema):
    barcode: Optional[int]
    pages: Optional[str]
    size: Optional[str]
    binding: Optional[str]
    ages: list[CategoryAgeSchema]
    publisher: Optional[ProductPublisherSchema]


class ProductDetailSchema(Schema):
    id: int
    title: str
    preview: Optional[str]
    description: Optional[str]
    price: Optional[str]
    images: list[ProductImageSchema]
    characteristics: Optional[ProductCharacteristicsSchema] = None

    @staticmethod
    def resolve_characteristics(obj: Product) -> ProductCharacteristicsSchema:
        return ProductCharacteristicsSchema(
            barcode=obj.barcode,
            ages=obj.ages.all(),
            publisher=obj.publisher,
            pages=obj.pages,
            size=obj.size,
            binding=obj.binding,
        )
