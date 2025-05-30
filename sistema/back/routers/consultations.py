from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/consultations",
    tags=["Consultations"]
)

@router.post("/", response_model=schemas.Consultation)
def create_consultation(
    consultation: schemas.ConsultationCreate, db: Session = Depends(get_db)
):
    return crud.create_consultation(db=db, consultation=consultation)

@router.get("/", response_model=List[schemas.Consultation])
def read_consultations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    consultations = crud.get_consultations(db, skip=skip, limit=limit)
    return consultations

@router.get("/{consultation_id}", response_model=schemas.Consultation)
def read_consultation(consultation_id: int, db: Session = Depends(get_db)):
    db_consultation = crud.get_consultation(db, consultation_id=consultation_id)
    if db_consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return db_consultation

@router.put("/{consultation_id}", response_model=schemas.Consultation)
def update_consultation(
    consultation_id: int, consultation: schemas.ConsultationCreate, db: Session = Depends(get_db)
):
    db_consultation = crud.update_consultation(db, consultation_id, consultation)
    if db_consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return db_consultation

@router.delete("/{consultation_id}", response_model=schemas.Consultation)
def delete_consultation(consultation_id: int, db: Session = Depends(get_db)):
    db_consultation = crud.delete_consultation(db, consultation_id=consultation_id)
    if db_consultation is None:
        raise HTTPException(status_code=404, detail="Consultation not found")
    return db_consultation
