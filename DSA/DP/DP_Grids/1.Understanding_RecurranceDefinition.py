def ninjaTraining_byTask(points):
    n = len(points)
    dp = [[0] * 3 for _ in range(n)]

    # Base case: first day
    for task in range(3):
        dp[0][task] = points[0][task]

    # Fill DP table
    for day in range(1, n):
        for task in range(3):
            dp[day][task] = points[day][task] + max(
                dp[day-1][prev] for prev in range(3) if prev != task
            )

    return max(dp[n-1])



def ninjaTraining_byLast(points):
    """
    Calculate maximum points for Ninja Training using DP by previous task.

    points: List[List[int]] -- points[i][j] = points for task j on day i
    """
    n = len(points)
    dp = [[0] * 4 for _ in range(n)]  # dp[day][last_task], last_task=0,1,2 or 3 (no restriction)

    # Base case: day 0
    for last in range(4):
        if last == 3:
            dp[0][last] = max(points[0])  # no restriction
        else:
            dp[0][last] = max(points[0][i] for i in range(3) if i != last)

    # Fill DP table
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = max(
                points[day][task] + dp[day-1][task]
                for task in range(3) if task != last
            )

    return dp[n-1][3]  # last day, no restriction on previous task


# Example usage:
points = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]

print(ninjaTraining_byLast(points))  # Output: 210
