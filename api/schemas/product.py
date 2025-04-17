from typing import Optional
from ninja import Schema


class ProductCreateSchema(Schema):
    title: str
    description: Optional[str] = ""
    barcode: str
    price: Optional[str] = ""
    size: Optional[str] = ""
    pages: Optional[str] = ""
    binding: Optional[str] = ""
    publisher: str
    main_category: str
    subcategory: str
