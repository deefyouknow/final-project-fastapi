from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
import requests
from io import BytesIO
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("AIFORTHAILINK")
API_KEY = os.getenv("AIFORTHAIKEY")
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB

app = FastAPI()
router = APIRouter()

# ✅ เปิดให้ React เข้าถึงได้
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.post("/proxy_capgen")
async def proxy_capgen(file: UploadFile = File(...)):
    try:
        # อ่านข้อมูลไฟล์
        file_bytes = await file.read()

        # ถ้าเกิน 2 MB → ย่อไฟล์อัตโนมัติ
        if len(file_bytes) > MAX_FILE_SIZE:
            try:
                image = Image.open(BytesIO(file_bytes))
            except Exception:
                raise HTTPException(status_code=400, detail="❌ ไม่สามารถเปิดไฟล์ภาพได้")

            scale = 1.0
            compressed_bytes = file_bytes
            while len(compressed_bytes) > MAX_FILE_SIZE and scale > 0.2:
                # ลดขนาดภาพลง
                new_w = int(image.width * scale)
                new_h = int(image.height * scale)
                resized = image.resize((new_w, new_h))
                buffer = BytesIO()
                resized.save(buffer, format="PNG", optimize=True, quality=80)
                compressed_bytes = buffer.getvalue()
                scale *= 0.85

            file_bytes = compressed_bytes

        # เตรียมข้อมูลส่งต่อไป AIForThai
        files = {"file": (file.filename, file_bytes, file.content_type)}
        headers = {"apikey": API_KEY}

        # ส่งต่อไป API
        response = requests.post(API_URL, headers=headers, files=files)
        response.raise_for_status()

        # ส่งต่อผลลัพธ์ JSON กลับให้ React
        return response.json()

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"API request error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")


# ลงทะเบียน router
app.include_router(router)
