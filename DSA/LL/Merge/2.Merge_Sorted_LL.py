# Node class for singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# ------------------------------
# Merge with dummy node
# ------------------------------
def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists using a dummy node
    Returns the head of the merged list
    """
    dummy = Node(0)  # Create a dummy node as the starting point
    curr = dummy     # Pointer to build the merged list

    # Traverse both lists until one is exhausted
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1  # Attach l1 node to merged list
            l1 = l1.next    # Move l1 pointer forward
        else:
            curr.next = l2  # Attach l2 node to merged list
            l2 = l2.next    # Move l2 pointer forward
        curr = curr.next    # Move current pointer forward

    # Attach remaining nodes (only one list will have leftover nodes)
    curr.next = l1 if l1 else l2

    # Return the merged list starting after dummy node
    return dummy.next


# ------------------------------
# Merge without dummy node
# ------------------------------
def merge_two_sorted_lists_no_dummy(l1, l2):
    """
    Merge two sorted linked lists without using a dummy node
    Returns the head of the merged list
    """
    # If one of the lists is empty, return the other
    if not l1: return l2
    if not l2: return l1

    # Choose the smaller node as the head
    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    curr = head  # Pointer to build the merged list

    # Traverse both lists until one is exhausted
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1  # Attach l1 node
            l1 = l1.next
        else:
            curr.next = l2  # Attach l2 node
            l2 = l2.next
        curr = curr.next  # Move current pointer forward

    # Attach remaining nodes
    curr.next = l1 if l1 else l2

    return head  # Return the head of merged list
