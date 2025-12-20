# 🟦 What is a Deque? (Double Ended Queue)
#
# A Deque (pronounced deck) is a double-ended queue that allows:
#     Insert at front
#     Insert at rear
#     Delete from front
#     Delete from rear

# 👉 Unlike a normal queue (FIFO), a deque can work both as:
#     Queue
#     Stack
#     Both at the same time


# 🟧 Operations Supported by a Deque
# | Operation       | Description          | Time |
# | --------------- | -------------------- | ---- |
# | `push_front(x)` | add element at front | O(1) |
# | `push_back(x)`  | add element at rear  | O(1) |
# | `pop_front()`   | remove front element | O(1) |
# | `pop_back()`    | remove rear element  | O(1) |
# | `front()`       | return front         | O(1) |
# | `back()`        | return last          | O(1) |
# | `is_empty()`    | check empty          | O(1) |
# | `size()`        | number of elements   | O(1) |


class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = -1
        self.rear = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push_front(self, value):
        if self.is_full():
            raise Exception("Deque is full")

        if self.front == -1:  # empty deque
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.capacity

        self.arr[self.front] = value
        self.size += 1

    def push_back(self, value):
        if self.is_full():
            raise Exception("Deque is full")

        if self.front == -1:  # empty deque
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.arr[self.rear] = value
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        value = self.arr[self.front]
        if self.front == self.rear:  # last element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        self.size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        value = self.arr[self.rear]
        if self.front == self.rear:  # last element
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

        self.size -= 1
        return value

    def get_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.arr[self.front]

    def get_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.arr[self.rear]
