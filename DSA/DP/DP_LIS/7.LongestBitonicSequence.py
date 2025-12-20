# A Bitonic Subsequence is a sequence that:
#
# First strictly increases
#
# Then strictly decreases
#
# We want to find the length of the Longest Bitonic Subsequence in a given array.

from typing import List

class LongestBitonicSubsequence:

    def longestBitonicMemo(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        # Memo arrays
        inc_memo = [-1] * n
        dec_memo = [-1] * n

        # LIS ending at index i
        def lis(i):
            if inc_memo[i] != -1:
                return inc_memo[i]
            best = 1
            for j in range(i):
                if arr[j] < arr[i]:
                    best = max(best, 1 + lis(j))
            inc_memo[i] = best
            return best

        # LDS starting at index i
        def lds(i):
            if dec_memo[i] != -1:
                return dec_memo[i]
            best = 1
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    best = max(best, 1 + lds(j))
            dec_memo[i] = best
            return best

        # Compute LBS length
        max_len = 0
        for i in range(n):
            max_len = max(max_len, lis(i) + lds(i) - 1)

        return max_len


class LongestBitonicSubsequence:

    def longestBitonicTab(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        # Step 1: LIS ending at i
        inc = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    inc[i] = max(inc[i], inc[j] + 1)

        # Step 2: LDS starting at i
        dec = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if arr[j] < arr[i]:
                    dec[i] = max(dec[i], dec[j] + 1)

        # Step 3: Combine
        max_len = 0
        for i in range(n):
            max_len = max(max_len, inc[i] + dec[i] - 1)

        return max_len




class LongestBitonicSubsequenceFront:

    def longestBitonicFront(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        # Step 1: LIS ending at i (same as usual)
        inc = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[j] < arr[i]:
                    inc[i] = max(inc[i], inc[j] + 1)

        # Step 2: LDS ending at i (front scan)
        dec = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[j] > arr[i]:   # previous element bigger → decreasing
                    dec[i] = max(dec[i], dec[j] + 1)

        # Step 3: Combine LIS + LDS at each peak
        max_len = 0
        for i in range(n):
            max_len = max(max_len, inc[i] + dec[i] - 1)

        return max_len
