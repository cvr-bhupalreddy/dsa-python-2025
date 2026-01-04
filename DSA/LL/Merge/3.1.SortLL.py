class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge(l1, l2):
    """
    Merge two sorted linked lists without dummy node
    """
    if not l1: return l2
    if not l2: return l1

    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    current = head

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append remaining nodes
    current.next = l1 if l1 else l2
    return head


def sort_linked_list(head):
    """
    Sort a linked list using merge sort (without dummy)
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head

    # Step 1: Find middle
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Disconnect left and right halves
    prev.next = None

    # Step 2: Sort left and right halves
    left_sorted = sort_linked_list(head)
    right_sorted = sort_linked_list(slow)

    # Step 3: Merge
    return merge(left_sorted, right_sorted)
