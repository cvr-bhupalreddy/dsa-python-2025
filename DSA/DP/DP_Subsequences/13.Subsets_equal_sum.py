arr = [1, 5, 11, 5]

# ================= Memoization =================
def can_partition_memo(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    n = len(arr)
    dp = [[-1]*(target+1) for _ in range(n)]

    def helper(i, k):
        if k == 0:
            return True
        if i < 0:
            return False
        if dp[i][k] != -1:
            return dp[i][k]

        not_take = helper(i-1, k)
        take = helper(i-1, k-arr[i]) if k >= arr[i] else False

        dp[i][k] = take or not_take
        return dp[i][k]

    return helper(n-1, target)


# ================= Tabulation =================
def can_partition_tab(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    n = len(arr)
    dp = [[False]*(target+1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    if arr[0] <= target:
        dp[0][arr[0]] = True

    for i in range(1, n):
        for k in range(1, target+1):
            not_take = dp[i-1][k]
            take = dp[i-1][k-arr[i]] if k >= arr[i] else False
            dp[i][k] = take or not_take

    return dp[n-1][target]


# ================= Space Optimized =================
def can_partition_space_opt(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    n = len(arr)
    prev = [False]*(target+1)
    prev[0] = True
    if arr[0] <= target:
        prev[arr[0]] = True

    for i in range(1, n):
        curr = [False]*(target+1)
        curr[0] = True
        for k in range(1, target+1):
            not_take = prev[k]
            take = prev[k-arr[i]] if k >= arr[i] else False
            curr[k] = take or not_take
        prev = curr

    return prev[target]


# ================= Testing =================
print("Memoization:", can_partition_memo(arr))
print("Tabulation:", can_partition_tab(arr))
print("Space Optimized:", can_partition_space_opt(arr))
