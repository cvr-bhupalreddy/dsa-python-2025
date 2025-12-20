class Solution:
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next
        return head

    def deleteMiddle_better(self, head):
        """ If the list is empty or has only one node,
        return None as there is no middle node to delete """
        if not head or not head.next:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head.next.next

        # Move 'fast' pointer twice as fast as 'slow'
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node by skipping it
        slow.next = slow.next.next
        return head
