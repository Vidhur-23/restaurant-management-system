from datetime import datetime, time

from pydantic import BaseModel, ConfigDict


class RestaurantBase(BaseModel):
    name: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None
    opening_time: time | None = None
    closing_time: time | None = None


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantUpdate(BaseModel):
    name: str | None = None
    address: str | None = None
    phone: str | None = None
    email: str | None = None
    opening_time: time | None = None
    closing_time: time | None = None


class RestaurantResponse(RestaurantBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
