# Brute Force Algorithm (O(N log N)):
#
# 1. Count frequency of each element.
# 2. Convert the frequency map into a list of (element, frequency) pairs.
# 3. Sort the list by frequency in descending order.
# 4. Return the first k elements from the sorted list.
#
#
#
#
# Better Approach — Max Heap (O(N log N)):
#
# 1. Count frequency of each element.
# 2. Push (-frequency, element) into a max heap.
# 3. Pop from the heap k times.
# 4. Each pop gives the next most frequent element.
# 5. Return the k popped elements.
#
#
#
# Optimal Approach — Min Heap of Size K (O(N log K)):
#
# 1. Count frequency of each element.
# 2. Create a min heap that stores (frequency, element).
# 3. For each (element, freq):
# push into heap
# if heap size exceeds k:
#     pop the smallest frequency element
# 4. After processing all elements, the heap contains the k most frequent ones.
# 5. Extract elements from the heap and return them.
#
#
# Most Optimal — Bucket Sort (O(N)):
#
# 1. Count frequency of each element.
# 2. Create a list of buckets, where index = frequency.
# 3. For each (element, freq):
# append element into bucket[freq]
# 4. Traverse buckets from highest index to lowest:
# collect elements until k elements are gathered
# 5. Return the collected k elements.


def top_k_frequent_bruteforce(nums, k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda x: -x[1])
    return [num for num, f in sorted_items[:k]]


import heapq


def top_k_frequent_heap(nums, k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    min_heap = []
    for num, f in freq.items():
        heapq.heappush(min_heap, (f, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for f, num in min_heap]


def top_k_frequent_bucket(nums, k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, f in freq.items():
        buckets[f].append(num)

    result = []
    for f in range(len(buckets) - 1, 0, -1):
        for num in buckets[f]:
            result.append(num)
            if len(result) == k:
                return result

# ✅ Summary Table
# | Approach           | Time Complexity | Space    | Notes                     |
# | ------------------ | --------------- | -------- | ------------------------- |
# | Brute Force (Sort) | O(N log N)      | O(N)     | Easiest                   |
# | Min-Heap           | O(N log K)      | O(N + K) | Good for large N, small K |
# | Bucket Sort        | **O(N)**        | O(N)     | Best possible             |
