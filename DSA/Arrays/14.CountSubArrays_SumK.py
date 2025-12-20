def count_subarrays_bruteforce(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count


def count_subarrays_leq(arr, X):
    left = 0
    curr = 0
    cnt = 0

    for right in range(len(arr)):
        curr += arr[right]

        while curr > X:  # shrink until valid
            curr -= arr[left]
            left += 1

        # all windows [left … right] are valid
        cnt += (right - left + 1)

    return cnt


def count_subarrays_sum_k(arr, k):
    return count_subarrays_leq(arr, k) - count_subarrays_leq(arr, k - 1)


def count_subarrays_with_sum(nums, k):
    from collections import defaultdict

    count_map = defaultdict(int)
    count_map[0] = 1  # empty subarray prefix
    prefix_sum = 0
    total_count = 0

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in count_map:
            total_count += count_map[prefix_sum - k]
        count_map[prefix_sum] += 1

    return total_count

# | Method               | Handles Negative Numbers?  | Time Complexity | Recommended    |
# | -------------------- | -------------------------- | --------------- | -------------- |
# | Brute Force          | ✔                          | O(n²)           | ❌ Slow         |
# | Sliding Window       | ❌ Only Non-Negative arrays | O(n)            | ⚠️ Conditional |
# | Prefix Sum + HashMap | ✔ All arrays               | O(n)            | ✅ Best         |
