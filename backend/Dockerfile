# 1. ใช้ Python 3.11-slim เป็น Base Image เพื่อความเบาและรวดเร็ว 
FROM python:3.11-slim 

# 2. กำหนด Working Directory ภายใน Container 
WORKDIR /app 

# 3. กำหนด Environment Variables ป้องกันไม่ให้ Python เขียนไฟล์ .pyc และให้แสดง Log ทันที 
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 

# 4. คัดลอกไฟล์ requirements.txt เข้ามาเพื่อติดตั้ง Dependencies 
COPY requirements.txt . 

# 5. ติดตั้ง แพ็กเกจภาษา Python ทั้งหมดโดยไม่เก็บ Cache 
RUN pip install --no-cache-dir -r requirements.txt 

# 6. คัดลอกซอร์สโค้ดทั้งหมดในโฟลเดอร์ backend เข้าไปที่ /app 
COPY . . 

# 7. เปิดพอร์ต 8000 สำหรับเรียกใช้งาน API 
EXPOSE 8000 

# 8. คำสั่งสำหรับเริ่มต้นรัน FastAPI Server ด้วย Uvicorn 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]