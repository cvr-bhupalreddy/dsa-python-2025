# ✅ Stock Span Problem — Definition
#
# Given an array of daily stock prices, the stock span for each day is the number of consecutive days (including today)
# the price has been less than or equal to today’s price.
#
# In short:
# For each day i, span[i] = number of previous consecutive days with price ≤ price[i].

def stock_span_bruteforce(prices):
    n = len(prices)
    span = [0] * n

    for i in range(n):
        span[i] = 1
        j = i - 1
        while j >= 0 and prices[j] <= prices[i]:
            span[i] += 1
            j -= 1

    return span


# 2. Better Approach — Use Previous Greater Element
def previous_greater_element(prices):
    """
    Computes Previous Greater Element (PGE) for each index.
    PGE[i] = index of previous element with price > prices[i].
    If none exists, return -1.
    """
    n = len(prices)
    pge = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        pge[i] = stack[-1] if stack else -1
        stack.append(i)

    return pge


def stock_span_using_pge(prices):
    """
    Computes the stock span using the Previous Greater Element (PGE).
    span[i] = i - PGE[i]
    If PGE[i] = -1, span[i] = i + 1
    """
    pge = previous_greater_element(prices)
    n = len(prices)
    span = [0] * n

    for i in range(n):
        if pge[i] == -1:
            span[i] = i + 1
        else:
            span[i] = i - pge[i]

    return span


def stock_spanner(prices):
    n = len(prices)
    span = [0] * n
    stack = []

    for i in range(n):
        # Pop prices smaller than or equal to current
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return span
