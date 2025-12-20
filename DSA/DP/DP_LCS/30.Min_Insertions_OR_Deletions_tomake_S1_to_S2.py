# Minimum Insertions + Deletions to Convert s1 → s2
#
# Let:
#
#   n = len(s1)
#   m = len(s2)
#   L = LCS(s1, s2)
#
#   Min Deletions  = n - L
#   Min Insertions = m - L
#
# Total operations = (n - L) + (m - L)


class MinInsertDelete:
    def min_operations(self, s1, s2):
        n, m = len(s1), len(s2)

        # LCS DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        L = dp[n][m]  # LCS length

        deletions = n - L
        insertions = m - L

        return deletions, insertions, deletions + insertions

