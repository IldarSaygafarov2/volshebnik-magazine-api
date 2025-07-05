from datetime import datetime
from typing import Optional

from ninja import Schema, Field


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


class CategoryPopularSchema(Schema):
    id: int
    name: str
    image: Optional[str]
    is_popular: bool = Field(default=False)