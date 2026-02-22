import threading
import time

def book_seat(user):
    print(f"[Thread {user}] 1. กำลังเช็คที่ว่าง...")
    time.sleep(1) 
    print(f"[Thread {user}] 2. มีที่ว่างแล้ว -> กำลังบันทึกการจองให้ {user}...")
    time.sleep(1)
    print(f"[Thread {user}] เสร็จสิ้นการจองสำหรับ {user}")

if __name__ == "__main__":
    users = ["Alice", "Bob"]
    threads = []

    for u in users:
        t = threading.Thread(target=book_seat, args=(u,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("ระบบ Threading ทำงานครบทุกขั้นตอน")