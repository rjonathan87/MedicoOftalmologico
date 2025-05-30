from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/dataaccesslogs",
    tags=["Data Access Logs"]
)

@router.post("/", response_model=schemas.DataAccessLog)
def create_data_access_log(
    data_access_log: schemas.DataAccessLogCreate, db: Session = Depends(get_db)
):
    return crud.create_data_access_log(db=db, data_access_log=data_access_log)

@router.get("/", response_model=List[schemas.DataAccessLog])
def read_data_access_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data_access_logs = crud.get_data_access_logs(db, skip=skip, limit=limit)
    return data_access_logs

@router.get("/{data_access_log_id}", response_model=schemas.DataAccessLog)
def read_data_access_log(data_access_log_id: int, db: Session = Depends(get_db)):
    db_data_access_log = crud.get_data_access_log(db, data_access_log_id=data_access_log_id)
    if db_data_access_log is None:
        raise HTTPException(status_code=404, detail="Data Access Log not found")
    return db_data_access_log

@router.put("/{data_access_log_id}", response_model=schemas.DataAccessLog)
def update_data_access_log(
    data_access_log_id: int, data_access_log: schemas.DataAccessLogCreate, db: Session = Depends(get_db)
):
    db_data_access_log = crud.update_data_access_log(db, data_access_log_id, data_access_log)
    if db_data_access_log is None:
        raise HTTPException(status_code=404, detail="Data Access Log not found")
    return db_data_access_log

@router.delete("/{data_access_log_id}", response_model=schemas.DataAccessLog)
def delete_data_access_log(data_access_log_id: int, db: Session = Depends(get_db)):
    db_data_access_log = crud.delete_data_access_log(db, data_access_log_id=data_access_log_id)
    if db_data_access_log is None:
        raise HTTPException(status_code=404, detail="Data Access Log not found")
    return db_data_access_log
