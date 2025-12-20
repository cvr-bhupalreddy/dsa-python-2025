# ---------------------------
# Build Min Heap
# ---------------------------
def build_min_heap(arr):
    n = len(arr)
    heap = arr.copy()  # make a copy so original array is unchanged
    for i in range((n - 2) // 2, -1, -1):
        reheap_down_min(heap, i, n)
    return heap


# ---------------------------
# Heap Sort Using Min Heap
# ---------------------------
def heap_sort(arr):
    heap = build_min_heap(arr)
    sorted_arr = []
    n = len(heap)
    for _ in range(n):
        # extract min (root)
        sorted_arr.append(heap[0])
        # move last element to root and heapify
        heap[0] = heap[-1]
        heap.pop()
        if heap:
            reheap_down_min(heap, 0, len(heap))
    return sorted_arr


# ---------------------------
# Helper Functions
# ---------------------------
def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


# ---------------------------
# Reheap Up
# ---------------------------
def reheap_up_max(heap, index):
    while index > 0 and heap[index] > heap[parent(index)]:
        heap[index], heap[parent(index)] = heap[parent(index)], heap[index]
        index = parent(index)


def reheap_up_min(heap, index):
    while index > 0 and heap[index] < heap[parent(index)]:
        heap[index], heap[parent(index)] = heap[parent(index)], heap[index]
        index = parent(index)


# ---------------------------
# Reheap Down
# ---------------------------
def reheap_down_max(heap, index, size):
    largest = index
    l = left(index)
    r = right(index)

    if l < size and heap[l] > heap[largest]:
        largest = l
    if r < size and heap[r] > heap[largest]:
        largest = r

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        reheap_down_max(heap, largest, size)


def reheap_down_min(heap, index, size):
    smallest = index
    l = left(index)
    r = right(index)

    if l < size and heap[l] < heap[smallest]:
        smallest = l
    if r < size and heap[r] < heap[smallest]:
        smallest = r

    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        reheap_down_min(heap, smallest, size)


# ---------------------------
# Build Heap
# ---------------------------
def build_max_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        reheap_down_max(arr, i, n)


def build_min_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        reheap_down_min(arr, i, n)


# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]

    print("Original Array:", arr)

    build_max_heap(arr)
    print("Max Heap:", arr)

    build_min_heap(arr)
    print("Min Heap:", arr)

    arr2 = [4, 10, 3, 5, 1]
    sorted_arr = heap_sort(arr2)
    print("Heap Sorted (Ascending):", sorted_arr)
