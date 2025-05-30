from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/surgical_procedures",
    tags=["Surgical Procedures"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.SurgicalProcedure)
def create_surgical_procedure(surgical_procedure: schemas.SurgicalProcedureCreate, db: Session = Depends(get_db)):
    return crud.create_surgical_procedure(db=db, surgical_procedure=surgical_procedure)

@router.get("/", response_model=List[schemas.SurgicalProcedure])
def read_surgical_procedures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    surgical_procedures = crud.get_surgical_procedures(db, skip=skip, limit=limit)
    return surgical_procedures

@router.get("/{surgical_procedure_id}", response_model=schemas.SurgicalProcedure)
def read_surgical_procedure(surgical_procedure_id: int, db: Session = Depends(get_db)):
    db_surgical_procedure = crud.get_surgical_procedure(db, surgical_procedure_id=surgical_procedure_id)
    if db_surgical_procedure is None:
        raise HTTPException(status_code=404, detail="Surgical Procedure not found")
    return db_surgical_procedure

@router.put("/{surgical_procedure_id}", response_model=schemas.SurgicalProcedure)
def update_surgical_procedure(surgical_procedure_id: int, surgical_procedure: schemas.SurgicalProcedureCreate, db: Session = Depends(get_db)):
    db_surgical_procedure = crud.update_surgical_procedure(db, surgical_procedure_id=surgical_procedure_id, surgical_procedure=surgical_procedure)
    if db_surgical_procedure is None:
        raise HTTPException(status_code=404, detail="Surgical Procedure not found")
    return db_surgical_procedure

@router.delete("/{surgical_procedure_id}", response_model=schemas.SurgicalProcedure)
def delete_surgical_procedure(surgical_procedure_id: int, db: Session = Depends(get_db)):
    db_surgical_procedure = crud.delete_surgical_procedure(db, surgical_procedure_id=surgical_procedure_id)
    if db_surgical_procedure is None:
        raise HTTPException(status_code=404, detail="Surgical Procedure not found")
    return db_surgical_procedure
