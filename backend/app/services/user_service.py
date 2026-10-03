from typing import List

from sqlalchemy.orm import Session 
from app.models.user import User, UserAuthentication
from app.core import security

# Note: ปรับ import schema ให้ตรงกับไฟล์ที่คุณเก็บ UserCreate (เช่น user หรือ auth หรือ token)
from app.schemas.token import UserCreate  # หรือ from app.schemas.user import UserCreate

class UserService: 
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """
        ดึงข้อมูลผู้ใช้งานทั้งหมดแบบมี Pagination (Skip / Limit)
        """
        return db.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_email(db: Session, email: str):
        """ค้นหาผู้ใช้จาก email ในตาราง users"""
        return db.query(User).filter(User.email == email).first()
  
    @staticmethod 
    def get_by_id(db: Session, user_id: int): 
        """ค้นหาผู้ใช้ด้วย ID""" 
        return db.query(User).filter(User.id == user_id).first() 

    # เพิ่ม Alias 'create' ชี้ไปที่ 'create_user' เพื่อให้รองรับทั้ง UserService.create และ UserService.create_user
    @staticmethod 
    def create(db: Session, user: UserCreate):
        """สร้างผู้ใช้ใหม่และบันทึกรหัสผ่านในตาราง user_authentications"""
        # 1. บันทึกลงตาราง users (ไม่มี password)
        db_user = User(
            email=user.email,
            phone=getattr(user, "phone", None)
        )
        db.add(db_user)
        db.commit() # commit เพื่อให้ได้ db_user.id ออกมา
        db.refresh(db_user)

        # 2. บันทึกรหัสผ่านแฮชลงตาราง user_authentications
        hashed_pwd = security.get_password_hash(user.password)
        db_auth = UserAuthentication(
            user_id=db_user.id,
            provider_type="LOCAL",
            password_hash=hashed_pwd
        )
        db.add(db_auth)
        db.commit()
        db.refresh(db_auth)

        # Refresh ข้อมูล user ก่อนส่งคืน
        db.refresh(db_user) 
        return db_user

    # กำหนด create_user เป็น alias ของ create เพื่อป้องกันปัญหาเรียกใช้ต่างกัน
    create_user = create