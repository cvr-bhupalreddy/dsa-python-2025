def lis_sequence(arr):
    n = len(arr)
    dp = [1]*n
    prev_index = [-1]*n  # stores previous index in LIS

    # Fill dp and prev_index
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev_index[i] = j

    # Find the index of maximum LIS
    max_len = max(dp)
    max_index = dp.index(max_len)

    # Reconstruct LIS
    lis_seq = []
    while max_index != -1:
        lis_seq.append(arr[max_index])
        max_index = prev_index[max_index]

    lis_seq.reverse()  # because we traced backwards
    return lis_seq
