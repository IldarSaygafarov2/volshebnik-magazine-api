from datetime import datetime
from typing import Optional

from ninja import Schema

from .ages import CategoryAgeSchema
from .category import CategorySchema
from .publisher import PublisherSchema
from .subcategory import SubcategorySchema
from main.models import Product


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
    preview: Optional[str] = ""


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


class ProductBaseCategorySchema(Schema):
    id: int
    name: str
    slug: str


class ProductCharacteristicsSchema(Schema):
    barcode: Optional[int]
    sku: Optional[str]
    pages: Optional[str]
    size: Optional[str]
    product_code: Optional[int]
    binding: Optional[str]
    base_categories: Optional[list[ProductBaseCategorySchema]]
    ages: list[CategoryAgeSchema]
    publisher: Optional[ProductPublisherSchema]


class ProductDetailSchema(Schema):
    id: int
    title: str
    description: Optional[str]
    price: Optional[str]
    images: list[ProductImageSchema]
    characteristics: Optional[ProductCharacteristicsSchema] = None

    @staticmethod
    def resolve_characteristics(obj: Product) -> ProductCharacteristicsSchema:
        return ProductCharacteristicsSchema(
            barcode=obj.barcode,
            sku=obj.sku,
            ages=obj.ages.all(),
            publisher=obj.publisher,
            base_categories=obj.base_category.all(),
            pages=obj.pages,
            size=obj.size,
            product_code=obj.product_code,
            binding=obj.binding,
        )
        return {
            "barcode": obj.barcode,
            "sku": obj.sku,
            "ages": [ProductCategoryAgeSchema(id=age.pk, age=age.age) for age in obj.ages.all()],
            "publisher": obj.publisher.name,
            "seria": obj.main_category.name,
            "pages": obj.pages,
            "size": obj.size,
            "product_code": obj.product_code
        }
