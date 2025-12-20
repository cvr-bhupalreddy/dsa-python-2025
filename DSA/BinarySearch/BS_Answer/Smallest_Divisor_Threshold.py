# Problem:
# Given an array nums[] and a threshold,
# find the smallest integer divisor D such that:
#     sum(ceil(nums[i] / D)) ≤ threshold

# Bruteforce Idea:
#     Try every divisor D starting from 1 upward.
#     For each D, compute the sum and check feasibility.

# Better Idea:
#     Only try divisors from 1 to max(nums). (Still slow)

# Optimal Idea (Binary Search on Answer):
# The feasibility function is monotonic:
#     If a divisor D works,
#     any larger divisor will also work.
#
# So search D between [1, max(nums)] using binary search:
#     mid = (l + r) // 2
#     If divisor mid satisfies threshold → move left
#     Else → move right


def smallestDivisor_bruteforce(nums, threshold):
    import math

    for D in range(1, max(nums) + 1):
        total = sum(math.ceil(n / D) for n in nums)
        if total <= threshold:
            return D

    return -1


def smallestDivisor_better(nums, threshold):
    import math

    low, high = 1, max(nums)

    for D in range(low, high + 1):
        total = sum(math.ceil(n / D) for n in nums)
        if total <= threshold:
            return D

    return -1
