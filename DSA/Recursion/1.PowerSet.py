def all_subsequences(arr):
    n = len(arr)
    total = 1 << n   # 2^n
    result = []

    for mask in range(total):
        subseq = []
        for i in range(n):
            if (mask >> i) & 1:   # if i-th bit is set
                subseq.append(arr[i])
        result.append(subseq)

    return result
