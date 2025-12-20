# BRUTE FORCE INVERSION COUNT — CORE IDEA
#
# 1. Loop i from 0 to n-1.
# 2. For each i, loop j from i+1 to n-1.
# 3. For every pair (i, j):
# if arr[i] > arr[j]:
#     it is an inversion.
# 4. Count all such pairs.
# 5. Time complexity = O(n²), simple but slow.


def count_inversions_bruteforce(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


# CORE IDEA FOR COUNTING INVERSIONS (MERGE SORT METHOD)
#
# 1. A brute-force method checks all pairs (i, j), but this takes O(n²).
# To optimize, we use Merge Sort to count inversions in O(n log n).
#
# 2. While merging two sorted halves:
# - Left half = sorted
# - Right half = sorted
#
# 3. If left[i] <= right[j], no inversion, move i forward.
#
# 4. If left[i] > right[j], then:
# → All remaining elements in left (from i to end)
# are greater than right[j].
# → That means (mid - i + 1) inversions are found.
#
# 5. Keep counting these during merge steps.
#
# 6. Total inversions = inversions in left half
# + inversions in right half
# + inversions found during merge.


def count_inversions(arr):
    return merge_sort(arr, 0, len(arr) - 1)


def merge_sort(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    inv_count = 0

    inv_count += merge_sort(arr, left, mid)  # inversions in left half
    inv_count += merge_sort(arr, mid + 1, right)  # inversions in right half
    inv_count += merge(arr, left, mid, right)  # cross inversions

    return inv_count


def merge(arr, left, mid, right):
    temp = []
    i, j = left, mid + 1
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += (mid - i + 1)  # all remaining left elements are > arr[j]
            j += 1

    # add remaining elements
    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    # write back to array
    arr[left:right + 1] = temp

    return inv_count


# 1. Coordinate Compression:
# - Since BIT works for indices 1..N, map array elements to ranks (1..N).
#
# 2. Initialize BIT (Fenwick Tree) of size N+1 with 0.
#
# 3. Traverse the array from right to left:
# for each element arr[i]:
#     - Query BIT for count of elements less than arr[i] (sum of indices 1..rank-1)
#     - Add this count to inversions
#     - Update BIT at index = rank of arr[i] by 1 (mark that this element has appeared)
#
# 4. Time Complexity: O(n log n)
# Space Complexity: O(n) for BIT


def count_inversions_BIT(arr):
    # Step 1: Coordinate compression
    sorted_unique = sorted(set(arr))
    rank = {val: i + 1 for i, val in enumerate(sorted_unique)}  # 1-indexed for BIT

    # Step 2: BIT functions
    def update(BIT, i):
        while i < len(BIT):
            BIT[i] += 1
            i += i & -i

    def query(BIT, i):
        res = 0
        while i > 0:
            res += BIT[i]
            i -= i & -i
        return res

    # Step 3: Initialize BIT
    n = len(rank)
    BIT = [0] * (n + 1)
    inversions = 0

    # Step 4: Traverse array from right to left
    for num in reversed(arr):
        r = rank[num]
        inversions += query(BIT, r - 1)  # count of smaller elements already seen
        update(BIT, r)  # mark current element as seen

    return inversions


# Example
arr = [8, 4, 2, 1]
print("Inversions (BIT):", count_inversions_BIT(arr))  # Output: 6
