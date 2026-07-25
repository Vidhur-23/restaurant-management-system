from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db

from .schemas import InventoryItemCreate, InventoryItemResponse, InventoryItemUpdate
from .service import inventory_service

router = APIRouter(prefix="/inventory-items", tags=["Inventory"])


@router.post(
    "/", response_model=InventoryItemResponse, status_code=status.HTTP_201_CREATED
)
def create_inventory_item(data: InventoryItemCreate, db: Session = Depends(get_db)):
    return inventory_service.create(db, data)


@router.get("/", response_model=list[InventoryItemResponse])
def list_inventory_items(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return inventory_service.get_all(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=InventoryItemResponse)
def get_inventory_item(item_id: int, db: Session = Depends(get_db)):
    obj = inventory_service.get(db, item_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found"
        )
    return obj


@router.put("/{item_id}", response_model=InventoryItemResponse)
def update_inventory_item(
    item_id: int, data: InventoryItemUpdate, db: Session = Depends(get_db)
):
    obj = inventory_service.get(db, item_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found"
        )
    return inventory_service.update(db, obj, data)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_inventory_item(item_id: int, db: Session = Depends(get_db)):
    obj = inventory_service.get(db, item_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Inventory item not found"
        )
    inventory_service.delete(db, obj)
