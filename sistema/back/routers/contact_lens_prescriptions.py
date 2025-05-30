from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/contactlensprescriptions",
    tags=["Contact Lens Prescriptions"]
)

@router.post("/", response_model=schemas.ContactLensPrescription)
def create_contact_lens_prescription(
    contact_lens_prescription: schemas.ContactLensPrescriptionCreate, db: Session = Depends(get_db)
):
    return crud.create_contact_lens_prescription(db=db, contact_lens_prescription=contact_lens_prescription)

@router.get("/", response_model=List[schemas.ContactLensPrescription])
def read_contact_lens_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contact_lens_prescriptions = crud.get_contact_lens_prescriptions(db, skip=skip, limit=limit)
    return contact_lens_prescriptions

@router.get("/{contact_lens_prescription_id}", response_model=schemas.ContactLensPrescription)
def read_contact_lens_prescription(contact_lens_prescription_id: int, db: Session = Depends(get_db)):
    db_contact_lens_prescription = crud.get_contact_lens_prescription(db, contact_lens_prescription_id=contact_lens_prescription_id)
    if db_contact_lens_prescription is None:
        raise HTTPException(status_code=404, detail="Contact Lens Prescription not found")
    return db_contact_lens_prescription

@router.put("/{contact_lens_prescription_id}", response_model=schemas.ContactLensPrescription)
def update_contact_lens_prescription(
    contact_lens_prescription_id: int, contact_lens_prescription: schemas.ContactLensPrescriptionCreate, db: Session = Depends(get_db)
):
    db_contact_lens_prescription = crud.update_contact_lens_prescription(db, contact_lens_prescription_id, contact_lens_prescription)
    if db_contact_lens_prescription is None:
        raise HTTPException(status_code=404, detail="Contact Lens Prescription not found")
    return db_contact_lens_prescription

@router.delete("/{contact_lens_prescription_id}", response_model=schemas.ContactLensPrescription)
def delete_contact_lens_prescription(contact_lens_prescription_id: int, db: Session = Depends(get_db)):
    db_contact_lens_prescription = crud.delete_contact_lens_prescription(db, contact_lens_prescription_id=contact_lens_prescription_id)
    if db_contact_lens_prescription is None:
        raise HTTPException(status_code=404, detail="Contact Lens Prescription not found")
    return db_contact_lens_prescription
