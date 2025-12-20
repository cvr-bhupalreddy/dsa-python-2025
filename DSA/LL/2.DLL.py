class DLLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def from_list(arr):
        dll = DoublyLinkedList()
        for x in arr:
            dll.insert_tail(x)
        return dll

    def insert_head(self, val):
        node = DLLNode(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def insert_tail(self, val):
        node = DLLNode(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def insert_k(self, val, k):
        if k == 1:
            self.insert_head(val)
            return
        cur = self.head
        for _ in range(k - 2):
            if not cur:
                return
            cur = cur.next
        if not cur:
            return
        node = DLLNode(val)
        node.next = cur.next
        node.prev = cur
        if cur.next:
            cur.next.prev = node
        cur.next = node

    def delete_head(self):
        if not self.head:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.prev.next = None

    def delete_k(self, k):
        if k == 1:
            self.delete_head()
            return
        cur = self.head
        for _ in range(k - 2):
            if not cur:
                return
            cur = cur.next
        if cur and cur.next:
            to_delete = cur.next
            cur.next = to_delete.next
            if to_delete.next:
                to_delete.next.prev = cur

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


if __name__ == "__main__":
    print("--- TEST DLL ---")
    d = DoublyLinkedList.from_list([10, 20, 30])
    d.insert_head(5)
    d.insert_tail(40)
    d.insert_k(99, 3)
    d.delete_head()
    d.delete_tail()
    d.delete_k(2)
    print(d.to_list())
    print("search(30)=", d.search(30))
