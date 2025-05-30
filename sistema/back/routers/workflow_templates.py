from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud
from models import models
from schemas import schemas
from database import get_db

router = APIRouter(
    prefix="/workflow_templates",
    tags=["Workflow Templates"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.WorkflowTemplate)
def create_workflow_template(workflow_template: schemas.WorkflowTemplateCreate, db: Session = Depends(get_db)):
    return crud.create_workflow_template(db=db, workflow_template=workflow_template)

@router.get("/", response_model=List[schemas.WorkflowTemplate])
def read_workflow_templates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workflow_templates = crud.get_workflow_templates(db, skip=skip, limit=limit)
    return workflow_templates

@router.get("/{workflow_template_id}", response_model=schemas.WorkflowTemplate)
def read_workflow_template(workflow_template_id: int, db: Session = Depends(get_db)):
    db_workflow_template = crud.get_workflow_template(db, workflow_template_id=workflow_template_id)
    if db_workflow_template is None:
        raise HTTPException(status_code=404, detail="Workflow Template not found")
    return db_workflow_template

@router.put("/{workflow_template_id}", response_model=schemas.WorkflowTemplate)
def update_workflow_template(workflow_template_id: int, workflow_template: schemas.WorkflowTemplateCreate, db: Session = Depends(get_db)):
    db_workflow_template = crud.update_workflow_template(db, workflow_template_id=workflow_template_id, workflow_template=workflow_template)
    if db_workflow_template is None:
        raise HTTPException(status_code=404, detail="Workflow Template not found")
    return db_workflow_template

@router.delete("/{workflow_template_id}", response_model=schemas.WorkflowTemplate)
def delete_workflow_template(workflow_template_id: int, db: Session = Depends(get_db)):
    db_workflow_template = crud.delete_workflow_template(db, workflow_template_id=workflow_template_id)
    if db_workflow_template is None:
        raise HTTPException(status_code=404, detail="Workflow Template not found")
    return db_workflow_template
