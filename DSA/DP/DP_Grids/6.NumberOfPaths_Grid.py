def numPaths_memoization(n, m):
    dp = [[-1] * m for _ in range(n)]

    def helper(i, j):
        if i == 0 and j == 0:
            return 1  # Start cell
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        # Paths from top + paths from left
        dp[i][j] = helper(i - 1, j) + helper(i, j - 1)
        return dp[i][j]

    return helper(n - 1, m - 1)


def numPaths_tabulation(n, m):
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = up + left

    return dp[n - 1][m - 1]


def numPaths_space(n, m):
    prev = [0]*m

    for i in range(n):
        curr = [0]*m
        for j in range(m):
            if i == 0 and j == 0:
                curr[j] = 1
            else:
                up = prev[j] if i > 0 else 0  # dp[i-1,j]
                left = curr[j-1] if j > 0 else 0  # dp[i,j-1]
                curr[j] = up + left
        prev = curr
    return prev[m-1]


