# Fix a starting index i from 0 to n-1
# For each start, extend the subarray to all end indices j >= i
# Print nums[i:j+1]


def subarrays(nums):
    n = len(nums)
    result = []

    for i in range(n):           # start index
        for j in range(i, n):    # end index
            result.append(nums[i:j+1])

    return result


# Recursive Approach :
# If start > end → move start to next index
# If end < n:
# record subarray start..end
# recurse with end+1
# Else:
# recurse with start+1 and end = start


def subarrays_recursive(nums):
    result = []
    n = len(nums)

    def dfs(start, end):
        if start == n:
            return
        if end == n:
            dfs(start + 1, start + 1)
            return

        result.append(nums[start:end+1])
        dfs(start, end + 1)

    dfs(0, 0)
    return result



