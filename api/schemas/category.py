from datetime import datetime
from ninja import Schema


class CategorySchema(Schema):
    id: int
    name: str
    created_at: datetime
