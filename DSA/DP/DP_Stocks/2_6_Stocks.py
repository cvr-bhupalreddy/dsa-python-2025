class StockDP:
    # --------------------------------------------------------------------
    #  Problem 2: BUY & SELL STOCK II (Unlimited Transactions)
    # --------------------------------------------------------------------
    def stock2_memo(self, prices):
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def solve(i, buy):
            # base case
            if i == n:
                return 0

            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy:
                take = -prices[i] + solve(i + 1, 0)
                skip = 0 + solve(i + 1, 1)
                dp[i][buy] = max(take, skip)
            else:
                take = prices[i] + solve(i + 1, 1)
                skip = 0 + solve(i + 1, 0)
                dp[i][buy] = max(take, skip)

            return dp[i][buy]

        return solve(0, 1)

    def stock2_tab(self, prices):
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
            dp[i][0] = max(prices[i] + dp[i+1][1], dp[i+1][0])

        return dp[0][1]

    def stock2_space(self, prices):
        n = len(prices)
        ahead_buy = ahead_sell = 0

        for i in range(n-1, -1, -1):
            cur_buy = max(-prices[i] + ahead_sell, ahead_buy)
            cur_sell = max(prices[i] + ahead_buy, ahead_sell)
            ahead_buy, ahead_sell = cur_buy, cur_sell

        return ahead_buy

    # --------------------------------------------------------------------
    #  Problem 3: BUY & SELL STOCK WITH COOLDOWN
    # --------------------------------------------------------------------
    def cooldown_memo(self, prices):
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]

        def solve(i, buy):
            if i >= n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy:
                take = -prices[i] + solve(i+1, 0)
                skip = solve(i+1, 1)
                dp[i][buy] = max(take, skip)
            else:
                take = prices[i] + solve(i+2, 1)
                skip = solve(i+1, 0)
                dp[i][buy] = max(take, skip)

            return dp[i][buy]

        return solve(0, 1)

    def cooldown_tab(self, prices):
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]

        for i in range(n-1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
            dp[i][0] = max(prices[i] + dp[i+2][1], dp[i+1][0])

        return dp[0][1]

    def cooldown_space(self, prices):
        n = len(prices)
        ahead1 = ahead2 = 0
        buy1 = sell1 = 0

        for i in range(n-1, -1, -1):
            cur_buy = max(-prices[i] + sell1, buy1)
            cur_sell = max(prices[i] + ahead2, sell1)
            ahead2 = sell1
            sell1 = cur_sell
            buy1 = cur_buy

        return buy1

    # --------------------------------------------------------------------
    #  Problem 4: BUY & SELL STOCK WITH TRANSACTION FEE
    # --------------------------------------------------------------------
    def fee_memo(self, prices, fee):
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]

        def solve(i, buy):
            if i == n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy:
                dp[i][buy] = max(-prices[i] + solve(i+1, 0),
                                 solve(i+1, 1))
            else:
                dp[i][buy] = max(prices[i] - fee + solve(i+1, 1),
                                 solve(i+1, 0))
            return dp[i][buy]

        return solve(0, 1)

    def fee_tab(self, prices, fee):
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
            dp[i][0] = max(prices[i] - fee + dp[i+1][1], dp[i+1][0])

        return dp[0][1]

    def fee_space(self, prices, fee):
        ahead_buy = ahead_sell = 0
        for i in range(len(prices)-1, -1, -1):
            cur_buy = max(-prices[i] + ahead_sell, ahead_buy)
            cur_sell = max(prices[i] - fee + ahead_buy, ahead_sell)
            ahead_buy, ahead_sell = cur_buy, cur_sell
        return ahead_buy

    # --------------------------------------------------------------------
    #  Problem 5: BUY & SELL STOCK III (at most 2 transactions)
    # --------------------------------------------------------------------
    def stock3_memo(self, prices):
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)]

        def solve(i, buy, cap):
            if i == n or cap == 0:
                return 0
            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]

            if buy:
                dp[i][buy][cap] = max(-prices[i] + solve(i+1, 0, cap),
                                      solve(i+1, 1, cap))
            else:
                dp[i][buy][cap] = max(prices[i] + solve(i+1, 1, cap-1),
                                      solve(i+1, 0, cap))
            return dp[i][buy][cap]

        return solve(0, 1, 2)

    def stock3_tab(self, prices):
        n = len(prices)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        dp[i][buy][cap] = max(-prices[i] + dp[i+1][0][cap],
                                              dp[i+1][1][cap])
                    else:
                        dp[i][buy][cap] = max(prices[i] + dp[i+1][1][cap-1],
                                              dp[i+1][0][cap])
        return dp[0][1][2]

    def stock3_space(self, prices):
        ahead = [[0]*3 for _ in range(2)]
        cur = [[0]*3 for _ in range(2)]

        for i in range(len(prices)-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy:
                        cur[buy][cap] = max(-prices[i] + ahead[0][cap],
                                            ahead[1][cap])
                    else:
                        cur[buy][cap] = max(prices[i] + ahead[1][cap-1],
                                            ahead[0][cap])
            ahead = [cur[0][:], cur[1][:]]

        return ahead[1][2]

    # --------------------------------------------------------------------
    #  Problem 6: BUY & SELL STOCK IV (at most k transactions)
    # --------------------------------------------------------------------
    def stock4_memo(self, prices, K):
        n = len(prices)
        dp = [[[-1]*(K+1) for _ in range(2)] for _ in range(n)]

        def solve(i, buy, cap):
            if i == n or cap == 0:
                return 0
            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]

            if buy:
                dp[i][buy][cap] = max(-prices[i] + solve(i+1, 0, cap),
                                      solve(i+1, 1, cap))
            else:
                dp[i][buy][cap] = max(prices[i] + solve(i+1, 1, cap-1),
                                      solve(i+1, 0, cap))
            return dp[i][buy][cap]

        return solve(0, 1, K)

    def stock4_tab(self, prices, K):
        n = len(prices)
        dp = [[[0]*(K+1) for _ in range(2)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, K+1):
                    if buy:
                        dp[i][buy][cap] = max(-prices[i] + dp[i+1][0][cap],
                                              dp[i+1][1][cap])
                    else:
                        dp[i][buy][cap] = max(prices[i] + dp[i+1][1][cap-1],
                                              dp[i+1][0][cap])
        return dp[0][1][K]

    def stock4_space(self, prices, K):
        ahead = [[0]*(K+1) for _ in range(2)]
        cur = [[0]*(K+1) for _ in range(2)]

        for i in range(len(prices)-1, -1, -1):
            for buy in range(2):
                for cap in range(1, K+1):
                    if buy:
                        cur[buy][cap] = max(-prices[i] + ahead[0][cap],
                                            ahead[1][cap])
                    else:
                        cur[buy][cap] = max(prices[i] + ahead[1][cap-1],
                                            ahead[0][cap])
            ahead = [cur[0][:], cur[1][:]]

        return ahead[1][K]
