import asyncio

async def send_email(target):
    print(f"[Async] เริ่มเตรียมไฟล์สำหรับ {target}...")
    await asyncio.sleep(1) 
    print(f"[Async] ไฟล์พร้อม! -> กำลังส่งอีเมลไปที่ {target}...")
    await asyncio.sleep(1)
    print(f"[Async] ส่งอีเมลให้ {target} เรียบร้อย")

async def main():
    await asyncio.gather(
        send_email("customer1@mail.com"),
        send_email("customer2@mail.com")
    )

if __name__ == "__main__":
    asyncio.run(main())