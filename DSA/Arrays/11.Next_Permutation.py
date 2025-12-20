# 1️⃣ Problem Statement
#
# Given an array of integers nums, rearrange it into the lexicographically next greater permutation.
# If such arrangement is not possible, rearrange it as the lowest possible order (sorted in ascending).
#
# In-place modification is required.


# Optimal Approach (In-Place, O(n))
#
# Core Idea:
#     Traverse from right to left to find the first decreasing element (index i) such that nums[i] < nums[i+1].
#     Traverse from right to left again to find the first element greater than nums[i] (index j).
#     Swap nums[i] and nums[j].
#     Reverse the subarray from i+1 to end.
#
# Why it works:
# Step 1 → find pivot where permutation can be increased.
# Step 2 → find smallest number just bigger than pivot to swap.
# Step 3 → reverse suffix to get the smallest next permutation.


def nextPermutation(nums):
    n = len(nums)

    # Step 1: find first decreasing element from right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: find number just bigger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: swap
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: reverse the suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
