from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from sqlite_utils import Database

app = FastAPI()

class Item(BaseModel):
    borrow_id: int
    item_name: str
    quantity: int
    purpose: str
    location: str
    borrow_date: str
    return_date: str
    handler: str
    note: str
    property_id: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/borrow")
def borrow_item(item: Item):
    # 建立資料庫連線
    conn = sqlite3.connect('property_management.db')

    # 檢查財產編號是否存在
    c = conn.cursor()
    c.execute("SELECT * FROM properties WHERE property_id = ?", (item.property_id,))
    row = c.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Property not found")

    # 插入借用記錄
    db = Database(conn)
    data = {
        "borrow_id": item.borrow_id,
        "item_name": item.item_name,
        "quantity": item.quantity,
        "purpose": item.purpose,
        "location": item.location,
        "borrow_date": item.borrow_date,
        "return_date": item.return_date,
        "handler": item.handler,
        "note": item.note,
        "property_id": item.property_id
    }
    db["borrow_records"].insert(data)

    # 關閉資料庫連線
    conn.close()

    return {"borrow_id": item.borrow_id}

