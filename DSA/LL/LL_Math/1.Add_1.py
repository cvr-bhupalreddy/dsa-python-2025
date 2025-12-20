class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_one(head):
    # Helper to reverse linked list
    def reverse(node):
        prev, curr = None, node
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    head = reverse(head)
    curr = head
    carry = 1

    while curr and carry:
        curr.val += carry
        if curr.val == 10:
            curr.val = 0
            carry = 1
        else:
            carry = 0
        if not curr.next and carry:
            curr.next = Node(1)
            carry = 0
        curr = curr.next

    head = reverse(head)
    return head


# ----------------------
# Example Usage
# ----------------------
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(9)  # 129
head = add_one(head)  # becomes 130
print_list(head)  # Output: [1,3,0]

head = Node(9)
head.next = Node(9)  # 99
head = add_one(head)  # becomes 100
print_list(head)  # Output: [1,0,0]
