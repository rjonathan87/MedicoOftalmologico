from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/iop_exams",
    tags=["IOP Exams"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.IOPExam)
def create_iop_exam(iop_exam: schemas.IOPExamCreate, db: Session = Depends(get_db)):
    return crud.create_iop_exam(db=db, iop_exam=iop_exam)

@router.get("/", response_model=List[schemas.IOPExam])
def read_iop_exams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    iop_exams = crud.get_iop_exams(db, skip=skip, limit=limit)
    return iop_exams

@router.get("/{iop_exam_id}", response_model=schemas.IOPExam)
def read_iop_exam(iop_exam_id: int, db: Session = Depends(get_db)):
    db_iop_exam = crud.get_iop_exam(db, iop_exam_id=iop_exam_id)
    if db_iop_exam is None:
        raise HTTPException(status_code=404, detail="IOP Exam not found")
    return db_iop_exam

@router.put("/{iop_exam_id}", response_model=schemas.IOPExam)
def update_iop_exam(iop_exam_id: int, iop_exam: schemas.IOPExamCreate, db: Session = Depends(get_db)):
    db_iop_exam = crud.update_iop_exam(db, iop_exam_id=iop_exam_id, iop_exam=iop_exam)
    if db_iop_exam is None:
        raise HTTPException(status_code=404, detail="IOP Exam not found")
    return db_iop_exam

@router.delete("/{iop_exam_id}", response_model=schemas.IOPExam)
def delete_iop_exam(iop_exam_id: int, db: Session = Depends(get_db)):
    db_iop_exam = crud.delete_iop_exam(db, iop_exam_id=iop_exam_id)
    if db_iop_exam is None:
        raise HTTPException(status_code=404, detail="IOP Exam not found")
    return db_iop_exam
