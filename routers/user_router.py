from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas import UserRegister
from models.models import UserLogin
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["User"])

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
        "lname" : result.lname
    }
