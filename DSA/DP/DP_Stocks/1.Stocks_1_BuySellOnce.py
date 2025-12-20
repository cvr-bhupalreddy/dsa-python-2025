def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)  # update min buy price so far
        profit = price - min_price  # profit if selling today
        max_profit = max(max_profit, profit)  # update max profit

    return max_profit


def max_profit_with_indices(prices):
    if not prices:
        return 0, -1, -1  # profit, buy_index, sell_index

    min_price = prices[0]
    min_index = 0
    max_profit = 0
    buy_index = 0
    sell_index = 0

    for i, price in enumerate(prices):
        # Update minimum price so far
        if price < min_price:
            min_price = price
            min_index = i

        # Calculate profit if selling today
        profit = price - min_price

        # Update maximum profit and indices
        if profit > max_profit:
            max_profit = profit
            buy_index = min_index
            sell_index = i

    return max_profit, buy_index, sell_index


def stocks_1(prices):
    if not prices or len(prices) < 2:
        return 0, -1, -1  # profit, buy_index, sell_index

    min_price = prices[0]
    min_index = 1  # starting from index 1
    max_profit = 0
    buy_index = 1
    sell_index = 2  # at least one day after buy

    for i in range(1, len(prices)):
        # Update minimum price so far
        if prices[i-1] < min_price:
            min_price = prices[i-1]
            min_index = i  # use 1-based indexing

        # Calculate profit if selling today
        profit = prices[i] - min_price

        # Update maximum profit and indices
        if profit > max_profit:
            max_profit = profit
            buy_index = min_index
            sell_index = i + 1  # +1 for 1-based day index

    return max_profit, buy_index, sell_index

# Example usage
prices = [7, 1, 5, 3, 6, 4]
profit, buy, sell = max_profit(prices)
print(f"Max Profit: {profit}, Buy on day {buy}, Sell on day {sell}")
# Output: Max Profit: 5, Buy on day 2, Sell on day 5
