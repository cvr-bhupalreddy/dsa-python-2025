# ✅ Core Idea Summary
#
# Brute Force: Check all triplets → O(n³) → handles duplicates using a set.
#
# Sort + Two Pointers:
#     Sort array.
#     Fix one element, use left & right pointers to find remaining two elements.
#     Skip duplicates to avoid repeated triplets.
#
# Time → O(n²), Space → O(1) extra (output excluded).


class ThreeSum:
    def __init__(self, nums):
        self.nums = nums

    # -------------------------
    # 1️⃣ Brute Force
    # -------------------------
    def brute_force(self):
        n = len(self.nums)
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.nums[i] + self.nums[j] + self.nums[k] == 0:
                        triplet = tuple(sorted([self.nums[i], self.nums[j], self.nums[k]]))
                        res.add(triplet)
        return list(res)

    # -------------------------
    # 2️⃣ Better / Optimal Approach - Sort + Two Pointers
    # -------------------------
    def two_pointers_method(self):
        nums_sorted = sorted(self.nums)
        n = len(nums_sorted)
        res = []

        for i in range(n):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue  # skip duplicates

            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                if current_sum == 0:
                    res.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    left += 1
                    right -= 1
                    # skip duplicates
                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res



class FourSum:
    def __init__(self, nums):
        self.nums = nums

    # -------------------------
    # 1️⃣ Brute Force
    # -------------------------
    def brute_force(self, target):
        n = len(self.nums)
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if self.nums[i] + self.nums[j] + self.nums[k] + self.nums[l] == target:
                            quadruplet = tuple(sorted([self.nums[i], self.nums[j], self.nums[k], self.nums[l]]))
                            res.add(quadruplet)
        return list(res)

    # -------------------------
    # 2️⃣ Better / Optimal Approach - Sort + Two Pointers
    # -------------------------
    def optimal(self, target):
        nums_sorted = sorted(self.nums)
        n = len(nums_sorted)
        res = []

        for i in range(n):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue  # skip duplicates for i
            for j in range(i + 1, n):
                if j > i + 1 and nums_sorted[j] == nums_sorted[j - 1]:
                    continue  # skip duplicates for j

                left, right = j + 1, n - 1
                while left < right:
                    total = nums_sorted[i] + nums_sorted[j] + nums_sorted[left] + nums_sorted[right]
                    if total == target:
                        res.append([nums_sorted[i], nums_sorted[j], nums_sorted[left], nums_sorted[right]])
                        left += 1
                        right -= 1
                        # skip duplicates for left and right
                        while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                            left += 1
                        while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
