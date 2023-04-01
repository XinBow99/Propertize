from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from app.models.property import Property_model
from app.models.borrowing import Borrowing_model
from app.schemas.property import PropertyCreate, PropertyUpdate, Property
from typing import List

router = APIRouter()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/properties", response_model=List[Property])
def read_properties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    properties = db.query(Property_model).offset(skip).limit(limit).all()
    return properties

@router.get("/properties/{id}", response_model=Property)
def read_property(id: int, db: Session = Depends(get_db)):
    property = db.query(Property_model).filter(Property_model.id == id).first()
    if property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@router.post("/properties", response_model=Property)
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    db_property = Property_model(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

@router.put("/properties/{id}", response_model=Property)
def update_property(id: int, property: PropertyUpdate, db: Session = Depends(get_db)):
    db_property = db.query(Property_model).filter(Property_model.id == id).first()
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    update_data = property.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_property, key, value)
    db.commit()
    db.refresh(db_property)
    return db_property

@router.delete("/properties/{id}")
def delete_property(id: int, db: Session = Depends(get_db)):
    db_property = db.query(Property_model).filter(Property_model.id == id).first()
    if db_property is None:
        raise HTTPException(status_code=404, detail="Property not found")
    db.delete(db_property)
    db.commit()
    return {"message": "Property deleted successfully."}


# Path: app/main.py
# from fastapi import FastAPI
# from app.routes import property
