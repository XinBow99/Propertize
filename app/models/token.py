from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from app.models.base import Base
from app.models.user import User_model

class Token_model(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String(255), unique=True, index=True)
    token_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)

    user = relationship(User_model)

    @classmethod
    def create(cls, access_token: str, token_type: str, user_id: int, expires_delta: timedelta):
        expires_at = datetime.utcnow() + expires_delta
        token = cls(access_token=access_token, token_type=token_type, user_id=user_id, expires_at=expires_at)
        return token
