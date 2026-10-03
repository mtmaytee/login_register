import http from 'k6/http'; 
import { check, sleep } from 'k6'; 

// กำหนดการตั้งค่าบททดสอบประสิทธิภาพ (Load Test Options) 
export const options = { 
  stages: [ 
    { duration: '30s', target: 50 }, // ค่อยๆ เพิ่ม Virtual Users (VUs) เป็น 50 
    { duration: '1m30s', target: 500 }, // เพิ่ม VUs เป็น 500 ให้ครบภายใน 2 นาที 
    { duration: '30s', target: 0 }, // ค่อยๆ ลด VUs ลงจนจบการทดสอบ 
  ], 
  thresholds: { 
    http_req_duration: ['p(95)<300'], // P95 Latency ต้องน้อยกว่า 300ms 
    http_req_failed: ['rate<0.01'], // อัตราข้อผิดพลาด (Error Rate) ต้องน้อยกว่า 1% 
  }, 
}; 

export default function () { 
  // URL ของ Endpoint Login ผ่าน Nginx Reverse Proxy 
  const url = 'http://localhost/api/v1/auth/login'; 
  
  // สุ่มเลือกข้อมูลสำหรับยิง Login const 
  payload = JSON.stringify({ email: 'user@example.com', password: 'password123', }); 

  const params = { headers: { 'Content-Type': 'application/json', }, }; 
  
  // ส่ง HTTP POST Request const 
  res = http.post(url, payload, params); 
  
  // ตรวจสอบความถูกต้องของ Response 
  check(res, { 
    'status is 200 OK': (r) => r.status === 200, 
    'has access_token': (r) => { 
      try { 
        const body = JSON.parse(r.body); 
        return body && body.access_token !== undefined; } catch (e) { return false; } }, }); 
        // หน่วงเวลาสุ่มระหว่าง Request sleep(1); 
      }