from ninja import Router
from django.http import HttpRequest
from api.schemas.slider import SliderItemSchema
from main.models import Slider

router = Router(
    tags=["Slider"],
)


@router.get("/slider", response=list[SliderItemSchema])
def get_slider_items(request: HttpRequest):
    items = Slider.objects.all()
    return items
