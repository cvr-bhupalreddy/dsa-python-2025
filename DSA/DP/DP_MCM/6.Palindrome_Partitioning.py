# n = len(s)
# pal = [[False]*n for _ in range(n)]
#
# for i in range(n-1, -1, -1):   # start index from end
#     for j in range(i, n):      # end index >= start
#         if s[i] == s[j] and (j - i <= 1 or pal[i+1][j-1]):
#             pal[i][j] = True

# n = len(s)
# pal = [[False]*n for _ in range(n)]
#
# for i in range(n):
#     pal[i][i] = True  # single char is palindrome
#
# for i in range(n-1):
#     pal[i][i+1] = (s[i] == s[i+1])  # length 2
#
# # For substrings of length >= 3
# for i in range(n-1, -1, -1):        # start from end to use i+1
#     for j in range(i+2, n):         # end index >= i+2
#         pal[i][j] = (s[i] == s[j] and pal[i+1][j-1])


# Diagonal Palindrome
# n = len(s)
# pal = [[False]*n for _ in range(n)]
#
# # All single characters
# for i in range(n):
#     pal[i][i] = True
#
# # Length 2 substrings
# for i in range(n-1):
#     pal[i][i+1] = (s[i] == s[i+1])
#
# # Length >=3
# for length in range(3, n+1):      # substring length
#     for i in range(n - length + 1):  # start index
#         j = i + length - 1           # end index
#         pal[i][j] = (s[i] == s[j] and pal[i+1][j-1])


class PalindromePartitioningAll:

    # ================================
    # Helper: check palindrome on the fly
    # ================================
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    # ================================
    # 1) MEMOIZATION – with precomputed palindrome table
    # ================================
    def minCutMemoPre(self, s: str) -> int:
        n = len(s)
        # Precompute palindrome table
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for i in range(n - 1):
            pal[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pal[i][j] = (s[i] == s[j] and pal[i + 1][j - 1])

        dp = [-1] * n

        def solve(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            if pal[i][n - 1]:
                dp[i] = 0
                return 0
            min_cuts = float('inf')
            for k in range(i, n):
                if pal[i][k]:
                    cuts = 1 + solve(k + 1)
                    min_cuts = min(min_cuts, cuts)
            dp[i] = min_cuts
            return dp[i]

        return solve(0)

    # ================================
    # 2) MEMOIZATION – without precomputed palindrome table
    # ================================
    def minCutMemoNoPre(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n

        def solve(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            if self.isPalindrome(s, i, n - 1):
                dp[i] = 0
                return 0
            min_cuts = float('inf')
            for k in range(i, n):
                if self.isPalindrome(s, i, k):
                    cuts = 1 + solve(k + 1)
                    min_cuts = min(min_cuts, cuts)
            dp[i] = min_cuts
            return dp[i]

        return solve(0)

    # ================================
    # 3) TABULATION 1-D SIMPLE LOOPS – with precompute
    # ================================
    def minCutTab1DPre(self, s: str) -> int:
        n = len(s)
        # Precompute palindrome
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for i in range(n - 1):
            pal[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pal[i][j] = (s[i] == s[j] and pal[i + 1][j - 1])
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            if pal[i][n - 1]:
                dp[i] = 0
            else:
                min_cuts = float('inf')
                for k in range(i, n):
                    if pal[i][k]:
                        cuts = 1 + (dp[k + 1] if k + 1 < n else 0)
                        min_cuts = min(min_cuts, cuts)
                dp[i] = min_cuts
        return dp[0]

    # ================================
    # 4) TABULATION 1-D SIMPLE LOOPS – without precompute
    # ================================
    def minCutTab1DNoPre(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            if self.isPalindrome(s, i, n - 1):
                dp[i] = 0
            else:
                min_cuts = float('inf')
                for k in range(i, n):
                    if self.isPalindrome(s, i, k):
                        cuts = 1 + (dp[k + 1] if k + 1 < n else 0)
                        min_cuts = min(min_cuts, cuts)
                dp[i] = min_cuts
        return dp[0]

    # ================================
    # 5) TABULATION 2-D DIAGONAL – with precompute
    # ================================
    def minCutTab2DPre(self, s: str) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for i in range(n - 1):
            pal[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                pal[i][j] = (s[i] == s[j] and pal[i + 1][j - 1])
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if pal[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        if pal[i][k]:
                            dp[i][j] = min(dp[i][j], 1 + dp[k + 1][j])
        return dp[0][n - 1]

    # ================================
    # 6) TABULATION 2-D DIAGONAL – without precompute
    # ================================
    def minCutTab2DNoPre(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if self.isPalindrome(s, i, j):
                    dp[i][j] = 0
                else:
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        if self.isPalindrome(s, i, k):
                            dp[i][j] = min(dp[i][j], 1 + dp[k + 1][j])
        return dp[0][n - 1]


# Forward recurrence
# let f(i) = minimum cuts needed for substring s[i : n-1]
#
#
# f(i) = 0                                          if s[i : n-1] is palindrome
# f(i) = min over all j >= i:
# 1 + f(j+1)        if s[i:j] is palindrome


class PalindromePartition:
    def __init__(self, s):
        self.s = s
        self.n = len(s)

        # Precompute palindrome table using forward 2-loops
        self.pal = [[False] * self.n for _ in range(self.n)]
        self._build_pal_table()

    # -----------------------------
    # Build palindrome table (forward loops)
    # pal[i][j] = True if s[i:j] is palindrome
    # -----------------------------
    def _build_pal_table(self):
        s = self.s
        n = self.n

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or self.pal[i + 1][j - 1]):
                    self.pal[i][j] = True

    # -----------------------------------------------------
    # FORWARD RECURRENCE
    #
    # f(i) = 0 if s[i:n] is a palindrome
    # f(i) = min( 1 + f(j+1) )  for all j>=i where s[i:j] is palindrome
    # -----------------------------------------------------

    # =========================
    # 1. Memoization (Top-Down)
    # =========================
    def min_cuts_memo(self):
        dp = [-1] * self.n

        def solve(i):
            if i == self.n:
                return -1  # No cuts needed beyond string end

            if dp[i] != -1:
                return dp[i]

            # If entire substring is palindrome → no cuts
            if self.pal[i][self.n - 1]:
                dp[i] = 0
                return 0

            best = float('inf')
            for j in range(i, self.n):
                if self.pal[i][j]:
                    best = min(best, 1 + solve(j + 1))

            dp[i] = best
            return best

        return solve(0)

    # =========================
    # 2. Tabulation (Bottom-Up)
    # =========================
    def min_cuts_tabu(self):
        dp = [0] * (self.n + 1)
        dp[self.n] = -1  # same base meaning as memoization

        for i in range(self.n - 1, -1, -1):
            if self.pal[i][self.n - 1]:
                dp[i] = 0
                continue

            best = float('inf')
            for j in range(i, self.n):
                if self.pal[i][j]:
                    best = min(best, 1 + dp[j + 1])
            dp[i] = best

        return dp[0]

    # =========================
    # 3. Space Optimized (Same DP Array)
    # =========================
    def min_cuts_space_opt(self):
        dp = [0] * (self.n + 1)
        dp[self.n] = -1

        # bottom-up same as tabulation; nothing more can be optimized
        for i in range(self.n - 1, -1, -1):
            if self.pal[i][self.n - 1]:
                dp[i] = 0
                continue

            best = float('inf')
            for j in range(i, self.n):
                if self.pal[i][j]:
                    best = min(best, 1 + dp[j + 1])

            dp[i] = best

        return dp[0]
