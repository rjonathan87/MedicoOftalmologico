from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/telemedicine_sessions",
    tags=["Telemedicine Sessions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.TelemedicineSession)
def create_telemedicine_session(telemedicine_session: schemas.TelemedicineSessionCreate, db: Session = Depends(get_db)):
    return crud.create_telemedicine_session(db=db, telemedicine_session=telemedicine_session)

@router.get("/", response_model=List[schemas.TelemedicineSession])
def read_telemedicine_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    telemedicine_sessions = crud.get_telemedicine_sessions(db, skip=skip, limit=limit)
    return telemedicine_sessions

@router.get("/{telemedicine_session_id}", response_model=schemas.TelemedicineSession)
def read_telemedicine_session(telemedicine_session_id: int, db: Session = Depends(get_db)):
    db_telemedicine_session = crud.get_telemedicine_session(db, telemedicine_session_id=telemedicine_session_id)
    if db_telemedicine_session is None:
        raise HTTPException(status_code=404, detail="Telemedicine Session not found")
    return db_telemedicine_session

@router.put("/{telemedicine_session_id}", response_model=schemas.TelemedicineSession)
def update_telemedicine_session(telemedicine_session_id: int, telemedicine_session: schemas.TelemedicineSessionCreate, db: Session = Depends(get_db)):
    db_telemedicine_session = crud.update_telemedicine_session(db, telemedicine_session_id=telemedicine_session_id, telemedicine_session=telemedicine_session)
    if db_telemedicine_session is None:
        raise HTTPException(status_code=404, detail="Telemedicine Session not found")
    return db_telemedicine_session

@router.delete("/{telemedicine_session_id}", response_model=schemas.TelemedicineSession)
def delete_telemedicine_session(telemedicine_session_id: int, db: Session = Depends(get_db)):
    db_telemedicine_session = crud.delete_telemedicine_session(db, telemedicine_session_id=telemedicine_session_id)
    if db_telemedicine_session is None:
        raise HTTPException(status_code=404, detail="Telemedicine Session not found")
    return db_telemedicine_session
