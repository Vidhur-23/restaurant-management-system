from app.core.crud import CRUDBase
from app.db.models import MenuItem

from .schemas import MenuItemCreate, MenuItemUpdate

menu_service: CRUDBase[MenuItem, MenuItemCreate, MenuItemUpdate] = CRUDBase(MenuItem)
