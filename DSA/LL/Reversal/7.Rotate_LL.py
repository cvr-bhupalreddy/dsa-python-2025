# 1. Compute the length (n) of the linked list.
# 2. Reduce k = k % n (rotating n times gives same list).
# 3. Connect the tail to head → make it a circular list.
# 4. Find the new tail: move (n - k - 1) steps from head.
# 5. New head = new_tail.next
# 6. Break the circle → new_tail.next = None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    # Step 1: compute length
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1

    # Step 2: effective rotation
    k = k % n
    if k == 0:
        return head

    # Step 3: make circular list
    tail.next = head

    # Step 4: find new tail → move n - k - 1 steps
    steps_to_new_tail = n - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # Step 5: new head
    new_head = new_tail.next

    # Step 6: break the circle
    new_tail.next = None

    return new_head
