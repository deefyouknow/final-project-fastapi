# **การเขียน API ด้วย FastAPI**

### **ติดตั้ง** Virtual Environment (venv)

- คำสั่งด้านล่างหมายถึง**การ**สร้าง virtual environment ที่ชื่อ .venv
- venv to .venv จะ**ได้**โฟลเดอร์ .venv ที่มีไฟล์ .venv/bin/activate ไว้ใช้ในการ**เปิด** virtual environment

```bash
python3 -m venv .venv
```

- **เริ่ม**การใช้งาน virtual environment

```bash
source .venv/bin/activate 
```

- **ปิด**การใช้งาน virtual environment

```bash
source .venv/bin/deactivate 
```

---

### **Libraly** ที่ใช้ทั้งหมดในโปรเจค

- สร้าง Rest API **ด้วย** FastAPI

```bash
pip install fastapi
```

- รันเซิฟเวอร์แบบ async 

> main:app ตัว app มาจาก app = FastAPI()

> - สามารถรัน  
Swagger UI → http://127.0.0.1:8000/docs  
ReDoc → http://127.0.0.1:8000/redoc 

- **syntax** ของตารางในฐานการรัน FastAPI
  - **uvicorn** **เป็น**โปรแกรม ASGI ที่รันแอปพลิเคชัน FastAPI
  - main มา**จาก**ชื่อไฟล main.py
  - --reload คือ รีโหลดไฟล์**เมื่อ**มีการแก้ไข  
  - --host คือ **กำ**หนด IP ที่จะ**ใช้**รันเซิฟเวอร์  
  - --port คือ **กำ**หนด Port ที่จะ**ใช้**รันเซิฟเวอร์  
  - --workers คือ **กำ**หนดจำนวนโปรเซส หรือ cpu

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 1234 --workers 4
```

- **Orm** จัดการฐานข้อมูลด้วย SQLAlchemy

```bash
pip install sqlalchemy
```

- ตรวจสอบและแปลงข้อมูล (schema validation) pydantic

```bash
pip install pydantic
```

- ตัวเชื่อมต่อ MySQL (เลือกอย่างใดอย่างหนึ่ง) mysqlclient หรือ aiomysql

- ความต่าง aiomysql = asynchronous (async/await) , mysqlclient = synchronous (ปกติ)

```bash
pip install aiomysql
# หรือ
pip install mysqlclient
```

- โหลดค่าจากไฟล์ .env เช่น DB_URL python-dotenv (แนะนำ)

> .env คืออะไร  
ไฟล์ .env ใช้เก็บ ค่าความลับ และ ค่าคอนฟิก เช่น  
- รหัสผ่านฐานข้อมูล  
- URL ของ Database  
- Secret keys  
- API token

```bash
pip install python-dotenv
```

---

### **วิธี**ใช้ .env

- เรียกใช้ library dotenv ด้วย `load_dotenv()`

```python
from dotenv import load_dotenv
```

- ทำไมต้อง import os  
ใน Python ระบบ environment variable ไม่ถูกโหลดอัตโนมัติ  
ต้องใช้สองอย่างร่วมกัน:

```python
# โหลดค่าจากไฟล์ .env
load_dotenv()
import os
```

- อ่านค่าตัวแปร DB_URL ใช้ os.getenv("กรอกชื่อตัวแปรในไฟล .environment")

```python
DATABASE_URL = os.getenv("DB_URL")
```

- จัดการ migration ตารางในฐานข้อมูล alembic (ทางเลือก)

```bash
pip install alembic
```

### __pycache__ คืออะไร

- มันถูกสร้างอัตโนมัติเมื่อ Python import ไฟล์ .py  
เก็บไฟล์ compiled .pyc เพื่อให้ import ครั้งต่อไปเร็วขึ้น  
ไม่ต้องสร้างเอง และไม่ต้องแก้ไข  
ควรเพิ่มใน .gitignore เช่น __pycache__/

---

### **รวม**การ import ทั้งหมก**ใน** 1 ไฟล

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
```

# **โครงสร้าง Tree Project**

```bash
project/
│
├── main.py                # จุดเริ่มโปรแกรม FastAPI
├── readme.md              # คู่มือโปรเจกต์
├── .gitignore             # รายการไฟล์ที่ไม่ให้ Git เก็บ
├── .env                   # ตัวแปร environment เช่น DB_URL
├── .venv/                 # Virtual environment (ไม่ push)
│
├── scripts/               # รวมสคริปต์แยกหมวด เช่น DB, Sensor, API test
│   ├── db_init.py
│   ├── lux_sensor_test.py
│   └── user_test_api.py
│
├── routers/               # รวม API routes แยกหมวด
│   ├── user_router.py
│   └── sensor_router.py
│
├── models/                # ORM และ schema
│   ├── models.py
│   └── schemas.py
│
├── database.py            # จัดการเชื่อมต่อฐานข้อมูล
└── utils/                 # ฟังก์ชันช่วยเหลือทั่วไป
    ├── helper.py
    └── auth.py
```

# ? **เพิ่มเติม**

### การ**ใช้** APIrouter

```python
from fastapi import FastAPI, APIRouter
app = FastAPI(title="ชื่อโปรเจกต์", description="คำอธิบายโปรเจกต์")
router = APIRouter()
# เรียกใช้ด้วย 
app.include_router(router)
```

### ถ้าอยู่**คนล**ะโฟลเดอร์

```python
from namefolder import filename
app.include_router(filename.router)
```

# **อธิบายองค์ประกอบของ Structure**

### **🧩 1. ORM (Object Relational Mapping)**

> อยู่**ใน** models/models.py  
คือ “**ตัวแทน**ของตารางในฐานข้อมูล”  
ใช้ SQLAlchemy ทำให้เขียนโค้ดแทนคำสั่ง SQL ได้โดยไม่ต้องเขียน SQL เอง  
**ตัวอย่าง** ORM model

```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "user"     # ชื่อตารางใน MySQL
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100))
```

→ **ORM** นี้จะสร้างตาราง **user** ใน DB **พร้อม**คอลัมน์ id, name, email

### **📦 2. Schema (Pydantic model)**

> อยู่ใน **models**/schemas.py  
คือ “โครงสร้างข้อมูลที่รับ–ส่ง**ผ่าน** API”  
ใช้ Pydantic.BaseModel ตรวจสอบชนิดข้อมูลและป้องกัน error เวลา client ส่ง JSON เข้ามา  
**ตัวอย่าง** schema

```python 
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True  # ใช้ให้ FastAPI แปลง ORM → JSON ได้
```

- **ORM** = ของฝั่งฐานข้อมูล
- **Schema** = ของฝั่ง **API** (request/response)

### **⚙️ 3. Routers**

> อยู่ใน routers/  
คือที่รวม endpoint (@router.get(), @router.post(), @router.put(), @router.delete())  
เช่น **user_router.py**

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import models, schemas

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

> → **พวก** router.get, router.post, router.put, router.delete คือ REST API **action** ทั้งหมด

## 🔗 **สรุปภาพรวมการทำงาน**

```bash
Client (React, Postman)
   ↓
FastAPI Router (GET/POST/PUT/DELETE)
   ↓
Schema (ตรวจข้อมูลเข้า/ออก)
   ↓
ORM (ทำงานกับตารางใน DB)
   ↓
MySQL
```
