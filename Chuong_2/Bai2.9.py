import json

a = '''
{
    "congty": {
        "ten": "Công ty TNHH Đất Việt",
        "diachi": "abc Giải Phóng - Hà Nội",
        "nhanvien": [
            {"ten": "A", "don_vi": "A1"},
            {"ten": "B", "don_vi": "A2"},
            {"ten": "C", "don_vi": "A2"},
            {"ten": "D", "don_vi": "A3"},
            {"ten": "E", "don_vi": "A2"},
            {"ten": "F", "don_vi": "A4"},
            {"ten": "G", "don_vi": "A4"}
        ]
    }
}'''

b = json.loads(a)

tong_so_nhan_vien = len(b["congty"]["nhanvien"])

thong_ke = {}
for i in b["congty"]["nhanvien"]:
    don_vi = i["don_vi"]
    if don_vi in thong_ke:
        thong_ke[don_vi] += 1 
    else:
        thong_ke[don_vi] = 1
x = b["congty"]["ten"]
print(f"Công ty: {x}")
s = b["congty"]["diachi"]
print(f"Địa chỉ: {s}")
print(f"Tổng số nhân viên: {tong_so_nhan_vien}")
print("--------Thống kế nhân viên theo đơn vị--------")
for i, j in thong_ke.items():
    ty_le = (j/tong_so_nhan_vien)*100
    print(f"Tên đơn vị: {i}")
    print(f"  - Số nhân viên: {j}")
    print(f"  - Tỷ lệ: {ty_le:.2f}% \n")
