def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # Helper function for linear version
    def rob_linear(arr):
        prev = arr[0]
        prev2 = 0
        for i in range(1, len(arr)):
            pick = arr[i] + prev2
            not_pick = prev
            curr = max(pick, not_pick)
            prev2, prev = prev, curr
        return prev

    # Two cases
    case1 = rob_linear(nums[1:])   # exclude first
    case2 = rob_linear(nums[:-1])  # exclude last

    return max(case1, case2)
