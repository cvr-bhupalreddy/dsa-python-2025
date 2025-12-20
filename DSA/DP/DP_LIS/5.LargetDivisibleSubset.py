def largestDivisibleSubset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)

    dp = [1] * n               # length of subset ending at i
    parent = [-1] * n          # predecessor pointer

    max_len = 1
    max_idx = 0

    # Build DP table
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

        # Track best subset
        if dp[i] > max_len:
            max_len = dp[i]
            max_idx = i

    # Reconstruct subset
    result = []
    while max_idx != -1:
        result.append(nums[max_idx])
        max_idx = parent[max_idx]

    return result[::-1]        # reverse to get increasing order
