from app.core.crud import CRUDBase
from app.db.models import Reservation

from .schemas import ReservationCreate, ReservationUpdate

reservation_service: CRUDBase[
    Reservation, ReservationCreate, ReservationUpdate
] = CRUDBase(Reservation)
