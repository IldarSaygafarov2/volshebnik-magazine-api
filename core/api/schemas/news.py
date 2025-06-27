from datetime import datetime

from ninja import Schema


class NewsPostSchema(Schema):
    id: int
    title: str
    slug: str
    preview: str | None
    content: str | None
    created_at: datetime
