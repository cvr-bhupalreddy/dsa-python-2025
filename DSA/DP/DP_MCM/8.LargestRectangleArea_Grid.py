# ✅ Idea to Solve
#
# This problem reduces to:
#
# For each row, treat it as the base of a histogram.
# Then compute the largest rectangle in histogram.


# 1️⃣ Build histogram heights
#
# For each cell:
#
# if grid[i][j] == 1:
#     height[j] += 1
# else:
#     height[j] = 0

#
# 2️⃣ For each row, compute largest rectangle using Monotonic Stack
#
# Histogram the largest rectangle recurrence:
#
# For each bar i:
# Expand left until height decreases
# Expand right until height decreases
# area = height[i] * width
# Take max of all


# We maintain a stack of indices where heights are in non-decreasing order.
# When the current height is smaller than the height at the stack top,
# the bar at the top cannot extend further to the right, so we pop it and
# compute the largest rectangle where that popped bar is the minimum height.
#
# Left boundary = index after the new stack top
# Right boundary = current index i
# Width = right - left - 1
# Area = height * width
#
# Process all bars and one extra bar of height 0 to flush remaining bars.

# function largestRectangleArea(heights):
# n = length(heights)
# stack = empty stack          // will store indices of bars
# maxArea = 0
#
# for i from 0 to n:           // run until n (extra virtual bar)
#
# // while current bar breaks increasing order
# while stack is not empty AND
#   (i == n OR heights[i] < heights[stack.top()]):
#
#       // height of the rectangle is the popped bar
#       height = heights[stack.pop()]
#
#       // find left boundary
#       if stack is empty:
#           left = -1
#       else:
#           left = stack.top()
#
#       // right boundary is i
#       width = i - left - 1
#
#       // compute area
#       area = height * width
#       maxArea = max(maxArea, area)
#
#       // push the current index
#   stack.push(i)
#
# return maxArea


# -------------------------------------------------------
# Largest Rectangle in Histogram (monotonic stack)
# -------------------------------------------------------
def largest_histogram_area(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        # Process while current bar is smaller than stack top
        while stack and (i == n or heights[i] < heights[stack[-1]]):
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area


# -------------------------------------------------------
# Maximum Rectangle of 1s in a Binary Matrix
# -------------------------------------------------------
def max_rectangle(grid):
    if not grid:
        return 0

    R = len(grid)
    C = len(grid[0])
    heights = [0] * C
    max_area = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                heights[c] += 1
            else:
                heights[c] = 0

        # Compute the largest rectangle for histogram of this row
        max_area = max(max_area, largest_histogram_area(heights))

    return max_area
