from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/triage_assessments",
    tags=["Triage Assessments"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.TriageAssessment)
def create_triage_assessment(triage_assessment: schemas.TriageAssessmentCreate, db: Session = Depends(get_db)):
    return crud.create_triage_assessment(db=db, triage_assessment=triage_assessment)

@router.get("/", response_model=List[schemas.TriageAssessment])
def read_triage_assessments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    triage_assessments = crud.get_triage_assessments(db, skip=skip, limit=limit)
    return triage_assessments

@router.get("/{triage_assessment_id}", response_model=schemas.TriageAssessment)
def read_triage_assessment(triage_assessment_id: int, db: Session = Depends(get_db)):
    db_triage_assessment = crud.get_triage_assessment(db, triage_assessment_id=triage_assessment_id)
    if db_triage_assessment is None:
        raise HTTPException(status_code=404, detail="Triage Assessment not found")
    return db_triage_assessment

@router.put("/{triage_assessment_id}", response_model=schemas.TriageAssessment)
def update_triage_assessment(triage_assessment_id: int, triage_assessment: schemas.TriageAssessmentCreate, db: Session = Depends(get_db)):
    db_triage_assessment = crud.update_triage_assessment(db, triage_assessment_id=triage_assessment_id, triage_assessment=triage_assessment)
    if db_triage_assessment is None:
        raise HTTPException(status_code=404, detail="Triage Assessment not found")
    return db_triage_assessment

@router.delete("/{triage_assessment_id}", response_model=schemas.TriageAssessment)
def delete_triage_assessment(triage_assessment_id: int, db: Session = Depends(get_db)):
    db_triage_assessment = crud.delete_triage_assessment(db, triage_assessment_id=triage_assessment_id)
    if db_triage_assessment is None:
        raise HTTPException(status_code=404, detail="Triage Assessment not found")
    return db_triage_assessment
