# ✅ Fractional Knapsack Problem
#  Statement
# Given:
#     n items, each with a weight w[i] and value v[i]
#     A knapsack with capacity W
#     You can take fractions of an item (unlike 0/1 knapsack).
#
# Goal: Maximize total value in knapsack.


# 1. Compute value/weight ratio for each item.
# 2. Sort items in descending order of ratio.
# 3. Take items in order:
#     a. If item fits entirely → take whole
#     b. If item cannot fit fully → take fraction to fill remaining capacity
# 4. Stop when knapsack is full.


def fractionalKnapsack(W, weights, values):
    n = len(weights)

    # Step 1: Compute value/weight ratio
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    # Step 2: Sort by ratio descending
    items.sort(reverse=True)

    total_value = 0.0
    remaining = W

    # Step 3: Take items greedily
    for ratio, w, v in items:
        if remaining >= w:
            total_value += v
            remaining -= w
        else:
            # Take fraction
            total_value += v * (remaining / w)
            break  # Knapsack full

    return total_value
