## 3. โครงสร้างไฟล์ที่จะถูกสร้าง (Expected Project Structure)

.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── endpoints/
│   │   │           ├── auth.py
│   │   │           └── users.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/
│   │   │   ├── redis.py
│   │   │   └── session.py
│   │   ├── models/
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   └── token.py
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   └── app/
│   │       ├── core/
│   │       │   ├── guards/
│   │       │   ├── interceptors/
│   │       │   └── services/
│   │       ├── pages/
│   │       │   ├── login/
│   │       │   └── register/
│   │       └── app.routes.ts
│   └── Dockerfile
├── nginx/
│   └── nginx.conf
├── scripts/
│   ├── init.sql
│   └── load_test.js
└── docker-compose.yml