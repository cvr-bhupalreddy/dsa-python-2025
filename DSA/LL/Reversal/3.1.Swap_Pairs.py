class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        a = prev.next
        b = prev.next.next

        # swap a and b
        prev.next = b
        a.next = b.next
        b.next = a

        # move prev to next pair
        prev = a

    return dummy.next


def swap_pairs_no_dummy(head):
    if not head or not head.next:
        return head

    # New head will be second node after first swap
    new_head = head.next

    prev = None
    curr = head

    while curr and curr.next:
        nxt = curr.next
        following = curr.next.next

        # Swap curr & nxt
        nxt.next = curr
        curr.next = following

        # Link previous pair to newly swapped pair
        if prev:
            prev.next = nxt

        # Update prev and move curr
        prev = curr
        curr = following

    return new_head
