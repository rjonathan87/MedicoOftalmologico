from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/marketing_campaigns",
    tags=["Marketing Campaigns"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.MarketingCampaign)
def create_marketing_campaign(marketing_campaign: schemas.MarketingCampaignCreate, db: Session = Depends(get_db)):
    return crud.create_marketing_campaign(db=db, marketing_campaign=marketing_campaign)

@router.get("/", response_model=List[schemas.MarketingCampaign])
def read_marketing_campaigns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    marketing_campaigns = crud.get_marketing_campaigns(db, skip=skip, limit=limit)
    return marketing_campaigns

@router.get("/{marketing_campaign_id}", response_model=schemas.MarketingCampaign)
def read_marketing_campaign(marketing_campaign_id: int, db: Session = Depends(get_db)):
    db_marketing_campaign = crud.get_marketing_campaign(db, marketing_campaign_id=marketing_campaign_id)
    if db_marketing_campaign is None:
        raise HTTPException(status_code=404, detail="Marketing Campaign not found")
    return db_marketing_campaign

@router.put("/{marketing_campaign_id}", response_model=schemas.MarketingCampaign)
def update_marketing_campaign(marketing_campaign_id: int, marketing_campaign: schemas.MarketingCampaignCreate, db: Session = Depends(get_db)):
    db_marketing_campaign = crud.update_marketing_campaign(db, marketing_campaign_id=marketing_campaign_id, marketing_campaign=marketing_campaign)
    if db_marketing_campaign is None:
        raise HTTPException(status_code=404, detail="Marketing Campaign not found")
    return db_marketing_campaign

@router.delete("/{marketing_campaign_id}", response_model=schemas.MarketingCampaign)
def delete_marketing_campaign(marketing_campaign_id: int, db: Session = Depends(get_db)):
    db_marketing_campaign = crud.delete_marketing_campaign(db, marketing_campaign_id=marketing_campaign_id)
    if db_marketing_campaign is None:
        raise HTTPException(status_code=404, detail="Marketing Campaign not found")
    return db_marketing_campaign
