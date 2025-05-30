from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/prescriptions",
    tags=["Prescriptions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Prescription)
def create_prescription(prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    return crud.create_prescription(db=db, prescription=prescription)

@router.get("/", response_model=List[schemas.Prescription])
def read_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prescriptions = crud.get_prescriptions(db, skip=skip, limit=limit)
    return prescriptions

@router.get("/{prescription_id}", response_model=schemas.Prescription)
def read_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = crud.get_prescription(db, prescription_id=prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription

@router.put("/{prescription_id}", response_model=schemas.Prescription)
def update_prescription(prescription_id: int, prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    db_prescription = crud.update_prescription(db, prescription_id=prescription_id, prescription=prescription)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription

@router.delete("/{prescription_id}", response_model=schemas.Prescription)
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = crud.delete_prescription(db, prescription_id=prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription
