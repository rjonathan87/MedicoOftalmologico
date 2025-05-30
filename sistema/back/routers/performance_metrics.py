from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/performance_metrics",
    tags=["Performance Metrics"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PerformanceMetric)
def create_performance_metric(performance_metric: schemas.PerformanceMetricCreate, db: Session = Depends(get_db)):
    return crud.create_performance_metric(db=db, performance_metric=performance_metric)

@router.get("/", response_model=List[schemas.PerformanceMetric])
def read_performance_metrics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    performance_metrics = crud.get_performance_metrics(db, skip=skip, limit=limit)
    return performance_metrics

@router.get("/{performance_metric_id}", response_model=schemas.PerformanceMetric)
def read_performance_metric(performance_metric_id: int, db: Session = Depends(get_db)):
    db_performance_metric = crud.get_performance_metric(db, performance_metric_id=performance_metric_id)
    if db_performance_metric is None:
        raise HTTPException(status_code=404, detail="Performance Metric not found")
    return db_performance_metric

@router.put("/{performance_metric_id}", response_model=schemas.PerformanceMetric)
def update_performance_metric(performance_metric_id: int, performance_metric: schemas.PerformanceMetricCreate, db: Session = Depends(get_db)):
    db_performance_metric = crud.update_performance_metric(db, performance_metric_id=performance_metric_id, performance_metric=performance_metric)
    if db_performance_metric is None:
        raise HTTPException(status_code=404, detail="Performance Metric not found")
    return db_performance_metric

@router.delete("/{performance_metric_id}", response_model=schemas.PerformanceMetric)
def delete_performance_metric(performance_metric_id: int, db: Session = Depends(get_db)):
    db_performance_metric = crud.delete_performance_metric(db, performance_metric_id=performance_metric_id)
    if db_performance_metric is None:
        raise HTTPException(status_code=404, detail="Performance Metric not found")
    return db_performance_metric
