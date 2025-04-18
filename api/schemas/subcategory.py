from datetime import datetime
from ninja import Schema
from .category import CategorySchema


class SubcategorySchema(Schema):
    id: int
    name: str
    slug: str
    category: CategorySchema
    created_at: datetime
