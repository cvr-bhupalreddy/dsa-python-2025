# Longest Common Palindromic Substring (LCPS) not naturally suited for memoization, because substring problems depend
# on contiguous matching and memoization stores results for arbitrary broken subproblems.


class LongestCommonPalindromicSubstring:

    def lcps(self, s1, s2):
        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        best_len = 0
        best_pal = ""

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s1[i - 1] == s2[j - 1]:

                    # common substring extends
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    length = dp[i][j]

                    # substring boundaries in s1
                    start = i - length
                    candidate = s1[start:i]

                    if candidate == candidate[::-1]:  # palindrome check
                        if length > best_len:
                            best_len = length
                            best_pal = candidate

                else:
                    dp[i][j] = 0

        return best_pal
