"""Để quản lý điểm thi vào một trường đại học, ta xây dựng lớp TS mô tả các thí sinh, bao gồm: 
+ Các thuộc tính: Họ tên thí sinh; điểm các môn Toán, Lý, Hoá. 
+ Các phương thức: Nhập thông tin thí sinh; In thông tin thí sinh; Tính tổng điểm của từng thí sinh. 
Trên cơ sở lớp trên, viết chương trình làm các công việc sau: 
+ Nhập họ tên và điểm của một danh sách thí sinh. 
+ Đưa ra màn hình danh sách thí sinh trúng tuyển 
(với giả thiết điểm chuẩn vào trường là 20) theo thứ tự điểm từ cao xuống thấp. """

class TS:
    def __init__(self, ho_ten='', diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ và tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def in_thong_tin(self):
        print("Họ và tên:", self.ho_ten)
        print("Điểm Toán:", self.diem_toan)
        print("Điểm Lý:", self.diem_ly)
        print("Điểm Hóa:", self.diem_hoa)

    def tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

n = int(input("Nhập số lượng thí sinh: "))
ds_ts = [TS() for _ in range(n)]
for ts in ds_ts:
    ts.nhap_thong_tin()
    tong_diem = ts.tong_diem() 
print("Tổng điểm của thí sinh:", tong_diem)

ds_ts_trung_tuyen = sorted(ds_ts, key=lambda x: x.tong_diem(), reverse=True)

print("Danh sách thí sinh trúng tuyển gồm:")
for ts in ds_ts_trung_tuyen:
    if ts.tong_diem() >= 20:
        ts.in_thong_tin()
