from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crud import crud
from schemas import schemas
from models import models
from database import get_db

router = APIRouter(
    prefix="/invoice_items",
    tags=["Invoice Items"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.InvoiceItem)
def create_invoice_item(invoice_item: schemas.InvoiceItemCreate, db: Session = Depends(get_db)):
    return crud.create_invoice_item(db=db, invoice_item=invoice_item)

@router.get("/", response_model=List[schemas.InvoiceItem])
def read_invoice_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    invoice_items = crud.get_invoice_items(db, skip=skip, limit=limit)
    return invoice_items

@router.get("/{invoice_item_id}", response_model=schemas.InvoiceItem)
def read_invoice_item(invoice_item_id: int, db: Session = Depends(get_db)):
    db_invoice_item = crud.get_invoice_item(db, invoice_item_id=invoice_item_id)
    if db_invoice_item is None:
        raise HTTPException(status_code=404, detail="Invoice Item not found")
    return db_invoice_item

@router.put("/{invoice_item_id}", response_model=schemas.InvoiceItem)
def update_invoice_item(invoice_item_id: int, invoice_item: schemas.InvoiceItemCreate, db: Session = Depends(get_db)):
    db_invoice_item = crud.update_invoice_item(db, invoice_item_id=invoice_item_id, invoice_item=invoice_item)
    if db_invoice_item is None:
        raise HTTPException(status_code=404, detail="Invoice Item not found")
    return db_invoice_item

@router.delete("/{invoice_item_id}", response_model=schemas.InvoiceItem)
def delete_invoice_item(invoice_item_id: int, db: Session = Depends(get_db)):
    db_invoice_item = crud.delete_invoice_item(db, invoice_item_id=invoice_item_id)
    if db_invoice_item is None:
        raise HTTPException(status_code=404, detail="Invoice Item not found")
    return db_invoice_item
