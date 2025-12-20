class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListFastSlow:
    def __init__(self, head=None):
        self.head = head

    # ------------------------------------------------------
    # 1. Detect Cycle (Floyd’s Tortoise & Hare)
    # ------------------------------------------------------
    def detect_cycle(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # meeting point
                return True
        return False

    def detect_cycle_hashset(head):
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True  # cycle detected
            visited.add(curr)
            curr = curr.next
        return False  # no cycle

    # ------------------------------------------------------
    # 2. Find Length of Cycle
    # ------------------------------------------------------
    def cycle_length(self):
        slow, fast = self.head, self.head

        # First detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # meeting point
                # count the cycle length
                count = 1
                fast = fast.next
                while slow != fast:
                    fast = fast.next
                    count += 1
                return count

        return 0  # no cycle

    # ------------------------------------------------------
    # 3. Find Start of Cycle
    # ------------------------------------------------------
    def cycle_start(self):
        slow, fast = self.head, self.head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # meeting point found
                break
        else:  # this is the while else loop
            return None  # no cycle

        # Step 2: Move slow to head; both move 1 step each
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # cycle starting node

    # ------------------------------------------------------
    # 4. Middle of Linked List
    # ------------------------------------------------------
    def find_middle(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow  # slow points to middle

    # ------------------------------------------------------
    # 5. Check Palindrome Linked List
    # ------------------------------------------------------
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        # Step 1: Find middle
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second_half = self.reverse_list(slow)

        # Step 3: Compare first & second halves
        first, second = self.head, second_half
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

    def is_palindrome_1(self, head):
        if not head or not head.next:
            return True

        # 1️⃣ Find first middle (slow stops at FIRST middle)
        slow = head
        fast = head
        while fast.next and fast.next.next:  # This logic is to stop at First Middle in Event length case
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Reverse ONLY second half
        second_half = self.reverse_list(slow.next)

        # 3️⃣ Compare first half and reversed second half
        p1 = head
        p2 = second_half
        result = True

        while p2:
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        # 4️⃣ Restore original list (re-reverse second half)
        # slow.next = self.reverse_list(second_half)
        self.reverse_list(second_half)  # this also works , I don't see any difference where you start

        return result

    # Helper — reverse list
    def reverse_list(self, node):
        prev = None
        curr = node

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    # ------------------------------------------------------
    # Utility to build from array
    # ------------------------------------------------------
    @staticmethod
    def from_array(arr):
        if not arr:
            return LinkedListFastSlow(None)

        head = ListNode(arr[0])
        curr = head

        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return LinkedListFastSlow(head)
