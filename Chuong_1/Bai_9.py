"""Xây dựng lớp đa giác, hình bình hành kế thừa từ đa giác, 
hình chữ nhật kế từ hình bình hành và hình vuông thừa kế từ hình chữ nhật. 
Nhập vào các thuộc tính cần thiết của mỗi hình và tính chu vi, diện tích của hình đó. """

import math
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh
        self.cac_canh = []

    def nhap_cac_canh(self):
        for i in range(self.so_canh):
            canh = float(input(f"Nhập chiều dài của cạnh {i + 1}: "))
            self.cac_canh.append(canh)

    def chu_vi(self):
        return sum(self.cac_canh)

class HinhBinhHanh(DaGiac):
    def __init__(self):
        super().__init__(4) 

    def dien_tich(self):
        day = self.cac_canh[0]
        chieu_cao = float(input("Nhập chiều cao: "))
        return day * chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self):
        super().__init__()

class HinhVuong(HinhChuNhat):
    def __init__(self):
        super().__init__()

hinh_vuong = HinhVuong()
hinh_vuong.nhap_cac_canh()

chu_vi_hinh_vuong = hinh_vuong.chu_vi()
dien_tich_hinh_vuong = hinh_vuong.dien_tich()

print(f"Chu vi hình vuông: {chu_vi_hinh_vuong}")
print(f"Diện tích hình vuông: {dien_tich_hinh_vuong}")
