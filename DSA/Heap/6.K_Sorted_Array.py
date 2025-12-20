# 🔹 1. Brute Force Approach
# Idea
#     1. Simply sort the entire array using built-in sort.
#     2. Return the sorted array.


# 🔹 2. Better Approach (Insertion-Like Scan)
# Idea
#     1. Iterate through the array from index 0 to N-1.
#     2. For each index i, compare it with next k elements.
#     3. Swap with smaller elements if needed (like insertion sort in k-sized window).
#     4. Repeat for all elements.


def sort_k_sorted_insertion(arr, k):
    n = len(arr)
    for i in range(n):
        # Compare with next k elements
        for j in range(i + 1, min(i + k + 1, n)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# 🔹 3. Optimal Approach (Min-Heap, FAANG Preferred)
# Idea
#     1. Create a min-heap of first k+1 elements.
#     2. Initialize result array.
#     3. For the rest of the array:
#           pop the smallest element from heap → append to result
#           push next element from array into heap
#     4. After processing all elements, pop remaining elements from heap and append to result.
#     5. Return result.

import heapq


def sort_k_sorted_heap(arr, k):
    n = len(arr)
    heap = arr[:k + 1]
    heapq.heapify(heap)
    result = []

    for i in range(k + 1, n):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        result.append(heapq.heappop(heap))

    return result


# | Approach            | Time Complexity | Space | Notes                    |
# | ------------------- | --------------- | ----- | ------------------------ |
# | Brute Force         | O(N log N)      | O(1)  | Simple                   |
# | Insertion-Like Scan | O(N * K)        | O(1)  | Good for small k         |
# | Min-Heap            | O(N log K)      | O(K)  | Optimal, FAANG preferred |
