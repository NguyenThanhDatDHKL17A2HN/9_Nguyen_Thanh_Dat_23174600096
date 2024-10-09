"""Hiệu chỉnh lớp Stack bằng cách thêm vào hàm thành phần count để trả về số phần tử trên ngăn xếp. """

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

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.size())