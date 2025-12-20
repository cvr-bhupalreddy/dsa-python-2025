#  Memoization (Top-Down from 0,0 → n-1,n-1)
# here No fixed point ,so we called helper from all elements in last row , which is not better

def minimumTotal_memoization(triangle):
    n = len(triangle)
    # DP matches triangle structure
    dp = [[-1 for _ in range(len(triangle[i]))] for i in range(n)]

    def helper(i, j):
        # Base: starting point
        if i == 0 and j == 0:
            return triangle[0][0]
        # Out of bounds
        if j < 0 or j > i:  # why we are doing need to fill the table and see where it's going out of boundary
            return float('inf')

        # Memoized
        if dp[i][j] != -1:
            return dp[i][j]

        # Recursive calls
        up = helper(i - 1, j)  # from directly above
        diag = helper(i - 1, j - 1)  # from top-left diagonal

        dp[i][j] = triangle[i][j] + min(up, diag)
        return dp[i][j]

    # Get minimum in the last row
    return min(helper(n - 1, j) for j in range(n))


# this is called from first row to last row so only one call is made
def minimumTotal_memo_1(triangle):
    n = len(triangle)
    dp = [[-1 for _ in range(len(triangle[i]))] for i in range(n)]  # memo table

    def helper(i, j):
        # Base case: last row
        if i == n - 1:
            return triangle[i][j]

        # If already computed
        if dp[i][j] != -1:
            return dp[i][j]

        # Recurse for down and diagonal paths
        down = triangle[i][j] + helper(i + 1, j)
        diag = triangle[i][j] + helper(i + 1, j + 1)

        # Store and return
        dp[i][j] = min(down, diag)
        return dp[i][j]

    return helper(0, 0)


def minimumTotal_tabulation(self, triangle):
    n = len(triangle)

    # Step 1: Initialize DP with same structure as triangle
    dp = [[0 for _ in range(len(triangle[i]))] for i in range(n)]

    # Step 2: Base case — last row is same as triangle last row
    dp[-1] = triangle[-1][:]

    # Step 3: Build from bottom to top
    for i in range(n - 2, -1, -1):  # from 2nd last row upwards
        for j in range(len(triangle[i])):  # each element in that row
            down = dp[i + 1][j]
            diag = dp[i + 1][j + 1]
            dp[i][j] = triangle[i][j] + min(down, diag)

    # Step 4: Result at top cell
    return dp[0][0]


def minimumTotal_space_optimization(self, triangle):
    n = len(triangle)
    front = triangle[-1][:]  # start with last row

    for i in range(n - 2, -1, -1):  # from 2nd last row upward
        curr = [0] * (i + 1)
        for j in range(i + 1):
            down = front[j]
            diag = front[j + 1]
            curr[j] = triangle[i][j] + min(down, diag)
        front = curr  # move current row up

    return front[0]
