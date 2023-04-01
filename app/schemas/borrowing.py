from pydantic import BaseModel
from datetime import datetime, timezone


class BorrowingBase(BaseModel):
    borrower: str
    property_id: int
    start_date: datetime
    end_date: datetime
    remark: str = None

class BorrowingCreate(BorrowingBase):
    pass

class BorrowingUpdate(BorrowingBase):
    pass

class Borrowing(BorrowingBase):
    id: int

    class Config:
        orm_mode = True
