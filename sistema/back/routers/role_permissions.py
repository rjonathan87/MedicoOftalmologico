from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/role_permissions",
    tags=["Role Permissions"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.RolePermission)
def create_role_permission(role_permission: schemas.RolePermissionCreate, db: Session = Depends(get_db)):
    return crud.create_role_permission(db=db, role_permission=role_permission)

@router.get("/", response_model=List[schemas.RolePermission])
def read_role_permissions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    role_permissions = crud.get_role_permissions(db, skip=skip, limit=limit)
    return role_permissions

@router.get("/{role_id}/{permission_id}", response_model=schemas.RolePermission)
def read_role_permission(role_id: int, permission_id: int, db: Session = Depends(get_db)):
    db_role_permission = crud.get_role_permission(db, role_id=role_id, permission_id=permission_id)
    if db_role_permission is None:
        raise HTTPException(status_code=404, detail="Role Permission not found")
    return db_role_permission

@router.delete("/{role_id}/{permission_id}", response_model=schemas.RolePermission)
def delete_role_permission(role_id: int, permission_id: int, db: Session = Depends(get_db)):
    db_role_permission = crud.delete_role_permission(db, role_id=role_id, permission_id=permission_id)
    if db_role_permission is None:
        raise HTTPException(status_code=404, detail="Role Permission not found")
    return db_role_permission
