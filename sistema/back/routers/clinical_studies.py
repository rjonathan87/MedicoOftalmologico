from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/clinicalstudies",
    tags=["Clinical Studies"]
)

@router.post("/", response_model=schemas.ClinicalStudy)
def create_clinical_study(
    clinical_study: schemas.ClinicalStudyCreate, db: Session = Depends(get_db)
):
    return crud.create_clinical_study(db=db, clinical_study=clinical_study)

@router.get("/", response_model=List[schemas.ClinicalStudy])
def read_clinical_studies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clinical_studies = crud.get_clinical_studies(db, skip=skip, limit=limit)
    return clinical_studies

@router.get("/{clinical_study_id}", response_model=schemas.ClinicalStudy)
def read_clinical_study(clinical_study_id: int, db: Session = Depends(get_db)):
    db_clinical_study = crud.get_clinical_study(db, clinical_study_id=clinical_study_id)
    if db_clinical_study is None:
        raise HTTPException(status_code=404, detail="Clinical Study not found")
    return db_clinical_study

@router.put("/{clinical_study_id}", response_model=schemas.ClinicalStudy)
def update_clinical_study(
    clinical_study_id: int, clinical_study: schemas.ClinicalStudyCreate, db: Session = Depends(get_db)
):
    db_clinical_study = crud.update_clinical_study(db, clinical_study_id, clinical_study)
    if db_clinical_study is None:
        raise HTTPException(status_code=404, detail="Clinical Study not found")
    return db_clinical_study

@router.delete("/{clinical_study_id}", response_model=schemas.ClinicalStudy)
def delete_clinical_study(clinical_study_id: int, db: Session = Depends(get_db)):
    db_clinical_study = crud.delete_clinical_study(db, clinical_study_id=clinical_study_id)
    if db_clinical_study is None:
        raise HTTPException(status_code=404, detail="Clinical Study not found")
    return db_clinical_study
