from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/surveys",
    tags=["Surveys"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Survey)
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    return crud.create_survey(db=db, survey=survey)

@router.get("/", response_model=List[schemas.Survey])
def read_surveys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    surveys = crud.get_surveys(db, skip=skip, limit=limit)
    return surveys

@router.get("/{survey_id}", response_model=schemas.Survey)
def read_survey(survey_id: int, db: Session = Depends(get_db)):
    db_survey = crud.get_survey(db, survey_id=survey_id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return db_survey

@router.put("/{survey_id}", response_model=schemas.Survey)
def update_survey(survey_id: int, survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    db_survey = crud.update_survey(db, survey_id=survey_id, survey=survey)
    if db_survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return db_survey

@router.delete("/{survey_id}", response_model=schemas.Survey)
def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    db_survey = crud.delete_survey(db, survey_id=survey_id)
    if db_survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return db_survey
