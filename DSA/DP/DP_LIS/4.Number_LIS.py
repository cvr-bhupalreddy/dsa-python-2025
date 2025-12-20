from typing import List


class NumberOfLIS:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        length = [1] * n  # length of LIS ending at i
        count = [1] * n  # number of LIS ending at i

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        return sum(count[i] for i in range(n) if length[i] == max_len)


# Example
nums = [1, 3, 5, 4, 7]
sol = NumberOfLIS()
print(sol.findNumberOfLIS(nums))  # Output: 2
