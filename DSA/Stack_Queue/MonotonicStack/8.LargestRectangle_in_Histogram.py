# 🟦 Problem Statement (Copy-Ready)
#
# Given an array heights[] representing the heights of bars in a histogram (each bar has width 1),
# find the area of the largest rectangle that can be formed inside the histogram.
#
# You may choose any number of consecutive bars.
# Return the maximum rectangle area.


# Idea: Bruteforce
#
# For every bar, expand to the left and right while the bars are ≥ current height.
# Current bar height is the limiting height of the rectangle.

def largest_rectangle_bruteforce(heights):
    n = len(heights)
    max_area = 0

    for i in range(n):
        min_height = heights[i]

        # Expand to the left
        left = i
        while left >= 0 and heights[left] >= heights[i]:
            left -= 1

        # Expand to the right
        right = i
        while right < n and heights[right] >= heights[i]:
            right += 1

        width = right - left - 1
        max_area = max(max_area, heights[i] * width)

    return max_area


# Better Approach — Next Smaller Left & Right
#
# Idea:
# For each bar:
# Find the index of the Next Smaller Element (NSE) on the left
# Find the index of the Next Smaller Element (NSE) on the right

# width = right_smaller[i] - left_smaller[i] - 1
# area  = heights[i] * width


def largest_rectangle_better(heights):
    n = len(heights)
    left = [-1] * n
    right = [n] * n
    stack = []

    # Next Smaller on Left
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    # Next Smaller on Right
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    max_area = 0
    for i in range(n):
        width = right[i] - left[i] - 1
        max_area = max(max_area, heights[i] * width)

    return max_area


# 🟩 Optimal Approach — Monotonic Increasing Stack
#
# Core Idea:
#
# Use a monotonic increasing stack that stores indices of bars.
#
# When we see a bar shorter than the stack top,
# that means the rectangle using the stack-top height ends here.
#
# Algorithm:
#
# Traverse all bars, push index while heights are increasing.
#
# When a shorter bar is found:
#     Pop from stack → this height is the limiting height
#     Right boundary = current index
#     Left boundary = new stack top
#
# Compute area:
#
# height = heights[top]
# width = i - stack[-1] - 1   (if stack not empty)
# width = i                   (if stack empty)


def largest_rectangle_optimal(heights):
    stack = []  # stores indices of increasing bars
    max_area = 0
    n = len(heights)

    for i in range(n + 1):  # this is going to still one extra element with height 0 , it will handle next small element
        curr_height = heights[i] if i < n else 0  # sentinel

        while stack and curr_height < heights[stack[-1]]:
            top = stack.pop()
            height = heights[top]

            # Determine width
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i  # no previous smaller → extend to the beginning 

            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area
