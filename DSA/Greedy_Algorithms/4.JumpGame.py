# 🍀 Jump Game I
# Problem Statement
#     You are given an array of non-negative integers nums,
#     where each element represents the maximum jump length from that position.
#     Determine if you can reach the last index starting from the first index.


def jump1(arr):
    maxReach = 0
    for index in range(len(arr)):
        if index > maxReach:
            return False
        maxReach = max(maxReach, index + arr[index])
    return True


# 🍀 Jump Game II
# Problem Statement
#     You are given an array of non-negative integers nums,
#     where each element represents the maximum jump length from that position.
#     Return the minimum number of jumps required to reach the last index.
#     You can assume you can always reach the last index.

#
# Core Idea (Greedy Approach)
#
# Keep track of two pointers:
#     currentEnd → the farthest index reachable with current number of jumps
#     farthest → the farthest index reachable in the next jump
#
# Iterate through array:
#     Update farthest = max(farthest, i + nums[i])
#     If i == currentEnd → jump += 1, update currentEnd = farthest
# Return the total number of jumps.


def jump_game2_range(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    left = 0  # start of current jump range
    right = 0  # end of current jump range
    farthest = 0  # farthest index reachable from current range

    while right < n - 1:
        # Explore current range to find farthest we can reach in next jump
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])

        # Make a jump
        jumps += 1
        left = right + 1
        right = farthest

    return jumps


def jump_game2_range_safe(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    left = 0  # start of current jump range
    right = 0  # end of current jump range
    farthest = 0  # farthest index reachable from current range

    while right < n - 1:
        # Explore current range to find farthest we can reach in next jump
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])

        # If we can't move forward, last index is unreachable
        if farthest <= right:
            return -1

        # Make a jump
        jumps += 1
        left = right + 1
        right = farthest

    return jumps


def jump_game2_greedy(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0  # total jumps made
    farthest = 0  # farthest index reachable in current jump
    end = 0  # end of current jump range

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])

        # When we reach the end of the current jump, increase jump count
        if i == end:
            jumps += 1
            end = farthest

    return jumps


def jump_game2_greedy_safe(nums):
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    farthest = 0
    end = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])

        if i == end:
            if end == farthest:
                return -1  # cannot move forward, last index unreachable
            jumps += 1
            end = farthest

    return jumps
