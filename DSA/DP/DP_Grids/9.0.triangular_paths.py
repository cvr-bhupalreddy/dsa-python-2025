class TriangularPaths:
    def __init__(self, n):
        self.n = n

    # ================================
    # Model 1: Top-Down (0,0 → last row)
    # ================================

    # 1️⃣ Memoization
    def topDownMemo(self):
        dp = [[-1 for _ in range(i+1)] for i in range(self.n)]

        def helper(i, j):
            if i == self.n - 1:
                return 1
            if j < 0 or j > i:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = helper(i+1, j) + helper(i+1, j+1)
            return dp[i][j]

        return helper(0, 0)

    # 2️⃣ Tabulation
    def topDownTab(self):
        dp = [[0 for _ in range(i+1)] for i in range(self.n)]
        # last row = 1 path each
        for j in range(self.n):
            dp[self.n - 1][j] = 1
        # fill bottom → top
        for i in range(self.n - 2, -1, -1):
            for j in range(i+1):
                dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
        return dp[0][0]

    # 3️⃣ Space Optimized
    def topDownSpace(self):
        front = [1]*self.n  # last row
        for i in range(self.n-2, -1, -1):
            curr = [0]*(i+1)
            for j in range(i+1):
                curr[j] = front[j] + front[j+1]
            front = curr
        return front[0]

    # ================================
    # Model 2: Bottom-Up (last row → 0,0)
    # ================================

    # 4️⃣ Memoization
    def bottomUpMemo(self):
        dp = [[-1 for _ in range(i+1)] for i in range(self.n)]

        def helper(i, j):
            if i == 0 and j == 0:
                return 1
            if j < 0 or j > i:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = helper(i-1, j) + helper(i-1, j-1)
            return dp[i][j]

        return helper(self.n-1, self.n-1)

    # 5️⃣ Tabulation
    def bottomUpTab(self):
        dp = [[0 for _ in range(i+1)] for i in range(self.n)]
        dp[0][0] = 1  # top base
        for i in range(1, self.n):
            for j in range(i+1):
                val = 0
                if j < i:
                    val += dp[i-1][j]
                if j-1 >= 0:
                    val += dp[i-1][j-1]
                dp[i][j] = val
        return dp[self.n-1][self.n-1]

    # 6️⃣ Space Optimized
    def bottomUpSpace(self):
        prev = [1]  # top row
        for i in range(1, self.n):
            curr = [0]*(i+1)
            for j in range(i+1):
                if j < i:
                    curr[j] += prev[j]
                if j-1 >= 0:
                    curr[j] += prev[j-1]
            prev = curr
        return prev[-1]

# ================================
# Example usage
# ================================
n = 4
solver = TriangularPaths(n)

print("Top-Down Memo:", solver.topDownMemo())
print("Top-Down Tab:", solver.topDownTab())
print("Top-Down Space:", solver.topDownSpace())
print("Bottom-Up Memo:", solver.bottomUpMemo())
print("Bottom-Up Tab:", solver.bottomUpTab())
print("Bottom-Up Space:", solver.bottomUpSpace())
