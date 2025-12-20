from typing import List

class PartitionArrayMaxSum:

    # ---------------- Problem Statement ----------------
    # Given an array arr of size n and integer k,
    # partition the array into contiguous subarrays of length at most k.
    # For each subarray, replace all elements with the maximum element in that subarray.
    # Return the maximum sum after partitioning.

    # ---------------- Idea / Recurrence ----------------
    # Let dp[i] = maximum sum for subarray arr[0..i]
    # dp[i] = max_{1 <= l <= k, i-l+1 >= 0} { dp[i-l] + max(arr[i-l+1..i])*l }
    # Base case: dp[-1] = 0

    # ---------------- Memoization (Top-Down) ----------------
    def maxSumMemo(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1]*n

        def solve(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]

            max_sum = 0
            curr_max = 0
            for l in range(1, k+1):
                if i - l + 1 < 0:
                    break
                curr_max = max(curr_max, arr[i - l + 1])
                max_sum = max(max_sum, solve(i - l) + curr_max * l)

            dp[i] = max_sum
            return dp[i]

        return solve(n-1)

    # ---------------- Tabulation (Bottom-Up) ----------------
    def maxSumTab(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)  # dp[i] = max sum for first i elements

        for i in range(1, n+1):
            curr_max = 0
            for l in range(1, min(k, i)+1):
                curr_max = max(curr_max, arr[i-l])
                dp[i] = max(dp[i], dp[i-l] + curr_max*l)

        return dp[n]

    # ---------------- Space Optimized ----------------
    def maxSumSpaceOpt(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(k+1)  # only need last k values

        for i in range(1, n+1):
            curr_max = 0
            max_val = 0
            for l in range(1, min(k, i)+1):
                curr_max = max(curr_max, arr[i-l])
                max_val = max(max_val, dp[(i-l) % (k+1)] + curr_max*l)
            dp[i % (k+1)] = max_val

        return dp[n % (k+1)]


class PartitionArrayMaxSumForward:

    # -------------------- Memoization (Top-Down) --------------------
    # solve(i) = max sum obtainable from subarray arr[i..n-1]
    def maxSumMemoForward(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * (n+1)

        def solve(i):
            if i == n:          # reached end
                return 0
            if dp[i] != -1:
                return dp[i]

            curr_max = 0
            best = 0

            # try all partition sizes from i
            for l in range(1, k+1):
                if i + l - 1 >= n:
                    break
                curr_max = max(curr_max, arr[i+l-1])
                best = max(best, curr_max * l + solve(i+l))

            dp[i] = best
            return best

        return solve(0)

    # -------------------- Tabulation (Bottom-Up Forward) --------------------
    # dp[i] = max sum obtainable from arr[i..n-1]
    def maxSumTabForward(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)   # dp[n] = 0

        for i in range(n-1, -1, -1):
            curr_max = 0
            best = 0
            for l in range(1, k+1):
                if i + l > n:
                    break
                curr_max = max(curr_max, arr[i+l-1])
                best = max(best, curr_max*l + dp[i+l])
            dp[i] = best

        return dp[0]

    # -------------------- Space Optimized --------------------
    def maxSumSpaceOptForward(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (k+1)  # only window of size k

        for i in range(n-1, -1, -1):
            curr_max = 0
            best = 0
            for l in range(1, k+1):
                if i + l > n:
                    break
                curr_max = max(curr_max, arr[i+l-1])
                best = max(best, curr_max*l + dp[(i+l) % (k+1)])

            dp[i % (k+1)] = best

        return dp[0]
