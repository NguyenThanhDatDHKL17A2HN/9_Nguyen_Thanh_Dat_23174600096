"""Xây dựng lớp điểm, lớp elip thừa kế từ lớp điểm, lớp đường tròn thừa kế từ lớp elip. 
Nhập vào các thuộc tính cần thiết của elip và tính diện tích. """

import math

class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, tam_x, tam_y, do_dai_truc_lon, do_dai_truc_nho):
        super().__init__(tam_x, tam_y)
        self.truc_lon = do_dai_truc_lon
        self.truc_nho = do_dai_truc_nho

    def dien_tich(self):
        return math.pi * self.truc_lon * self.truc_nho

class DuongTron(Elip):
    def __init__(self, tam_x, tam_y, ban_kinh):
        super().__init__(tam_x, tam_y, ban_kinh, ban_kinh)

elip = Elip(1, 1, 8, 4)
dien_tich_elip = elip.dien_tich()
print("Diện tích của elip là:", dien_tich_elip)

duong_tron = DuongTron(2, 2, 7)
dien_tich_duong_tron = duong_tron.dien_tich()
print("Diện tích của hình tròn là:", dien_tich_duong_tron)
