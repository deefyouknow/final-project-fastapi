from fastapi import FastAPI, APIRouter , Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
app = FastAPI(title="ProjectOne2025", description="API for ProjectOne2025", version="1.0.0", 
    contact={"name": "deef", "email": "thanawat.deef@gmail.com"},
    docs_url=None,
    redoc_url=None
)
router = APIRouter()

from utils import apilogin
app.include_router(apilogin.router)

app.include_router(router)

from routers import user_router
app.include_router(user_router.router)
