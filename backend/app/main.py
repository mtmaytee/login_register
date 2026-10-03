from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 

# นำเข้า settings จาก app/core/config.py 
from app.core.config import settings 

# นำเข้า router หลักจาก app/api/v1/routers.py 
from app.api.v1.routers import router as api_router 

# หมายเหตุ: เอา Base.metadata.create_all(bind=engine) ออกแล้ว 
# เนื่องจากฐานข้อมูล PostgreSQL ถูกสร้างและจัดการตารางล่วงหน้าผ่านไฟล์ scripts/init.sql เรียบร้อยแล้ว

# สร้าง instance ของ FastAPI 
app = FastAPI( 
    title=settings.PROJECT_NAME, 
    openapi_url=f"{settings.API_V1_STR}/openapi.json" 
) 

# ตั้งค่า CORS Middleware อนุญาตให้ Frontend ส่ง Request เข้ามาได้ 
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=settings.BACKEND_CORS_ORIGINS, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
) 

# รวม API Routers ทั้งหมดภายใต้ Prefix /api/v1 
app.include_router(api_router, prefix=settings.API_V1_STR) 

@app.get("/") 
async def root(): 
    return {"message": "Welcome to Login/Register API"}