class NumberOfLCS:

    # ---------------------------------------------------
    # 1. MEMOIZATION (Backward: start at n-1, m-1)
    # ---------------------------------------------------
    def lcs_count_memo_backward(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[-1] * m for _ in range(n)]
        cnt = [[-1] * m for _ in range(n)]

        def lcs(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s1[i] == s2[j]:
                dp[i][j] = 1 + lcs(i - 1, j - 1)
            else:
                dp[i][j] = max(lcs(i - 1, j), lcs(i, j - 1))
            return dp[i][j]

        def count(i, j):
            if i < 0 or j < 0:
                return 1
            if cnt[i][j] != -1:
                return cnt[i][j]

            if s1[i] == s2[j]:
                cnt[i][j] = count(i - 1, j - 1)
            else:
                total = 0
                if lcs(i - 1, j) == lcs(i, j):
                    total += count(i - 1, j)
                if lcs(i, j - 1) == lcs(i, j):
                    total += count(i, j - 1)
                if lcs(i - 1, j) == lcs(i, j - 1):
                    total //= 2  # remove duplicates
                cnt[i][j] = total
            return cnt[i][j]

        length = lcs(n - 1, m - 1)
        ways = count(n - 1, m - 1)
        return length, ways

    # ---------------------------------------------------
    # 2. MEMOIZATION (Forward: start at 0,0)
    # ---------------------------------------------------
    def lcs_count_memo_forward(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[-1] * m for _ in range(n)]
        cnt = [[-1] * m for _ in range(n)]

        def lcs(i, j):
            if i == n or j == m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s1[i] == s2[j]:
                dp[i][j] = 1 + lcs(i + 1, j + 1)
            else:
                dp[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))
            return dp[i][j]

        def count(i, j):
            if i == n or j == m:
                return 1
            if cnt[i][j] != -1:
                return cnt[i][j]

            if s1[i] == s2[j]:
                cnt[i][j] = count(i + 1, j + 1)
            else:
                total = 0
                if lcs(i + 1, j) == lcs(i, j):
                    total += count(i + 1, j)
                if lcs(i, j + 1) == lcs(i, j):
                    total += count(i, j + 1)
                if lcs(i + 1, j) == lcs(i, j + 1):
                    total //= 2  # remove duplicates
                cnt[i][j] = total
            return cnt[i][j]

        length = lcs(0, 0)
        ways = count(0, 0)
        return length, ways

    # ---------------------------------------------------
    # 3. TABULATION (Length + Count)
    # ---------------------------------------------------
    def lcs_count_tabulation(self, s1, s2):
        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        cnt = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    cnt[i][j] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    cnt[i][j] = cnt[i - 1][j - 1]
                else:
                    if dp[i - 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                        cnt[i][j] = cnt[i - 1][j]
                    elif dp[i][j - 1] > dp[i - 1][j]:
                        dp[i][j] = dp[i][j - 1]
                        cnt[i][j] = cnt[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]
                        cnt[i][j] = cnt[i - 1][j] + cnt[i][j - 1]

                        if dp[i - 1][j - 1] == dp[i][j]:
                            cnt[i][j] -= cnt[i - 1][j - 1]

        return dp[n][m], cnt[n][m]

    # ---------------------------------------------------
    # Extract ALL LCS Strings
    # ---------------------------------------------------
    def all_lcs(self, s1, s2):
        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        def collect(i, j):
            if i == 0 or j == 0:
                return {""}
            if s1[i - 1] == s2[j - 1]:
                return {x + s1[i - 1] for x in collect(i - 1, j - 1)}

            res = set()
            if dp[i - 1][j] == dp[i][j]:
                res |= collect(i - 1, j)
            if dp[i][j - 1] == dp[i][j]:
                res |= collect(i, j - 1)
            return res

        return collect(n, m)


def all_lcs_iterative(s1, s2, dp):
    n, m = len(s1), len(s2)
    stack = [(n, m, "")]
    result = set()

    while stack:
        i, j, curr = stack.pop()
        if i == 0 or j == 0:
            result.add(curr[::-1])  # reverse because we built from end
        elif s1[i - 1] == s2[j - 1]:
            stack.append((i - 1, j - 1, curr + s1[i - 1]))
        else:
            if dp[i - 1][j] == dp[i][j]:
                stack.append((i - 1, j, curr))
            if dp[i][j - 1] == dp[i][j]:
                stack.append((i, j - 1, curr))
    return result
