from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db

from .schemas import ReservationCreate, ReservationResponse, ReservationUpdate
from .service import reservation_service

router = APIRouter(prefix="/reservations", tags=["Reservations"])


@router.post(
    "/", response_model=ReservationResponse, status_code=status.HTTP_201_CREATED
)
def create_reservation(data: ReservationCreate, db: Session = Depends(get_db)):
    return reservation_service.create(db, data)


@router.get("/", response_model=list[ReservationResponse])
def list_reservations(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return reservation_service.get_all(db, skip=skip, limit=limit)


@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    obj = reservation_service.get(db, reservation_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found"
        )
    return obj


@router.put("/{reservation_id}", response_model=ReservationResponse)
def update_reservation(
    reservation_id: int, data: ReservationUpdate, db: Session = Depends(get_db)
):
    obj = reservation_service.get(db, reservation_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found"
        )
    return reservation_service.update(db, obj, data)


@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    obj = reservation_service.get(db, reservation_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Reservation not found"
        )
    reservation_service.delete(db, obj)
