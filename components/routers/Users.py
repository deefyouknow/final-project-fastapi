from fastapi import APIRouter
from typing import Union

# prefix กำหนd root เริ่มต้น tage จัดหมวดหมู่ ไม่มีผลต่อการใช้งานในส่วนของ tag
router = APIRouter(prefix="/users", tags=["Users"])
from ..database import get_db
from ..models.alchemymodels import User_init
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy import Integer, String
from ..models.schemas import User
    
@router.post("/post_user")
async def post_user(user: User, db: Session = Depends(get_db)):
    result = User_init(
        firstname = user.firstname,
        lastname = user.lastname
    )
    db.add(result)
    db.commit()
    db.refresh(result)
    return {
        "msg": "success",
        "first name": result.firstname,
        "last name": result.lastname
    }
