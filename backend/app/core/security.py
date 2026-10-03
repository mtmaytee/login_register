from passlib.context import CryptContext 
from jose import jwt 
from datetime import datetime, timedelta
from app.core.config import settings 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

def verify_password(plain_password: str, hashed_password: str) -> bool:
  """ตรวจสอบรหัสผ่าน Plain Text กับ Hashed Password""" 
  return pwd_context.verify(plain_password[:72], hashed_password) 

def get_password_hash(password: str) -> str: 
  """แปลงรหัสผ่านเป็น Hash ด้วย bcrypt""" 
  return pwd_context.hash(password[:72])  # bcrypt มีข้อจำกัดความยาวรหัสผ่าน 72 ตัวอักษร

def create_access_token(data: dict) -> str: 
  """สร้าง JWT Access Token พร้อมตั้งเวลาหมดอายุ""" 
  to_encode = data.copy() 
  expire = datetime.utcnow() + timedelta(hours=1)  # กำหนดอายุ Access Token เป็น 1 ชั่วโมง
  to_encode.update({"exp": expire}) 
  encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256") 
  return encoded_jwt

def create_refresh_token(data: dict) -> str:
    to_encode = data.copy()
    # กำหนดอายุ Refresh Token เป็น 7 วัน
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt