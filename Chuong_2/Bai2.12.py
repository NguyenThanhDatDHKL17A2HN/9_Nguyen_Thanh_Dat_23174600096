import requests

def hien_thi_sach_noi_bat(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            hien_thi_thong_tin_sach_noi_bat(data)
        else:
            print(f"Không thể kết nối đến API. Mã lỗi: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {e}")

def hien_thi_thong_tin_sach_noi_bat(data):
    print("Danh sách các bài post nổi bật:\n")

    for i, post in enumerate(data[:3], 1):
        print(f"Bài Post {i}:")
        print(f"   - Name: {post['name']}")
        print(f"   - Email: {post['email']}")
        print(f"   - Body: {post['body']}\n")

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/comments?postId=1"

    print("Đang tải thông tin sách nổi bật từ API...\n")
    hien_thi_sach_noi_bat(api_url)
