# 🔹 Approach (Using DP)
#
#     Compute total sum of array: total = sum(arr).
#
#     Idea: Let subset S1 sum to s1. Then S2 sum = total - s1.
#     Absolute difference: abs(total - 2*s1).
#
#     Goal: Find all possible subset sums ≤ total//2 using DP.
#         Why ≤ total//2? Because minimizing abs(total - 2*s1) is easier if s1 <= total//2.
#
#     Subset sum DP:
#         Let dp[i][k] = True if we can form sum k using first i elements.


arr = [1, 6, 11, 5]


def min_subset_sum_diff(arr):
    n = len(arr)
    total = sum(arr)
    target = total // 2

    # DP table: dp[i][k] = True if sum k is possible with first i elements
    dp = [[False] * (target + 1) for _ in range(n)]

    # Base case: sum 0 is always possible
    for i in range(n):
        dp[i][0] = True

    if arr[0] <= target:
        dp[0][arr[0]] = True

    # Fill the DP table
    for i in range(1, n):
        for k in range(1, target + 1):
            not_take = dp[i - 1][k]
            take = dp[i - 1][k - arr[i]] if k >= arr[i] else False
            dp[i][k] = take or not_take

    # Find the maximum possible subset sum s1 <= total//2
    s1 = max(k for k in range(target + 1) if dp[n - 1][k])
    s2 = total - s1
    return abs(s2 - s1)


def min_subset_sum_diff_space_opt(arr):
    n = len(arr)
    total = sum(arr)
    target = total // 2
    prev = [False] * (target + 1)
    prev[0] = True
    if arr[0] <= target:
        prev[arr[0]] = True

    for i in range(1, n):
        curr = [False] * (target + 1)
        curr[0] = True
        for k in range(1, target + 1):
            not_take = prev[k]
            take = prev[k - arr[i]] if k >= arr[i] else False
            curr[k] = take or not_take
        prev = curr

    s1 = max(k for k in range(target + 1) if prev[k])
    s2 = total - s1
    return abs(s2 - s1)


print("Minimum subset sum difference (space optimized):", min_subset_sum_diff_space_opt(arr))
