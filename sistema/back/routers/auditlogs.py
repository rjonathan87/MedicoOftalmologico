from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/auditlogs",
    tags=["Audit Logs"]
)

@router.post("/", response_model=schemas.AuditLog)
def create_audit_log(
    audit_log: schemas.AuditLogCreate, db: Session = Depends(get_db)
):
    return crud.create_audit_log(db=db, audit_log=audit_log)

@router.get("/", response_model=List[schemas.AuditLog])
def read_audit_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    audit_logs = crud.get_audit_logs(db, skip=skip, limit=limit)
    return audit_logs

@router.get("/{audit_log_id}", response_model=schemas.AuditLog)
def read_audit_log(audit_log_id: int, db: Session = Depends(get_db)):
    db_audit_log = crud.get_audit_log(db, audit_log_id=audit_log_id)
    if db_audit_log is None:
        raise HTTPException(status_code=404, detail="Audit Log not found")
    return db_audit_log

@router.put("/{audit_log_id}", response_model=schemas.AuditLog)
def update_audit_log(
    audit_log_id: int, audit_log: schemas.AuditLogCreate, db: Session = Depends(get_db)
):
    db_audit_log = crud.update_audit_log(db, audit_log_id, audit_log)
    if db_audit_log is None:
        raise HTTPException(status_code=404, detail="Audit Log not found")
    return db_audit_log

@router.delete("/{audit_log_id}", response_model=schemas.AuditLog)
def delete_audit_log(audit_log_id: int, db: Session = Depends(get_db)):
    db_audit_log = crud.delete_audit_log(db, audit_log_id=audit_log_id)
    if db_audit_log is None:
        raise HTTPException(status_code=404, detail="Audit Log not found")
    return db_audit_log
