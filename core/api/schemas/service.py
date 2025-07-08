from ninja import Schema


class ServiceSchema(Schema):
    id: int
    title: str
    icon: str | None
    is_visible: bool
    description: str