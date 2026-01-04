# Problem: Sort a singly linked list in ascending order.
#
# Optimal Approach: Merge Sort on Linked List
# - Merge sort works well for linked lists because:
#     1. We can split the list in O(n) using slow/fast pointers.
#     2. Merge two sorted linked lists in O(n) without extra space.
#
# Steps:
# 1. Base Case: If head is None or only one node, return head.
# 2. Split the list into two halves using slow/fast pointer.
# 3. Recursively sort left and right halves.
# 4. Merge the two sorted halves.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # ---------------------------
    # Merge two sorted lists
    # ---------------------------
    def merge(self, l1, l2):
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

        curr.next = l1 if l1 else l2
        return dummy.next

    # ---------------------------
    # Find middle of list
    # ---------------------------
    def get_middle(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None  # split the list
        return slow

    # ---------------------------
    # Merge sort main
    # ---------------------------
    def merge_sort(self, head):
        if not head or not head.next:
            return head

        mid = self.get_middle(head)
        left = self.merge_sort(head)
        right = self.merge_sort(mid)

        return self.merge(left, right)

    # ---------------------------
    # Call this to sort whole LL
    # ---------------------------
    def sort_list(self):
        self.head = self.merge_sort(self.head)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_with_dummy(l1, l2):
    """
    Merge two sorted linked lists using dummy node
    """
    dummy = ListNode(-1)
    current = dummy

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
    return dummy.next


def sort_linked_list_dummy(head):
    """
    Sort linked list using merge sort with dummy node
    """
    if not head or not head.next:
        return head

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None

    left_sorted = sort_linked_list_dummy(head)
    right_sorted = sort_linked_list_dummy(slow)

    return merge_with_dummy(left_sorted, right_sorted)
