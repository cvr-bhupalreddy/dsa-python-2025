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
