from datetime import datetime
from ninja import Schema


class CategorySchema(Schema):
    id: int
    name: str
    created_at: datetime


class SubcategorySchema(Schema):
    id: int
    name: str
    slug: str
    created_at: datetime


class CategoryExpandedSchema(Schema):
    id: int
    name: str
    created_at: datetime
    subcategories: list[SubcategorySchema]
