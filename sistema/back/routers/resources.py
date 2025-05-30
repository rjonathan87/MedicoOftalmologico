from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/resources",
    tags=["Resources"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Resource)
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return crud.create_resource(db=db, resource=resource)

@router.get("/", response_model=List[schemas.Resource])
def read_resources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resources = crud.get_resources(db, skip=skip, limit=limit)
    return resources

@router.get("/{resource_id}", response_model=schemas.Resource)
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = crud.get_resource(db, resource_id=resource_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return db_resource

@router.put("/{resource_id}", response_model=schemas.Resource)
def update_resource(resource_id: int, resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    db_resource = crud.update_resource(db, resource_id=resource_id, resource=resource)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return db_resource

@router.delete("/{resource_id}", response_model=schemas.Resource)
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    db_resource = crud.delete_resource(db, resource_id=resource_id)
    if db_resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return db_resource
