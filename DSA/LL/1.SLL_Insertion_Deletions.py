class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def from_list(arr):
        ll = SinglyLinkedList()
        for x in arr:
            ll.insert_tail(x)
        return ll

    def insert_head(self, val):
        node = SLLNode(val)
        node.next = self.head
        self.head = node

    def insert_tail(self, val):
        node = SLLNode(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert_k(self, val, k):
        if k == 1:
            self.insert_head(val)
            return
        cur = self.head
        for _ in range(k-2):
            if not cur:
                return
            cur = cur.next
        if not cur:
            return
        node = SLLNode(val)
        node.next = cur.next
        cur.next = node

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def delete_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def delete_k(self, k):
        if k == 1:
            self.delete_head()
            return
        cur = self.head
        for _ in range(k-2):
            if not cur:
                return
            cur = cur.next
        if cur and cur.next:
            cur.next = cur.next.next

    def search(self, val):
        cur = self.head
        pos = 1
        while cur:
            if cur.val == val:
                return pos
            cur = cur.next
            pos += 1
        return -1

    def to_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res



# TESTS
if __name__ == "__main__":
    print("--- TEST SLL ---")
    s = SinglyLinkedList.from_list([1,2,3])
    s.insert_head(0)
    s.insert_tail(4)
    s.insert_k(99, 3)
    s.delete_head()
    s.delete_tail()
    s.delete_k(2)
    print(s.to_list())
    print("search(3)=", s.search(3))

    print("--- TEST DLL ---")
    d = DoublyLinkedList.from_list([10,20,30])
    d.insert_head(5)
    d.insert_tail(40)
    d.insert_k(99, 3)
    d.delete_head()
    d.delete_tail()
    d.delete_k(2)
    print(d.to_list())
    print("search(30)=", d.search(30))
