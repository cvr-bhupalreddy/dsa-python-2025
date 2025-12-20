from typing import List

class StockDPForwardFull:

    # -----------------------------
    # 1) Best Time I — Single Transaction
    # -----------------------------
    def maxProfitI(self, prices: List[int]) -> int:
        if not prices: return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return max_profit

    # -----------------------------
    # 2) Best Time II — Infinite Transactions
    # -----------------------------
    def maxProfitII_memo(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        def solve(i,buy):
            if i<0: return 0
            if dp[i][buy]!=-1: return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i]+solve(i-1,0), solve(i-1,1))
            else:
                dp[i][buy] = max(prices[i]+solve(i-1,1), solve(i-1,0))
            return dp[i][buy]
        return solve(n-1,1)

    def maxProfitII_tab(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][1] = max(-prices[i]+dp[i-1][0], dp[i-1][1])
            dp[i][0] = max(prices[i]+dp[i-1][1], dp[i-1][0])
        return dp[n-1][0]

    def maxProfitII_space(self, prices: List[int]) -> int:
        prev_buy, prev_sell = -prices[0], 0
        for i in range(1,len(prices)):
            cur_buy = max(-prices[i]+prev_sell, prev_buy)
            cur_sell = max(prices[i]+prev_buy, prev_sell)
            prev_buy, prev_sell = cur_buy, cur_sell
        return prev_sell

    # -----------------------------
    # 3) Best Time III — At Most 2 Transactions
    # -----------------------------
    def maxProfitIII_memo(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)]
        def solve(i,buy,cap):
            if i<0 or cap==0: return 0
            if dp[i][buy][cap]!=-1: return dp[i][buy][cap]
            if buy:
                dp[i][buy][cap] = max(-prices[i]+solve(i-1,0,cap), solve(i-1,1,cap))
            else:
                dp[i][buy][cap] = max(prices[i]+solve(i-1,1,cap-1), solve(i-1,0,cap))
            return dp[i][buy][cap]
        return solve(n-1,1,2)

    def maxProfitIII_tab(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n)]
        dp[0][1][2] = -prices[0]
        for i in range(1,n):
            for cap in range(1,3):
                dp[i][1][cap] = max(-prices[i]+dp[i-1][0][cap], dp[i-1][1][cap])
                dp[i][0][cap] = max(prices[i]+dp[i-1][1][cap-1], dp[i-1][0][cap])
        return dp[n-1][0][2]

    def maxProfitIII_space(self, prices: List[int]) -> int:
        ahead = [[0]*3 for _ in range(2)]
        ahead[1][2] = -prices[0]
        for i in range(1,len(prices)):
            cur = [[0]*3 for _ in range(2)]
            for cap in range(1,3):
                cur[1][cap] = max(-prices[i]+ahead[0][cap], ahead[1][cap])
                cur[0][cap] = max(prices[i]+ahead[1][cap-1], ahead[0][cap])
            ahead = cur
        return ahead[0][2]

    # -----------------------------
    # 4) Best Time IV — At Most K Transactions
    # -----------------------------
    def maxProfitIV_memo(self, prices: List[int], K:int) -> int:
        n = len(prices)
        dp = [[[-1]*(K+1) for _ in range(2)] for _ in range(n)]
        def solve(i,buy,cap):
            if i<0 or cap==0: return 0
            if dp[i][buy][cap]!=-1: return dp[i][buy][cap]
            if buy:
                dp[i][buy][cap] = max(-prices[i]+solve(i-1,0,cap), solve(i-1,1,cap))
            else:
                dp[i][buy][cap] = max(prices[i]+solve(i-1,1,cap-1), solve(i-1,0,cap))
            return dp[i][buy][cap]
        return solve(len(prices)-1,1,K)

    def maxProfitIV_tab(self, prices: List[int], K:int) -> int:
        n = len(prices)
        dp = [[[0]*(K+1) for _ in range(2)] for _ in range(n)]
        dp[0][1][K] = -prices[0]
        for i in range(1,n):
            for cap in range(1,K+1):
                dp[i][1][cap] = max(-prices[i]+dp[i-1][0][cap], dp[i-1][1][cap])
                dp[i][0][cap] = max(prices[i]+dp[i-1][1][cap-1], dp[i-1][0][cap])
        return dp[n-1][0][K]

    def maxProfitIV_space(self, prices: List[int], K:int) -> int:
        ahead = [[0]*(K+1) for _ in range(2)]
        ahead[1][K] = -prices[0]
        for i in range(1,len(prices)):
            cur = [[0]*(K+1) for _ in range(2)]
            for cap in range(1,K+1):
                cur[1][cap] = max(-prices[i]+ahead[0][cap], ahead[1][cap])
                cur[0][cap] = max(prices[i]+ahead[1][cap-1], ahead[0][cap])
            ahead = cur
        return ahead[0][K]

    # -----------------------------
    # 5) Cooldown — Forward Recurrence
    # -----------------------------
    def maxProfitCooldown_memo(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        def solve(i,buy):
            if i<0: return 0
            if dp[i][buy]!=-1: return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i]+solve(i-1,0), solve(i-1,1))
            else:
                dp[i][buy] = max(prices[i]+(solve(i-2,1) if i-2>=0 else 0), solve(i-1,0))
            return dp[i][buy]
        return solve(n-1,0)

    def maxProfitCooldown_tab(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][1] = max(-prices[i]+dp[i-1][0], dp[i-1][1])
            dp[i][0] = max(prices[i]+(dp[i-2][1] if i>=2 else 0), dp[i-1][0])
        return dp[n-1][0]

    def maxProfitCooldown_space(self, prices: List[int]) -> int:
        prev_buy, prev_sell = -prices[0], 0
        prev2_sell = 0
        for i in range(1,len(prices)):
            cur_buy = max(-prices[i]+prev_sell, prev_buy)
            cur_sell = max(prices[i]+prev2_sell, prev_sell)
            prev_buy, prev_sell, prev2_sell = cur_buy, cur_sell, prev_sell
        return prev_sell

    # -----------------------------
    # 6) Transaction Fee — Forward Recurrence
    # -----------------------------
    def maxProfitFee_memo(self, prices: List[int], fee:int) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        def solve(i,buy):
            if i<0: return 0
            if dp[i][buy]!=-1: return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i]+solve(i-1,0), solve(i-1,1))
            else:
                dp[i][buy] = max(prices[i]-fee+solve(i-1,1), solve(i-1,0))
            return dp[i][buy]
        return solve(n-1,0)

    def maxProfitFee_tab(self, prices: List[int], fee:int) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][1] = max(-prices[i]+dp[i-1][0], dp[i-1][1])
            dp[i][0] = max(prices[i]-fee+dp[i-1][1], dp[i-1][0])
        return dp[n-1][0]

    def maxProfitFee_space(self, prices: List[int], fee:int) -> int:
        prev_buy, prev_sell = -prices[0], 0
        for i in range(1,len(prices)):
            cur_buy = max(-prices[i]+prev_sell, prev_buy)
            cur_sell = max(prices[i]-fee+prev_buy, prev_sell)
            prev_buy, prev_sell = cur_buy, cur_sell
        return prev_sell
