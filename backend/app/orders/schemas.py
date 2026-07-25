from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    table_number: int | None = None
    customer_name: str | None = None
    total_amount: Decimal = Decimal(0)
    status: str = "pending"


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    table_number: int | None = None
    customer_name: str | None = None
    total_amount: Decimal | None = None
    status: str | None = None


class OrderResponse(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
