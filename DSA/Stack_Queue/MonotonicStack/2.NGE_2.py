def nextGreaterElements_bruteforce(nums):
    n = len(nums)
    res = [-1] * n

    for i in range(n):
        for j in range(1, n):            # look at next n-1 positions
            next_index = (i + j) % n     # wrap around (circular)
            if nums[next_index] > nums[i]:
                res[i] = nums[next_index]
                break                    # stop at first greater element

    return res


def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # stores values (monotonic decreasing)

    for i in range(2 * n - 1, -1, -1):  # traverse twice
        curr = nums[i % n]

        # maintain decreasing stack
        while stack and stack[-1] <= curr:
            stack.pop()

        # fill answer only during first pass (i < n)
        if i < n:
            res[i] = stack[-1] if stack else -1

        stack.append(curr)

    return res
