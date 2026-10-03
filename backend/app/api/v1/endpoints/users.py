from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from typing import List, Optional 
from pydantic import BaseModel, EmailStr 

from app.schemas import token as schemas 
from app.services.user_service import UserService 
from app.db.session import get_db # <-- เปลี่ยน Import มาที่ app.db.session 

router = APIRouter() 

# Pydantic Schema สำหรับรับข้อมูลเข้ามาอัปเดต (Request Body)
class UserUpdate(BaseModel): 
    email: Optional[EmailStr] = None 
    phone: Optional[str] = None 

# 1. GET /api/v1/users/{user_id} - ดึงข้อมูลผู้ใช้ตาม ID
@router.get("/{user_id}", response_model=schemas.User) 
async def get_user(user_id: int, db: Session = Depends(get_db)): 
    user = UserService.get_by_id(db, user_id) 
    if not user: 
        raise HTTPException( 
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found" 
        ) 
    return user 

# 1.1 GET all users
@router.get("/", response_model=List[schemas.User])
async def get_all_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    ดึงข้อมูลรายการผู้ใช้งานทั้งหมดในระบบ (รองรับ Pagination)
    - skip: จำนวนข้อมูลที่ต้องการข้าม (Default: 0)
    - limit: จำนวนข้อมูลสูงสุดที่คืนค่า (Default: 100)
    """
    users = UserService.get_all(db, skip=skip, limit=limit)
    return users

# 2. PUT /api/v1/users/{user_id} - อัปเดตข้อมูลผู้ใช้ตาม ID
@router.put("/{user_id}", response_model=schemas.User) 
async def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)): 
    # ตรวจสอบว่ามี User นี้อยู่ในระบบหรือไม่
    user = UserService.get_by_id(db, user_id) 
    if not user: 
        raise HTTPException( 
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found" 
        ) 

    # หากมีการขอเปลี่ยน Email ให้เช็คก่อนว่า Email ใหม่ถูกใช้งานไปแล้วหรือยัง
    if user_data.email is not None and user_data.email != user.email: 
        existing_user = UserService.get_by_email(db, user_data.email) 
        if existing_user and existing_user.id != user_id: 
            raise HTTPException( 
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Email already in use" 
            ) 
        user.email = user_data.email 

    # อัปเดตเบอร์โทรศัพท์ (ถ้ามีส่งมา)
    if user_data.phone is not None: 
        user.phone = user_data.phone 

    db.commit() 
    db.refresh(user) 
    return user