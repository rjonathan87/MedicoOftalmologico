from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/inventory_items",
    tags=["Inventory Items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.InventoryItem)
def create_inventory_item(inventory_item: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    return crud.create_inventory_item(db=db, inventory_item=inventory_item)

@router.get("/", response_model=List[schemas.InventoryItem])
def read_inventory_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    inventory_items = crud.get_inventory_items(db, skip=skip, limit=limit)
    return inventory_items

@router.get("/{inventory_item_id}", response_model=schemas.InventoryItem)
def read_inventory_item(inventory_item_id: int, db: Session = Depends(get_db)):
    db_inventory_item = crud.get_inventory_item(db, inventory_item_id=inventory_item_id)
    if db_inventory_item is None:
        raise HTTPException(status_code=404, detail="Inventory Item not found")
    return db_inventory_item

@router.put("/{inventory_item_id}", response_model=schemas.InventoryItem)
def update_inventory_item(inventory_item_id: int, inventory_item: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    db_inventory_item = crud.update_inventory_item(db, inventory_item_id=inventory_item_id, inventory_item=inventory_item)
    if db_inventory_item is None:
        raise HTTPException(status_code=404, detail="Inventory Item not found")
    return db_inventory_item

@router.delete("/{inventory_item_id}", response_model=schemas.InventoryItem)
def delete_inventory_item(inventory_item_id: int, db: Session = Depends(get_db)):
    db_inventory_item = crud.delete_inventory_item(db, inventory_item_id=inventory_item_id)
    if db_inventory_item is None:
        raise HTTPException(status_code=404, detail="Inventory Item not found")
    return db_inventory_item
