class LCS:

    # -----------------------------
    # 1. MEMOIZATION (Start at n-1, m-1)
    # -----------------------------
    def lcs_memo_backward(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[-1]*m for _ in range(n)]

        def lcs(i, j):   # ← inner function renamed to 'lcs'
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = 1 + lcs(i-1, j-1)
            else:
                dp[i][j] = max(lcs(i-1, j), lcs(i, j-1))

            return dp[i][j]

        return lcs(n-1, m-1)

    # -----------------------------
    # 2. MEMOIZATION (Start at 0, 0)
    # -----------------------------
    def lcs_memo_forward(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[-1]*m for _ in range(n)]

        def lcs(i, j):   # ← renamed inner function
            if i == n or j == m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = 1 + lcs(i+1, j+1)
            else:
                dp[i][j] = max(lcs(i+1, j), lcs(i, j+1))

            return dp[i][j]

        return lcs(0, 0)

    # -----------------------------
    # 3. TABULATION
    # -----------------------------
    def lcs_tabulation(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)] # Base case uses shifting of indices

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]

    # -----------------------------
    # 4. SPACE OPTIMIZED (1D)
    # -----------------------------
    def lcs_space_optimized(self, s1, s2):
        n, m = len(s1), len(s2)
        prev = [0]*(m+1)

        for i in range(1, n+1):
            curr = [0]*(m+1)
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr

        return prev[m]
