from app.core.crud import CRUDBase
from app.db.models import Order

from .schemas import OrderCreate, OrderUpdate

order_service: CRUDBase[Order, OrderCreate, OrderUpdate] = CRUDBase(Order)
