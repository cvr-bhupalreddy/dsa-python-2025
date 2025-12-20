# ⭐ CORE OBSERVATION
# Sum of Subarray Ranges=( ∑of all subarray maximums)− ( ∑of all subarray minimums)
#
#
# So this becomes the same as:
#
# Sum of subarray maximums → monotonic decreasing stack
# Sum of subarray minimums → monotonic increasing stack

def sumOfSubarrayRange_brute(nums):
    range_sum = 0
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            sub = nums[i:j + 1]
            range_sum += max(sub) - min(sub)
    return range_sum


def sumOfSubarrayRange_better(nums):
    range_sum = 0
    n = len(nums)
    for i in range(n):
        curr_min = curr_max = nums[i]
        for j in range(i, n):
            curr_min = min(curr_min, nums[j])
            curr_max = max(curr_max, nums[j])
            range_sum += curr_max - curr_min
    return range_sum


class Solution:
    def subArrayRanges(self, nums):
        n = len(nums)

        # Helper for contributions (generic stack logic)
        def contribution(nums, compare):
            n = len(nums)
            stack = []

            left = [0] * n
            right = [0] * n

            # LEFT contribution (previous greater/smaller)
            for i in range(n):
                while stack and compare(nums[stack[-1]], nums[i]):
                    stack.pop()
                left[i] = i - stack[-1] if stack else i + 1
                stack.append(i)

            stack = []

            # RIGHT contribution (next greater/smaller)
            for i in range(n-1, -1, -1):
                while stack and compare(nums[stack[-1]], nums[i]):
                    stack.pop()
                right[i] = stack[-1] - i if stack else n - i
                stack.append(i)

            total = 0
            for i in range(n):
                total += nums[i] * left[i] * right[i]
            return total

        # Max contribution → use <
        max_sum = contribution(nums, lambda a, b: a <= b)
        # Min contribution → use >
        min_sum = contribution(nums, lambda a, b: a >= b)

        return max_sum - min_sum
