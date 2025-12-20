def climbStairs_td(n):
    dp = [-1] * (n + 1)

    def solve(i):
        if i == 0 or i == 1:
            return 1
        if dp[i] != -1:
            return dp[i]
        dp[i] = solve(i - 1) + solve(i - 2)
        return dp[i]

    return solve(n)


def climbStairs_tabulation(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climbStairs_spaceOptimization(n):
    if n <= 1:
        return 1

    prev2, prev1 = 1, 1

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1
