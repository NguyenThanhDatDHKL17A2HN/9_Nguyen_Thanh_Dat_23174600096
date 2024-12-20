import requests

def hien_thi_sach_tu_api(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            hien_thi_thong_tin_sach(data)
        else:
            print(f"Không thể kết nối đến API. Mã lỗi: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {e}")

def hien_thi_thong_tin_sach(data):
    print(f"Tổng số bài post: {len(data)}\n")

    for post in data:
        print(f"userID: {post['userId']}")
        print(f"id: {post['id']}")
        print(f"title: {post['title']}")
        print(f"body: {post['body']}\n")

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"

    print("Đang tải thông tin sách từ API...\n")
    hien_thi_sach_tu_api(api_url)
