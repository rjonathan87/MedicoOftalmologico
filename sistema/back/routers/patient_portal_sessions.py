from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/patient_portal_sessions",
    tags=["Patient Portal Sessions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PatientPortalSession)
def create_patient_portal_session(patient_portal_session: schemas.PatientPortalSessionCreate, db: Session = Depends(get_db)):
    return crud.create_patient_portal_session(db=db, patient_portal_session=patient_portal_session)

@router.get("/", response_model=List[schemas.PatientPortalSession])
def read_patient_portal_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patient_portal_sessions = crud.get_patient_portal_sessions(db, skip=skip, limit=limit)
    return patient_portal_sessions

@router.get("/{patient_portal_session_id}", response_model=schemas.PatientPortalSession)
def read_patient_portal_session(patient_portal_session_id: int, db: Session = Depends(get_db)):
    db_patient_portal_session = crud.get_patient_portal_session(db, patient_portal_session_id=patient_portal_session_id)
    if db_patient_portal_session is None:
        raise HTTPException(status_code=404, detail="Patient Portal Session not found")
    return db_patient_portal_session

@router.put("/{patient_portal_session_id}", response_model=schemas.PatientPortalSession)
def update_patient_portal_session(patient_portal_session_id: int, patient_portal_session: schemas.PatientPortalSessionCreate, db: Session = Depends(get_db)):
    db_patient_portal_session = crud.update_patient_portal_session(db, patient_portal_session_id=patient_portal_session_id, patient_portal_session=patient_portal_session)
    if db_patient_portal_session is None:
        raise HTTPException(status_code=404, detail="Patient Portal Session not found")
    return db_patient_portal_session

@router.delete("/{patient_portal_session_id}", response_model=schemas.PatientPortalSession)
def delete_patient_portal_session(patient_portal_session_id: int, db: Session = Depends(get_db)):
    db_patient_portal_session = crud.delete_patient_portal_session(db, patient_portal_session_id=patient_portal_session_id)
    if db_patient_portal_session is None:
        raise HTTPException(status_code=404, detail="Patient Portal Session not found")
    return db_patient_portal_session
