# ------------------------------
# Node class for linked list
# ------------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# ------------------------------
# 1️⃣ Using Dummy Nodes
# ------------------------------
def segregate_odd_even_dummy(head):
    """
    Segregate linked list into odd and even nodes using dummy nodes.
    All odd nodes come first, followed by all even nodes.

    Time: O(n), Space: O(1) extra (dummy nodes only)
    """
    if not head:
        return None

    # Create dummy nodes to simplify edge cases
    odd_dummy = Node(0)
    even_dummy = Node(0)

    odd_tail = odd_dummy   # tail pointer for odd list
    even_tail = even_dummy # tail pointer for even list

    curr = head

    # Traverse the original list
    while curr:
        if curr.val % 2 != 0:  # Odd
            odd_tail.next = curr
            odd_tail = odd_tail.next
        else:                  # Even
            even_tail.next = curr
            even_tail = even_tail.next

        curr = curr.next

    # Terminate even list to avoid cycle
    even_tail.next = None

    # Connect odd list → even list
    odd_tail.next = even_dummy.next

    # Return head of new list
    return odd_dummy.next


# ------------------------------
# 2️⃣ Without Dummy Nodes
# ------------------------------
def segregate_odd_even(head):
    """
    Segregate linked list into odd and even nodes without using dummy nodes.
    Handles empty list and single element edge cases.

    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return head

    # Initialize head and tail pointers for odd and even lists
    odd_head = odd_tail = None
    even_head = even_tail = None

    curr = head

    while curr:
        if curr.val % 2 != 0:  # Odd
            if not odd_head:
                odd_head = odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = odd_tail.next
        else:                  # Even
            if not even_head:
                even_head = even_tail = curr
            else:
                even_tail.next = curr
                even_tail = even_tail.next

        curr = curr.next

    # Connect odd list → even list
    if odd_tail:
        odd_tail.next = even_head

    # Terminate even list to avoid cycles
    if even_tail:
        even_tail.next = None

    # If there are no odd nodes, return even head
    return odd_head if odd_head else even_head
