import sqlite3

def tao_bang_nhan_vien(database_file):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nhan_vien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten TEXT,
            tuoi INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("Đã tạo bảng 'nhan_vien' thành công.")

def cap_nhat_cot(database_file, ten_bang, cot_can_cap_nhat, gia_tri_moi):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute(f"UPDATE {ten_bang} SET {cot_can_cap_nhat} = ?", (gia_tri_moi,))
    conn.commit()
    print(f"Cập nhật thành công. Tất cả giá trị trong cột {cot_can_cap_nhat} đã được đặt thành {gia_tri_moi}.")
    conn.close()

duong_dan_csdls = 'nhan_su.db'

tao_bang_nhan_vien(duong_dan_csdls)

conn = sqlite3.connect(duong_dan_csdls)
cursor = conn.cursor()
cursor.execute("INSERT INTO nhan_vien (ten, tuoi) VALUES ('Nguyễn Văn A', 25)")
conn.commit()
conn.close()

ten_bang_can_cap_nhat = 'nhan_vien'
cot_can_cap_nhat = 'tuoi'
gia_tri_moi = 21

cap_nhat_cot(duong_dan_csdls, ten_bang_can_cap_nhat, cot_can_cap_nhat, gia_tri_moi)