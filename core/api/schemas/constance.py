from ninja import Schema


class ConstanceSchema(Schema):
    data: dict[str, str | None]
