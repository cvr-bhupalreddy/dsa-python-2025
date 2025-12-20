class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


#  Dummy node only giving clean logic
def add_two_numbers_lsb_first(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next


def add_two_numbers_II(l1, l2):
    stack1, stack2 = [], []

    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    carry = 0
    prev = None
    while stack1 or stack2 or carry:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        node = Node(total % 10)
        node.next = prev
        prev = node

    return prev


def add_two_numbers_MSB_optimal(l1, l2):
    # Helper: reverse linked list
    def reverse(head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # Step 1: Reverse both lists
    l1 = reverse(l1)
    l2 = reverse(l2)

    # Step 2: Add like normal reverse-order addition
    carry = 0
    head = None  # head of result
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10

        node = Node(total % 10)
        node.next = head  # prepend node
        head = node

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return head
