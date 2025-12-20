# 1️⃣ Problem
# Given an array nums, find the maximum sum of a contiguous subarray.
#
# 2️⃣ Core Idea
#
#     Maintain a running sum current_sum for the subarray ending at the current index.
#     If current_sum becomes negative, reset it to 0 (start a new subarray).
#     Keep track of the maximum sum seen so far in max_sum.


def kadane(nums):
    max_sum = float('-inf')  # overall maximum
    current_sum = 0           # max subarray ending at current index

    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0  # reset if negative

    return max_sum
