from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db

from .schemas import MenuItemCreate, MenuItemResponse, MenuItemUpdate
from .service import menu_service

router = APIRouter(prefix="/menu-items", tags=["Menu"])


@router.post("/", response_model=MenuItemResponse, status_code=status.HTTP_201_CREATED)
def create_menu_item(data: MenuItemCreate, db: Session = Depends(get_db)):
    return menu_service.create(db, data)


@router.get("/", response_model=list[MenuItemResponse])
def list_menu_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return menu_service.get_all(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=MenuItemResponse)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    obj = menu_service.get(db, item_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found"
        )
    return obj


@router.put("/{item_id}", response_model=MenuItemResponse)
def update_menu_item(
    item_id: int, data: MenuItemUpdate, db: Session = Depends(get_db)
):
    obj = menu_service.get(db, item_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found"
        )
    return menu_service.update(db, obj, data)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    obj = menu_service.get(db, item_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu item not found"
        )
    menu_service.delete(db, obj)
