
# -----------------------------
# CORE IDEA
# -----------------------------
# 1. dp[i][j] = max coins from bursting balloons in interval [i..j]
# 2. When k is chosen as last balloon to burst:
#    - Left interval [i..k-1] already burst
#    - Right interval [k+1..j] already burst
#    - Only neighbors i-1 and j+1 remain
#    coins = nums[i-1] * nums[k] * nums[j+1]
# 3. Total coins: dp[i][k-1] + dp[k+1][j] + coins
# 4. dp[i][j] = max over all k in [i..j]
# 5. Base case: i > j → 0

class BurstBalloons:

    # ---------------------------------------------------------
    # 1) MEMOIZATION (NO LRU CACHE)
    # ---------------------------------------------------------
    def maxCoinsMemo(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[-1] * n for _ in range(n)]

        def solve(i, j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            best = 0
            for k in range(i, j + 1):
                coins = nums[i-1] * nums[k] * nums[j+1]
                total = solve(i, k - 1) + solve(k + 1, j) + coins
                best = max(best, total)

            dp[i][j] = best
            return best

        return solve(1, n - 2)

    # ---------------------------------------------------------
    # 2) TABULATION — DIAGONAL (LENGTH-BASED)
    # ---------------------------------------------------------
    def maxCoinsTabDiagonal(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):
            for i in range(1, n - length):
                j = i + length - 1
                for k in range(i, j + 1):
                    coins = nums[i-1] * nums[k] * nums[j+1]
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k-1] + dp[k+1][j] + coins)

        return dp[1][n-2]

    # ---------------------------------------------------------
    # 3) TABULATION — SIMPLE (i decreasing, j increasing)
    # ---------------------------------------------------------
    def maxCoinsTabSimple(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):
                best = 0
                for k in range(i, j + 1):
                    coins = nums[i-1] * nums[k] * nums[j+1]
                    best = max(best,
                               dp[i][k-1] + dp[k+1][j] + coins)
                dp[i][j] = best

        return dp[1][n - 2]
