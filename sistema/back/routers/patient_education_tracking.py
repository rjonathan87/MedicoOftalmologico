from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/patient_education_tracking",
    tags=["Patient Education Tracking"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PatientEducationTracking)
def create_patient_education_tracking(patient_education_tracking: schemas.PatientEducationTrackingCreate, db: Session = Depends(get_db)):
    return crud.create_patient_education_tracking(db=db, patient_education_tracking=patient_education_tracking)

@router.get("/", response_model=List[schemas.PatientEducationTracking])
def read_patient_education_tracking(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patient_education_tracking = crud.get_patient_education_trackings(db, skip=skip, limit=limit)
    return patient_education_tracking

@router.get("/{patient_education_tracking_id}", response_model=schemas.PatientEducationTracking)
def read_patient_education_tracking_by_id(patient_education_tracking_id: int, db: Session = Depends(get_db)):
    db_patient_education_tracking = crud.get_patient_education_tracking(db, patient_education_tracking_id=patient_education_tracking_id)
    if db_patient_education_tracking is None:
        raise HTTPException(status_code=404, detail="Patient Education Tracking not found")
    return db_patient_education_tracking

@router.put("/{patient_education_tracking_id}", response_model=schemas.PatientEducationTracking)
def update_patient_education_tracking(patient_education_tracking_id: int, patient_education_tracking: schemas.PatientEducationTrackingCreate, db: Session = Depends(get_db)):
    db_patient_education_tracking = crud.update_patient_education_tracking(db, patient_education_tracking_id=patient_education_tracking_id, patient_education_tracking=patient_education_tracking)
    if db_patient_education_tracking is None:
        raise HTTPException(status_code=404, detail="Patient Education Tracking not found")
    return db_patient_education_tracking

@router.delete("/{patient_education_tracking_id}", response_model=schemas.PatientEducationTracking)
def delete_patient_education_tracking(patient_education_tracking_id: int, db: Session = Depends(get_db)):
    db_patient_education_tracking = crud.delete_patient_education_tracking(db, patient_education_tracking_id=patient_education_tracking_id)
    if db_patient_education_tracking is None:
        raise HTTPException(status_code=404, detail="Patient Education Tracking not found")
    return db_patient_education_tracking
