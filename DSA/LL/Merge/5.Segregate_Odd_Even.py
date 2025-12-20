class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def segregate_odd_even_dummy(head):
    if not head:
        return None

    odd_dummy = Node(0)
    even_dummy = Node(0)

    odd_tail = odd_dummy
    even_tail = even_dummy

    curr = head

    while curr:
        if curr.val % 2 != 0:  # Odd
            odd_tail.next = curr
            odd_tail = odd_tail.next
        else:  # Even
            even_tail.next = curr
            even_tail = even_tail.next

        curr = curr.next

    # terminate even list
    even_tail.next = None

    # connect odd list → even list
    odd_tail.next = even_dummy.next

    return odd_dummy.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def segregate_odd_even(head):
    if not head or not head.next:
        return head

    odd_head = odd_tail = None
    even_head = even_tail = None

    curr = head

    while curr:
        if curr.val % 2 != 0:
            # odd
            if not odd_head:
                odd_head = odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = odd_tail.next
        else:
            # even
            if not even_head:
                even_head = even_tail = curr
            else:
                even_tail.next = curr
                even_tail = even_tail.next

        curr = curr.next

    # Connect odd list → even list
    if odd_tail:
        odd_tail.next = even_head

    if even_tail:
        even_tail.next = None

    return odd_head
