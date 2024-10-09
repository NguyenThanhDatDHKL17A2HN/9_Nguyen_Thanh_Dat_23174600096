"""Viết một lớp biểu diễn hình chữ nhật với các thuộc tính là độ dài hai cạnh và có các phương thức: 
Nhập dữ liệu hai cạnh cho hình chữ nhật; 
Tính chu vi hình chữ nhật; 
Tính diện tích hình chữ nhật; 
In thông tin hình chữ nhật (gồm độ dài hai cạnh, chu vi, diện tích) ra màn hình. 
Trên cơ sở lớp trên viết chương trình cho phép người dùng nhập dữ liệu của một hình chữ nhật, 
sau đó in thông tin của nó ra màn hình. """

class Hinh_Chu_Nhat:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def dien_tich_hcn(self):
        return self.length * self.width

    def chu_vi_hcn(self):
        return 2 * (self.length + self.width)

Hinh_Chu_Nhat = Hinh_Chu_Nhat(8, 4) 
dien_tich = Hinh_Chu_Nhat.dien_tich_hcn()  
chu_vi = Hinh_Chu_Nhat.chu_vi_hcn() 

print("Độ dài 2 cạnh của hình chữ nhật lần lượt là: ", Hinh_Chu_Nhat.length, Hinh_Chu_Nhat.width)
print("Diện tích của hình chữ nhật là:", dien_tich)
print("Chu vi của hình chữ nhật là:", chu_vi)      