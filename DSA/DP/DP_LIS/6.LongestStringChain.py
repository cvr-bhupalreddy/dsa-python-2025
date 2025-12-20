# 1. Sort all words in increasing order of their lengths.
#
# 2. Initialize a DP array:
# dp[i] = 1 for every word i
# (Each word is at least a chain of length 1 by itself.)
#
# 3. Define a function isPredecessor(a, b) that checks if:
# - len(a) + 1 == len(b)
# - by scanning both strings with two pointers, you can match
# every character of 'a' inside 'b' while allowing at most one skip.
# If these conditions hold, 'a' is a valid predecessor of 'b'.
#
# 4. Build the DP table (Forward Tabulation):
# for i from 0 to n-1:
#     for j from 0 to i-1:
#         if words[j] is a predecessor of words[i]:
#             dp[i] = max(dp[i], 1 + dp[j])
#
# 5. The answer to the Longest String Chain is:
# max(dp)


# function isPredecessor(shorter, longer):
#
# # Length condition must hold
# if length(longer) != length(shorter) + 1:
#     return false
#
# i = 0        # pointer for shorter
# j = 0        # pointer for longer
# mismatch = 0 # count extra characters in longer
#
# while j < length(longer):
#
#     if i < length(shorter) and shorter[i] == longer[j]:
#         # characters match → move both
#         i = i + 1
#         j = j + 1
#
#     else:
#         # longer has one extra character
#         mismatch = mismatch + 1
#         j = j + 1
#
#         if mismatch > 1:
#             return false
#
# return true



class LongestStringChain:

    # ---------------------------
    # Predecessor check
    # ---------------------------
    def isPred(self, a, b):
        # a must be exactly 1 letter shorter than b
        if len(a) + 1 != len(b):
            return False

        i = j = 0
        mismatch = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                mismatch += 1
                j += 1
                if mismatch > 1:
                    return False
        return True  # mismatch <= 1

    # ---------------------------
    # Constructor
    # ---------------------------
    def __init__(self, words):
        self.words = sorted(words, key=len)
        self.n = len(words)

    # ---------------------------------------------------------
    # 1) Memoization without LRU CACHE (using dp list)
    # dp[i] = best chain ending at index i
    # ---------------------------------------------------------
    def longestStrChain_memo(self):
        dp = [-1] * self.n     # for memo storage

        def solve(i):
            if dp[i] != -1:
                return dp[i]

            best = 1
            for j in range(i):
                if self.isPred(self.words[j], self.words[i]):
                    best = max(best, 1 + solve(j))

            dp[i] = best
            return dp[i]

        ans = 1
        for i in range(self.n):
            ans = max(ans, solve(i))
        return ans

    # ---------------------------------------------------------
    # 2) Forward Tabulation
    # dp[i] = best chain ending at i
    # ---------------------------------------------------------
    def longestStrChain_tab(self):
        dp = [1] * self.n

        for i in range(self.n):
            for j in range(i):
                if self.isPred(self.words[j], self.words[i]):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    # ---------------------------------------------------------
    # 3) Backward Tabulation
    # dp[i] = best chain starting at i
    # ---------------------------------------------------------
    def longestStrChain_backward_tab(self):
        dp = [1] * self.n

        for i in range(self.n - 1, -1, -1):
            for j in range(i + 1, self.n):
                if self.isPred(self.words[i], self.words[j]):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    # ---------------------------------------------------------
    # 4) Space Optimized (already 1D → cannot optimize further)
    # ---------------------------------------------------------
    def longestStrChain_space_opt(self):
        dp = [1] * self.n

        for i in range(self.n):
            for j in range(i):
                if self.isPred(self.words[j], self.words[i]):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
