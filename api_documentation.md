powershell -Command "Set-Content -Path 'D:\login_register\api_documentation.txt' -Value '# ตารางสอนวิธีใช้ API สำหรับ Postman

## 1. รายละเอียดโปรเจกต์

### โครงสร้าง API
- **Base URL**: `http://localhost:8000/api/v1`
- **ระบบ Authentication**: JWT Bearer Token
- **Database**: SQLite (พัฒนาเบื้องต้น)

## 2. ตาราง API สำหรับ Postman

| ประเภท | Endpoint | Method | Description |
|---------|----------|--------|-------------|
| Auth | `/auth/register` | POST | สร้างบัญชีผู้ใช้ใหม่ |
| Auth | `/auth/login` | POST | เข้าสู่ระบบและได้รับ token |
| Users | `/users/{user_id}` | GET | ดึงข้อมูลผู้ใช้ตาม ID |
| Users | `/users/{user_id}` | PUT | อัปเดตข้อมูลผู้ใช้ |

## 3. การใช้งาน API แบบละเอียด

### 3.1 Register (สร้างบัญชีผู้ใช้)
**URL**: `http://localhost:8000/api/v1/auth/register`
**Method**: POST
**Headers**: 
- Content-Type: application/json

**Body (JSON)**:
{
    "email": "user@example.com",
    "full_name": "John Doe",
    "password": "password123"
}

**Response Success**:
{
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_active": true
}

### 3.2 Login (เข้าสู่ระบบ)
**URL**: `http://localhost:8000/api/v1/auth/login`
**Method**: POST
**Headers**: 
- Content-Type: application/json

**Body (JSON)**:
{
    "email": "user@example.com",
    "password": "password123"
}

**Response Success**:
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}

### 3.3 Get User (ดึงข้อมูลผู้ใช้)
**URL**: `http://localhost:8000/api/v1/users/1`
**Method**: GET
**Headers**: 
- Authorization: Bearer [access_token]

**Response Success**:
{
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_active": true
}

### 3.4 Update User (อัปเดตข้อมูลผู้ใช้)
**URL**: `http://localhost:8000/api/v1/users/1`
**Method**: PUT
**Headers**: 
- Content-Type: application/json
- Authorization: Bearer [access_token]

**Body (JSON)**:
{
    "email": "updated@example.com",
    "full_name": "Updated Name"
}

**Response Success**:
{
    "id": 1,
    "email": "updated@example.com",
    "full_name": "Updated Name",
    "is_active": true
}

## 4. ข้อควรระวัง

### 4.1 การใช้งาน Token
- หลังจาก login สำเร็จ ให้เก็บ access_token ที่ได้
- ใส่ token ใน header ของ API ที่ต้องการใช้งานด้วยรูปแบบ:
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

### 4.2 การจัดการข้อผิดพลาด
- **401 Unauthorized**: ไม่มี token หรือ token ไม่ถูกต้อง
- **404 Not Found**: ไม่พบผู้ใช้ตาม ID ที่ระบุ
- **422 Unprocessable Entity**: ข้อมูลที่ส่งมามีรูปแบบผิด

## 5. ตัวอย่างการใช้งานใน Postman

### 5.1 การ Register
1. เลือก POST method
2. ใส่ URL: `http://localhost:8000/api/v1/auth/register`
3. ไปที่ tab Body
4. เลือก radio button "raw" และ "JSON"
5. ใส่ JSON data ตามตัวอย่างในส่วน 3.1

### 5.2 การ Login
1. เลือก POST method
2. ใส่ URL: `http://localhost:8000/api/v1/auth/login`
3. ไปที่ tab Body
4. เลือก radio button "raw" และ "JSON"
5. ใส่ JSON data ตามตัวอย่างในส่วน 3.2

### 5.3 การใช้งาน API ที่ต้องการ token
1. หลังจาก login สำเร็จ ให้เก็บ access_token
2. เลือก GET/PUT method ตามที่ต้องการ
3. ใส่ URL: `http://localhost:8000/api/v1/users/1`
4. ไปที่ tab Headers
5. เพิ่ม header:
Key: Authorization
Value: Bearer [access_token]

## 6. ข้อมูลเพิ่มเติม

### 6.1 Validation Rules
- **Email**: ต้องเป็นรูปแบบอีเมลที่ถูกต้อง
- **Full Name**: ต้องไม่น้อยกว่า 2 ตัวอักษร
- **Password**: ต้องไม่น้อยกว่า 6 ตัวอักษร

### 6.2 การทดสอบ API ด้วย Postman
1. ตั้งค่า Collection ใหม่ใน Postman
2. เพิ่ม request สำหรับแต่ละ endpoint
3. กำหนด headers และ body ตามตารางที่ระบุไว้
4. รัน request เพื่อดูผลลัพธ์

## 7. คำแนะนำเพิ่มเติม

### 7.1 การจัดการ session
- หลังจาก login แล้วเก็บ access_token ไว้ใน environment variables
- ใช้ Postman environment ในการจัดการ token

### 7.2 การทดสอบ API
- เริ่มจากการ register และ login เพื่อได้ token
- ใช้ token ที่ได้เพื่อทดสอบ endpoint อื่นๆ
- ตรวจสอบ response status และ body ทุกครั้ง

## 8. ตัวอย่างการตั้งค่า Postman Environment

### 8.1 Variables ที่ควรกำหนด
- `base_url`: `http://localhost:8000/api/v1`
- `access_token`: [token ที่ได้จากการ login]

### 8.2 การใช้งานใน request URL
- \`{{base_url}}/auth/register\`
- \`{{base_url}}/users/{{user_id}}\`

## 9. ข้อผิดพลาดที่พบบ่อย

### 9.1 Authentication Error
- **401 Unauthorized**: Token ไม่ถูกต้องหรือหมดอายุ
- **403 Forbidden**: ไม่มีสิทธิ์เข้าถึง

### 9.2 Data Validation Error
- **422 Unprocessable Entity**: ข้อมูลที่ส่งมามีรูปแบบผิด เช่น email ไม่ถูกต้อง

### 9.3 Resource Not Found
- **404 Not Found**: ไม่พบ resource ตามที่ระบุใน URL

## 10. สรุป
ตารางนี้ให้ข้อมูลการใช้งาน API แบบครบถ้วนสำหรับการทดสอบใน Postman โดยเฉพาะ:
- การจัดการ register, login และ user management
- การใช้งาน token authentication
- การจัดการ headers และ body สำหรับแต่ละ endpoint
- การจัดการข้อผิดพลาดที่พบบ่อย

สามารถนำไปใช้ในการทดสอบ API ได้ทันทีหลังจากเริ่มต้น server แล้ว.'

The string is missing the terminator: ".
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : TerminatorExpectedAtEndOfString
 
