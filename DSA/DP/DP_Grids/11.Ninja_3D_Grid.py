class Solution:
    # ---------------------- 1️⃣ Memoization ----------------------
    def maximumChocolatesMemo(self, n, m, grid):
        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        def helper(i, j1, j2):
            # Boundary check
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
                return float('-inf')

            # Base case: last row
            if i == n - 1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]

            # Memoization check
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            maxi = float('-inf')
            # Explore 9 possibilities (3×3 moves)
            for dj1 in [-1, 0, 1]:
                for dj2 in [-1, 0, 1]:
                    if j1 == j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]
                    value += helper(i + 1, j1 + dj1, j2 + dj2)
                    maxi = max(maxi, value)

            dp[i][j1][j2] = maxi
            return maxi

        return helper(0, 0, m - 1)

    # ---------------------- 2️⃣ Tabulation ----------------------

    def maximumChocolatesTab(self, n, m, grid):
        dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        # Base case: last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n - 1][j1][j2] = grid[n - 1][j1]
                else:
                    dp[n - 1][j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

        # Fill table bottom-up
        for i in range(n - 2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float('-inf')
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            if 0 <= j1 + dj1 < m and 0 <= j2 + dj2 < m:
                                value = grid[i][j1] + (grid[i][j2] if j1 != j2 else 0)
                                value += dp[i + 1][j1 + dj1][j2 + dj2]
                            else:
                                value = float('-inf')
                            maxi = max(maxi, value)
                    dp[i][j1][j2] = maxi

        return dp[0][0][m - 1]

    # ---------------------- 3️⃣ Space Optimization ----------------------
    def maximumChocolatesSpaceOpt(self, n, m, grid):
        front = [[0 for _ in range(m)] for _ in range(m)]

        # Base case: last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    front[j1][j2] = grid[n - 1][j1]
                else:
                    front[j1][j2] = grid[n - 1][j1] + grid[n - 1][j2]

        # Iterate upward
        for i in range(n - 2, -1, -1):
            cur = [[0 for _ in range(m)] for _ in range(m)]
            for j1 in range(m):
                for j2 in range(m):
                    maxi = float('-inf')
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            if 0 <= j1 + dj1 < m and 0 <= j2 + dj2 < m:
                                value = grid[i][j1] + (grid[i][j2] if j1 != j2 else 0)
                                value += front[j1 + dj1][j2 + dj2]
                            else:
                                value = float('-inf')
                            maxi = max(maxi, value)
                    cur[j1][j2] = maxi
            front = cur

        return front[0][m - 1]
