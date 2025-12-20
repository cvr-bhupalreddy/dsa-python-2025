class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def build(self, arr):
        self.head = None
        prev = None
        for x in arr:
            node = Node(x)
            if not self.head:
                self.head = node
            else:
                prev.next = node
            prev = node

    def reverse_between(self, m, n):
        if m == n or not self.head:
            return self.head

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # Step 1: move prev to node before m
        for _ in range(m-1):
            prev = prev.next

        # Reverse sublist
        curr = prev.next
        tail = curr
        prev_sub = None

        for _ in range(n - m + 1):
            nxt = curr.next
            curr.next = prev_sub
            prev_sub = curr
            curr = nxt

        # Connect reversed sublist back
        prev.next = prev_sub
        tail.next = curr

        self.head = dummy.next
        return self.head

    def print_list(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        print(res)
