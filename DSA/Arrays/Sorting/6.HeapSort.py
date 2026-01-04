# Heap Sort uses a Binary Heap (Max Heap for ascending sort):
#
# 1. Build a Max Heap from the array.
#     - Largest element moves to root (index 0).
# 2. Swap the root with the last element.
#     - The largest element is now at its correct position.
# 3. Reduce heap size by 1 and heapify the root again.
# 4. Repeat until the heap size is 1.
#
# Properties:
#     - In-place sorting (no extra array needed)
#     - Not stable
#     - O(n log n) time complexity in all cases


# 2️⃣ Optimal Approach (Bottom-Up Heapify)
#
# Idea:
#     Start from the last non-leaf node and heapify all nodes bottom-up.
#     Leaf nodes are already valid heaps (size 1).
#     Only internal nodes need heapify.
#
# Why it’s O(N):
#     Nodes near the bottom have smaller height → cheaper heapify.
#     Total cost summed over all nodes is O(N).

def heapify(arr, n, i):
    """
    Maintain Max Heap property for subtree rooted at index i.
    n : size of heap
    i : root index of subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # recursively heapify


def build_max_heap(arr):
    n = len(arr)
    # Start from last non-leaf node and heapify all nodes
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    """
    Heap Sort using max heap
    """
    n = len(arr)

    # Step 1: Build max heap
    build_max_heap(arr)

    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Swap root (max) with last element
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify root to maintain max heap for reduced heap
        heapify(arr, i, 0)
