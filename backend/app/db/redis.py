import redis 
from app.core.config import settings 
# สร้าง Redis Connection Client 
redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True) 

def get_redis(): 
  """Dependency สำหรับดึง Redis Client ไปใช้งาน""" 
  return redis_client