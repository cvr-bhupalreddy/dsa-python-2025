def knapsack_memo(weights, values, W):
    n = len(weights)
    dp = [[-1] * (W + 1) for _ in range(n)]

    def solve(i, cap):
        if i == 0:
            return values[0] if weights[0] <= cap else 0

        if dp[i][cap] != -1:
            return dp[i][cap]

        not_take = solve(i - 1, cap)

        take = 0
        if weights[i] <= cap:
            take = values[i] + solve(i - 1, cap - weights[i])

        dp[i][cap] = max(take, not_take)
        return dp[i][cap]

    return solve(n - 1, W)


def knapsack_tab(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n)]

    # Base case: first item
    for w in range(weights[0], W + 1):
        dp[0][w] = values[0]

    for i in range(1, n):
        for cap in range(W + 1):
            not_take = dp[i - 1][cap]
            take = 0
            if weights[i] <= cap:
                take = values[i] + dp[i - 1][cap - weights[i]]
            dp[i][cap] = max(take, not_take)

    return dp[n - 1][W]


def knapsack_space_opt(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)

    # Base case: first item
    for cap in range(weights[0], W + 1):
        dp[cap] = values[0]

    # Process next items
    for i in range(1, n):
        for cap in range(W, weights[i] - 1, -1):
            dp[cap] = max(
                dp[cap],
                values[i] + dp[cap - weights[i]]
            )

    return dp[W]

#
# | Method              | Time     | Space                | Notes                |
# | ------------------- | -------- | -------------------- | -------------------- |
# | **Memoization**     | O(N × W) | O(N × W) + recursion | Easiest conceptually |
# | **Tabulation**      | O(N × W) | O(N × W)             | Bottom-up            |
# | **Space Optimized** | O(N × W) | O(W)                 | Most efficient       |
