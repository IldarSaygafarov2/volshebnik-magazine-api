from datetime import datetime
from ninja import Schema


class PublisherSchema(Schema):
    id: int
    name: str
    slug: str
    created_at: datetime
