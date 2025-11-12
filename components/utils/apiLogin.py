# ---------------------------------------------------------------------
# หนัาล็อกอิน /docs and /redocs
from fastapi import FastAPI, APIRouter , Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()
router = APIRouter(tags=["Login"])

from dotenv import load_dotenv
import os
load_dotenv()

def verify(credentials: HTTPBasicCredentials = Depends(security)):
    if not (credentials.username == os.getenv("docsredoc_user") and credentials.password == os.getenv("docsredoc_pass")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

@router.get("/", dependencies=[Depends(verify)])
def root():
    return {"msg": "secured"}

# ✅ ป้องกันหน้า docs และ redoc
@router.get("/docs", include_in_schema=False)
def get_docs_auth(ok: bool = Depends(verify)):
    from fastapi.openapi.docs import get_swagger_ui_html
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Secure Docs")

@router.get("/redoc", include_in_schema=False)
def get_redoc_auth(ok: bool = Depends(verify)):
    from fastapi.openapi.docs import get_redoc_html
    return get_redoc_html(openapi_url="/openapi.json", title="Secure Redoc")
