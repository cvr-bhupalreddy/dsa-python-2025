def unique_paths_memo(grid):
    n, m = len(grid), len(grid[0])
    dp = [[-1] * m for _ in range(n)]

    def helper(i, j):
        # Base conditions
        if i < 0 or j < 0 or grid[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        up = helper(i - 1, j)
        left = helper(i, j - 1)

        dp[i][j] = up + left
        return dp[i][j]

    return helper(n - 1, m - 1)


def unique_paths_tab(grid):
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = up + left

    return dp[n - 1][m - 1]


def unique_paths_space_optimized(grid):
    n, m = len(grid), len(grid[0])
    prev = [0] * m

    for i in range(n):
        curr = [0] * m
        for j in range(m):
            if grid[i][j] == 1:
                curr[j] = 0
                continue
            if i == 0 and j == 0:
                curr[j] = 1
                continue

            up = prev[j] if i > 0 else 0
            left = curr[j - 1] if j > 0 else 0
            curr[j] = up + left

        prev = curr

    return prev[m - 1]
