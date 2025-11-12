from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Adjust the imports below to match your project's file structure
from ..database import get_db

router = APIRouter()

from ..models.alchemymodels import lux_data

@router.get("/all/lux_values")
def get_all_lux_values(db: Session = Depends(get_db)):
    x = db.query(lux_data).all()
    return { "msg": x }
