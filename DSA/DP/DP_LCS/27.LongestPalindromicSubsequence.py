# Minimum Insertions to make one string as palindrome = Length(string) - LPS(string)

class LongestPalindromicSubsequence:

    # --------------------------------------
    # 1. MEMOIZATION (Top-down recursion)
    # --------------------------------------
    def lps_memo(self, s):
        n = len(s)
        memo = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]

            if s[i] == s[j]:
                memo[i][j] = 2 + solve(i + 1, j - 1)
            else:
                memo[i][j] = max(solve(i + 1, j), solve(i, j - 1))
            return memo[i][j]

        return solve(0, n - 1)

    # --------------------------------------
    # 2. TABULATION (Bottom-up DP)
    # --------------------------------------
    def lps_tab(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Base: length-1 substrings
        for i in range(n):
            dp[i][i] = 1

        # Build from shorter to longer ranges
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n - 1]

    # --------------------------------------
    # 3. SPACE OPTIMIZATION (1D DP)
    # --------------------------------------
    def lps_space_opt(self, s):
        n = len(s)
        prev = [0] * n
        curr = [0] * n

        # Base case for single characters
        for i in range(n):
            prev[i] = 1

        # Fill DP from bottom to top
        for i in range(n - 2, -1, -1):
            curr[i] = 1  # single character
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    curr[j] = 2 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])

            prev, curr = curr, [0] * n

        return prev[n - 1]


class LPS_LCS:

    # ---------------------------------------------------------
    # LPS LENGTH USING LCS
    # ---------------------------------------------------------
    def lps_length(self, s):
        t = s[::-1]
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # LCS of s and reversed s
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]

    # ---------------------------------------------------------
    # RECONSTRUCT THE LPS STRING USING LCS DP TABLE
    # ---------------------------------------------------------
    def lps_string(self, s):
        t = s[::-1]
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Fill table (LCS)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Reconstruct actual LPS (reverse LCS)
        i, j = n, n
        lps = []

        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                lps.append(s[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

        return ''.join(lps)
