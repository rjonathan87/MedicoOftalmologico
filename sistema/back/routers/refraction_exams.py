from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/refraction_exams",
    tags=["Refraction Exams"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.RefractionExam)
def create_refraction_exam(refraction_exam: schemas.RefractionExamCreate, db: Session = Depends(get_db)):
    return crud.create_refraction_exam(db=db, refraction_exam=refraction_exam)

@router.get("/", response_model=List[schemas.RefractionExam])
def read_refraction_exams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    refraction_exams = crud.get_refraction_exams(db, skip=skip, limit=limit)
    return refraction_exams

@router.get("/{refraction_exam_id}", response_model=schemas.RefractionExam)
def read_refraction_exam(refraction_exam_id: int, db: Session = Depends(get_db)):
    db_refraction_exam = crud.get_refraction_exam(db, refraction_exam_id=refraction_exam_id)
    if db_refraction_exam is None:
        raise HTTPException(status_code=404, detail="Refraction Exam not found")
    return db_refraction_exam

@router.put("/{refraction_exam_id}", response_model=schemas.RefractionExam)
def update_refraction_exam(refraction_exam_id: int, refraction_exam: schemas.RefractionExamCreate, db: Session = Depends(get_db)):
    db_refraction_exam = crud.update_refraction_exam(db, refraction_exam_id=refraction_exam_id, refraction_exam=refraction_exam)
    if db_refraction_exam is None:
        raise HTTPException(status_code=404, detail="Refraction Exam not found")
    return db_refraction_exam

@router.delete("/{refraction_exam_id}", response_model=schemas.RefractionExam)
def delete_refraction_exam(refraction_exam_id: int, db: Session = Depends(get_db)):
    db_refraction_exam = crud.delete_refraction_exam(db, refraction_exam_id=refraction_exam_id)
    if db_refraction_exam is None:
        raise HTTPException(status_code=404, detail="Refraction Exam not found")
    return db_refraction_exam
