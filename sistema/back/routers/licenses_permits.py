from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/licenses_permits",
    tags=["Licenses and Permits"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.LicensePermit)
def create_license_permit(license_permit: schemas.LicensePermitCreate, db: Session = Depends(get_db)):
    return crud.create_license_permit(db=db, license_permit=license_permit)

@router.get("/", response_model=List[schemas.LicensePermit])
def read_licenses_permits(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    licenses_permits = crud.get_license_permits(db, skip=skip, limit=limit)
    return licenses_permits

@router.get("/{license_permit_id}", response_model=schemas.LicensePermit)
def read_license_permit(license_permit_id: int, db: Session = Depends(get_db)):
    db_license_permit = crud.get_license_permit(db, license_permit_id=license_permit_id)
    if db_license_permit is None:
        raise HTTPException(status_code=404, detail="License Permit not found")
    return db_license_permit

@router.put("/{license_permit_id}", response_model=schemas.LicensePermit)
def update_license_permit(license_permit_id: int, license_permit: schemas.LicensePermitCreate, db: Session = Depends(get_db)):
    db_license_permit = crud.update_license_permit(db, license_permit_id=license_permit_id, license_permit=license_permit)
    if db_license_permit is None:
        raise HTTPException(status_code=404, detail="License Permit not found")
    return db_license_permit

@router.delete("/{license_permit_id}", response_model=schemas.LicensePermit)
def delete_license_permit(license_permit_id: int, db: Session = Depends(get_db)):
    db_license_permit = crud.delete_license_permit(db, license_permit_id=license_permit_id)
    if db_license_permit is None:
        raise HTTPException(status_code=404, detail="License Permit not found")
    return db_license_permit
