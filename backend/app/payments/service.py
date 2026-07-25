from app.core.crud import CRUDBase
from app.db.models import Payment

from .schemas import PaymentCreate, PaymentUpdate

payment_service: CRUDBase[Payment, PaymentCreate, PaymentUpdate] = CRUDBase(Payment)
