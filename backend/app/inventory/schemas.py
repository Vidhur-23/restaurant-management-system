from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class InventoryItemBase(BaseModel):
    name: str
    quantity: Decimal = Decimal(0)
    unit: str | None = None
    minimum_quantity: Decimal = Decimal(0)
    cost_per_unit: Decimal = Decimal(0)


class InventoryItemCreate(InventoryItemBase):
    pass


class InventoryItemUpdate(BaseModel):
    name: str | None = None
    quantity: Decimal | None = None
    unit: str | None = None
    minimum_quantity: Decimal | None = None
    cost_per_unit: Decimal | None = None


class InventoryItemResponse(InventoryItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
