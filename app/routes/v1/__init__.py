from fastapi import APIRouter, Depends
from . import borrowing, property, user, login
from app.utils.security import get_current_user

router = APIRouter()


router.include_router(borrowing.router, prefix="/api/v1",dependencies=[Depends(get_current_user)], tags=["物品借用"])
router.include_router(property.router, prefix="/api/v1",dependencies=[Depends(get_current_user)], tags=["物品管理"])
router.include_router(user.router, prefix="/api/v1",dependencies=[Depends(get_current_user)], tags=["使用者管理"])
router.include_router(login.router, prefix="/api/v1", tags=["登入"])
