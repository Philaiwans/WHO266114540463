from clickhouse_connect import get_client

# สร้าง client หนึ่งครั้ง แล้ว reuse
client = get_client(
    host='localhost',     # หรือ IP ที่รัน ClickHouse
    username='default',
    password='',          # ถ้ามี password ให้ใส่
    # port=8123,          # เพิ่มถ้าคุณใช้ HTTP Interface
    # database='ชื่อฐานข้อมูล',  # ถ้ามีฐานข้อมูลเฉพาะ
)

def query_clickhouse(sql):
    """ ส่ง query ไปยัง ClickHouse และคืนค่าผลลัพธ์ """
    result = client.query(sql)
    return result.result_rows
