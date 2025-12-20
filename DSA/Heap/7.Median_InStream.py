# 🔹 3. Optimal Approach (Two Heaps — FAANG Preferred)


# 1. Maintain two heaps:
#     - Max-heap (left) for smaller half of numbers
#     - Min-heap (right) for larger half of numbers
# 2. Balance heaps: sizes differ by at most 1
# 3. Median:
#     - If equal sizes → average of roots
#     - If unequal → root of larger heap
# 4. Insert each element:
#     - Push to max-heap if smaller than left max
#     - Else push to min-heap
#     - Rebalance if needed


import heapq


def median_optimal(stream):
    min_heap = []  # right half (min-heap)
    max_heap = []  # left half (max-heap, store negatives)
    medians = []

    for num in stream:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # Balance heaps
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Get median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = -max_heap[0]

        medians.append(median)

    return medians
