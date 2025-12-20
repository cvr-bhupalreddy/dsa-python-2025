def frogJump(i, heights):
    if i == 0:
        return 0

    left = frogJump(i - 1, heights) + abs(heights[i] - heights[i - 1])
    right = float('inf')
    if i > 1:
        right = frogJump(i - 2, heights) + abs(heights[i] - heights[i - 2])

    return min(left, right)


def frogJump_memoization(i, heights, dp):
    if i == 0:
        return 0
    if dp[i] != -1:
        return dp[i]

    left = frogJump_memoization(i - 1, heights, dp) + abs(heights[i] - heights[i - 1])
    right = float('inf')
    if i > 1:
        right = frogJump_memoization(i - 2, heights, dp) + abs(heights[i] - heights[i - 2])

    dp[i] = min(left, right)
    return dp[i]


def frogJump_helper(heights):
    n = len(heights)
    dp = [-1] * n  # Initialize memo array

    # Helper function: min energy to reach stone i
    def helper(i):
        if i == 0:
            return 0  # Base case: first stone, no cost
        if dp[i] != -1:
            return dp[i]  # Return already computed value

        # Option 1: Jump from previous stone
        jump_one = helper(i - 1) + abs(heights[i] - heights[i - 1])

        # Option 2: Jump from two stones back
        jump_two = float('inf')
        if i > 1:
            jump_two = helper(i - 2) + abs(heights[i] - heights[i - 2])

        # Store minimum energy in dp
        dp[i] = min(jump_one, jump_two)
        return dp[i]

    # Start recursion from the last stone
    return helper(n - 1)


def frogJump_tabulation(heights):
    n = len(heights)
    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        one = dp[i - 1] + abs(heights[i] - heights[i - 1])
        two = dp[i - 2] + abs(heights[i] - heights[i - 2]) if i > 1 else float('inf')
        dp[i] = min(one, two)

    return dp[-1]


def frogJump_spaceOptimized(heights):
    n = len(heights)
    if n == 0:
        return 0
    if n == 1:
        return 0  # Only one stone, no energy required

    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]

    for i in range(1, n):
        # Jump from previous stone
        jump_one = prev1 + abs(heights[i] - heights[i - 1])

        # Jump from two stones back
        jump_two = float('inf')
        if i > 1:
            jump_two = prev2 + abs(heights[i] - heights[i - 2])

        # Minimum energy to reach current stone
        curr = min(jump_one, jump_two)

        # Update prev variables for next iteration
        prev2, prev1 = prev1, curr

    return prev1


# Example
heights = [10, 20, 30, 10]
print(frogJump(heights))  # Output: 20
