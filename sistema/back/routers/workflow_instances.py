from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/workflow_instances",
    tags=["Workflow Instances"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.WorkflowInstance)
def create_workflow_instance(workflow_instance: schemas.WorkflowInstanceCreate, db: Session = Depends(get_db)):
    return crud.create_workflow_instance(db=db, workflow_instance=workflow_instance)

@router.get("/", response_model=List[schemas.WorkflowInstance])
def read_workflow_instances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workflow_instances = crud.get_workflow_instances(db, skip=skip, limit=limit)
    return workflow_instances

@router.get("/{workflow_instance_id}", response_model=schemas.WorkflowInstance)
def read_workflow_instance(workflow_instance_id: int, db: Session = Depends(get_db)):
    db_workflow_instance = crud.get_workflow_instance(db, workflow_instance_id=workflow_instance_id)
    if db_workflow_instance is None:
        raise HTTPException(status_code=404, detail="Workflow Instance not found")
    return db_workflow_instance

@router.put("/{workflow_instance_id}", response_model=schemas.WorkflowInstance)
def update_workflow_instance(workflow_instance_id: int, workflow_instance: schemas.WorkflowInstanceCreate, db: Session = Depends(get_db)):
    db_workflow_instance = crud.update_workflow_instance(db, workflow_instance_id=workflow_instance_id, workflow_instance=workflow_instance)
    if db_workflow_instance is None:
        raise HTTPException(status_code=404, detail="Workflow Instance not found")
    return db_workflow_instance

@router.delete("/{workflow_instance_id}", response_model=schemas.WorkflowInstance)
def delete_workflow_instance(workflow_instance_id: int, db: Session = Depends(get_db)):
    db_workflow_instance = crud.delete_workflow_instance(db, workflow_instance_id=workflow_instance_id)
    if db_workflow_instance is None:
        raise HTTPException(status_code=404, detail="Workflow Instance not found")
    return db_workflow_instance
