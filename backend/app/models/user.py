import uuid6
from uuid import UUID as PyUUID
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID  # 👈 Import UUID สำหรับ PostgreSQL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # ให้ Python สร้าง UUIDv7 ให้อัตโนมัติเมื่อมีการสมัครสมาชิก
    # 2. เปลี่ยนชนิดข้อมูลจาก String เป็น UUID 
    # 3. แก้ default เป็น uuid6.uuid7 (ส่งเป็นออบเจ็กต์ฟังก์ชันโดยไม่ต้องมี lambda และ str())
    # uuid = Column(String, unique=True, index=True , default=lambda: str(uuid6.uuid7()))
    uuid = Column(UUID(as_uuid=True), unique=True, index=True, default=uuid6.uuid7)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, nullable=True)
    status = Column(String, default="ACTIVE")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    line_user_id = Column(String, unique=True, nullable=True)
    hashed_password = Column(String, nullable=True)  # เพิ่มคอลัมน์ hashed_password

    # เชื่อมไปยังตาราง user_authentications
    authentication = relationship("UserAuthentication", 
                              back_populates="user", 
                              uselist=False)    
    # ✅ เพิ่ม property นี้เพื่อให้ Pydantic Schema อ่านค่า is_active ได้
    @property
    def is_active(self) -> bool:
        return self.status == "ACTIVE"

class UserAuthentication(Base):
    __tablename__ = "user_authentications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    provider_type = Column(String, default="LOCAL")
    password_hash = Column(String, nullable=False)

    user = relationship("User", back_populates="authentication")
