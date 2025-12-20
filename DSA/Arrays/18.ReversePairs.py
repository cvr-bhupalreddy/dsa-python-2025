# Given an integer array nums. Return the number of reverse pairs in the array.
#
# An index pair (i, j) is called a reverse pair if:
#     0 <= i < j < nums.length
#     nums[i] > 2 * nums[j]


def reverse_pairs_brute(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count


# Approach 2 — Better (Using Sorted List / BST-like insertion)
# Idea
#     Traverse the array backwards.
#     Maintain a sorted list of elements already seen.
#     For current element nums[i], count how many elements in the sorted list satisfy nums[i] > 2 * x.
#     Insert nums[i] into the sorted list.
#
# Time Complexity: O(n log n) (if balanced BST, or bisect in Python)
# Space Complexity: O(n)

import bisect


def reverse_pairs_better(nums):
    sorted_list = []
    count = 0

    for num in reversed(nums):
        idx = bisect.bisect_left(sorted_list, num / 2 + 1)
        count += idx
        bisect.insort(sorted_list, num)

    return count


def reverse_pairs_optimal(nums):
    return merge_sort(nums, 0, len(nums) - 1)


# Core Idea
#
# Similar to count inversions problem.
#
# Use merge sort to:
# Count reverse pairs within left, right, and across halves.
#
# Merge the halves.
# While merging, for each element in left half, count number of elements in
# right half satisfying nums[i] > 2 * nums[j] using two pointers (because both halves are sorted).
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)


def merge_sort(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    count = merge_sort(arr, left, mid) + merge_sort(arr, mid + 1, right)
    count += count_cross_pairs(arr, left, mid, right)
    merge(arr, left, mid, right)
    return count


def count_cross_pairs(arr, left, mid, right):
    count = 0
    j = mid + 1
    for i in range(left, mid + 1):
        while j <= right and arr[i] > 2 * arr[j]:
            j += 1
        count += (j - (mid + 1))
    return count


def merge(arr, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    temp.extend(arr[i:mid + 1])
    temp.extend(arr[j:right + 1])
    arr[left:right + 1] = temp
