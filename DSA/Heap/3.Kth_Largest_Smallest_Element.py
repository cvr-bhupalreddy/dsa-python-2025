# 1️⃣ Brute Force
# Core Idea:
# - Sort the array in ascending (for kth smallest) or descending (for kth largest) order.
# - Return the element at index k-1.
# - Simple and intuitive, but sorting costs O(n log n).

# 2️⃣ Better Approach (Heap)
# Core Idea:
# - Maintain a heap of size k:
#     * For kth largest → use a min-heap: always keep k largest elements.
#     * For kth smallest → use a max-heap: always keep k smallest elements.
# - Iterate through the array and update the heap accordingly.
# - At the end, the root of the heap is the answer.
# - Time Complexity: O(n log k), Space Complexity: O(k)

# 3️⃣ Optimal Approach (QuickSelect)
# Core Idea:
# - Use a partitioning algorithm similar to QuickSort.
# - Partition array around a pivot: elements <= pivot go left, > pivot go right.
# - If pivot index == k-1 (for kth smallest) or n-k (for kth largest), we found the element.
# - Otherwise, recurse on the side containing the k-th element.
# - Average Time Complexity: O(n), worst-case O(n^2), Space Complexity: O(1)

# ✅ Summary Table
# | Approach    | Time Complexity | Space Complexity | Notes                                               |
# | ----------- | --------------- | ---------------- | --------------------------------------------------- |
# | Brute Force | O(n log n)      | O(n)             | Sort array and pick k-th                            |
# | Heap        | O(n log k)      | O(k)             | Min-heap for kth largest, max-heap for kth smallest |
# | QuickSelect | O(n) average    | O(1)             | Partition-based selection algorithm                 |


# Brute Force: Sort the array
def kth_largest_bruteforce(arr, k):
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[k - 1]


def kth_smallest_bruteforce(arr, k):
    arr_sorted = sorted(arr)
    return arr_sorted[k - 1]


import heapq


# Kth Largest using Min-Heap of size k
def kth_largest_heap(arr, k):
    min_heap = arr[:k]
    heapq.heapify(min_heap)
    for num in arr[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap[0]


# Kth Smallest using Max-Heap of size k
def kth_smallest_heap(arr, k):
    max_heap = [-x for x in arr[:k]]
    heapq.heapify(max_heap)
    for num in arr[k:]:
        if -num > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)
    return -max_heap[0]


import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    # Continue until pointers cross
    while i <= j:
        # Move i right until arr[i] >= pivot
        while i <= j and arr[i] < pivot:
            i += 1

        # Move j left until arr[j] <= pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        # If still i <= j, swap arr[i] and arr[j]
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # Finally put pivot in its correct location
    arr[low], arr[j] = arr[j], arr[low]

    # j is final pivot position
    return j


def quickselect(arr, low, high, k):
    """Return element with index k in sorted order (0-based)."""
    if low <= high:
        p = partition(arr, low, high)

        if k == p:
            return arr[p]
        elif k < p:
            return quickselect(arr, low, p - 1, k)
        else:
            return quickselect(arr, p + 1, high, k)


def kth_smallest(arr, k):
    # k is 1-based
    return quickselect(arr, 0, len(arr) - 1, k - 1)


def kth_largest(arr, k):
    n = len(arr)
    # Kth largest = (n-k)th smallest (0-based)
    return quickselect(arr, 0, n - 1, n - k)
