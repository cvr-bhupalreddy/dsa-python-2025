arr = [2, 3, 5, 6, 8]
target = 10


# ================= Memoization =================
def count_subsets_memo(arr, target):
    n = len(arr)
    dp = [[-1] * (target + 1) for _ in range(n)]

    def helper(i, k):
        if k == 0:
            return 1  # empty subset counts
        if i < 0:
            return 0
        if dp[i][k] != -1:
            return dp[i][k]

        not_take = helper(i - 1, k)
        take = helper(i - 1, k - arr[i]) if k >= arr[i] else 0

        dp[i][k] = take + not_take
        return dp[i][k]

    return helper(n - 1, target), dp


# ================= Tabulation =================
def count_subsets_tab(arr, target):
    n = len(arr)
    dp = [[0] * (target + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1  # sum 0 always possible

    if arr[0] <= target:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for k in range(1, target + 1):
            not_take = dp[i - 1][k]
            take = dp[i - 1][k - arr[i]] if k >= arr[i] else 0
            dp[i][k] = take + not_take

    return dp[n - 1][target], dp


# ================= Space Optimized =================
def count_subsets_space_opt(arr, target):
    n = len(arr)
    prev = [0] * (target + 1)
    prev[0] = 1
    if arr[0] <= target:
        prev[arr[0]] = 1

    for i in range(1, n):
        curr = [0] * (target + 1)
        curr[0] = 1
        for k in range(1, target + 1):
            not_take = prev[k]
            take = prev[k - arr[i]] if k >= arr[i] else 0
            curr[k] = take + not_take
        prev = curr

    return prev[target]


# ================= Reconstruct Subsets =================
def reconstruct_subsets(arr, target, dp):
    subsets = []
    n = len(arr)

    def helper(i, k, path):
        if k == 0:
            subsets.append(path[::-1])
            return
        if i < 0:
            return

        # If not take element
        if dp[i - 1][k] > 0:
            helper(i - 1, k, path)

        # If take element
        if k >= arr[i] and dp[i - 1][k - arr[i]] > 0:
            helper(i - 1, k - arr[i], path + [arr[i]])

    helper(n - 1, target, [])
    return subsets


# ================= Testing =================
print("Memoization count:", count_subsets_memo(arr, target)[0])
count_tab, dp_table = count_subsets_tab(arr, target)
print("Tabulation count:", count_tab)
print("Subsets with sum", target, ":", reconstruct_subsets(arr, target, dp_table))
print("Space optimized count:", count_subsets_space_opt(arr, target))
