from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/patient_documents",
    tags=["Patient Documents"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PatientDocument)
def create_patient_document(patient_document: schemas.PatientDocumentCreate, db: Session = Depends(get_db)):
    return crud.create_patient_document(db=db, patient_document=patient_document)

@router.get("/", response_model=List[schemas.PatientDocument])
def read_patient_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patient_documents = crud.get_patient_documents(db, skip=skip, limit=limit)
    return patient_documents

@router.get("/{patient_document_id}", response_model=schemas.PatientDocument)
def read_patient_document(patient_document_id: int, db: Session = Depends(get_db)):
    db_patient_document = crud.get_patient_document(db, patient_document_id=patient_document_id)
    if db_patient_document is None:
        raise HTTPException(status_code=404, detail="Patient Document not found")
    return db_patient_document

@router.put("/{patient_document_id}", response_model=schemas.PatientDocument)
def update_patient_document(patient_document_id: int, patient_document: schemas.PatientDocumentCreate, db: Session = Depends(get_db)):
    db_patient_document = crud.update_patient_document(db, patient_document_id=patient_document_id, patient_document=patient_document)
    if db_patient_document is None:
        raise HTTPException(status_code=404, detail="Patient Document not found")
    return db_patient_document

@router.delete("/{patient_document_id}", response_model=schemas.PatientDocument)
def delete_patient_document(patient_document_id: int, db: Session = Depends(get_db)):
    db_patient_document = crud.delete_patient_document(db, patient_document_id=patient_document_id)
    if db_patient_document is None:
        raise HTTPException(status_code=404, detail="Patient Document not found")
    return db_patient_document
