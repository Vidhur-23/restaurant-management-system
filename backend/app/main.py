from fastapi import FastAPI

from app.db import models  # noqa: F401  (ensure models are registered on Base)
from app.db.database import Base, engine
from app.inventory.router import router as inventory_router
from app.menu.router import router as menu_router
from app.orders.router import router as orders_router
from app.payments.router import router as payments_router
from app.reservations.router import router as reservations_router
from app.restaurant.router import router as restaurant_router

# No Alembic in Phase 1 — create tables directly from the models.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Restaurant Management System", version="0.1.0")

app.include_router(restaurant_router)
app.include_router(menu_router)
app.include_router(inventory_router)
app.include_router(reservations_router)
app.include_router(orders_router)
app.include_router(payments_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
