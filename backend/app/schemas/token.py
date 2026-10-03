# D:\login_register\backend\app\schemas\token.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# 1. Schema สำหรับ Response ตอบกลับเมื่อ Login สำเร็จ
class Token(BaseModel): 
    access_token: str 
    refresh_token: str
    token_type: str = "bearer" 

class RefreshTokenRequest(BaseModel):  # 👈 เพิ่ม Schema ใหม่
    refresh_token: str

# 2. Schema สำหรับข้อมูลที่ถอดได้จาก Payload ของ JWT Token
class TokenData(BaseModel): 
    email: Optional[str] = None 

# 3. Schema สำหรับรับข้อมูลเข้าเมื่อผู้ใช้ Login
class LoginForm(BaseModel): 
    email: EmailStr 
    password: str 

# 4. Schema สำหรับรับข้อมูลเข้าเมื่อผู้ใช้ลงทะเบียน (Register)
class UserCreate(BaseModel): 
    email: EmailStr 
    password: str 
    phone: Optional[str] = None  # รองรับเบอร์โทรตาม init.sql

# 5. Schema สำหรับส่งข้อมูลผู้ใช้กลับไปให้ Frontend (Response)
class User(BaseModel): 
    id: int 
    email: EmailStr 
    phone: Optional[str] = None
    status: str = "ACTIVE" # 👈 ใช้ status ให้ตรงกับตารางใน Database
    created_at: Optional[datetime] = None

    class Config: 
        from_attributes = True  # ช่วยแปลงข้อมูลจาก SQLAlchemy ORM Model เป็น Pydantic ได้อัตโนมัติ