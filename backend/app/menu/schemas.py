from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class MenuItemBase(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    category: str | None = None
    available: bool = True


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    category: str | None = None
    available: bool | None = None


class MenuItemResponse(MenuItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
