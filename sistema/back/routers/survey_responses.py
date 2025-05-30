from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/survey_responses",
    tags=["Survey Responses"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.SurveyResponse)
def create_survey_response(survey_response: schemas.SurveyResponseCreate, db: Session = Depends(get_db)):
    return crud.create_survey_response(db=db, survey_response=survey_response)

@router.get("/", response_model=List[schemas.SurveyResponse])
def read_survey_responses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    survey_responses = crud.get_survey_responses(db, skip=skip, limit=limit)
    return survey_responses

@router.get("/{survey_response_id}", response_model=schemas.SurveyResponse)
def read_survey_response(survey_response_id: int, db: Session = Depends(get_db)):
    db_survey_response = crud.get_survey_response(db, survey_response_id=survey_response_id)
    if db_survey_response is None:
        raise HTTPException(status_code=404, detail="Survey Response not found")
    return db_survey_response

@router.put("/{survey_response_id}", response_model=schemas.SurveyResponse)
def update_survey_response(survey_response_id: int, survey_response: schemas.SurveyResponseCreate, db: Session = Depends(get_db)):
    db_survey_response = crud.update_survey_response(db, survey_response_id=survey_response_id, survey_response=survey_response)
    if db_survey_response is None:
        raise HTTPException(status_code=404, detail="Survey Response not found")
    return db_survey_response

@router.delete("/{survey_response_id}", response_model=schemas.SurveyResponse)
def delete_survey_response(survey_response_id: int, db: Session = Depends(get_db)):
    db_survey_response = crud.delete_survey_response(db, survey_response_id=survey_response_id)
    if db_survey_response is None:
        raise HTTPException(status_code=404, detail="Survey Response not found")
    return db_survey_response
