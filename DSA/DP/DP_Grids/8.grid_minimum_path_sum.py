def min_path_sum_memo(grid):
    n, m = len(grid), len(grid[0])
    dp = [[-1] * m for _ in range(n)]

    def helper(i, j):
        # Base cases
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')  # out of bounds

        if dp[i][j] != -1:
            return dp[i][j]

        up = grid[i][j] + helper(i - 1, j)
        left = grid[i][j] + helper(i, j - 1)

        dp[i][j] = min(up, left)
        return dp[i][j]

    return helper(n - 1, m - 1)


def min_path_sum_tab(grid):
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                up = grid[i][j] + (dp[i - 1][j] if i > 0 else float('inf'))
                left = grid[i][j] + (dp[i][j - 1] if j > 0 else float('inf'))
                dp[i][j] = min(up, left)

    return dp[n - 1][m - 1]


def min_path_sum_space(grid):
    n, m = len(grid), len(grid[0])
    prev = [float('inf')] * m

    for i in range(n):
        curr = [float('inf')] * m
        for j in range(m):
            if i == 0 and j == 0:
                curr[j] = grid[i][j]
            else:
                up = grid[i][j] + (prev[j] if i > 0 else float('inf'))
                left = grid[i][j] + (curr[j - 1] if j > 0 else float('inf'))
                curr[j] = min(up, left)
        prev = curr

    return prev[m - 1]





