from ninja import NinjaAPI
from api.routes import product_router

api = NinjaAPI()
api.add_router("/api/", product_router)
