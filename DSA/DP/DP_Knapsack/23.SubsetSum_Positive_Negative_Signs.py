class TargetSumAsSubset:
    def find_target_sum_ways(self, nums, target):
        S = sum(nums)
        # Check if (target + sum) is even and non-negative
        if (S + target) % 2 != 0 or (S + target) < 0:
            return 0

        subset_sum = (S + target) // 2
        n = len(nums)

        # dp[i][s] = number of subsets using first i numbers that sum to s
        dp = [[0] * (subset_sum + 1) for _ in range(n)]

        # Base case: first number
        if nums[0] == 0:
            dp[0][0] = 2  # include or exclude zero
        else:
            dp[0][0] = 1  # exclude
            if nums[0] <= subset_sum:
                dp[0][nums[0]] = 1  # include

        for i in range(1, n):
            for s in range(subset_sum + 1):
                not_take = dp[i - 1][s]
                take = dp[i - 1][s - nums[i]] if s >= nums[i] else 0
                dp[i][s] = take + not_take

        return dp[n - 1][subset_sum]


class TargetSum:
    def find_target_sum_ways_memo(self, nums, target):
        n = len(nums)
        total = sum(nums)
        # dp[i][curr_sum + total] = number of ways to reach curr_sum using first i numbers
        dp = [[-1] * (2 * total + 1) for _ in range(n)]

        def recur(ind, curr_sum):
            if ind == 0:
                # Base case: check if + or - first number achieves target
                count = 0
                if curr_sum == nums[0]:
                    count += 1
                if curr_sum == -nums[0]:
                    count += 1
                return count

            if dp[ind][curr_sum + total] != -1:
                return dp[ind][curr_sum + total]

            # Option 1: add current number
            add = recur(ind - 1, curr_sum - nums[ind])
            # Option 2: subtract current number
            subtract = recur(ind - 1, curr_sum + nums[ind])

            dp[ind][curr_sum + total] = add + subtract
            return dp[ind][curr_sum + total]

        return recur(n - 1, target)

    def find_target_sum_ways_tab(self, nums, target):
        n = len(nums)
        total = sum(nums)
        dp = [[0] * (2 * total + 1) for _ in range(n)]

        # Base case for first number
        dp[0][nums[0] + total] += 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, n):
            for s in range(-total, total + 1):
                if dp[i - 1][s + total] > 0:
                    dp[i][s + nums[i] + total] += dp[i - 1][s + total]
                    dp[i][s - nums[i] + total] += dp[i - 1][s + total]

        return dp[n - 1][target + total] if -total <= target <= total else 0

    def find_target_sum_ways_space_opt(self, nums, target):
        total = sum(nums)
        if abs(target) > total:
            return 0

        dp = [0] * (2 * total + 1)
        dp[nums[0] + total] += 1
        dp[-nums[0] + total] += 1

        for i in range(1, len(nums)):
            next_dp = [0] * (2 * total + 1)
            for s in range(-total, total + 1):
                if dp[s + total] > 0:
                    next_dp[s + nums[i] + total] += dp[s + total]
                    next_dp[s - nums[i] + total] += dp[s + total]
            dp = next_dp

        return dp[target + total]
