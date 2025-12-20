class StackArray:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        return self.arr.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty Stack")
        return self.arr[-1]

    def is_empty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLL:
    def __init__(self):
        self.top = None

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow")
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty Stack")
        return self.top.data

    def is_empty(self):
        return self.top is None
