## FastAPI Login/Register System Architecture

### Project Structure

```

D:\login_register\
├── backend/
│   ├── app/
│   │   ├── main.py
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
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── auth.py
│   │   │       │   └── users.py
│   │   │       └── routers.py
│   │   └── services/
│   │       ├── auth_service.py
│   │       └── user_service.py
│   ├── database.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── core/
│   │   │   │   ├── guards/
│   │   │   │   ├── interceptors/
│   │   │   │   └── services/
│   │   │   ├── pages/
│   │   │   │   ├── login/
│   │   │   │   └── register/
│   │   │   └── app.routes.ts
│   ├── Dockerfile
│   └── .env
├── nginx/
│   └── nginx.conf
├── scripts/
│   ├── init.sql
│   └── load_test.js
└── docker-compose.yml
```
