# 📌 Problem Statement — Aggressive Cows / Horses
# You are given:
# - An array `stalls[]` representing positions of stalls along a straight line.
# - An integer `c` representing the number of cows to place in the stalls.
#
# Constraints / Rules:
# 1. Each stall can contain **at most one cow**.
# 2. Cows must be placed in the stalls such that
# the **minimum distance between any two cows is maximized**.
# 3. You cannot move the stalls — positions are fixed.
# 4. Goal: Place all `c` cows in stalls obeying the rules and **maximize the minimum distance** between any two cows.


def aggressive_cows_bruteforce(stalls, c):
    """
    Brute-force approach to maximize minimum distance between cows.

    Args:
    stalls : List[int] - positions of stalls
    c      : int       - number of cows

    Returns:
    int - maximum minimum distance achievable
    """
    stalls.sort()
    max_distance = stalls[-1] - stalls[0]
    result = 0

    # Try every possible distance
    for d in range(1, max_distance + 1):
        count = 1  # place first cow at stalls[0]
        last_pos = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= d:
                count += 1
                last_pos = stalls[i]
                if count == c:  # all cows placed
                    break

        if count == c:
            result = d  # feasible distance
        else:
            break  # distance too large, cannot place all cows

    return result


# ✅ Better / Greedy + Checking Feasibility

# Core Idea:
#     1. Sort the stall positions.
#     2. Guess a distance 'd' and check if it is possible to place all cows with at least 'd' distance.
#     3. Use a greedy approach to place cows starting from the first stall.
#     4. Binary search over possible distances to find the **maximum feasible distance**.


# need minimum distance between cows [ minimum comes from consecutive stalls ]
def is_feasible(stalls, c, dist):
    last_pos = stalls[0]
    count = 1
    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= dist:
            count += 1
            last_pos = stalls[i]
            if count == c:
                return True
    return False


def aggressive_cows_optimal(stalls, c):
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if is_feasible(stalls, c, mid):
            ans = mid
            low = mid + 1  # try larger distance
        else:
            high = mid - 1
    return ans
