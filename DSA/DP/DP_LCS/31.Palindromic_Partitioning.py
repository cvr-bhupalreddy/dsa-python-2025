# Palindromic Partitioning Problem — Definition
#
# Given a string s, you must cut it into the minimum number of substrings such that: Every substring is a palindrome


class PalindromePartitioning:

    # -------------------------------------------------------
    # Utility to precompute palindrome table: isPal[i][j]
    # This is Diagonal method popularly used in Partition DP like MCM
    # -------------------------------------------------------
    def compute_pal_table(self, s):
        n = len(s)
        isPal = [[False]*n for _ in range(n)]

        for i in range(n):
            isPal[i][i] = True

        for length in range(2, n+1):  # substring length
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        isPal[i][j] = True
                    else:
                        isPal[i][j] = isPal[i+1][j-1]
        return isPal

    # -------------------------------------------------------
    # 1. Memoization (Top-Down)
    # dp[i] = minimum cuts for substring s[i:]
    # -------------------------------------------------------
    def min_cuts_memo(self, s):
        n = len(s)
        isPal = self.compute_pal_table(s)
        dp = [-1] * n

        def solve(i):
            if i == n or isPal[i][n-1]:
                return 0  # no more cuts needed

            if dp[i] != -1:
                return dp[i]

            ans = float('inf')
            for j in range(i, n):
                if isPal[i][j]:
                    ans = min(ans, 1 + solve(j + 1))

            dp[i] = ans
            return ans

        return solve(0)

    # -------------------------------------------------------
    # 2. Tabulation (Bottom-Up)
    # -------------------------------------------------------
    def min_cuts_tabulation(self, s):
        n = len(s)
        isPal = self.compute_pal_table(s)

        dp = [0] * (n+1)
        dp[n] = 0  # no cuts needed after end

        for i in range(n-1, -1, -1):
            if isPal[i][n-1]:
                dp[i] = 0
                continue

            best = float('inf')
            for j in range(i, n):
                if isPal[i][j]:
                    best = min(best, 1 + dp[j+1])
            dp[i] = best

        return dp[0]

    # -------------------------------------------------------
    # 3. Space Optimized
    #
    # NOTE: Full O(n^2) space cannot be reduced to O(n)
    #       unless we compute palindrome on the fly using
    #       "expand around center".
    #
    # This is the BEST space optimization possible.
    # -------------------------------------------------------
    def min_cuts_space_opt(self, s):
        n = len(s)
        dp = [float('inf')] * (n+1)
        dp[n] = 0

        # Expand palindrome around center → O(n^2)
        for center in range(n):
            # Odd-length palindromes
            l = r = center
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l] = min(dp[l], 1 + dp[r+1])
                l -= 1
                r += 1

            # Even-length palindromes
            l, r = center, center+1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l] = min(dp[l], 1 + dp[r+1])
                l -= 1
                r += 1

        return dp[0] - 1   # dp counts partitions, so cuts = partitions-1

