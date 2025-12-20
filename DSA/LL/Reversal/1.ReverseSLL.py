# - Maintain 3 pointers: prev, curr, next.
# - Move through the list and reverse the direction of each link.
# - At each step:
#     next = curr.next
#     curr.next = prev
#     prev = curr
#     curr = next
# - When curr becomes None, prev is the new head.


def reverse_iterative(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next    # store next
        curr.next = prev         # reverse link
        prev = curr              # move prev
        curr = next_node         # move curr

    return prev  # new head


# - Base Case: if head is None or head.next is None → return head.
# - Recursively reverse the rest of the list.
# - After recursion returns new_head:
#     head.next.next = head   (reverse the link)
#     head.next = None        (terminate old link)
# - Return new_head.


def reverse_recursive(head):
    # Base case: single node or empty list
    if not head or not head.next:
        return head

    # Reverse the rest of the list
    new_head = reverse_recursive(head.next)

    # Fix links
    head.next.next = head
    head.next = None

    return new_head
