from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/appointmentservices",
    tags=["Appointment Services"]
)

@router.post("/", response_model=schemas.AppointmentService)
def create_appointment_service(
    appointment_service: schemas.AppointmentServiceCreate, db: Session = Depends(get_db)
):
    return crud.create_appointment_service(db=db, appointment_service=appointment_service)

@router.get("/", response_model=List[schemas.AppointmentService])
def read_appointment_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointment_services = crud.get_appointment_services(db, skip=skip, limit=limit)
    return appointment_services

@router.get("/{appointment_id}/{service_id}", response_model=schemas.AppointmentService)
def read_appointment_service(appointment_id: int, service_id: int, db: Session = Depends(get_db)):
    db_appointment_service = crud.get_appointment_service(db, appointment_id=appointment_id, service_id=service_id)
    if db_appointment_service is None:
        raise HTTPException(status_code=404, detail="Appointment Service not found")
    return db_appointment_service

@router.delete("/{appointment_id}/{service_id}", response_model=schemas.AppointmentService)
def delete_appointment_service(appointment_id: int, service_id: int, db: Session = Depends(get_db)):
    db_appointment_service = crud.delete_appointment_service(db, appointment_id=appointment_id, service_id=service_id)
    if db_appointment_service is None:
        raise HTTPException(status_code=404, detail="Appointment Service not found")
    return db_appointment_service
