from sqlalchemy.orm import Session 
from app.services.user_service import UserService 
from app.core import security 

class AuthService: 
  @staticmethod 
  def authenticate_user(db: Session, email: str, password: str): 
    """ตรวจสอบความถูกต้องของอีเมลและรหัสผ่านเมื่อ Login""" 
    user = UserService.get_by_email(db, email) 
    # ตรวจสอบว่ามี user และมีข้อมูล authentication หรือไม่
    if not user or not user.authentication: 
      return False 
        
    # อ่านค่า password_hash จากตาราง user_authentications
    if not security.verify_password(password, user.authentication.password_hash): 
      return False 
            
    return user
