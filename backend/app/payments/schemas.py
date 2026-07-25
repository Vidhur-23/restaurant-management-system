from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    order_id: int
    amount: Decimal
    method: str | None = None
    status: str = "pending"
    paid_at: datetime | None = None


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    order_id: int | None = None
    amount: Decimal | None = None
    method: str | None = None
    status: str | None = None
    paid_at: datetime | None = None


class PaymentResponse(PaymentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
