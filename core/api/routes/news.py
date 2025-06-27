from ninja import Router

from core.api.schemas.news import NewsPostSchema
from core.apps.news.models import NewsPost

router = Router(tags=["News"])


@router.get("/news/", response=list[NewsPostSchema])
def get_news(request):
    news = NewsPost.objects.filter(is_visible=True).order_by('-created_at')
    return news