class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._reheap_up(len(self.heap) - 1)

    def _reheap_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            raise Exception("Heap is empty")
        min_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._reheap_down(0)
        return min_val

    def _reheap_down(self, index):
        n = len(self.heap)
        smallest = index
        l = self.left(index)
        r = self.right(index)

        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._reheap_down(smallest)

    def peek(self):
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]

    def size(self):
        return len(self.heap)
