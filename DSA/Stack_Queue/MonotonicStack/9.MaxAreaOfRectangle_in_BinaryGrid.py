# Core Idea
#
# Treat each row of the matrix as a histogram of heights:
# heights[j] = number of consecutive 1s in column j ending at current row.
#
# For row 0: heights[j] = matrix[0][j]
#
# For row i:
# heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
#
#
# For each row, use the Largest Rectangle in Histogram algorithm to compute max rectangle area in that row histogram.
#
# Keep track of the maximum area across all rows.


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    n = len(heights)
    for i in range(n + 1):
        curr_height = heights[i] if i < n else 0
        while stack and curr_height < heights[stack[-1]]:
            top = stack.pop()
            height = heights[top]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


def maximalRectangle(matrix):
    if not matrix:
        return 0

    n, m = len(matrix), len(matrix[0])
    heights = [0] * m
    max_area = 0

    for i in range(n):
        for j in range(m):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
        max_area = max(max_area, largestRectangleArea(heights))

    return max_area
