from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/permissions",
    tags=["Permissions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Permission)
def create_permission(permission: schemas.PermissionCreate, db: Session = Depends(get_db)):
    return crud.create_permission(db=db, permission=permission)

@router.get("/", response_model=List[schemas.Permission])
def read_permissions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    permissions = crud.get_permissions(db, skip=skip, limit=limit)
    return permissions

@router.get("/{permission_id}", response_model=schemas.Permission)
def read_permission(permission_id: int, db: Session = Depends(get_db)):
    db_permission = crud.get_permission(db, permission_id=permission_id)
    if db_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return db_permission

@router.put("/{permission_id}", response_model=schemas.Permission)
def update_permission(permission_id: int, permission: schemas.PermissionCreate, db: Session = Depends(get_db)):
    db_permission = crud.update_permission(db, permission_id=permission_id, permission=permission)
    if db_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return db_permission

@router.delete("/{permission_id}", response_model=schemas.Permission)
def delete_permission(permission_id: int, db: Session = Depends(get_db)):
    db_permission = crud.delete_permission(db, permission_id=permission_id)
    if db_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return db_permission
