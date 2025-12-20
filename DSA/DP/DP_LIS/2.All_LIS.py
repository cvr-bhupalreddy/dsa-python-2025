import bisect

class LIS:
    # -----------------------------
    # 1. Memoization (Top-down)
    # -----------------------------
    def lis_memo(self, arr):
        n = len(arr)
        dp = [[-1]*(n+1) for _ in range(n)]

        def solve(i, prev_index):
            if i == n:
                return 0
            if dp[i][prev_index+1] != -1:
                return dp[i][prev_index+1]

            # Skip current
            not_take = solve(i+1, prev_index)
            # Take current if valid
            take = 0
            if prev_index == -1 or arr[i] > arr[prev_index]:
                take = 1 + solve(i+1, i)

            dp[i][prev_index+1] = max(take, not_take)
            return dp[i][prev_index+1]

        return solve(0, -1)

    # -----------------------------
    # 2. Tabulation (Bottom-up)
    # -----------------------------
    def lis_tab(self, arr):
        n = len(arr)
        dp = [1]*n
        prev_index = [-1]*n  # For sequence reconstruction

        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    prev_index[i] = j

        # Optional: reconstruct one LIS
        max_len = max(dp)
        index = dp.index(max_len)
        seq = []
        while index != -1:
            seq.append(arr[index])
            index = prev_index[index]
        seq.reverse()

        return max_len, seq

    # -----------------------------
    # 3. Space Optimized (O(n log n))
    # -----------------------------
    def lis_optimized(self, arr):
        sub = []
        for num in arr:
            idx = bisect.bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)

    # -----------------------------
    # 4. All LIS sequences
    # -----------------------------
    def all_lis(self, arr):
        n = len(arr)
        dp = [1]*n
        prev = [[] for _ in range(n)]

        # Fill dp and prev
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        prev[i] = [j]
                    elif dp[j]+1 == dp[i]:
                        prev[i].append(j)

        max_len = max(dp)
        end_indices = [i for i, x in enumerate(dp) if x == max_len]
        result = []

        def dfs(index, path):
            path.append(arr[index])
            if not prev[index]:
                result.append(path[::-1])
            else:
                for p in prev[index]:
                    dfs(p, path.copy())

        for idx in end_indices:
            dfs(idx, [])

        return result
