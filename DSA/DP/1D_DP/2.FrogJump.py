def frogJumpK_td(heights, k):
    n = len(heights)
    dp = [-1] * n

    def solve(i):
        if i == 0:
            return 0
        if dp[i] != -1:
            return dp[i]

        min_energy = float('inf')
        for j in range(1, k + 1):
            if i - j >= 0:
                energy = solve(i - j) + abs(heights[i] - heights[i - j])
                min_energy = min(min_energy, energy)

        dp[i] = min_energy
        return dp[i]

    return solve(n - 1)


def frogJumpK_tabulation(heights, k):
    n = len(heights)
    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        min_energy = float('inf')
        for j in range(1, k + 1):
            if i - j >= 0:
                energy = dp[i - j] + abs(heights[i] - heights[i - j])
                min_energy = min(min_energy, energy)
        dp[i] = min_energy

    return dp[-1]


# Example
heights = [10, 30, 40, 50, 20]



