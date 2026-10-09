from pydantic_settings import BaseSettings, SettingsConfigDict 
import os 

class Settings(BaseSettings): 
    PROJECT_NAME: str = "Login/Register API" 
    API_V1_STR: str = "/api/v1" 
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0") 
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey") 
    BACKEND_CORS_ORIGINS: list = ["*"] 
    LINE_CHANNEL_ID: str = os.getenv("LINE_CHANNEL_ID", "")
    LINE_CHANNEL_SECRET: str = os.getenv("LINE_CHANNEL_SECRET", "")
    LINE_REDIRECT_URI: str = os.getenv("LINE_REDIRECT_URI", "")

#class Config: 
    #case_sensitive = True 
    # ตั้งค่าแบบ Pydantic v2
    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()