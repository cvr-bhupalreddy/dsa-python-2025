# ✅ Core Idea
#
# Because product of negatives can become positive, we need to track both maximum and minimum products at each index.
#
# At each element nums[i]:
#     max_prod[i] = max(nums[i], nums[i]*prev_max, nums[i]*prev_min)
#     min_prod[i] = min(nums[i], nums[i]*prev_max, nums[i]*prev_min)
#
# The answer is the maximum of all max_prod[i].

#
# | Approach         | Idea                                         | Time  | Space            |
# | ---------------- | -------------------------------------------- | ----- | ---------------- |
# | Brute Force      | Check product of all subarrays               | O(n²) | O(1)             |
# | DP / Kadane-like | Track `max_prod` and `min_prod` at each step | O(n)  | O(1) (optimized) |

# ✅ Reason for max(num, num*max_prod, num*min_prod)
#
# At index i (element num = nums[i]), the maximum product subarray ending at i can be one of three things:
#
# Start a new subarray at num
#
# Sometimes the previous product is negative or zero, so starting fresh is better.
# Extend previous max product subarray (num * max_prod)
#
# If num is positive, extending previous max product gives a bigger product.
# Extend previous min product subarray (num * min_prod)
#
# If num is negative, multiplying it with previous min product can become maximum


def maxProduct(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        # When num is negative, swap max and min
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, num * max_prod)
        min_prod = min(num, num * min_prod)

        result = max(result, max_prod)

    return result


class Solution:
    # Function to find the product of elements in maximum product subarray
    def maxProduct_prefix_suffix(self, nums):
        n = len(nums)

        ans = float('-inf')  # to store the answer

        # Indices to store the prefix and suffix multiplication
        prefix, suffix = 1, 1

        # Iterate on the elements of the given array
        for i in range(n):

            # Resetting the prefix and suffix multiplication if they turn out to be zero
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            # update the prefix and suffix multiplication
            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            # store the maximum as the answer
            ans = max(ans, max(prefix, suffix))

        # return the result
        return ans


# Example usage
nums = [4, 5, 3, 7, 1, 2]
sol = Solution()
ans = sol.maxProduct(nums)
print("The product of elements in maximum product subarray is:", ans)
