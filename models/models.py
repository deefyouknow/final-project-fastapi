# basemodel
from sqlalchemy import Column, Integer, String
# ตาราง ข้อมูลต้องมี Primary Key 1 ตัว
from database import Base

from sqlalchemy import create_engine, Column, Integer, String, desc, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

# ----------------------
# table name = user_pass
class UserLogin(Base):
    __tablename__ = "user_pass"   # ชื่อตารางในฐานข้อมูล
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fname = Column(String(99))
    lname = Column(String(99))
    phone = Column(Integer)
# ----------------------

class lux_data(Base):
    __tablename__ = "lux_data2"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lux_value = Column(Integer)
    data_time = Column(
        DateTime(timezone=True),
        server_default=func.convert_tz(func.now(), '+00:00', '+07:00'),
        nullable=False
    )
