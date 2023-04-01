from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base

class Borrowing_model(Base):
    __tablename__ = "borrowings"

    id = Column(Integer, primary_key=True, index=True)
    borrower = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"))
    property = relationship("Property_model", back_populates="borrowings")
    remark = Column(String, nullable=True)

