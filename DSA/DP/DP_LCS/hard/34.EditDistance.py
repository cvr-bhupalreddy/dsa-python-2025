# Problem Definition
#
# Given two strings:
#     s1 of length n
#     s2 of length m
#
# The edit distance (also called Levenshtein distance) is the minimum number of operations to convert s1 into s2,
# where the allowed operations are:
#   Insert a character
#   Delete a character
#   Replace a character

# Let dp[i][j] = minimum edit distance to convert s1[0..i-1] → s2[0..j-1]
#
# Base cases:
#     i == 0 → dp[0][j] = j  # insert all
#     j == 0 → dp[i][0] = i  # delete all
#
# Recurrence:
#     if s1[i-1] == s2[j-1]:
#         dp[i][j] = dp[i-1][j-1]
#     else:
#         dp[i][j] = 1 + min(
#             dp[i-1][j],    # delete
#             dp[i][j-1],    # insert
#             dp[i-1][j-1]   # replace
#         )


class EditDistance:

    # -----------------------------
    # 1. MEMOIZATION (TOP-DOWN DP)
    # -----------------------------
    def memoized(self, s1, s2):
        n, m = len(s1), len(s2)
        memo = [[-1]*(m+1) for _ in range(n+1)]

        def dfs(i, j):
            # Base cases
            if i == 0: return j      # need j insertions
            if j == 0: return i      # need i deletions

            if memo[i][j] != -1:
                return memo[i][j]

            if s1[i-1] == s2[j-1]:
                memo[i][j] = dfs(i-1, j-1)
            else:
                memo[i][j] = 1 + min(
                    dfs(i-1, j),     # delete
                    dfs(i, j-1),     # insert
                    dfs(i-1, j-1)    # replace
                )
            return memo[i][j]

        return dfs(n, m)

    # -----------------------------
    # 2. TABULATION (BOTTOM-UP DP)
    # -----------------------------
    def tabulation(self, s1, s2):
        n, m = len(s1), len(s2)

        dp = [[0]*(m+1) for _ in range(n+1)]

        # Base rows + columns
        for i in range(n+1):
            dp[i][0] = i   # delete all
        for j in range(m+1):
            dp[0][j] = j   # insert all

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # delete
                        dp[i][j-1],    # insert
                        dp[i-1][j-1]   # replace
                    )

        return dp[n][m]

    # ------------------------------------
    # 3. SPACE OPTIMIZED DP (O(min(n,m)))
    # ------------------------------------
    def space_optimized(self, s1, s2):
        n, m = len(s1), len(s2)

        prev = [0]*(m+1)

        # Base case: convert empty s1 to s2
        for j in range(m+1):
            prev[j] = j

        for i in range(1, n+1):
            curr = [0]*(m+1)
            curr[0] = i   # delete all to get empty s2

            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(
                        prev[j],      # delete
                        curr[j-1],    # insert
                        prev[j-1]     # replace
                    )
            prev = curr

        return prev[m]
