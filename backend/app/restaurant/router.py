from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db

from .schemas import RestaurantCreate, RestaurantResponse, RestaurantUpdate
from .service import restaurant_service

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.post("/", response_model=RestaurantResponse, status_code=status.HTTP_201_CREATED)
def create_restaurant(data: RestaurantCreate, db: Session = Depends(get_db)):
    return restaurant_service.create(db, data)


@router.get("/", response_model=list[RestaurantResponse])
def list_restaurants(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return restaurant_service.get_all(db, skip=skip, limit=limit)


@router.get("/{restaurant_id}", response_model=RestaurantResponse)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    obj = restaurant_service.get(db, restaurant_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found"
        )
    return obj


@router.put("/{restaurant_id}", response_model=RestaurantResponse)
def update_restaurant(
    restaurant_id: int, data: RestaurantUpdate, db: Session = Depends(get_db)
):
    obj = restaurant_service.get(db, restaurant_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found"
        )
    return restaurant_service.update(db, obj, data)


@router.delete("/{restaurant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    obj = restaurant_service.get(db, restaurant_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found"
        )
    restaurant_service.delete(db, obj)
