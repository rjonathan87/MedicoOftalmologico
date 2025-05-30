from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/patient_communications",
    tags=["Patient Communications"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PatientCommunication)
def create_patient_communication(patient_communication: schemas.PatientCommunicationCreate, db: Session = Depends(get_db)):
    return crud.create_patient_communication(db=db, patient_communication=patient_communication)

@router.get("/", response_model=List[schemas.PatientCommunication])
def read_patient_communications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patient_communications = crud.get_patient_communications(db, skip=skip, limit=limit)
    return patient_communications

@router.get("/{patient_communication_id}", response_model=schemas.PatientCommunication)
def read_patient_communication(patient_communication_id: int, db: Session = Depends(get_db)):
    db_patient_communication = crud.get_patient_communication(db, patient_communication_id=patient_communication_id)
    if db_patient_communication is None:
        raise HTTPException(status_code=404, detail="Patient Communication not found")
    return db_patient_communication

@router.put("/{patient_communication_id}", response_model=schemas.PatientCommunication)
def update_patient_communication(patient_communication_id: int, patient_communication: schemas.PatientCommunicationCreate, db: Session = Depends(get_db)):
    db_patient_communication = crud.update_patient_communication(db, patient_communication_id=patient_communication_id, patient_communication=patient_communication)
    if db_patient_communication is None:
        raise HTTPException(status_code=404, detail="Patient Communication not found")
    return db_patient_communication

@router.delete("/{patient_communication_id}", response_model=schemas.PatientCommunication)
def delete_patient_communication(patient_communication_id: int, db: Session = Depends(get_db)):
    db_patient_communication = crud.delete_patient_communication(db, patient_communication_id=patient_communication_id)
    if db_patient_communication is None:
        raise HTTPException(status_code=404, detail="Patient Communication not found")
    return db_patient_communication
