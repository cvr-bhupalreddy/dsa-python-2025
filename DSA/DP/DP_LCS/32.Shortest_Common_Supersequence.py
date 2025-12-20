# Algorithm (reconstruction idea)
#
#     Build the LCS DP table for s1 and s2.
#
#     Reconstruct the LCS string from the table (or directly use the table while merging).
#
#     Use the LCS string to merge s1 and s2:
#
#         Walk through s1 and s2 with pointers i, j and iterate over characters of lcs.
#
#         For each character c in lcs:
#
#             append all characters from s1[i:] until you reach c,
#
#             append all characters from s2[j:] until you reach c,
#
#             append c and advance both i and j past that c.
#
#       After the loop append remaining tails of s1 and s2.
#
#     The merged string is a shortest common super sequence. Its length equals len(s1)+len(s2)-len(lcs).


class ShortestCommonSupersequence:
    def _lcs_table(self, a: str, b: str):
        n, m = len(a), len(b)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j] if dp[i-1][j] >= dp[i][j-1] else dp[i][j-1]
        return dp

    def scs_length(self, s1: str, s2: str) -> int:
        dp = self._lcs_table(s1, s2)
        lcs_len = dp[len(s1)][len(s2)]
        return len(s1) + len(s2) - lcs_len

    def scs(self, s1: str, s2: str) -> str:
        # build LCS table
        dp = self._lcs_table(s1, s2)
        # reconstruct LCS string (optional but helpful for merging)
        i, j = len(s1), len(s2)
        lcs_chars = []
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                lcs_chars.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] >= dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        lcs = ''.join(reversed(lcs_chars))

        # merge s1 and s2 using lcs
        res = []
        i = j = 0
        for c in lcs:
            # append chars from s1 until we hit c
            while i < len(s1) and s1[i] != c:
                res.append(s1[i]); i += 1
            # append chars from s2 until we hit c
            while j < len(s2) and s2[j] != c:
                res.append(s2[j]); j += 1
            # append the LCS character once and advance both
            res.append(c); i += 1; j += 1

        # append remaining tails
        if i < len(s1):
            res.append(s1[i:])
        if j < len(s2):
            res.append(s2[j:])

        return ''.join(res)


class ShortestCommonSupersequence_optimal:
    def _lcs_table(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp

    def scs_length(self, s1, s2):
        dp = self._lcs_table(s1, s2)
        return len(s1) + len(s2) - dp[len(s1)][len(s2)]

    def scs(self, s1, s2):
        dp = self._lcs_table(s1, s2)
        i, j = len(s1), len(s2)
        res = []

        # Traverse from dp[n][m] backwards
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                res.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                res.append(s1[i-1])
                i -= 1
            else:
                res.append(s2[j-1])
                j -= 1

        # Append remaining characters
        while i > 0:
            res.append(s1[i-1])
            i -= 1
        while j > 0:
            res.append(s2[j-1])
            j -= 1

        # Reverse to get correct order
        return ''.join(reversed(res))
