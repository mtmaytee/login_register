import httpx
from fastapi import HTTPException
from sqlalchemy.orm import Session 
from app.services.user_service import UserService 
from app.core import security 
from app.core.config import settings
from app.schemas import UserCreate # หรือ schema ที่ใช้สร้าง user

class AuthService: 
    @staticmethod 
    def authenticate_user(db: Session, email: str, password: str): 
        """ตรวจสอบความถูกต้องของอีเมลและรหัสผ่านเมื่อ Login""" 
        user = UserService.get_by_email(db, email) 
        if not user or not user.authentication: 
            return False 
        if not security.verify_password(password, user.authentication.password_hash): 
            return False 
        return user

    @staticmethod
    async def authenticate_line_user(db: Session, code: str):
        """แลก Code เป็น Token และดึงข้อมูลผู้ใช้จาก LINE"""
        token_url = "https://api.line.me/oauth2/v2.1/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.LINE_REDIRECT_URI,
            "client_id": settings.LINE_CHANNEL_ID,
            "client_secret": settings.LINE_CHANNEL_SECRET
        }
        
        async with httpx.AsyncClient() as client:
            # 1. ขอ Access Token
            token_res = await client.post(token_url, data=data, headers=headers)
            if token_res.status_code != 200:
                raise HTTPException(status_code=400, detail="Failed to validate LINE code")
            
            access_token = token_res.json().get("access_token")

            # 2. ดึงข้อมูลโปรไฟล์
            profile_url = "https://api.line.me/v2/profile"
            profile_headers = {"Authorization": f"Bearer {access_token}"}
            profile_res = await client.get(profile_url, headers=profile_headers)
            
            if profile_res.status_code != 200:
                raise HTTPException(status_code=400, detail="Failed to fetch LINE profile")
            
            profile_data = profile_res.json()
            line_user_id = profile_data.get("userId")
            display_name = profile_data.get("displayName")
            
            # ใช้ Email จำลองหากไม่ได้ขอ Scope Email จาก LINE
            email = f"{line_user_id}@line-login.com" 

        # 3. ค้นหาหรือสร้างผู้ใช้ใหม่
        user = UserService.get_by_email(db, email=email)
        if not user:
            new_user = UserCreate(
                email=email,
                password="", # หรือสุ่มรหัสผ่าน
                # เพิ่มฟิลด์ provider="line", provider_id=line_user_id หากโมเดลรองรับ
            )
            user = UserService.create(db, new_user)
            
        return user