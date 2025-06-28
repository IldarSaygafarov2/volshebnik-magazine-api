from django.http import HttpRequest, Http404
from ninja import Router

from core.api.schemas.news import NewsPostSchema
from core.apps.news.models import NewsPost

router = Router(tags=["News"])


@router.get("/news/", response=list[NewsPostSchema])
def get_news(request):
    news = NewsPost.objects.filter(is_visible=True).order_by('-created_at')
    return news


@router.get('/news/{news_slug}', response=NewsPostSchema)
def get_news_detail(request: HttpRequest, news_slug: str):
    detail = NewsPost.objects.filter(slug=news_slug)
    if not detail.exists():
        raise Http404()
    return detail.first()


