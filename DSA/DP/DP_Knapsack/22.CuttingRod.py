# Unbounded Knapsack to Rod cutting mapping
# wt[i] = i + 1  # piece lengths
# val[i] = price[i]  # prices of pieces
# W = N  # rod length

# weights[i] = i+1 for rod cutting 
#
# | Aspect         | Unbounded Knapsack                     | Rod Cutting                                     |
# | -------------- | -------------------------------------- | ----------------------------------------------- |
# | Input          | `wt[], val[], W`                       | `price[], N`                                    |
# | Capacity       | `W`                                    | Rod length `N`                                  |
# | Base case      | `(cap // wt[0]) * val[0]`              | `length * price[0]`                             |
# | Take condition | `if wt[ind] <= cap`                    | `if (ind + 1) <= length`                        |
# | Take value     | `val[ind] + recur(ind, cap - wt[ind])` | `price[ind] + recur(ind, length - (ind + 1))`   |
# | Concept        | General items with unlimited supply    | Rod pieces of length 1..N with unlimited supply |


class RodCutting:
    def __init__(self):
        pass

    # 1️⃣ Memoization (2D DP, backward)
    def rod_cut_memo(self, price, N):
        n = len(price)
        dp = [[-1] * (N + 1) for _ in range(n)]

        def recur(ind, length):
            if ind == 0:
                return length * price[0]

            if dp[ind][length] != -1:
                return dp[ind][length]

            # Skip current piece
            not_take = recur(ind - 1, length)
            # Take current piece (unbounded)
            take = float('-inf')
            if (ind + 1) <= length:
                take = price[ind] + recur(ind, length - (ind + 1))

            dp[ind][length] = max(not_take, take)
            return dp[ind][length]

        return recur(n - 1, N)

    # 2️⃣ Tabulation (2D DP, backward)
    def rod_cut_tab(self, price, N):
        n = len(price)
        dp = [[0] * (N + 1) for _ in range(n)]

        # Base case: only piece of length 1
        for length in range(N + 1):
            dp[0][length] = length * price[0]

        for ind in range(1, n):
            for length in range(N + 1):
                not_take = dp[ind - 1][length]
                take = 0
                if (ind + 1) <= length:
                    take = price[ind] + dp[ind][length - (ind + 1)]
                dp[ind][length] = max(not_take, take)

        return dp[n - 1][N]

    # 3️⃣ Space Optimization (1D DP)
    def rod_cut_space_opt(self, price, N):
        n = len(price)
        dp = [0] * (N + 1)

        # Base case: only first piece
        for length in range(N + 1):
            dp[length] = length * price[0]

        for ind in range(1, n):
            for length in range(ind + 1, N + 1):
                dp[length] = max(dp[length], price[ind] + dp[length - (ind + 1)])

        return dp[N]
