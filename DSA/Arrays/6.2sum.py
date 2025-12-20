class TwoSum:
    def __init__(self, nums):
        self.nums = nums

    # -------------------------
    # 1️⃣ Brute Force
    # -------------------------
    def brute_force(self, target):
        n = len(self.nums)
        for i in range(n):
            for j in range(i + 1, n):
                if self.nums[i] + self.nums[j] == target:
                    return True, (self.nums[i], self.nums[j])
        return False, ()

    # -------------------------
    # 2️⃣ Better Approach - Two Pointers
    # -------------------------
    def two_pointers(self, target):
        nums_sorted = sorted(self.nums)
        left, right = 0, len(nums_sorted) - 1

        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                return True, (nums_sorted[left], nums_sorted[right])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False, ()

    # -------------------------
    # 3️⃣ Optimal Approach - Hashmap
    # -------------------------
    def hashmap_method(self, target):
        seen = set()
        for num in self.nums:
            if target - num in seen:
                return True, (num, target - num)
            seen.add(num)
        return False, ()
