class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # Attach the leftover part
    curr.next = l1 if l1 else l2
    return dummy.next


def merge_two_sorted_lists_no_dummy(l1, l2):
    if not l1: return l2
    if not l2: return l1

    # pick the smaller one as head
    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    curr = head

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2
    return head
