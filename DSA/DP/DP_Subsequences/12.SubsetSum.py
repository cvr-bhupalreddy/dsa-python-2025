arr = [2, 3, 7, 8, 10]
target = 11


# ================= Memoization =================
def target_sum_memo(arr, target):
    n = len(arr)
    dp = [[-1] * (target + 1) for _ in range(n)]

    def helper(i, k):
        if k == 0:
            return True
        if i < 0:
            return False
        if dp[i][k] != -1:
            return dp[i][k]

        not_take = helper(i - 1, k)
        take = helper(i - 1, k - arr[i]) if k >= arr[i] else False

        dp[i][k] = take or not_take
        return dp[i][k]

    return helper(n - 1, target)


# ================= Tabulation =================
def target_sum_tab(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    if arr[0] <= target:
        dp[0][arr[0]] = True

    for i in range(1, n):
        for k in range(1, target + 1):
            not_take = dp[i - 1][k]
            take = dp[i - 1][k - arr[i]] if k >= arr[i] else False
            dp[i][k] = take or not_take

    return dp[n - 1][target], dp  # return dp for reconstruction


# ================= Space Optimized =================
def target_sum_space_opt(arr, target):
    n = len(arr)
    prev = [False] * (target + 1)
    prev[0] = True
    if arr[0] <= target:
        prev[arr[0]] = True

    for i in range(1, n):
        curr = [False] * (target + 1)
        curr[0] = True
        for k in range(1, target + 1):
            not_take = prev[k]
            take = prev[k - arr[i]] if k >= arr[i] else False
            curr[k] = take or not_take
        prev = curr

    return prev[target]


# ================= Subset Reconstruction =================
def reconstruct_subset(arr, target, dp):
    n = len(arr)
    subset = []
    i = n - 1
    k = target

    while k > 0 and i >= 0:
        if i == 0:
            if dp[i][k]:
                subset.append(arr[i])
            break
        if dp[i - 1][k]:
            i -= 1  # element not included
        else:
            subset.append(arr[i])
            k -= arr[i]
            i -= 1

    return subset[::-1]


# ================= Testing =================
print("Memoization:", target_sum_memo(arr, target))

res_tab, dp_table = target_sum_tab(arr, target)
print("Tabulation:", res_tab)
print("Subset from Tabulation:", reconstruct_subset(arr, target, dp_table))

print("Space Optimized:", target_sum_space_opt(arr, target))
