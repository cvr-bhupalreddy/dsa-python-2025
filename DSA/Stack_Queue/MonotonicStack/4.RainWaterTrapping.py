def trap_brute(height):
    n = len(height)
    water = 0

    for i in range(n):
        leftMax = max(height[:i + 1])
        rightMax = max(height[i:])

        water += min(leftMax, rightMax) - height[i]

    return water


# precompute left_max and right_max

def trap_2(height):
    n = len(height)
    if n == 0: return 0

    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = height[0]
    for i in range(1, n):  # Prefix max
        leftMax[i] = max(leftMax[i - 1], height[i])

    rightMax[-1] = height[-1]
    for i in range(n - 2, -1, -1):  # Suffix max
        rightMax[i] = max(rightMax[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(leftMax[i], rightMax[i]) - height[i]

    return water


# Best is 2 pointers

# Move pointer on the smaller max side.
# Water depends on smaller of leftMax/rightMax.
# Update max or add trapped water.

def trap_2ptr(height):
    left, right = 0, len(height) - 1
    leftMax = rightMax = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1

    return water


# Using Monotonic Stack

# Steps
#     Traverse array left → right
#     Maintain a stack of bars in decreasing height
#     When height[i] > height[stack.top], pop:
#     The popped index is the bottom of a pit
#     Stack new top = left boundary
#     height[i] = right boundary

# Stack stores Indices , if we found element greater than top of stack then it means we found right boundary
# current array element = right , bottom = pop stack , left = current stack top  

def trap_stack(height):
    stack = []
    water = 0
    n = len(height)

    for i in range(n):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]
            width = i - left - 1
            depth = min(height[left], height[i]) - height[bottom]

            water += width * depth

        stack.append(i)

    return water


# | Approach        | Time   | Space  | Notes                                 |
# | --------------- | ------ | ------ | ------------------------------------- |
# | Brute           | O(n²)  | O(1)   | Easy but slow                         |
# | Better          | O(n)   | O(n)   | Prefix/suffix arrays                  |
# | Two Pointers    | O(n)   | O(1)   | Best in competitive coding            |
# | Monotonic Stack | O(n)   | O(n)   | Good for understanding stack patterns |
