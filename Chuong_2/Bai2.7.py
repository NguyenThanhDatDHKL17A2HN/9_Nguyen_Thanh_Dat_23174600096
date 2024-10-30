import json

if __name__ == "__main__":
    python_object = {
        "name": "Dat",
        "age": 19,
        "city": "Son La",
        "is_student": True,
        "grades": [97, 90, 88]
    }

    json_string = json.dumps(python_object)
    print("Chuỗi JSON sau khi chuyển đổi:")
    print(json_string)
