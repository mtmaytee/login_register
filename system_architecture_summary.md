## 1. สรุปสถาปัตยกรรมระบบ (System Architecture Summary)

**Backend Framework:** Python 3.11+ (FastAPI) ประมวลผลแบบ Asynchronous ทั้งหมด เพื่อให้ประมวลผล I/O ไวที่สุด
**Database & Pooling:** PostgreSQL 16 ทำงานร่วมกับ asyncpg + PgBouncer เพื่อจัดการ Connection Pooling
**Caching & Session:** Redis 7 Cluster สำหรับเก็บ Session, Refresh Token และ Caching
**API Gateway / Load Balancer:** Nginx ทำหน้าที่เป็น Reverse Proxy และ Load Balancer กระจาย Traffic
**Frontend Framework:** Angular v17+ (Standalone Components + Signals / RxJS) แบบ Lazy Loading
**Load Testing Tool:** k6 สำหรับจำลองการยิง Request ทดสอบประสิทธิภาพระดับ High QPS