# Wildcard Matching Problem — Explanation
#
# You are given:
#     s → input string (length = n)
#     p → pattern (length = m)
#
# The pattern can contain two special characters:
#     ? → matches exactly one character
#     * → matches zero or more characters
#
# You must determine:
#     Does pattern p match the entire string s?
#
# Recurrence :
#     match(i, j) = does s[0..i] match p[0..j] ?
#     i ranges from n-1 … -1
#     j ranges from m-1 … -1
#
# Base Cases :
#     Both finished
#         i < 0 and j < 0 → True (both matched)
#
# If pattern finished but string not:
#     i >= 0 and j < 0 → False
#
# If string finished but pattern not:
# The pattern can still match only if the remaining chars are all *
#     i < 0 and j >= 0:
#         return p[0..j] all are '*'
#
#
# Case 1: exact character match OR '?'
# s[i] == p[j]   OR   p[j] == '?'
#     match(i,j) = match(i-1,j-1)
#
# Case 2: p[j] == '*':
#     match(i,j) = match(i,j-1) [* acts like empty ]
#     match(i,j) = match(i-1,j) [* acts like one or more characters match ]
#
# case 2: characters doesn't match
#     match(i,j) = false

#
# if at least one character + also included then
#
# | Pattern Char       | Transition                                              |
# | ------------------ | ------------------------------------------------------- |
# | Exact match or `?` | `match(i-1, j-1)`                                       |
# | `*`                | `match(i, j-1) OR match(i-1, j)`                        |
# | `+`                | `match(i-1, j) OR match(i, j-1)` (must consume ≥1 char) |
# | Mismatch           | `False`                                                 |


class WildcardMatching:

    # ---------------------------------------------------------
    # 1) MEMOIZATION (Top–Down)
    # ---------------------------------------------------------
    def isMatchMemo(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[-1] * m for _ in range(n)]

        # helper inside the function (nested function)
        def solve(i, j):
            # both finished
            if i < 0 and j < 0:
                return 1

            # pattern finished, string not
            if j < 0:
                return 0

            # string finished -> pattern must be all '*'
            if i < 0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return 0
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            # match or '?'
            if p[j] == s[i] or p[j] == '?':
                dp[i][j] = solve(i - 1, j - 1)
                return dp[i][j]

            # '*'
            if p[j] == '*':
                zero = solve(i, j - 1)     # '*' matches empty
                one  = solve(i - 1, j)     # '*' matches one+
                dp[i][j] = 1 if (zero == 1 or one == 1) else 0
                return dp[i][j]

            dp[i][j] = 0
            return 0

        return solve(n - 1, m - 1) == 1

    # ---------------------------------------------------------
    # 2) TABULATION (Bottom–Up)
    # ---------------------------------------------------------
    def isMatchTab(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True

        # empty string, pattern prefix
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                else:
                    dp[i][j] = False

        return dp[n][m]

    # ---------------------------------------------------------
    # 3) SPACE OPTIMIZED (O(m))
    # ---------------------------------------------------------
    def isMatchSpaceOpt(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        prev = [False] * (m + 1)
        cur  = [False] * (m + 1)

        prev[0] = True

        # empty string match with pattern prefix (only '*')
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]

        for i in range(1, n + 1):
            cur[0] = False

            for j in range(1, m + 1):

                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    cur[j] = prev[j - 1]

                elif p[j - 1] == '*':
                    cur[j] = cur[j - 1] or prev[j]

                else:
                    cur[j] = False

            prev, cur = cur, [False] * (m + 1)

        return prev[m]


# ---------------------------------------------------------
# TESTING
# ---------------------------------------------------------
if __name__ == "__main__":
    w = WildcardMatching()
    s = "abdef"
    p = "a*?f"

    print("Memo:", w.isMatchMemo(s, p))
    print("Tab:", w.isMatchTab(s, p))
    print("Space Opt:", w.isMatchSpaceOpt(s, p))
