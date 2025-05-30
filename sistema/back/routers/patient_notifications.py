from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/patient_notifications",
    tags=["Patient Notifications"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PatientNotification)
def create_patient_notification(patient_notification: schemas.PatientNotificationCreate, db: Session = Depends(get_db)):
    return crud.create_patient_notification(db=db, patient_notification=patient_notification)

@router.get("/", response_model=List[schemas.PatientNotification])
def read_patient_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patient_notifications = crud.get_patient_notifications(db, skip=skip, limit=limit)
    return patient_notifications

@router.get("/{patient_notification_id}", response_model=schemas.PatientNotification)
def read_patient_notification(patient_notification_id: int, db: Session = Depends(get_db)):
    db_patient_notification = crud.get_patient_notification(db, patient_notification_id=patient_notification_id)
    if db_patient_notification is None:
        raise HTTPException(status_code=404, detail="Patient Notification not found")
    return db_patient_notification

@router.put("/{patient_notification_id}", response_model=schemas.PatientNotification)
def update_patient_notification(patient_notification_id: int, patient_notification: schemas.PatientNotificationCreate, db: Session = Depends(get_db)):
    db_patient_notification = crud.update_patient_notification(db, patient_notification_id=patient_notification_id, patient_notification=patient_notification)
    if db_patient_notification is None:
        raise HTTPException(status_code=404, detail="Patient Notification not found")
    return db_patient_notification

@router.delete("/{patient_notification_id}", response_model=schemas.PatientNotification)
def delete_patient_notification(patient_notification_id: int, db: Session = Depends(get_db)):
    db_patient_notification = crud.delete_patient_notification(db, patient_notification_id=patient_notification_id)
    if db_patient_notification is None:
        raise HTTPException(status_code=404, detail="Patient Notification not found")
    return db_patient_notification
