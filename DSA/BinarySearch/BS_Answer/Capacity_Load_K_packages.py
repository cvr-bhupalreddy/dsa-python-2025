# You are given an array `weights[]` where weights[i] represents the weight of the i-th package.
# All packages must be shipped in the given order (no reordering is allowed).
#
# You have a ship that can carry a maximum load of `C` per day.
#
# Rules / Constraints:
# 1. You may load **multiple packages on the same day** as long as the total weight
#     loaded that day does not exceed the ship capacity C.
# 2. **Fractional loading is NOT allowed.**
#     Each package must be shipped as a whole. You cannot split a package across days.
# 3. If adding the next package exceeds the capacity C, you must start a **new day**.
# 4. You must ship **all packages** within `D` days.
#
# Goal:
# Find the **minimum ship capacity C** such that all packages can be shipped within exactly `D` or fewer days.


# Start capacity from max(weights) up to sum(weights).
#     For each capacity C:
#         Simulate the shipping process.
#         If it finishes in <= D days:
#     return C
# Time: O(N * SUM)  (too slow)

def shipWithinDays_bruteforce(weights, D):
    def days_needed(cap):
        days = 1
        load = 0
        for w in weights:
            if load + w > cap:
                days += 1
                load = 0
            load += w
        return days

    low = max(weights)
    high = sum(weights)

    for cap in range(low, high + 1):
        if days_needed(cap) <= D:
            return cap

# Search space = [max(weights), sum(weights)]
#
# Feasibility(C):
#     simulate days needed if ship capacity is C
#     if days_required <= D → feasible
#
# Binary search to find minimum feasible capacity.
# Time: O(N log(sum(weights)))


# function feasible(C):
# days = 1
# currentLoad = 0
# for w in weights:
#     if currentLoad + w > C:
#         days += 1
#         currentLoad = 0
#     currentLoad += w
# return days <= D


def shipWithinDays(weights, D):
    def feasible(cap):
        days = 1
        load = 0
        for w in weights:
            if load + w > cap:
                days += 1
                load = 0
            load += w
        return days <= D

    low, high = max(weights), sum(weights)

    while low < high:
        mid = (low + high) // 2
        if feasible(mid):
            high = mid
        else:
            low = mid + 1

    return low
