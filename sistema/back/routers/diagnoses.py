from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/diagnoses",
    tags=["Diagnoses"]
)

@router.post("/", response_model=schemas.Diagnosis)
def create_diagnosis(
    diagnosis: schemas.DiagnosisCreate, db: Session = Depends(get_db)
):
    return crud.create_diagnosis(db=db, diagnosis=diagnosis)

@router.get("/", response_model=List[schemas.Diagnosis])
def read_diagnoses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    diagnoses = crud.get_diagnoses(db, skip=skip, limit=limit)
    return diagnoses

@router.get("/{diagnosis_id}", response_model=schemas.Diagnosis)
def read_diagnosis(diagnosis_id: int, db: Session = Depends(get_db)):
    db_diagnosis = crud.get_diagnosis(db, diagnosis_id=diagnosis_id)
    if db_diagnosis is None:
        raise HTTPException(status_code=404, detail="Diagnosis not found")
    return db_diagnosis

@router.put("/{diagnosis_id}", response_model=schemas.Diagnosis)
def update_diagnosis(
    diagnosis_id: int, diagnosis: schemas.DiagnosisCreate, db: Session = Depends(get_db)
):
    db_diagnosis = crud.update_diagnosis(db, diagnosis_id, diagnosis)
    if db_diagnosis is None:
        raise HTTPException(status_code=404, detail="Diagnosis not found")
    return db_diagnosis

@router.delete("/{diagnosis_id}", response_model=schemas.Diagnosis)
def delete_diagnosis(diagnosis_id: int, db: Session = Depends(get_db)):
    db_diagnosis = crud.delete_diagnosis(db, diagnosis_id=diagnosis_id)
    if db_diagnosis is None:
        raise HTTPException(status_code=404, detail="Diagnosis not found")
    return db_diagnosis
