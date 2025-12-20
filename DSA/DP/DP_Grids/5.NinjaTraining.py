

def ninjaTraining_memo(points):
    n = len(points)
    dp = [[-1] * 4 for _ in range(n)]

    def helper(day, last):
        if day == 0:
            max_points = 0
            for i in range(3):
                if i != last:
                    max_points = max(max_points, points[0][i])
            return max_points

        if dp[day][last] != -1:  # already sub problem is solved
            return dp[day][last]

        max_points = 0
        for i in range(3):
            if i != last:
                curr = points[day][i] + helper(day - 1, i)
                max_points = max(max_points, curr)

        dp[day][last] = max_points
        return dp[day][last]

    # Start from last day with 'no activity done before' (last = 3)
    return helper(n - 1, 3)


def ninjaTraining_memo1(self, points):
    n = len(points)
    dp = [[-1] * 4 for _ in range(n)]

    def solve(day, last):
        # Base case: last day
        if day == n - 1:
            best = 0
            for task in range(3):
                if task != last:
                    best = max(best, points[day][task])
            return best

            # If already computed
        if dp[day][last] != -1:
            return dp[day][last]

            # Recurrence: try all tasks except last
        best = 0
        for task in range(3):
            if task != last:
                val = points[day][task] + solve(day + 1, task)
                best = max(best, val)

        dp[day][last] = best
        return best

        # Start from day 0 with 'no previous task' (3 represents none)

    return solve(0, 3)


def ninjaTraining_tabulation(points):
    n = len(points)
    dp = [[0] * 4 for _ in range(n)]

    # Base case: day 0
    for last in range(4):
        dp[0][last] = max(points[0][i] for i in range(3) if i != last)

    # Fill dp table
    for day in range(1, n):
        for last in range(4):
            dp[day][last] = max(points[day][i] + dp[day - 1][i] for i in range(3) if i != last )
    return dp[n - 1][3]  # Last day, no restriction on previous activity


def ninjaTraining_tabulation_reverse(points):
    n = len(points)
    dp = [[0] * 4 for _ in range(n)]

    # Base case → last day
    for last in range(4):
        dp[n - 1][last] = max(points[n - 1][task] for task in range(3) if task != last)

    # Fill table from second-last day up to day 0
    for day in range(n - 2, -1, -1):
        for last in range(4):
            best = 0
            for task in range(3):
                if task != last:
                    val = points[day][task] + dp[day + 1][task]
                    best = max(best, val)
            dp[day][last] = best

    # Result: starting from day 0, no restriction on last task
    return dp[0][3]


def ninjaTraining_tabulation_reverse1(points):
    n = len(points)
    dp = [[0] * 4 for _ in range(n)]

    # Base case → last day
    for last in range(4):
        dp[n - 1][last] = max(points[n - 1][task] for task in range(3) if task != last)

    # Fill from bottom to top
    for day in range(n - 2, -1, -1):
        for last in range(4):
            dp[day][last] = max(points[day][task] + dp[day + 1][task] for task in range(3) if task != last)

    return dp[0][3]


def ninjaTraining_spaceOptimized(points):
    n = len(points)
    prev = [0] * 4

    # Base case: day 0
    for last in range(4):
        prev[last] = max(points[0][i] for i in range(3) if i != last)

    # Loop over remaining days
    for day in range(1, n):
        temp = [0] * 4
        for last in range(4):
            temp[last] = max(
                points[day][i] + prev[i] for i in range(3) if i != last
            )
        prev = temp

    return prev[3]


# Example
points = [
    [10, 50, 40],
    [5, 100, 11],
    [50, 20, 70]
]


