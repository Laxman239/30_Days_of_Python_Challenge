from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# Usage:
s = Stack()
s.push(5)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Peek after pop:", s.peek())
