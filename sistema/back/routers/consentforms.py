from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/consentforms",
    tags=["Consent Forms"]
)

@router.post("/", response_model=schemas.ConsentForm)
def create_consent_form(
    consent_form: schemas.ConsentFormCreate, db: Session = Depends(get_db)
):
    return crud.create_consent_form(db=db, consent_form=consent_form)

@router.get("/", response_model=List[schemas.ConsentForm])
def read_consent_forms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    consent_forms = crud.get_consent_forms(db, skip=skip, limit=limit)
    return consent_forms

@router.get("/{consent_form_id}", response_model=schemas.ConsentForm)
def read_consent_form(consent_form_id: int, db: Session = Depends(get_db)):
    db_consent_form = crud.get_consent_form(db, consent_form_id=consent_form_id)
    if db_consent_form is None:
        raise HTTPException(status_code=404, detail="Consent Form not found")
    return db_consent_form

@router.put("/{consent_form_id}", response_model=schemas.ConsentForm)
def update_consent_form(
    consent_form_id: int, consent_form: schemas.ConsentFormCreate, db: Session = Depends(get_db)
):
    db_consent_form = crud.update_consent_form(db, consent_form_id, consent_form)
    if db_consent_form is None:
        raise HTTPException(status_code=404, detail="Consent Form not found")
    return db_consent_form

@router.delete("/{consent_form_id}", response_model=schemas.ConsentForm)
def delete_consent_form(consent_form_id: int, db: Session = Depends(get_db)):
    db_consent_form = crud.delete_consent_form(db, consent_form_id=consent_form_id)
    if db_consent_form is None:
        raise HTTPException(status_code=404, detail="Consent Form not found")
    return db_consent_form
