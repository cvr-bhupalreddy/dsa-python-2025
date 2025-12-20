def count_subarrays_bruteforce(nums, K):
    n = len(nums)
    count = 0

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s == K:
                count += 1

    return count


def count_subarrays_optimal(nums, K):
    from collections import defaultdict

    prefix = 0
    freq = defaultdict(int)
    freq[0] = 1   # empty prefix sum

    count = 0

    for num in nums:
        prefix += num

        # valid previous prefix making sum = K
        if prefix - K in freq:
            count += freq[prefix - K]

        freq[prefix] += 1

    return count


# nums = [1,0,1,0,1]
# K = 2
#
#
# | i | num | prefix | prefix-K | count added | freq map after       |
# | - | --- | ------ | -------- | ----------- | -------------------- |
# | 0 | 1   | 1      | -1       | 0           | {0:1, 1:1}           |
# | 1 | 0   | 1      | -1       | 0           | {0:1, 1:2}           |
# | 2 | 1   | 2      | 0        | 1           | {0:1, 1:2, 2:1}      |
# | 3 | 0   | 2      | 0        | 1           | {0:1, 1:2, 2:2}      |
# | 4 | 1   | 3      | 1        | 2           | {0:1, 1:2, 2:2, 3:1} |


def count_subarrays_with_sum_at_most(nums, K):
    n = len(nums)
    left = 0
    total = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += nums[right]

        while curr_sum > K:
            curr_sum -= nums[left]
            left += 1

        # all subarrays ending at `right` with sum <= K
        total += (right - left + 1)

    return total


def count_subarrays_sum_equals_K(nums, K):
    return count_subarrays_with_sum_at_most(nums, K) - \
        count_subarrays_with_sum_at_most(nums, K - 1)
