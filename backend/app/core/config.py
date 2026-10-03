from pydantic_settings import BaseSettings, SettingsConfigDict 
import os 

class Settings(BaseSettings): 
    PROJECT_NAME: str = "Login/Register API" 
    API_V1_STR: str = "/api/v1" 
    #DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/login_register") 
    DATABASE_URL: str = os.getenv("DATABASE_URL", 
                                  "postgresql://postgres.hnfjjlxfpkxihbgcnyuo:admin-login-register-db@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0") 
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey") 
    BACKEND_CORS_ORIGINS: list = ["*"] 

#class Config: 
    #case_sensitive = True 
    # ตั้งค่าแบบ Pydantic v2
    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()