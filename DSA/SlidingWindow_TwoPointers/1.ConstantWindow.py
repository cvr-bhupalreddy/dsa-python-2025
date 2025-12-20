def maxScore(cardScore, k):
    n = len(cardScore)
    total = sum(cardScore[:k])
    maxSum = total

    # Slide the window: remove from front, add from back
    for i in range(k - 1, -1, -1):
        total -= cardScore[i]
        total += cardScore[n - (k - i)]
        maxSum = max(maxSum, total)

    return maxSum


def maxScore1(cardScore, k):
    total = 0
    n = len(cardScore)

    for index in range(k):
        total += cardScore[index]
    maxSum = total

    # Slide the window: remove from front, add from back
    for i in range(k - 1, -1, -1):
        total -= cardScore[i]
        total += cardScore[n - (k - i)]
        maxSum = max(maxSum, total)
    return maxSum
