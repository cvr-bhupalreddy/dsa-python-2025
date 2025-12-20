# ✅ Idea / Approach
#
# Use DP where dp[i][j] = size of largest square ending at (i,j).
#
# If matrix[i][j] == 0, dp[i][j] = 0
#
# Else dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


# 1️⃣ Backward Recurrence (Classic)
# DP definition
#
# dp[i][j] = size of the largest square ending at cell (i,j)
#
# In other words: the square’s bottom-right corner is at (i,j).
#
# Recurrence
# if matrix[i][j] == 0:
#     dp[i][j] = 0
# else:
#     dp[i][j] = 1 + min(
#         dp[i-1][j],     # top
#         dp[i][j-1],     # left
#         dp[i-1][j-1]    # top-left
#     )
# Base Cases
#
# If i == 0 or j == 0 → dp[i][j] = matrix[i][j] (either 0 or 1)
# Iteration
#
# Top-left → bottom-right (i=0..m-1, j=0..n-1)

# 2️⃣ Forward Recurrence
# DP definition
#
# dp[i][j] = size of the largest square starting at cell (i,j)
#
# In other words: the square’s top-left corner is at (i,j).
#
# Recurrence

# if matrix[i][j] == 0:
#     dp[i][j] = 0
# else:
#     dp[i][j] = 1 + min(
#         dp[i+1][j],     # down
#         dp[i][j+1],     # right
#         dp[i+1][j+1]    # down-right
#     )

#
# Base Cases
#
# If i == m-1 or j == n-1 → dp[i][j] = matrix[i][j] (either 0 or 1)
#
# Iteration
#
# Bottom-right → top-left (i=m-1..0, j=n-1..0)


def count_squares(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    total = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0: # for boundaries
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                total += dp[i][j]

    return total


def count_squares_space_optimized(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    total = 0
    prev = 0  # dp[i-1][j-1]

    for i in range(m):
        for j in range(n):
            temp = dp[j]
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1] if j > 0 else 0, prev)
                total += dp[j]
            else:
                dp[j] = 0
            prev = temp
    return total
