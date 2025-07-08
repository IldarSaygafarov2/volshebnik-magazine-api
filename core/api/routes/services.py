from ninja import Router

from core.api.schemas.service import ServiceSchema
from core.apps.services.models import Service

router = Router(tags=["Services"])


@router.get('/services/', response=list[ServiceSchema])
def get_services(request):
    services = Service.objects.all()
    return services