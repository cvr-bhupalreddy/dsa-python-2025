# 1. Move fast pointer N steps ahead.
# 2. If fast becomes None, it means the node to delete is the head → delete head.
# 3. Now move slow and fast together until fast.next becomes None.
# 4. At this point, slow is exactly at the node before the one to delete.
# 5. Delete slow.next.


def deleteNthFromEnd(head, n):
    if not head:
        return None

    fast = head
    slow = head

    # Step 1: Move fast n steps ahead
    for _ in range(n):
        fast = fast.next
        # If n == length of list → delete head
        if fast is None:
            return head.next

    # Step 2: Move both fast and slow until fast is at last node
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Step 3: slow is at (N+1)-th node from end
    slow.next = slow.next.next  # delete node

    return head
