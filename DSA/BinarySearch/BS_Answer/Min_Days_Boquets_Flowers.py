# 📌 Problem Statement
#
# You are given:
#     • bloomDay[] — an array where bloomDay[i] is the day the i-th flower blooms.
#     • M — number of bouquets needed.
#     • K — number of adjacent flowers required for one bouquet.
#
# Goal:
# Find the minimum number of days required such that:
#     • At least M bouquets can be formed.
#     • Each bouquet must use K adjacent (contiguous) flowers.
#     • A flower can be used at most once.
#
# If it is impossible to make M bouquets, return -1.


# Core Idea (Brute Force):
# • Try every possible day D from min(bloomDay) to max(bloomDay).
# • For each D, count how many bouquets can be made:
#     - Traverse bloomDay[]
#     - Count adjacent flowers with bloomDay[i] ≤ D
#     - Every K consecutive bloomed flowers form 1 bouquet
#     • The first D where bouquetCount ≥ M is the answer.
#
# Why it is slow:
#     • For every day, we scan the entire array → O(N)
#     • Days range up to 10⁹ → very slow

def minDays_bruteforce(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    low = min(bloomDay)
    high = max(bloomDay)

    # Try each possible day
    for day in range(low, high + 1):
        bouquets = 0
        flowers = 0

        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
            else:
                flowers = 0

            if flowers == k:
                bouquets += 1
                flowers = 0

        if bouquets >= m:
            return day

    return -1


# Core Idea:
# • Same as brute force but instead of checking every day,
# check only unique bloom days (sorted).
#
# Steps:
# • Extract sorted unique bloom days.
# • For each D in uniqueDays:
#     - Check how many bouquets can be made.
# • Pick the minimum D that works.
#
# Why better than brute force:
# • Reduces number of days drastically.
#
# Still not optimal:
# • Worst-case still O(N²) for large inputs.

def minDays_better(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1

    unique_days = sorted(set(bloomDay))

    def canMake(day):
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
            else:
                flowers = 0

            if flowers == k:
                bouquets += 1
                flowers = 0
        return bouquets >= m

    for day in unique_days:
        if canMake(day):
            return day

    return -1


# Core Idea (Binary Search on Minimum Valid Day):
#
# • The number of days needed is monotonic:
#     If we can make M bouquets on day D,
#     then we can also make M bouquets on any day > D.
#
# • Therefore, we binary-search on the number of days.
#
# • Define a helper function canMake(D):
#     Count adjacent flowers with bloomDay[i] ≤ D.
#     Each time we collect K adjacent, form a bouquet.
#     Return True if bouquetCount ≥ M.
#
# • Low = min(bloomDay)
# • High = max(bloomDay)
#
# • Binary search for the first day where canMake(D) = True.


def minDays_optimal(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1  # impossible

    def canMake(day):
        bouquets = 0
        flowers = 0

        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
            else:
                flowers = 0

            if flowers == k:
                bouquets += 1
                flowers = 0  # reset after forming bouquet

            if bouquets >= m:
                return True

        return False

    low, high = min(bloomDay), max(bloomDay)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if canMake(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
