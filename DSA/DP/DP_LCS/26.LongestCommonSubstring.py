def longest_common_substring_brute(s1, s2):
    n, m = len(s1), len(s2)
    max_len = 0
    longest_substr = ""

    for i in range(n):
        for j in range(i, n):
            sub = s1[i:j + 1]
            if sub in s2:
                if len(sub) > max_len:
                    max_len = len(sub)
                    longest_substr = sub
    return max_len, longest_substr


def longest_common_substring_memo(s1, s2):
    n, m = len(s1), len(s2)
    memo = [[-1] * m for _ in range(n)]
    max_len = [0]  # Use list to modify inside nested function

    def lcs(i, j):
        if i < 0 or j < 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]

        if s1[i] == s2[j]:
            memo[i][j] = 1 + lcs(i-1, j-1)
            max_len[0] = max(max_len[0], memo[i][j])
        else:
            memo[i][j] = 0

        # Also compute subproblems without ending at (i,j) to ensure all pairs are checked
        lcs(i-1, j)
        lcs(i, j-1)
        return memo[i][j]

    lcs(n-1, m-1)
    return max_len[0]


def longest_common_substring(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_index = 0  # end index in s1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    # Extract substring
    longest_substr = s1[end_index - max_len: end_index]
    return max_len, longest_substr


def longest_common_substring_optimized(s1, s2):
    n, m = len(s1), len(s2)
    prev = [0] * (m+1)
    max_len = 0
    end_index = 0

    for i in range(1, n+1):
        curr = [0] * (m+1)
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
                if curr[j] > max_len:
                    max_len = curr[j]
                    end_index = i
            else:
                curr[j] = 0
        prev = curr

    return s1[end_index-max_len:end_index], max_len


