class UnboundedKnapsack:

    # 1. Memoization
    def memo(self, wt, val, W):
        n = len(wt)
        dp = [[-1] * (W+1) for _ in range(n)]

        def solve(i, w):
            if i == 0:
                return (w // wt[0]) * val[0]

            if dp[i][w] != -1:
                return dp[i][w]

            not_take = solve(i-1, w)
            take = float('-inf')
            if wt[i] <= w:
                take = val[i] + solve(i, w - wt[i])

            dp[i][w] = max(take, not_take)
            return dp[i][w]

        return solve(n-1, W)

    # 2. Tabulation
    def tabulation(self, wt, val, W):
        n = len(wt)
        dp = [[0] * (W+1) for _ in range(n)]

        for w in range(W+1):
            dp[0][w] = (w // wt[0]) * val[0]

        for i in range(1, n):
            for w in range(W+1):
                not_take = dp[i-1][w]
                take = float('-inf')
                if wt[i] <= w:
                    take = val[i] + dp[i][w - wt[i]]
                dp[i][w] = max(take, not_take)

        return dp[n-1][W]

    # 3. Space Optimization
    def space_opt(self, wt, val, W):
        n = len(wt)
        dp = [0] * (W+1)

        for w in range(W+1):
            dp[w] = (w // wt[0]) * val[0]

        for i in range(1, n):
            for w in range(wt[i], W+1):
                dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

        return dp[W]
