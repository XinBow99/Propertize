from sqlalchemy import create_engine
from app.models.base import Base
from app.models.user import User_model
from app.models.token import Token_model
from app.models.borrowing import Borrowing_model
from app.models.property import Property_model


# 連接到 SQLite 資料庫
engine = create_engine('sqlite:///database/property_management.db', connect_args={"check_same_thread": False})

# 建立資料表
Base.metadata.create_all(bind=engine, tables=[
    User_model.metadata.tables['users'], 
    Token_model.metadata.tables['tokens'],
    Borrowing_model.metadata.tables['borrowings'],
    Property_model.metadata.tables['properties']
    ])
