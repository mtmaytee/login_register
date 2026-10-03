# D:\login_register\backend\app\api\v1\endpoints\auth.py
from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from app.schemas import token as schemas 
from app.services.auth_service import AuthService 
from app.services.user_service import UserService 
from app.core import security 
from app.db.session import get_db # <-- เปลี่ยน Import มาที่ app.db.session 
from jose import JWTError, jwt
from app.core.config import settings

router = APIRouter() 

@router.post("/login", response_model=schemas.Token) 
async def login_for_access_token(form_data: schemas.LoginForm, db: Session = Depends(get_db)): 
  user = AuthService.authenticate_user(db, form_data.email, form_data.password) 
  if not user: 
    raise HTTPException( status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail="Incorrect email or password", 
                        headers={"WWW-Authenticate": "Bearer"}, ) 
  # ใช้ security module ในการออก Access Token 
  access_token = security.create_access_token(data={"sub": user.email}) 
  refresh_token = security.create_refresh_token(data={"sub": user.email})

  return {"access_token": access_token,
           "refresh_token": refresh_token,
           "token_type": "bearer"} 

@router.post("/register", response_model=schemas.User) 
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)): 
  # เรียกใช้ UserService ในการเช็คอีเมลและสร้างผู้ใช้ใหม่ 
  db_user = UserService.get_by_email(db, email=user.email) 
  if db_user: 
    raise HTTPException(status_code=400, detail="Email already registered") 
  created_user = UserService.create(db, user) 
  return created_user

# 👈 เพิ่ม Endpoint สำหรับยิงมาขอ Access Token ใบใหม่
@router.post("/refresh-token", response_model=schemas.Token)
async def refresh_access_token(body: schemas.RefreshTokenRequest, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate refresh token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(body.refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")
        token_type: str = payload.get("type")
        
        if email is None or token_type != "refresh":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = AuthService.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception

    # ออก Token ชุดใหม่กลับไปให้ Frontend
    new_access_token = security.create_access_token(data={"sub": user.email})
    new_refresh_token = security.create_refresh_token(data={"sub": user.email})

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }