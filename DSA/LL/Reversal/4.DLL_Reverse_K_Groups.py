class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def build(self, arr):
        self.head = None
        prev = None
        for x in arr:
            node = DNode(x)
            if not self.head:
                self.head = node
            else:
                prev.next = node
                node.prev = prev
            prev = node

    # ---------- REVERSE K GROUPS - ITERATIVE ----------
    def reverse_k_group_iterative(self, k):
        if k <= 1 or not self.head:
            return self.head

        curr = self.head
        new_head = None
        group_prev_tail = None

        while curr:
            # Step 1: Check k nodes
            check = curr
            count = 0
            while check and count < k:
                check = check.next
                count += 1

            if count < k:
                break

            # Step 2: Reverse K nodes
            prev = None
            temp = curr
            for _ in range(k):
                nxt = temp.next
                temp.next = prev
                temp.prev = nxt
                prev = temp
                temp = nxt

            # prev = new head of reversed block
            # curr = old head of block, now tail

            if not new_head:
                new_head = prev

            if group_prev_tail:
                group_prev_tail.next = prev
                prev.prev = group_prev_tail

            curr.next = temp
            if temp:
                temp.prev = curr

            group_prev_tail = curr
            curr = temp

        self.head = new_head
        return self.head

    def reverse_k_group_iterative_dummy(self, k):
        if k <= 1 or not self.head:
            return self.head

        dummy = DNode(0)
        dummy.next = self.head
        self.head.prev = dummy

        prev_group_tail = dummy
        curr = self.head

        while curr:
            # Step 1: check if there are K nodes ahead
            count = 0
            check = curr
            while check and count < k:
                check = check.next
                count += 1
            if count < k:
                break  # less than K nodes left

            # Step 2: reverse K nodes
            prev = None
            temp = curr
            for _ in range(k):
                nxt = temp.next
                temp.next = prev
                temp.prev = nxt
                prev = temp
                temp = nxt

            # Step 3: connect previous group to new head
            prev_group_tail.next = prev
            prev.prev = prev_group_tail

            # Step 4: connect tail of reversed group to next part
            curr.next = temp
            if temp:
                temp.prev = curr

            # Step 5: move prev_group_tail and curr to next group
            prev_group_tail = curr
            curr = temp

        self.head = dummy.next
        self.head.prev = None
        return self.head

    def reverse_k_group_recursive(self, head, k):
        # Step 1: count if we have k nodes
        cnt = 0
        temp = head
        while temp and cnt < k:
            temp = temp.next
            cnt += 1

        if cnt < k:
            return head

        # Step 2: reverse K nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            curr.prev = nxt
            prev = curr
            curr = nxt

        # prev = new head of this block
        # head = tail of block

        head.next = self.reverse_k_group_recursive(curr, k)
        if head.next:
            head.next.prev = head

        return prev
