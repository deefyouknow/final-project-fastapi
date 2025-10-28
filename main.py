from fastapi import FastAPI, APIRouter  
app = FastAPI(title="ProjectOne2025", description="API for ProjectOne2025", version="1.0.0", contact={"name": "deef", "email": "thanawat.deef@gmail.com"})
router = APIRouter()

@router.get("/app")
def index():
    return {
        "msg" : "Hello World!"
    }
    
app.include_router(router)
