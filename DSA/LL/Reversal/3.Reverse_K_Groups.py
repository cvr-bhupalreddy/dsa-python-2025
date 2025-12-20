# 1. We want to reverse nodes in groups of size K.
# 2. Every consecutive group of K nodes MUST be reversed.
# 3. If the remaining nodes < K, do NOT reverse them.
# 4. Iterative:
#     - Move pointer ‘curr’ K steps to check group size.
#     - Reverse that K-sized chunk.
#     - Connect previous group’s tail to new head of current group.
# 5. Recursive:
#     - Count K nodes.
#     - Reverse first K nodes.
#     - Recursively call for the rest of list.
#     - Connect tail of reversed group with head of recursively processed list.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseKGroup(head, k):
    if not head or k == 1:
        return head

    prev_tail = None
    current = head
    new_head = None

    while current:
        # Step 1: check if there are k nodes remaining
        count = 0
        check = current
        while check and count < k:
            check = check.next
            count += 1
        if count < k:
            break

        # Step 2: reverse k nodes
        prev = None
        temp = current
        for _ in range(k):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        # Step 3: connect previous part
        if not new_head:
            new_head = prev  # first group's new head
        if prev_tail:
            prev_tail.next = prev

        prev_tail = current
        current = temp

    # Step 4: connect remaining nodes
    if prev_tail:
        prev_tail.next = current

    return new_head if new_head else head


def reverse_k_group_iterative_Dummy(self, k):
    if k <= 1 or not self.head:
        return self.head

    dummy = Node(0)
    dummy.next = self.head

    prev_group_tail = dummy
    curr = self.head

    while True:
        # Step 1: check if we have k nodes
        check = curr
        count = 0
        while check and count < k:
            check = check.next
            count += 1

        if count < k:
            break  # not enough nodes to reverse

        # Step 2: reverse k nodes
        prev = None
        temp = curr
        for _ in range(k):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        # prev = new head of reversed block
        # curr = original head of block (now tail) it needs to connect to next group
        prev_group_tail.next = prev
        curr.next = temp

        prev_group_tail = curr  # tail of reversed list
        curr = temp

    self.head = dummy.next
    return self.head


def reverse_k_group_recursive(self, head, k):
    # Step 1: check availability of k nodes
    count = 0
    temp = head
    while temp and count < k:
        temp = temp.next
        count += 1

    if count < k:
        return head   # not enough nodes

    # Step 2: reverse first k nodes
    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # prev = new head of block
    # head = tail of block

    head.next = self.reverse_k_group_recursive(curr, k)
    return prev


