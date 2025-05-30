from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/clinicalprotocols",
    tags=["Clinical Protocols"]
)

@router.post("/", response_model=schemas.ClinicalProtocol)
def create_clinical_protocol(
    clinical_protocol: schemas.ClinicalProtocolCreate, db: Session = Depends(get_db)
):
    return crud.create_clinical_protocol(db=db, clinical_protocol=clinical_protocol)

@router.get("/", response_model=List[schemas.ClinicalProtocol])
def read_clinical_protocols(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clinical_protocols = crud.get_clinical_protocols(db, skip=skip, limit=limit)
    return clinical_protocols

@router.get("/{clinical_protocol_id}", response_model=schemas.ClinicalProtocol)
def read_clinical_protocol(clinical_protocol_id: int, db: Session = Depends(get_db)):
    db_clinical_protocol = crud.get_clinical_protocol(db, clinical_protocol_id=clinical_protocol_id)
    if db_clinical_protocol is None:
        raise HTTPException(status_code=404, detail="Clinical Protocol not found")
    return db_clinical_protocol

@router.put("/{clinical_protocol_id}", response_model=schemas.ClinicalProtocol)
def update_clinical_protocol(
    clinical_protocol_id: int, clinical_protocol: schemas.ClinicalProtocolCreate, db: Session = Depends(get_db)
):
    db_clinical_protocol = crud.update_clinical_protocol(db, clinical_protocol_id, clinical_protocol)
    if db_clinical_protocol is None:
        raise HTTPException(status_code=404, detail="Clinical Protocol not found")
    return db_clinical_protocol

@router.delete("/{clinical_protocol_id}", response_model=schemas.ClinicalProtocol)
def delete_clinical_protocol(clinical_protocol_id: int, db: Session = Depends(get_db)):
    db_clinical_protocol = crud.delete_clinical_protocol(db, clinical_protocol_id=clinical_protocol_id)
    if db_clinical_protocol is None:
        raise HTTPException(status_code=404, detail="Clinical Protocol not found")
    return db_clinical_protocol
