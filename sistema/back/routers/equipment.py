from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/equipment",
    tags=["Equipment"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Equipment)
def create_equipment(equipment: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    return crud.create_equipment(db=db, equipment=equipment)

@router.get("/", response_model=List[schemas.Equipment])
def read_equipment(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipment = crud.get_equipments(db, skip=skip, limit=limit)
    return equipment

@router.get("/{equipment_id}", response_model=schemas.Equipment)
def read_equipment_by_id(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = crud.get_equipment(db, equipment_id=equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment

@router.put("/{equipment_id}", response_model=schemas.Equipment)
def update_equipment(equipment_id: int, equipment: schemas.EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = crud.update_equipment(db, equipment_id=equipment_id, equipment=equipment)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment

@router.delete("/{equipment_id}", response_model=schemas.Equipment)
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = crud.delete_equipment(db, equipment_id=equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment
