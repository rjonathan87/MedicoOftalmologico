from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/educational_resources",
    tags=["Educational Resources"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.EducationalResource)
def create_educational_resource(educational_resource: schemas.EducationalResourceCreate, db: Session = Depends(get_db)):
    return crud.create_educational_resource(db=db, educational_resource=educational_resource)

@router.get("/", response_model=List[schemas.EducationalResource])
def read_educational_resources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    educational_resources = crud.get_educational_resources(db, skip=skip, limit=limit)
    return educational_resources

@router.get("/{educational_resource_id}", response_model=schemas.EducationalResource)
def read_educational_resource(educational_resource_id: int, db: Session = Depends(get_db)):
    db_educational_resource = crud.get_educational_resource(db, educational_resource_id=educational_resource_id)
    if db_educational_resource is None:
        raise HTTPException(status_code=404, detail="Educational Resource not found")
    return db_educational_resource

@router.put("/{educational_resource_id}", response_model=schemas.EducationalResource)
def update_educational_resource(educational_resource_id: int, educational_resource: schemas.EducationalResourceCreate, db: Session = Depends(get_db)):
    db_educational_resource = crud.update_educational_resource(db, educational_resource_id=educational_resource_id, educational_resource=educational_resource)
    if db_educational_resource is None:
        raise HTTPException(status_code=404, detail="Educational Resource not found")
    return db_educational_resource

@router.delete("/{educational_resource_id}", response_model=schemas.EducationalResource)
def delete_educational_resource(educational_resource_id: int, db: Session = Depends(get_db)):
    db_educational_resource = crud.delete_educational_resource(db, educational_resource_id=educational_resource_id)
    if db_educational_resource is None:
        raise HTTPException(status_code=404, detail="Educational Resource not found")
    return db_educational_resource
