from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/visual_acuity_exams",
    tags=["Visual Acuity Exams"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.VisualAcuityExam)
def create_visual_acuity_exam(visual_acuity_exam: schemas.VisualAcuityExamCreate, db: Session = Depends(get_db)):
    return crud.create_visual_acuity_exam(db=db, visual_acuity_exam=visual_acuity_exam)

@router.get("/", response_model=List[schemas.VisualAcuityExam])
def read_visual_acuity_exams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    visual_acuity_exams = crud.get_visual_acuity_exams(db, skip=skip, limit=limit)
    return visual_acuity_exams

@router.get("/{visual_acuity_exam_id}", response_model=schemas.VisualAcuityExam)
def read_visual_acuity_exam(visual_acuity_exam_id: int, db: Session = Depends(get_db)):
    db_visual_acuity_exam = crud.get_visual_acuity_exam(db, visual_acuity_exam_id=visual_acuity_exam_id)
    if db_visual_acuity_exam is None:
        raise HTTPException(status_code=404, detail="Visual Acuity Exam not found")
    return db_visual_acuity_exam

@router.put("/{visual_acuity_exam_id}", response_model=schemas.VisualAcuityExam)
def update_visual_acuity_exam(visual_acuity_exam_id: int, visual_acuity_exam: schemas.VisualAcuityExamCreate, db: Session = Depends(get_db)):
    db_visual_acuity_exam = crud.update_visual_acuity_exam(db, visual_acuity_exam_id=visual_acuity_exam_id, visual_acuity_exam=visual_acuity_exam)
    if db_visual_acuity_exam is None:
        raise HTTPException(status_code=404, detail="Visual Acuity Exam not found")
    return db_visual_acuity_exam

@router.delete("/{visual_acuity_exam_id}", response_model=schemas.VisualAcuityExam)
def delete_visual_acuity_exam(visual_acuity_exam_id: int, db: Session = Depends(get_db)):
    db_visual_acuity_exam = crud.delete_visual_acuity_exam(db, visual_acuity_exam_id=visual_acuity_exam_id)
    if db_visual_acuity_exam is None:
        raise HTTPException(status_code=404, detail="Visual Acuity Exam not found")
    return db_visual_acuity_exam
