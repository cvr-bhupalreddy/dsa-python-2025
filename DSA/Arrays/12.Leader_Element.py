# 1️⃣ Problem Statement
# Given an array arr of size n, an element is called a leader if it is strictly greater than all elements to its right.
# The rightmost element is always a leader.
#
# Goal: Find all leaders in the array.


def leaders_better(arr):
    n = len(arr)
    leaders = []
    suffix_max = [0] * n
    suffix_max[-1] = arr[-1]

    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(arr[i + 1], suffix_max[i + 1])

    for i in range(n - 1):
        if arr[i] > suffix_max[i]:
            leaders.append(arr[i])

    leaders.append(arr[-1])  # last element always a leader
    return leaders

# C. Optimal Approach (Single Pass, O(1) Extra Space)
#
# Traverse from right to left.
# Keep track of maximum element seen so far (max_from_right).
# If current element > max_from_right, it’s a leader.
# Update max_from_right


def leaders_optimal(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    # Optional: reverse to maintain order from left to right
    leaders.reverse()
    return leaders
