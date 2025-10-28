# basemodel
from sqlalchemy import Column, Integer, String
# ตาราง ข้อมูลต้องมี Primary Key 1 ตัว
from database import Base

class UserLogin(Base):
    __tablename__ = "user_pass"   # ชื่อตารางในฐานข้อมูล
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fname = Column(String(99))
    lname = Column(String(99))
    phone = Column(Integer)
