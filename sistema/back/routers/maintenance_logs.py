from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/maintenance_logs",
    tags=["Maintenance Logs"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.MaintenanceLog)
def create_maintenance_log(maintenance_log: schemas.MaintenanceLogCreate, db: Session = Depends(get_db)):
    return crud.create_maintenance_log(db=db, maintenance_log=maintenance_log)

@router.get("/", response_model=List[schemas.MaintenanceLog])
def read_maintenance_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    maintenance_logs = crud.get_maintenance_logs(db, skip=skip, limit=limit)
    return maintenance_logs

@router.get("/{maintenance_log_id}", response_model=schemas.MaintenanceLog)
def read_maintenance_log(maintenance_log_id: int, db: Session = Depends(get_db)):
    db_maintenance_log = crud.get_maintenance_log(db, maintenance_log_id=maintenance_log_id)
    if db_maintenance_log is None:
        raise HTTPException(status_code=404, detail="Maintenance Log not found")
    return db_maintenance_log

@router.put("/{maintenance_log_id}", response_model=schemas.MaintenanceLog)
def update_maintenance_log(maintenance_log_id: int, maintenance_log: schemas.MaintenanceLogCreate, db: Session = Depends(get_db)):
    db_maintenance_log = crud.update_maintenance_log(db, maintenance_log_id=maintenance_log_id, maintenance_log=maintenance_log)
    if db_maintenance_log is None:
        raise HTTPException(status_code=404, detail="Maintenance Log not found")
    return db_maintenance_log

@router.delete("/{maintenance_log_id}", response_model=schemas.MaintenanceLog)
def delete_maintenance_log(maintenance_log_id: int, db: Session = Depends(get_db)):
    db_maintenance_log = crud.delete_maintenance_log(db, maintenance_log_id=maintenance_log_id)
    if db_maintenance_log is None:
        raise HTTPException(status_code=404, detail="Maintenance Log not found")
    return db_maintenance_log
