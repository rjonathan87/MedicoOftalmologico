from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/optical_prescription_details",
    tags=["Optical Prescription Details"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.OpticalPrescriptionDetail)
def create_optical_prescription_detail(optical_prescription_detail: schemas.OpticalPrescriptionDetailCreate, db: Session = Depends(get_db)):
    return crud.create_optical_prescription_detail(db=db, optical_prescription_detail=optical_prescription_detail)

@router.get("/", response_model=List[schemas.OpticalPrescriptionDetail])
def read_optical_prescription_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    optical_prescription_details = crud.get_optical_prescription_details(db, skip=skip, limit=limit)
    return optical_prescription_details

@router.get("/{prescription_id}", response_model=schemas.OpticalPrescriptionDetail)
def read_optical_prescription_detail(prescription_id: int, db: Session = Depends(get_db)):
    db_optical_prescription_detail = crud.get_optical_prescription_detail(db, prescription_id=prescription_id)
    if db_optical_prescription_detail is None:
        raise HTTPException(status_code=404, detail="Optical Prescription Detail not found")
    return db_optical_prescription_detail

@router.put("/{prescription_id}", response_model=schemas.OpticalPrescriptionDetail)
def update_optical_prescription_detail(prescription_id: int, optical_prescription_detail: schemas.OpticalPrescriptionDetailCreate, db: Session = Depends(get_db)):
    db_optical_prescription_detail = crud.update_optical_prescription_detail(db, prescription_id=prescription_id, optical_prescription_detail=optical_prescription_detail)
    if db_optical_prescription_detail is None:
        raise HTTPException(status_code=404, detail="Optical Prescription Detail not found")
    return db_optical_prescription_detail

@router.delete("/{prescription_id}", response_model=schemas.OpticalPrescriptionDetail)
def delete_optical_prescription_detail(prescription_id: int, db: Session = Depends(get_db)):
    db_optical_prescription_detail = crud.delete_optical_prescription_detail(db, prescription_id=prescription_id)
    if db_optical_prescription_detail is None:
        raise HTTPException(status_code=404, detail="Optical Prescription Detail not found")
    return db_optical_prescription_detail
