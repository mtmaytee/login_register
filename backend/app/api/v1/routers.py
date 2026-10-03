from fastapi import APIRouter 
from app.api.v1.endpoints import auth, users 

router = APIRouter() 

# รวม Endpoints สำหรับระบบ ยืนยันตัวตน (Login/Register) 
router.include_router(auth.router, prefix="/auth", tags=["Authentication"]) 

# รวม Endpoints สำหรับจัดการข้อมูลผู้ใช้งาน 
router.include_router(users.router, prefix="/users", tags=["Users"])