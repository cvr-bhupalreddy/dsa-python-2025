class CoinChangeMinCoins:

    # 1. Memoization
    def memo(self, coins, target):
        n = len(coins)
        dp = [[-1] * (target + 1) for _ in range(n)]

        def solve(i, t):
            if i == 0:
                return t // coins[0] if (t % coins[0] == 0) else float('inf')

            if dp[i][t] != -1:
                return dp[i][t]

            not_take = solve(i - 1, t)
            take = float('inf')
            if coins[i] <= t:
                take = 1 + solve(i, t - coins[i])

            dp[i][t] = min(take, not_take)
            return dp[i][t]

        ans = solve(n - 1, target)
        return ans if ans != float('inf') else -1

    # 2. Tabulation
    def tabulation(self, coins, target):
        n = len(coins)
        dp = [[float('inf')] * (target + 1) for _ in range(n)]

        for t in range(target + 1):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]

        for i in range(1, n):
            for t in range(target + 1):
                not_take = dp[i - 1][t]
                take = float('inf')
                if coins[i] <= t:
                    take = 1 + dp[i][t - coins[i]]
                dp[i][t] = min(take, not_take)

        return dp[n - 1][target] if dp[n - 1][target] != float('inf') else -1

    # 3. Space Optimization
    def space_opt(self, coins, target):
        dp = [float('inf')] * (target + 1)
        dp[0] = 0

        for coin in coins:
            for t in range(coin, target + 1):
                dp[t] = min(dp[t], 1 + dp[t - coin])

        return dp[target] if dp[target] != float('inf') else -1


def coin_change_min_space_opt(coins, target):
    dp = [0] + [float('inf')] * target  # 1D array

    for i in range(len(coins) - 1, -1, -1):
        for amt in range(coins[i], target + 1):
            dp[amt] = min(dp[amt], 1 + dp[amt - coins[i]])

    return dp[target] if dp[target] != float('inf') else -1
