# Front Partitioning

# for end in range(i, n):
#     substring = s[i:end+1]
#     if substring is valid:
#         recursively solve the rest starting from end+1

#
# 1️⃣ Palindrome Partitioning Problem Statement: Given a string s, partition it into substrings such that every
# substring is a palindrome. Return all possible palindrome partitioning.
#
# Core Idea / Front Partitioning:
# - Start at index i = 0.
# - Try all substrings s[i:end+1].
# - If substring is palindrome:
# - Include it in the current path.
# - Recurse from end+1.
# - Base case: i == len(s) → store current path.
#
# Front Partitioning: Always partition from the current index i forward, exploring all possible "first pieces" before
# recursing on the remaining string.
#
# ---
#
# 2️⃣ Word Break / Word Break II
# Problem Statement:
# Given a string s and a dictionary of words dict, find all ways to break s into a sequence of dictionary words.
#
# Core Idea / Front Partitioning:
# - Start at index i = 0.
# - Try all substrings s[i:end+1].
# - If substring exists in dictionary:
# - Include in path.
# - Recurse from end+1.
# - Base case: i == len(s) → store the constructed sentence.
#
# Front Partitioning:
# Each recursive call considers all possible "first words" starting from the current index.
#
# ---
#
# 3️⃣ Restore IP Addresses
# Problem Statement:
# Given a string of digits, restore all possible valid IP addresses.
# Each address consists of 4 integers [0-255], separated by dots.
#
# Core Idea / Front Partitioning:
# - Start at index i = 0.
# - Take substrings of length 1, 2, or 3.
# - Validate segment (0 not prefixed, ≤ 255).
# - If valid, append to path and recurse.
# - Base case: 4 segments formed and i == len(s) → store IP.
#
# Front Partitioning:
# Partitioning from the front allows trying all possible first segments before moving forward.
#
# ---
#
# 4️⃣ Decode Ways / Number Encoding
# Problem Statement:
# Given a string of digits, count the number of ways to decode it using mapping 1->A, 2->B, ..., 26->Z.
#
# Core Idea / Front Partitioning:
# - Start at index i = 0.
# - Take 1 or 2 digits.
# - If valid (1 <= val <= 26): recurse on the remaining string.
# - Base case: i == len(s) → valid decoding found.
#
# Front Partitioning:
# Each recursive call considers all possible "next pieces" from the front (1 or 2 digits).
#
# ---
#
# 5️⃣ Partition DP Problems (Front-based Recursion)
# Problem Statement:
# Any problem where you need to partition an array or string into
# subarrays/substrings and compute some property (such as sum, product, palindrome checks, etc.).
#
# Core Idea / Front Partitioning:
# - At index i, try all possible next cuts.
# - Solve recursively for the remaining part.
# - Use DP/memoization to cache results of solve(i) to avoid recomputation.
#
# Front Partitioning:
# Instead of trying all possible endings, start from the current index and explore all forward possibilities.

from typing import List


class FrontPartitionDPList:
    """
    Implements DP problems using front partitioning with lists/matrices only.
    """

    # ----------------- 1️⃣ Palindrome Partitioning -----------------
    # Generating all sequences, DP memoization not meaningful here
    def palindrome_partitioning(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def dfs(i: int, path: List[str]):
            if i == len(s):
                res.append(path.copy())
                return
            for end in range(i, len(s)):
                if is_palindrome(s[i:end + 1]):
                    path.append(s[i:end + 1])
                    dfs(end + 1, path)
                    path.pop()

        res = []
        dfs(0, [])
        return res

    # ----------------- 2️⃣ Word Break II -----------------
    def word_break_ii(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp: List[List[str]] = [[] for _ in range(n + 1)]
        dp[n] = [""]  # base case: empty string

        wordSet = set(wordDict)

        for i in range(n - 1, -1, -1):
            temp = []
            for j in range(i, n):
                sub = s[i:j + 1]
                if sub in wordSet:
                    for suffix in dp[j + 1]:
                        temp.append(sub + (" " + suffix if suffix else ""))
            dp[i] = temp
        return dp[0]

    # ----------------- 3️⃣ Restore IP Addresses -----------------
    # Recursion only
    def restore_ip_addresses(self, s: str) -> List[str]:
        def dfs(i: int, path: List[str]):
            if len(path) == 4 and i == len(s):
                res.append(".".join(path))
                return
            if len(path) >= 4:
                return
            for l in range(1, 4):
                if i + l > len(s):
                    break
                part = s[i:i + l]
                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue
                path.append(part)
                dfs(i + l, path)
                path.pop()

        res = []
        dfs(0, [])
        return res

    # ----------------- 4️⃣ Decode Ways / Number Encoding -----------------
    # Memoization, Tabulation, Space Optimization using list
    def num_decodings(self, s: str) -> int:
        n = len(s)
        # Memoization
        memo = [-1] * (n + 1)

        def dfs(i: int) -> int:
            if i == n:
                return 1
            if memo[i] != -1:
                return memo[i]
            if s[i] == '0':
                memo[i] = 0
                return 0
            ans = dfs(i + 1)
            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                ans += dfs(i + 2)
            memo[i] = ans
            return ans

        # Tabulation
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            dp[i] = dp[i + 1]
            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]

        # Space optimization: same as tabulation because 1D array already minimal
        return dp[0]

    # ----------------- 5️⃣ Min Cut Palindrome (Partition DP Example) -----------------
    # Memoization, Tabulation, Space Optimization using lists
    def min_cut_palindrome(self, s: str) -> int:
        n = len(s)
        # Precompute palindrome table
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        # Memoization
        memo = [-1] * n

        def dfs(i: int) -> int:
            if i == n:
                return -1
            if memo[i] != -1:
                return memo[i]
            ans = float('inf')
            for j in range(i, n):
                if is_pal[i][j]:
                    ans = min(ans, 1 + dfs(j + 1))
            memo[i] = ans
            return ans

        # Tabulation
        dp = [float('inf')] * (n + 1)
        dp[n] = -1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if is_pal[i][j]:
                    dp[i] = min(dp[i], 1 + dp[j + 1])

        # Space optimization: 1D dp array already minimal
        return dp[0]


# -------------------- Example Usage --------------------
if __name__ == "__main__":
    dp = FrontPartitionDPList()

    # Palindrome Partitioning
    s = "aab"
    print("Palindrome partitions:", dp.palindrome_partitioning(s))

    # Word Break II
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print("Word Break II:", dp.word_break_ii(s, wordDict))

    # Restore IP Addresses
    s = "25525511135"
    print("Restore IPs:", dp.restore_ip_addresses(s))

    # Decode Ways
    s = "226"
    print("Number of decodings:", dp.num_decodings(s))

    # Min Cut Palindrome
    s = "aab"
    print("Minimum cuts for palindrome partitioning:", dp.min_cut_palindrome(s))
