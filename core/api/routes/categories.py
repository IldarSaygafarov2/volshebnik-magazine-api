from django.http import HttpRequest
from ninja import Router
from core.api.schemas.category import CategoryExpandedSchema
from core.apps.main.models import Category

router = Router(tags=["Categories"])


@router.get("/categories/", response=list[CategoryExpandedSchema])
def get_categories(request: HttpRequest):
    categories = Category.objects.all()
    return categories
