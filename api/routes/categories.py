from django.http import HttpRequest
from ninja import Router
from api.schemas.category import CategoryExpandedSchema
from main.models import Category

router = Router(tags=["Categories"])


@router.get("/categories/", response=list[CategoryExpandedSchema])
def get_categories(request: HttpRequest):
    categories = Category.objects.all()
    return categories
