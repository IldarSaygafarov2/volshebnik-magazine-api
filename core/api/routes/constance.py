from ninja import Router
from core.api.schemas.constance import ConstanceSchema
from django.http import HttpRequest
from constance import config
from core.shop.settings import CONSTANCE_CONFIG

router = Router(tags=["Constance"])


@router.get("/settings/", response=ConstanceSchema)
def get_constance_data(request: HttpRequest):
    keys = CONSTANCE_CONFIG.keys()
    data = {}
    for key in keys:
        data[key.lower()] = getattr(config, key)
    return ConstanceSchema(data=data)
