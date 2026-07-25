from app.core.crud import CRUDBase
from app.db.models import InventoryItem

from .schemas import InventoryItemCreate, InventoryItemUpdate

inventory_service: CRUDBase[
    InventoryItem, InventoryItemCreate, InventoryItemUpdate
] = CRUDBase(InventoryItem)
