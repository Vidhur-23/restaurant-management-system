from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReservationBase(BaseModel):
    customer_name: str
    phone: str | None = None
    party_size: int
    reservation_time: datetime
    notes: str | None = None


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(BaseModel):
    customer_name: str | None = None
    phone: str | None = None
    party_size: int | None = None
    reservation_time: datetime | None = None
    notes: str | None = None


class ReservationResponse(ReservationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
