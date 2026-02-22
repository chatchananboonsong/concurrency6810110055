import multiprocessing
import time

def process_file(file_name):
    print(f"[Process] กำลังประมวลผลไฟล์: {file_name}")
    sum(i*i for i in range(10**6)) # คำนวณเลข
    print(f"[Process] {file_name} คำนวณเสร็จ -> กำลังเขียนสรุปผล...")
    time.sleep(1)
    return f"ไฟล์ {file_name} สำเร็จ"
if __name__ == "__main__":
    files = ["Data1.csv", "Data2.csv"]
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(process_file, files)
    print(f"ผลลัพธ์จากทุก Process: {results}")