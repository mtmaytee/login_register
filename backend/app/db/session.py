from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from app.core.config import settings 

# สร้าง Engine คุยกับ Database 
engine = create_engine(settings.DATABASE_URL) 

# สร้าง SessionLocal สำหรับสร้าง DB Session ในแต่ละ Request 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

# Declarative Base สำหรับ SQLAlchemy Models 
Base = declarative_base() 

def get_db(): 
  """Dependency สำหรับฉีด DB Session เข้าไปใน Endpoints""" 
  db = SessionLocal() 
  try: 
    yield db 
  finally: 
    db.close()