def longest_subarray_k_distinct_brute(nums, k):
    n = len(nums)
    max_len = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(nums[j])
            if len(seen) > k:
                break
            max_len = max(max_len, j - i + 1)

    return max_len


def longest_subarray_k_distinct_better(nums, k):
    from collections import defaultdict

    n = len(nums)
    freq = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(n):
        freq[nums[right]] += 1

        # Shrink window if distinct elements exceed k
        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def longest_subarray_k_distinct_optimal(fruits, k):
    from collections import defaultdict

    n = len(fruits)
    fruit_counts = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(n):
        fruit_counts[fruits[right]] += 1

        # Shrink window until distinct elements ≤ k
        if len(fruit_counts) > k:
            fruit_counts[fruits[left]] -= 1
            if fruit_counts[fruits[left]] == 0:
                del fruit_counts[fruits[left]]
                fruit_counts.pop(fruits[left], None)
            left += 1

        # Update max_len only when window is valid
        if len(fruit_counts) <= k:
            max_len = max(max_len, right - left + 1)

    return max_len
