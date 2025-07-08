from ninja import NinjaAPI

from core.api.routes import category_router
from core.api.routes import news_router
from core.api.routes import product_router
from core.api.routes import slider_router
from core.api.routes import subcategory_router
from core.api.routes import constance_router

api = NinjaAPI()

api.add_router("/api/", product_router)
api.add_router("/api/", category_router)
api.add_router("/api/", subcategory_router)
api.add_router("/api/", slider_router)
api.add_router("/api/", news_router)
api.add_router('/api/', constance_router)
