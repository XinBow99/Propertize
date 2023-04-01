from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from app.models.user import User_model
from app.schemas.user import UserCreate, UserUpdate, User as UserSchema
from app.utils.security import hash_password
from sqlalchemy.exc import IntegrityError
from typing import List

router = APIRouter()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/users", response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print("current_user")
    users = db.query(User_model).offset(skip).limit(limit).all()
    return users


@router.get("/users/{id}", response_model=UserSchema)
def read_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User_model).filter(User_model.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User_model(
            email=user.email.lower(),
            password=hash_password(user.password),
            full_name=user.full_name,
            username=user.username.lower(),
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        if "UNIQUE constraint failed: users.username" in str(e):
            raise HTTPException(status_code=400, detail="Username already exists")
        elif "UNIQUE constraint failed: users.email" in str(e):
            raise HTTPException(status_code=400, detail="Email already exists")
        else:
            raise HTTPException(status_code=400, detail="Bad Request")


@router.put("/users/{id}", response_model=UserSchema)
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User_model).filter(User_model.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(User_model).filter(User_model.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully."}
