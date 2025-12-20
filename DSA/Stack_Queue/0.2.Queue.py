class QueueArray:
    def __init__(self):
        self.arr = []

    def enqueue(self, x):
        self.arr.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")
        return self.arr.pop(0)  # costly O(n)

    def front(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        return self.arr[0]

    def is_empty(self):
        return len(self.arr) == 0


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        node = Node(x)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue Underflow")
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val

    def peek(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        return self.front.data


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class QueueDLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        node = DLLNode(x)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        node.prev = self.rear
        self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue Underflow")
        val = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return val

    def peek(self):
        if self.front is None:
            raise IndexError("Empty Queue")
        return self.front.data


class CircularQueueArray:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            raise OverflowError("Circular Queue Overflow")
        self.arr[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Circular Queue Underflow")
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return val

    def peek(self):
        if self.size == 0:
            raise IndexError("Empty Queue")
        return self.arr[self.front]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueueLL:
    def __init__(self):
        self.rear = None

    def enqueue(self, x):
        node = Node(x)
        if self.rear is None:
            self.rear = node
            node.next = node
        else:
            node.next = self.rear.next
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.rear is None:
            raise IndexError("Queue Underflow")

        head = self.rear.next
        val = head.data

        if self.rear == head:
            self.rear = None
        else:
            self.rear.next = head.next

        return val

    def peek(self):
        if self.rear is None:
            raise IndexError("Empty Queue")
        return self.rear.next.data
