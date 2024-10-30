import json

if __name__ == "__main__":
    python_dict = {
        "name": "Dat",
        "age": 19,
        "city": "Son La",
        "is_student": True,
        "grades": [97, 90, 88]
    }
    json_string = json.dumps(python_dict, indent=4, sort_keys=True)
    print(f"Chuỗi JSON sau khi chuyển đổi:\n{json_string}")
