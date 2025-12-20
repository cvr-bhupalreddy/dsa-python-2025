# Count of occurrences of s2 as a subsequence in s1. This is a classic DP problem

# dp[i][j] = number of times s2[0..j-1] occurs in s1[0..i-1]

# Recurrence:
# if s1[i-1] == s2[j-1]:
#     dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
# else:
#     dp[i][j] = dp[i-1][j]

# Base Case:
#     dp[i][0] = 1 → Empty string is a subsequence of any prefix of s1.
#     dp[0][j] = 0 for j>0 → Non-empty s2 cannot appear in empty s1.


# Recurrence from (0,0)
# Let dp[i][j] = number of times s2[j:] occurs in s1[i:]

# if j == m:  # s2 is exhausted
#     return 1
# if i == n:  # s1 is exhausted but s2 not
#     return 0
#
# if s1[i] == s2[j]:
#     # take s1[i] for matching s2[j] or skip s1[i]
#     dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
# else:
#     # skip s1[i]
#     dp[i][j] = dp[i+1][j]


class SubsequenceCounter:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        self.n = len(s1)
        self.m = len(s2)

    # -------------------------
    # Forward recursion + memoization using array
    # -------------------------
    def forward_memo_array(self):
        memo = [[-1] * (self.m + 1) for _ in range(self.n + 1)]

        def dfs(i, j):
            if j == self.m:  # matched all of s2
                return 1
            if i == self.n:  # s1 exhausted
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if self.s1[i] == self.s2[j]:
                memo[i][j] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[i][j] = dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)

    # -------------------------
    # Backward recursion + memoization using array
    # -------------------------
    def backward_memo_array(self):
        memo = [[-1] * (self.m) for _ in range(self.n)]  # indices 0..n-1, 0..m-1

        def dfs(i, j):
            if j < 0:  # matched all of s2
                return 1
            if i < 0:  # s1 exhausted
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if self.s1[i] == self.s2[j]:
                memo[i][j] = dfs(i - 1, j - 1) + dfs(i - 1, j)
            else:
                memo[i][j] = dfs(i - 1, j)
            return memo[i][j]

        return dfs(self.n - 1, self.m - 1)

    # -------------------------
    # Forward tabulation
    # -------------------------
    def forward_tab(self):
        dp = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(self.n + 1):
            dp[i][self.m] = 1  # empty s2
        for i in range(self.n - 1, -1, -1):
            for j in range(self.m - 1, -1, -1):
                if self.s1[i] == self.s2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]

    # -------------------------
    # Backward tabulation
    # -------------------------
    def backward_tab(self):
        dp = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(self.n + 1):
            dp[i][0] = 1  # empty s2
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[self.n][self.m]

    # -------------------------
    # Forward space optimized
    # -------------------------
    def forward_space(self):
        dp = [0] * (self.m + 1)
        dp[self.m] = 1  # empty s2
        for i in range(self.n - 1, -1, -1):
            prev = dp[:]
            for j in range(self.m - 1, -1, -1):
                if self.s1[i] == self.s2[j]:
                    dp[j] = prev[j + 1] + prev[j]
                else:
                    dp[j] = prev[j]
        return dp[0]

    # -------------------------
    # Backward space optimized
    # -------------------------
    def backward_space(self):
        dp = [0] * (self.m + 1)
        dp[0] = 1  # empty s2
        for i in range(1, self.n + 1):
            prev = dp[:]
            for j in range(1, self.m + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[j] = prev[j - 1] + prev[j]
                else:
                    dp[j] = prev[j]
        return dp[self.m]


# -------------------------
# Example Usage
# -------------------------
s1 = "babgbag"
s2 = "bag"

counter = SubsequenceCounter(s1, s2)

print("Forward Memo (array):", counter.forward_memo_array())
print("Backward Memo (array):", counter.backward_memo_array())
print("Forward Tabulation:", counter.forward_tab())
print("Backward Tabulation:", counter.backward_tab())
print("Forward Space Optimized:", counter.forward_space())
print("Backward Space Optimized:", counter.backward_space())
