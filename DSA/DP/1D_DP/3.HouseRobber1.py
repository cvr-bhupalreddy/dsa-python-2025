def maxSumNonAdjacent(arr):
    n = len(arr)
    dp = [-1] * n

    def solve(i):
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        pick = arr[i] + solve(i - 2)
        not_pick = solve(i - 1)
        dp[i] = max(pick, not_pick)
        return dp[i]

    return solve(n - 1)


def maxSumNonAdjacent_Tabulation(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])

    return dp[-1]


def maxSumNonAdjacent_spaceOptimization(arr):
    prev = arr[0]
    prev2 = 0

    for i in range(1, len(arr)):
        pick = arr[i] + prev2
        not_pick = prev
        curr = max(pick, not_pick)
        prev2, prev = prev, curr

    return prev


arr = [3, 2, 7, 10]
print(maxSumNonAdjacent(arr))  # Output: 12

