def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update max profit if selling today is better
        max_profit = max(max_profit, price - min_price)
        # Update minimum price seen so far
        min_price = min(min_price, price)

    return max_profit
