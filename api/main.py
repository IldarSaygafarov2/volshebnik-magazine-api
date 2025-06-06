from ninja import NinjaAPI
from api.routes import product_router
from api.routes import category_router
from api.routes import subcategory_router
from api.routes import slider_router

api = NinjaAPI()

api.add_router("/api/", product_router)
api.add_router("/api/", category_router)
api.add_router("/api/", subcategory_router)
api.add_router("/api/", slider_router)
