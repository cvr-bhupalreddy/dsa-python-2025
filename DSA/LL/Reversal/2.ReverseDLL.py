class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ---------------------------
    # Insert at tail
    # ---------------------------
    def insert_tail(self, data):
        node = DLLNode(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.prev = cur

    # ---------------------------
    # Print forward
    # ---------------------------
    def print_forward(self):
        cur = self.head
        out = []
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    # ---------------------------
    # Print backward
    # ---------------------------
    def print_backward(self):
        cur = self.head
        if not cur:
            return []

        while cur.next:
            cur = cur.next
        out = []
        while cur:
            out.append(cur.data)
            cur = cur.prev
        return out

    # =====================================================
    # Reverse DLL — Iterative
    # =====================================================
    def reverse_iterative(self):
        curr = self.head
        if not curr:
            return

        while curr:
            curr.prev, curr.next = curr.next, curr.prev  # swap pointers
            new_head = curr
            curr = curr.prev  # move to next node (originally next)

        self.head = new_head

    def reverse_iterative1(self):
        curr = self.head
        if curr is None:
            return

        new_head = None
        while curr is not None:
            # store original next
            next_node = curr.next

            # swap next and prev pointers
            curr.next = curr.prev
            curr.prev = next_node

            # update new_head (will be last node processed)
            new_head = curr

            # move to original next node
            curr = next_node

        # update head
        self.head = new_head

    # =====================================================
    # Reverse DLL — Recursive
    # =====================================================
    def reverse_recursive(self):
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, node):
        # Base case: empty list or last node
        if node is None or node.next is None:
            return node

        # Recurse on next node
        new_head = self._reverse_recursive(node.next)

        # Swap pointers
        node.next.next = node
        node.prev = node.next
        node.next = None

        return new_head

    def reverse_recursive1(self):
        # Wrapper function: start recursion with head and None
        self.head = self._reverse_recursive(curr=self.head, prev=None)

    def _reverse_recursive1(self, curr, prev):
        if curr is None:
            return prev  # new head

        # Store next node
        next_node = curr.next

        # Reverse pointers
        curr.next = prev
        curr.prev = next_node

        # Recurse to next node in original order
        return self._reverse_recursive(next_node, curr)


# ==========================
# TEST
# ==========================
if __name__ == "__main__":
    dll = DoublyLinkedList()
    for x in [1, 2, 3, 4, 5]:
        dll.insert_tail(x)

    print("Original Forward :", dll.print_forward())
    print("Original Backward:", dll.print_backward())

    # Iterative reverse
    dll.reverse_iterative()
    print("After Iterative Reverse Forward :", dll.print_forward())
    print("After Iterative Reverse Backward:", dll.print_backward())

    # Recursive reverse
    dll.reverse_recursive()
    print("After Recursive Reverse Forward :", dll.print_forward())
    print("After Recursive Reverse Backward:", dll.print_backward())
