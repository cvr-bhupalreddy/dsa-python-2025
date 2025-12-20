arr = [1, 1, 2, 3]
diff = 1


def count_subsets_with_diff(arr, diff):
    total = sum(arr)
    if (diff + total) % 2 != 0:
        return 0  # no solution possible
    target = (diff + total) // 2
    n = len(arr)

    # dp[i][s] = number of ways to get sum s using first i elements
    dp = [[-1] * (target + 1) for _ in range(n)]

    def helper(i, s):
        if s == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == s else 0
        if dp[i][s] != -1:
            return dp[i][s]

        # Not take
        not_take = helper(i - 1, s)
        # Take
        take = helper(i - 1, s - arr[i]) if s >= arr[i] else 0

        dp[i][s] = take + not_take
        return dp[i][s]

    return helper(n - 1, target)


print("Number of subsets with given difference:", count_subsets_with_diff(arr, diff))


def count_subsets_with_diff_tab(arr, diff):
    total = sum(arr)
    if (diff + total) % 2 != 0:
        return 0
    target = (diff + total) // 2
    n = len(arr)

    dp = [[0] * (target + 1) for _ in range(n)]

    # Base case
    for i in range(n):
        dp[i][0] = 1
    if arr[0] <= target:
        dp[0][arr[0]] = 1

    for i in range(1, n):
        for s in range(1, target + 1):
            not_take = dp[i - 1][s]
            take = dp[i - 1][s - arr[i]] if s >= arr[i] else 0
            dp[i][s] = take + not_take

    return dp[n - 1][target]


print("Number of subsets with given difference (tabulation):", count_subsets_with_diff_tab(arr, diff))


def count_subsets_with_diff_space_opt(arr, diff):
    total = sum(arr)
    if (diff + total) % 2 != 0:
        return 0
    target = (diff + total) // 2
    n = len(arr)
    prev = [0] * (target + 1)
    prev[0] = 1
    if arr[0] <= target:
        prev[arr[0]] = 1

    for i in range(1, n):
        curr = [0] * (target + 1)
        curr[0] = 1
        for s in range(1, target + 1):
            not_take = prev[s]
            take = prev[s - arr[i]] if s >= arr[i] else 0
            curr[s] = take + not_take
        prev = curr

    return prev[target]


print("Number of subsets with given difference (space optimized):", count_subsets_with_diff_space_opt(arr, diff))
