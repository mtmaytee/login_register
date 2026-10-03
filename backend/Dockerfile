# 1. ใช้ Python 3.11-slim เป็น Base Image เพื่อความเบาและรวดเร็ว
FROM python:3.11-slim 

# 2. กำหนด Working Directory ภายใน Container[cite: 1]
WORKDIR /app 

# 3. กำหนด Environment Variables ป้องกันไม่ให้ Python เขียนไฟล์ .pyc และให้แสดง Log ทันที[cite: 1]
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

# 4. คัดลอกไฟล์ requirements.txt เข้ามาเพื่อติดตั้ง Dependencies[cite: 1]
COPY requirements.txt . 

# 5. ติดตั้ง แพ็กเกจภาษา Python ทั้งหมดโดยไม่เก็บ Cache[cite: 1]
RUN pip install --no-cache-dir -r requirements.txt 

# 6. คัดลอกไฟล์ทั้งหมดภายในโฟลเดอร์ backend เข้ามาที่ /app[cite: 1]
COPY . . 

# 7. เปิดพอร์ต 8000 สำหรับเรียกใช้งาน API[cite: 1]
EXPOSE 8000 

# 8. คำสั่งสำหรับเริ่มต้นรัน FastAPI Server ด้วย Uvicorn (ตั้งค่า $PORT เผื่อสำหรับ Render)[cite: 1]
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]