# standard DP order: solve from i → j)
#
# We try every partition k such that:
#
#     i ≤ k < j
# dp[i][j] = min(
#     dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
# )
# Break at k:
#
#     Left side = Ai…Ak
#     Right side = A(k+1)…Aj
#
# Dimension multiplication term
#
#     Left matrix → arr[i-1] × arr[k]
#     Right matrix → arr[k] × arr[j]
#     Final multiply → cost: arr[i-1]*arr[k]*arr[j]
#
#
# RECURRANCE — BACKWARD VERSION
#
# (solve subproblems from j → i)
#
# You reverse the direction of choosing partitions:
#
# j > k ≥ i
#
#
# Backward recurrence:
#
# dp[i][j] = min(
#     dp[i][k] + dp[k][j] + arr[i-1] * arr[k-1] * arr[j]
# )   where i < k ≤ j
#
# Why is it different?
#
# Because when using backward, "k" belongs to the right-side first, so dimensions shift one position:
#
# Left = Ai … A(k−1)
#
# Right = Ak … Aj
#
# So the multiplication dimensions become:
# Left  → arr[i-1] × arr[k-1]
# Right → arr[k-1] × arr[j]


from typing import List


class MatrixChainMultiplication:

    # ------------------------------------------------------------
    # 1. MEMOIZATION (FORWARD) – Standard recurrence
    # dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])
    # ------------------------------------------------------------
    def mcm_memo_forward(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            ans = float('inf')
            # i ≤ k < j
            for k in range(i, j):
                cost = (
                        solve(i, k) +
                        solve(k + 1, j) +
                        arr[i - 1] * arr[k] * arr[j]
                )
                ans = min(ans, cost)

            dp[i][j] = ans
            return ans

        return solve(1, n - 1)

    # ------------------------------------------------------------
    # 2. MEMOIZATION (BACKWARD)
    # dp[i][j] = min(dp[i][k-1] + dp[k][j] + arr[i-1]*arr[k-1]*arr[j])
    # ------------------------------------------------------------
    def mcm_memo_backward(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            ans = float('inf')
            # i < k ≤ j
            for k in range(i + 1, j + 1):
                cost = (
                        solve(i, k - 1) +
                        solve(k, j) +
                        arr[i - 1] * arr[k - 1] * arr[j]
                )
                ans = min(ans, cost)

            dp[i][j] = ans
            return ans

        return solve(1, n - 1)

    # ------------------------------------------------------------
    # 3. TABULATION (FORWARD) – Standard
    # Same recurrence as memo_forward
    # ------------------------------------------------------------
    def mcm_tab_forward(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        # length = number of matrices from i to j
        for length in range(2, n):  # length = (j - i + 1)
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                # forward k: i ≤ k < j
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n - 1]

    # ------------------------------------------------------------
    # 4. TABULATION (BACKWARD)
    # Same recurrence as memo_backward
    # ------------------------------------------------------------
    def mcm_tab_backward(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')

                # backward k: i < k ≤ j
                for k in range(i + 1, j + 1):
                    cost = dp[i][k - 1] + dp[k][j] + arr[i - 1] * arr[k - 1] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n - 1]

# Yes, MCM tabulation can be written as:
#
# for i = n-1 down to 1:
#     for j = i+1 to n-1:
#         dp[i][j] = min over k in [i..j-1] of
#         dp[i][k] + dp[k+1][j] + cost
#
# This works because:
# - dp[i][k] is computed earlier in the same j-loop (k < j)
# - dp[k+1][j] is computed earlier since row (k+1) > row (i)
# So all required subproblems are available.
#
# The classical length-based loop is used mainly because it is
# easier to understand, visualize, and generalize, not because
# your version is incorrect.


# Classical Diagonal loop structure Here N meaning Chain length
# for length = 2 to n-1:        # chain length
#     for i = 1 to n - length:
#         j = i + length - 1
#         dp[i][j] = +infinity
#
#         for k = i to j-1:    # partition
#             cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
#             dp[i][j] = min(dp[i][j], cost)
#
#
# | Variable | Meaning                                                      |
# | -------- | ------------------------------------------------------------ |
# | `length` | size of chain (2 matrices, 3 matrices, 4 matrices...)        |
# | `i`      | starting matrix index of chain                               |
# | `j`      | ending matrix index of chain                                 |
# | `k`      | partition point: splits chain into left and right sub-chains |
