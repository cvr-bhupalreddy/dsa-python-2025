# 🟦 LRU Cache Problem
#
# Problem statement:
#
# Design a data structure that supports the following operations in O(1) time:
#     get(key) → return the value of the key if it exists in the cache, otherwise return -1.
#     put(key, value) → insert or update the value of the key. If the cache reaches its capacity,
#     remove the least recently used (LRU) item before inserting the new item.
#
# Key idea:
#
# "Least Recently Used" means the key that was accessed the longest time ago (either get or put).
# Cache capacity is fixed.



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper to remove node
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Helper to insert node at head
    def _insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Move to head
        self._remove(node)
        self._insert_at_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._insert_at_head(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove LRU node
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
