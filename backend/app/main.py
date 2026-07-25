from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.restaurant import router as restaurant_router
from app.payments import router as payments_router
from app.orders import router as orders_router
from app.menu import router as menu_router
from app.inventory import router as inventory_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(restaurant_router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(payments_router, prefix="/payments", tags=["Payments"])
app.include_router(orders_router, prefix="/orders", tags=["Orders"])
app.include_router(menu_router, prefix="/menu", tags=["Menu"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])