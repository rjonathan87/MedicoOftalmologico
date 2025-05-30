from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/security_policies",
    tags=["Security Policies"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.SecurityPolicy)
def create_security_policy(security_policy: schemas.SecurityPolicyCreate, db: Session = Depends(get_db)):
    return crud.create_security_policy(db=db, security_policy=security_policy)

@router.get("/", response_model=List[schemas.SecurityPolicy])
def read_security_policies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    security_policies = crud.get_security_policies(db, skip=skip, limit=limit)
    return security_policies

@router.get("/{security_policy_id}", response_model=schemas.SecurityPolicy)
def read_security_policy(security_policy_id: int, db: Session = Depends(get_db)):
    db_security_policy = crud.get_security_policy(db, security_policy_id=security_policy_id)
    if db_security_policy is None:
        raise HTTPException(status_code=404, detail="Security Policy not found")
    return db_security_policy

@router.put("/{security_policy_id}", response_model=schemas.SecurityPolicy)
def update_security_policy(security_policy_id: int, security_policy: schemas.SecurityPolicyCreate, db: Session = Depends(get_db)):
    db_security_policy = crud.update_security_policy(db, security_policy_id=security_policy_id, security_policy=security_policy)
    if db_security_policy is None:
        raise HTTPException(status_code=404, detail="Security Policy not found")
    return db_security_policy

@router.delete("/{security_policy_id}", response_model=schemas.SecurityPolicy)
def delete_security_policy(security_policy_id: int, db: Session = Depends(get_db)):
    db_security_policy = crud.delete_security_policy(db, security_policy_id=security_policy_id)
    if db_security_policy is None:
        raise HTTPException(status_code=404, detail="Security Policy not found")
    return db_security_policy
