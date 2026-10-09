-- login_register\scripts\init.sql
-- เปิดใช้งาน Extension สำหรับสร้าง UUID อัตโนมัติ 
CREATE EXTENSION IF NOT EXISTS "pgcrypto"; 

-- 1. ตารางผู้ใช้งานหลัก (users) 
CREATE TABLE IF NOT EXISTS users ( 
  id BIGSERIAL PRIMARY KEY, 
  uuid UUID DEFAULT gen_random_uuid(), 
  email VARCHAR(255) UNIQUE NOT NULL, 
  phone VARCHAR(50) UNIQUE, 
  status VARCHAR(20) DEFAULT 'ACTIVE', 
  line_user_id VARCHAR(255) UNIQUE,
  hashed_password VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP ); 

  -- 2. ตารางเก็บรหัสผ่านและการยืนยันตัวตน (user_authentications) 
  CREATE TABLE IF NOT EXISTS user_authentications ( 
    id BIGSERIAL PRIMARY KEY, 
    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
    provider_type VARCHAR(50) DEFAULT 'LOCAL', 
    password_hash VARCHAR(255) NOT NULL ); 
    
  -- 3. ตารางเก็บ Refresh Tokens สำหรับการต่ออายุ Token (refresh_tokens) 
  CREATE TABLE IF NOT EXISTS refresh_tokens (   
    id BIGSERIAL PRIMARY KEY, 
    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE, 
    token_hash VARCHAR(255) UNIQUE NOT NULL, 
    is_revoked BOOLEAN DEFAULT FALSE, 
    expires_at TIMESTAMPTZ NOT NULL ); 
    
  -- 4. ตารางบันทึก ประวัติการเข้าสู่ระบบ (login_logs) 
  CREATE TABLE IF NOT EXISTS login_logs ( 
    id BIGSERIAL PRIMARY KEY, 
    user_id BIGINT, 
    email_attempt VARCHAR(255), 
    ip_address VARCHAR(45), 
    status VARCHAR(20), 
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP ); 
    
  -- 5. สร้าง Indexes เพื่อเพิ่มประสิทธิภาพในการค้นหาข้อมูล (Performance Indexing) 
  CREATE UNIQUE INDEX IF NOT EXISTS idx_users_email ON users(email); 
  CREATE UNIQUE INDEX IF NOT EXISTS idx_users_uuid ON users(uuid); 
  CREATE UNIQUE INDEX IF NOT EXISTS idx_refresh_tokens_hash ON refresh_tokens(token_hash); 
  CREATE INDEX IF NOT EXISTS idx_user_auth_provider ON user_authentications(user_id, provider_type); 
  CREATE INDEX IF NOT EXISTS idx_login_logs_ip_time ON login_logs(ip_address, created_at);