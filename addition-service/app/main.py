from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.routers.operations import router as operations_router

# קונפיגורציית לוגים
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("addition-service")

# אתחול אפליקציית FastAPI
app = FastAPI(
    title="שירות חיבור וחיסור",
    description="מיקרוסרוויס לפעולות חיבור וחיסור במחשבון מבוזר",
    version="1.0.0"
)

# הוספת CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # בסביבת ייצור, הגדר מקורות ספציפיים
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# כלילת ראוטרים
app.include_router(operations_router)

# נקודת קצה לבדיקת בריאות
@app.get("/health")
async def health_check():
    """נקודת קצה לבדיקת בריאות השירות"""
    logger.info("בקשת בדיקת בריאות התקבלה")
    return {"status": "healthy"}