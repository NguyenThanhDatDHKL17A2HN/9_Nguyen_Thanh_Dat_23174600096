""""Hiệu chỉnh lớp Stack bằng cách thêm vào hàm thành phần print để in nội dung của ngăn xếp. """

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print_stack(self):
        for item in reversed(self.stack):  # In ngược từ cuối đến đầu
            print(item)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Nội dung của ngăn xếp:")
stack.print_stack()  