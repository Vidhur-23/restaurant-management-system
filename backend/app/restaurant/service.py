from app.core.crud import CRUDBase
from app.db.models import Restaurant

from .schemas import RestaurantCreate, RestaurantUpdate

restaurant_service: CRUDBase[Restaurant, RestaurantCreate, RestaurantUpdate] = CRUDBase(
    Restaurant
)
