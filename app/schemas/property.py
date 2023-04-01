from pydantic import BaseModel


class PropertyBase(BaseModel):
    property_number: str
    serial_number: str
    property_name: str
    brand_type: str
    vendor_name: str
    quantity: int
    cost: float
    current_value: float
    acquisition_date: str
    service_life: int
    custodian: str
    user: str
    location_id: str
    location: str
    location_remark: str
    custody_classification: str
    image: str
    remark: str = None


class PropertyCreate(PropertyBase):
    pass


class PropertyUpdate(PropertyBase):
    pass


class Property(PropertyBase):
    id: int

    class Config:
        orm_mode = True
