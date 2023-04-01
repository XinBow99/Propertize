from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.borrowing import Borrowing_model


class Property_model(Base):
    __tablename__ = "properties"
    
    id = Column(Integer, primary_key=True, index=True)
    property_number = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    property_name = Column(String, nullable=False)
    brand_type = Column(String, nullable=False)
    vendor_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    current_value = Column(Integer, nullable=False)
    acquisition_date = Column(String, nullable=False)
    service_life = Column(Integer, nullable=False)
    custodian = Column(String, nullable=False)
    user = Column(String, nullable=False)
    location_id = Column(String, nullable=False)
    location = Column(String, nullable=False)
    location_remark = Column(String, nullable=False)
    custody_classification = Column(String, nullable=False)
    image = Column(String, nullable=False)
    remark = Column(String, nullable=False)
    borrowings = relationship(Borrowing_model, back_populates="property")
