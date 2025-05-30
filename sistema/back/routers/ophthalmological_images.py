from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/ophthalmological_images",
    tags=["Ophthalmological Images"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.OphthalmologicalImage)
def create_ophthalmological_image(ophthalmological_image: schemas.OphthalmologicalImageCreate, db: Session = Depends(get_db)):
    return crud.create_ophthalmological_image(db=db, ophthalmological_image=ophthalmological_image)

@router.get("/", response_model=List[schemas.OphthalmologicalImage])
def read_ophthalmological_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ophthalmological_images = crud.get_ophthalmological_images(db, skip=skip, limit=limit)
    return ophthalmological_images

@router.get("/{ophthalmological_image_id}", response_model=schemas.OphthalmologicalImage)
def read_ophthalmological_image(ophthalmological_image_id: int, db: Session = Depends(get_db)):
    db_ophthalmological_image = crud.get_ophthalmological_image(db, ophthalmological_image_id=ophthalmological_image_id)
    if db_ophthalmological_image is None:
        raise HTTPException(status_code=404, detail="Ophthalmological Image not found")
    return db_ophthalmological_image

@router.put("/{ophthalmological_image_id}", response_model=schemas.OphthalmologicalImage)
def update_ophthalmological_image(ophthalmological_image_id: int, ophthalmological_image: schemas.OphthalmologicalImageCreate, db: Session = Depends(get_db)):
    db_ophthalmological_image = crud.update_ophthalmological_image(db, ophthalmological_image_id=ophthalmological_image_id, ophthalmological_image=ophthalmological_image)
    if db_ophthalmological_image is None:
        raise HTTPException(status_code=404, detail="Ophthalmological Image not found")
    return db_ophthalmological_image

@router.delete("/{ophthalmological_image_id}", response_model=schemas.OphthalmologicalImage)
def delete_ophthalmological_image(ophthalmological_image_id: int, db: Session = Depends(get_db)):
    db_ophthalmological_image = crud.delete_ophthalmological_image(db, ophthalmological_image_id=ophthalmological_image_id)
    if db_ophthalmological_image is None:
        raise HTTPException(status_code=404, detail="Ophthalmological Image not found")
    return db_ophthalmological_image
