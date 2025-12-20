# ✅ Candy Distribution Problem
#  Statement
#
#     You are given an array ratings of length n representing the ratings of n children standing in a line.
#     Distribute candies to children according to these rules:
#     Each child must have at least one candy.
#     Children with a higher rating than their neighbor must get more candies than that neighbor.
#
# Goal:
# Minimize the total number of candies distributed.


# 💡 Core Idea (Greedy / Two Pass)
#
# Initialize candies array with 1 for all children.
#
# Left-to-right pass:
#     If ratings[i] > ratings[i-1] → candies[i] = candies[i-1] + 1
#
# Right-to-left pass:
#     If ratings[i] > ratings[i+1] → candies[i] = max(candies[i], candies[i+1] + 1)
#
# Sum up candies array → minimum total candies.
#
# Why two passes?
#     Left-to-right ensures each child has more than left neighbor
#     Right-to-left ensures each child has more than right neighbor
#
# Using max prevents overwriting previous valid values.


def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    # Step 1: Initialize candies
    candies = [1] * n

    # Step 2: Left to Right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Step 3: Right to Left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Step 4: Sum up total candies
    return sum(candies)

# ✅ Candy Distribution using Slope Concept
# Core Idea
#
# Think of the ratings as a sequence of slopes:
#     Increasing slope (up) → ratings[i] > ratings[i-1]
#     Decreasing slope (down) → ratings[i] < ratings[i-1]
#
#     Flat slope → ratings[i] == ratings[i-1]
#
# Count lengths of uphill and downhill slopes:
#     For an increasing slope of length up, candies = 1 + 2 + ... + up = up*(up+1)/2
#     For a decreasing slope of length down, candies = 1 + 2 + ... + down = down*(down+1)/2
#
# At the peak (transition from up → down), we must give max(up, down) candies to the peak.
#     Flat slopes → give 1 candy.
#
# Sum all candies using slope lengths.


def candy(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    total = 1      # first child gets at least 1
    up = 0         # length of current increasing slope
    down = 0       # length of current decreasing slope
    peak = 0       # length of last peak

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            up += 1
            peak = up
            down = 0
            total += 1 + up  # candies on increasing slope
        elif ratings[i] < ratings[i-1]:
            down += 1
            up = 0
            # Add candies for decreasing slope
            total += 1 + down
            if down >= peak:  # adjust peak if needed
                total += 1
        else:  # flat slope
            up = down = peak = 0
            total += 1

    return total


def candy_slope(ratings):
    n = len(ratings)
    if n == 0:
        return 0

    total = 0
    i = 0

    while i < n:
        up = 0
        down = 0

        # Count increasing slope
        while i + 1 < n and ratings[i + 1] > ratings[i]:
            up += 1
            i += 1

        # Count decreasing slope
        while i + 1 < n and ratings[i + 1] < ratings[i]:
            down += 1
            i += 1

        # Count flat slope
        while i + 1 < n and ratings[i + 1] == ratings[i]:
            i += 1

        # Add candies for slopes
        # Sum of up slope: 1 + 2 + ... + up = up*(up+1)//2
        # Sum of down slope: 1 + 2 + ... + down = down*(down+1)//2
        # Peak gets max(up, down)
        total += (up * (up + 1)) // 2
        total += (down * (down + 1)) // 2
        total += max(up, down) + 1  # peak or flat

        i += 1  # move to next element after current slope

    return total
