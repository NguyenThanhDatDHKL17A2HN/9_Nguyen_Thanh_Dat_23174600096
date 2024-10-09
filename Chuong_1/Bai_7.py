"""Xây dựng lớp Date mô tả thông tin về ngày, tháng, năm. 
Lớp Date gồm: Hàm tạo với ba ñối có giá trị mặc định, phương thức display để in thông tin về ngày ra màn hình 
và phương thức next để tính ngày tiếp theo. """

class Date:
    def __init__(self, ngay=1, thang=1, nam=1900):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"Ngày: {self.ngay}/{self.thang}/{self.nam}")

    def next(self):
        import datetime
        current_date = datetime.date(self.nam, self.thang, self.ngay)
        next_date = current_date + datetime.timedelta(days=1)
        self.ngay = next_date.day
        self.thang = next_date.month
        self.nam = next_date.year

ngay = Date(1, 3, 2023)
ngay.display()
ngay.next()
ngay.display()