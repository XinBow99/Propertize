from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings
from app.models.token import Token_model
from app.models.user import User_model
from app.schemas.token import TokenPayload
from app.schemas.user import User
from app.utils.security import verify_password
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_
from database.db import SessionLocal

router = APIRouter()

# 設置用於驗證令牌的配置
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

# Dependency


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 定義用於創建令牌的函數
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


@router.post("/login", response_model=TokenPayload)
async def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # 查找用戶
    user = db.query(User_model).filter(or_(User_model.email == form_data.username.lower(
    ), User_model.username == form_data.username.lower())).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    # 驗證密碼
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    # 創建訪問令牌
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )

    # 儲存訪問令牌
    db_token = Token_model(
        access_token=access_token,
        token_type="bearer",
        user_id=user.id
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    # 返回令牌信息
    return {
        "access_token": db_token.access_token,
        "token_type": db_token.token_type
    }

@router.post("/logout")
async def logout(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    # 查找令牌是否存在於資料庫中
    db_token = db.query(Token_model).filter(Token_model.access_token == token).first()
    if not db_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    # 刪除令牌
    db.delete(db_token)
    db.commit()
    return {"detail": "Successfully logged out"}
