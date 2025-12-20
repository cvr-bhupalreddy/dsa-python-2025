#  variable starting point to variable ending point


def maxPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[-1] * m for _ in range(n)]

    def helper(i, j):
        if j < 0 or j >= m:  # out of bounds
            return float('-inf')  # for max path
        if i == n - 1:  # last row, base case
            return grid[i][j]
        # Option 2: direct assignment
        # dp[n-1] = grid[n-1] # this just makes a reference , original grid changes it's a issue
        if dp[i][j] != -1:
            return dp[i][j]

        down = helper(i + 1, j)
        left_diag = helper(i + 1, j - 1)
        right_diag = helper(i + 1, j + 1)

        dp[i][j] = grid[i][j] + max(down, left_diag, right_diag)
        return dp[i][j]

    # variable starting point: any column in first row
    return max(helper(0, j) for j in range(m))


def maxPathSumTab(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[0]*m for _ in range(n)]

    # Base: last row = grid last row
    # for j in range(m):
    #     dp[n-1][j] = grid[n-1][j]
    dp[n-1] = grid[n-1][:]

    # Fill bottom → top
    for i in range(n-2, -1, -1):
        for j in range(m):
            down = dp[i+1][j]
            left_diag = dp[i+1][j-1] if j-1 >= 0 else float('-inf')
            right_diag = dp[i+1][j+1] if j+1 < m else float('-inf')
            dp[i][j] = grid[i][j] + max(down, left_diag, right_diag)

    # variable starting point: any column in first row
    return max(dp[0])


def maxPathSumSpace(grid):
    n = len(grid)
    m = len(grid[0])
    prev = grid[-1][:]  # start from last row

    for i in range(n-2, -1, -1):
        curr = [0]*m
        for j in range(m):
            down = prev[j]
            left_diag = prev[j-1] if j-1 >= 0 else float('-inf')
            right_diag = prev[j+1] if j+1 < m else float('-inf')
            curr[j] = grid[i][j] + max(down, left_diag, right_diag)
        prev = curr

    return max(prev)
