from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from app.models.property import Property_model
from app.models.borrowing import Borrowing_model
from app.schemas.borrowing import BorrowingCreate, BorrowingUpdate, Borrowing
from typing import List


router = APIRouter()

# Dependency
def get_db():
    """
    Dependency to get a database session.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/borrowings", response_model=List[Borrowing])
def read_borrowings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    borrowings = db.query(Borrowing_model).offset(skip).limit(limit).all()
    return borrowings

@router.get("/borrowings/{id}", response_model=Borrowing)
def read_borrowing(id: int, db: Session = Depends(get_db)):
    borrowing = db.query(Borrowing_model).filter(Borrowing_model.id == id).first()
    if borrowing is None:
        raise HTTPException(status_code=404, detail="Borrowing record not found")
    return borrowing

@router.post("/borrowings", response_model=Borrowing)
def create_borrowing(borrowing: BorrowingCreate, db: Session = Depends(get_db)):
    property = db.query(Property_model).filter(Property_model.id == borrowing.property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    if property.quantity <= 0:
        raise HTTPException(status_code=400, detail="No available properties for borrowing")
    db_borrowing = Borrowing_model(**borrowing.dict())
    db.add(db_borrowing)
    property.quantity -= 1
    db.commit()
    db.refresh(db_borrowing)
    return db_borrowing


@router.put("/borrowings/{id}", response_model=Borrowing)
def update_borrowing(id: int, borrowing: BorrowingUpdate, db: Session = Depends(get_db)):
    db_borrowing = db.query(Borrowing_model).filter(Borrowing_model.id == id).first()
    if db_borrowing is None:
        raise HTTPException(status_code=404, detail="Borrowing record not found")
    update_data = borrowing.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_borrowing, key, value)
    db.commit()
    db.refresh(db_borrowing)
    return db_borrowing

@router.delete("/borrowings/{id}")
def delete_borrowing(id: int, db: Session = Depends(get_db)):
    db_borrowing = db.query(Borrowing_model).filter(Borrowing_model.id == id).first()
    if db_borrowing is None:
        raise HTTPException(status_code=404, detail="Borrowing record not found")

    # 取得被歸還物品的 property_id
    property_id = db_borrowing.property_id
    # 取得物品資訊
    db_property = db.query(Property_model).filter(Property_model.id == property_id).first()
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")

    # 將該物品的 quantity 加 1
    db_property.quantity += 1
    db.commit()
    
    # 刪除借用紀錄
    db.delete(db_borrowing)
    db.commit()
    return {"message": "Borrowing record deleted successfully."}


# Path: app/main.py
# from fastapi import FastAPI
# from app.routes import property
