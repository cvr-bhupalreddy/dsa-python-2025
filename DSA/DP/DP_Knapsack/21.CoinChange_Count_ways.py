def coin_change_ways_memo_backward(coins, amount):
    n = len(coins)
    memo = [[-1] * (amount + 1) for _ in range(n)]

    def dp(i, amt):
        if amt == 0:
            return 1  # one way: no coins needed
        if i < 0 or amt < 0:
            return 0  # no ways

        if memo[i][amt] != -1:
            return memo[i][amt]

        # Backward recurrence: take current coin or move to previous coin
        take = dp(i, amt - coins[i])  # use current coin
        skip = dp(i - 1, amt)         # skip current coin

        memo[i][amt] = take + skip
        return memo[i][amt]

    return dp(n - 1, amount)


def coin_change_ways_tab_backward(coins, amount):
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]

    # Base case: amount 0 → 1 way
    for i in range(n):
        dp[i][0] = 1

    # Fill table from last coin to first
    for i in range(n):
        for amt in range(1, amount + 1):
            take = dp[i][amt - coins[i]] if coins[i] <= amt else 0
            skip = dp[i-1][amt] if i > 0 else 0
            dp[i][amt] = take + skip

    return dp[n-1][amount]


def coin_change_ways_space_opt_backward(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0

    for coin in coins:
        for amt in range(coin, amount + 1):
            dp[amt] += dp[amt - coin]

    return dp[amount]


def coin_change_ways_space_opt_index(coins, amount):
    n = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0

    # Loop over coins using index
    for i in range(n):
        for amt in range(coins[i], amount + 1):
            dp[amt] += dp[amt - coins[i]]

    return dp[amount]
