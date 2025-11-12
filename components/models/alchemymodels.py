from sqlalchemy import Column, Integer, String, desc, DateTime, func
from sqlalchemy.orm import relationship
from ..database import Base

class User_init(Base):
    __tablename__ = "usersssssss"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False) #nullable false คือต้องไม่เป็นค่าว่าง
    lastname = Column(String(100), nullable=True) #nullable false คือต้องไม่เป็นค่าว่าง

class lux_data(Base):
    __tablename__ = "lux_data2"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    lux_value = Column(Integer)
    data_time = Column(
        DateTime(timezone=True),
        server_default=func.convert_tz(func.now(), '+00:00', '+07:00'),
        nullable=False
    )
