from fastapi import FastAPI, APIRouter
app = FastAPI(
    title="DEEF",
    description="DEEF is a fastapi project",
    version="0.0.1",
    docs_url=None,
    redoc_url=None
)
router = APIRouter()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # หรือระบุเฉพาะ React URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
from components.database import Base, Mysql_Engine
from components.models import alchemymodels
# เรียกคำสั่งนี้ 1 ครั้ง เพื่อสร้างตารางทั้งหมดที่สืบทอดจาก Base
Base.metadata.create_all(bind=Mysql_Engine)
# -----------------------

from components.utils import apiLogin
app.include_router(apiLogin.router)

from components.routers import Users
app.include_router(Users.router)

from components.routers import aiforthai
app.include_router(aiforthai.router)

from components.routers import luxall
app.include_router(luxall.router)
