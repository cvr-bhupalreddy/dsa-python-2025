# Given a binary array nums and an integer k, flip at most k 0's.
#
# Return the maximum number of consecutive 1's after performing the flipping operation.

# Core Idea (Copyable)
#
#     Use two pointers left and right to define a window.
#     Count zeros in the current window.
#     If zeros exceed k, shrink the window from the left until zeros ≤ k.
#     Keep track of the maximum window size.

def longest_ones_brute(nums, k):
    n = len(nums)
    max_len = 0

    for i in range(n):
        zeros = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            if zeros > k:
                break
            max_len = max(max_len, j - i + 1)
    return max_len


def longest_ones_better(nums, k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def longest_ones_fixed(nums, k):
    n = len(nums)
    left = 0
    zeros_count = 0
    max_len = 0

    for right in range(n):
        if nums[right] == 0:
            zeros_count += 1

        # Shrink window until zeros_count <= k
        if zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1

        # Update max length only if zeros_count <= k
        if zeros_count <= k:
            max_len = max(max_len, right - left + 1)

    return max_len


