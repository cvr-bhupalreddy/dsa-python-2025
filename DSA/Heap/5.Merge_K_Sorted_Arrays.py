# 1. Concatenate all arrays into one array.
# 2. Sort the resulting array.
# 3. Return the sorted array.

def merge_k_sorted_bruteforce(arrays):
    merged = []
    for arr in arrays:
        merged.extend(arr)
    merged.sort()
    return merged


# 🔹 2. Better Approach (Two-way Merge Iteratively)
#     1. Take first array as merged result.
#     2. Iteratively merge it with next array using two-pointer merge.
#     3. Repeat until all K arrays are merged.

def merge_two(arr1, arr2):
    i = j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


def merge_k_sorted_iterative(arrays):
    if not arrays:
        return []
    merged = arrays[0]
    for i in range(1, len(arrays)):
        merged = merge_two(merged, arrays[i])
    return merged


# 🔹 3. Optimal Approach (Min-Heap)
#         1. Push the first element of each array into a min-heap along with array index and element index.
#         2. Pop the smallest element from heap and add to result.
#         3. If the array of the popped element has more elements, push the next element into heap.
#         4. Repeat until heap is empty.


import heapq


def merge_k_sorted_heap(arrays):
    heap = []
    result = []

    # Push first element of each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))  # (value, array_index, element_index)

    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        # Push next element of same array
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result


# | Approach        | Time Complexity | Space    | Notes                           |
# | --------------- | --------------- | -------- | ------------------------------- |
# | Brute Force     | O(N log N)      | O(N)     | Easy                            |
# | Iterative Merge | O(K * N)        | O(N)     | Two-way merge, good for small K |
# | Min-Heap        | O(N log K)      | O(K + N) | Optimal, FAANG preferred        |
