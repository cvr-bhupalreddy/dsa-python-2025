class LargestSubarraySumK:
    def __init__(self, nums):
        self.nums = nums

    # -------------------------
    # 1️⃣ Brute Force
    # Check all subarrays
    # Time: O(n^2), Space: O(1)
    # Returns length of largest subarray with sum=k
    # -------------------------
    def brute_force(self, k):
        n = len(self.nums)
        max_len = 0
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += self.nums[end]
                if current_sum == k:
                    max_len = max(max_len, end - start + 1)
        return max_len

    # -------------------------
    # 2️⃣ Prefix Sum
    # Precompute prefix sums
    # Time: O(n^2), Space: O(n)
    # -------------------------
    def prefix_sum_method(self, k):
        n = len(self.nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + self.nums[i]

        max_len = 0
        for start in range(n):
            for end in range(start, n):
                current_sum = prefix[end + 1] - prefix[start]
                if current_sum == k:
                    max_len = max(max_len, end - start + 1)
        return max_len

    # -------------------------
    # 3️⃣ Hashing / Optimal
    # Use hashmap to store first occurrence of prefix sums
    # Time: O(n), Space: O(n)
    # -------------------------
    def hashing_method(self, k):
        prefix_sum_map = {}
        prefix = 0
        max_len = 0
        for i, num in enumerate(self.nums):
            prefix += num
            if prefix == k:
                max_len = i + 1
            if (prefix - k) in prefix_sum_map:
                max_len = max(max_len, i - prefix_sum_map[prefix - k])
            if prefix not in prefix_sum_map:
                prefix_sum_map[prefix] = i
        return max_len

    # -------------------------
    # 4️⃣ Sliding Window
    # Only works for positive numbers
    # Time: O(n), Space: O(1)
    # -------------------------
    def sliding_window_positive(self, k):
        n = len(self.nums)
        max_len = 0
        start = 0
        current_sum = 0
        for end in range(n):
            current_sum += self.nums[end]
            while current_sum > k and start <= end:
                current_sum -= self.nums[start]
                start += 1
            if current_sum == k:
                max_len = max(max_len, end - start + 1)
        return max_len
