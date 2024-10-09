"""Xây dựng lớp phân số PS gồm: 
+ Các thuộc tính: tử số và mẫu số. 
+ Các phương thức: Kiểm tra tính hợp lệ của phân số; Nhập phân số; In phân số ra màn hình. """

class PS:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số (khác 0): "))

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def in_phan_so(self):
        print(f"Phân số là: {self.tu_so}/{self.mau_so}")

ps = PS()

ps.nhap_phan_so()

ps.in_phan_so()

if ps.kiem_tra_hop_le():
    print("Phân số hợp lệ.")
else:
    print("Phân số không hợp lệ.")