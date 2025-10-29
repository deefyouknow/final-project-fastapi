from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas import UserRegister
from models.models import UserLogin, lux_data
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["User"])

from dotenv import load_dotenv
import os
load_dotenv()

@router.post("/")
def loginpost(tableuser: UserRegister ,db: Session = Depends(get_db)):
    # x = query.tableuser.filter(tableuser.fname == tableuser.lname).first()
    result = UserLogin(fname=tableuser.fname, lname=tableuser.lname)
    db.add(result)
    db.commit()
    db.refresh(result)
    return {
        "msg" : "success",
        "fname" : result.fname,
        "lname" : result.lname,
        "all" : x.__dict__
    }
    
@router.get("/all")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(UserLogin).all()
    return users

@router.get("all/lux_values")
def get_all_lux_values(db: Session = Depends(get_db)):
    x = db.query(lux_data).all()
    return { "msg": x }
