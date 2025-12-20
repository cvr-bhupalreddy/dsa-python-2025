# 5️⃣ Explanation of Dutch National Flag
#
#     low → next position for 0
#     mid → current element being inspected
#     high → next position for 2
#
# Logic:
#
#     If arr[mid] == 0: swap with low, move low and mid forward.
#     If arr[mid] == 1: just move mid forward.
#     If arr[mid] == 2: swap with high, move high backward.
#
# This guarantees one-pass in-place sorting.


class Sort012:
    def __init__(self, nums):
        self.nums = nums

    # -------------------------
    # 1️⃣ Brute Force - Count 0,1,2
    # -------------------------
    def brute_force(self):
        count0 = count1 = count2 = 0
        for num in self.nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        index = 0
        for _ in range(count0):
            self.nums[index] = 0
            index += 1
        for _ in range(count1):
            self.nums[index] = 1
            index += 1
        for _ in range(count2):
            self.nums[index] = 2
            index += 1
        return self.nums

    # -------------------------
    # 2️⃣ Better Approach - Sort
    # -------------------------
    def better_sort(self):
        self.nums.sort()
        return self.nums

    # -------------------------
    # 3️⃣ Optimal Approach - Dutch National Flag
    # -------------------------
    def dutch_national_flag(self):
        low, mid, high = 0, 0, len(self.nums) - 1

        while mid <= high:
            if self.nums[mid] == 0:
                self.nums[low], self.nums[mid] = self.nums[mid], self.nums[low]
                low += 1
                mid += 1
            elif self.nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                self.nums[mid], self.nums[high] = self.nums[high], self.nums[mid]
                high -= 1
        return self.nums
