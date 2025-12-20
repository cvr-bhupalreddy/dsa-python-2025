# ✅ 1. Problem Statement
#
#     For every element in an array, find the next element on the right side that is greater.
#     If none exists → return -1.


def next_greater_bruteforce(arr):
    n = len(arr)
    res = [-1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res


# ✅ 3. Better Approach – Using Stack (Left → Right) (O(n))
#
# This avoids scanning repeatedly.
# ✔ Algorithm
#
# Traverse from left to right
# Keep stack of indices whose NGE is not found yet
# For each element:
#
#     While stack top element < current → NGE found → pop and fill
#     Push current index


def next_greater_better(arr):
    n = len(arr)
    res = [-1] * n
    stack = []  # indices

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = arr[i]
        stack.append(i)

    return res


# ✔ Core Idea
#
# Use a monotonically decreasing stack (top is the smallest).
#
# For each element arr[i] from right:
#     Pop while stack top ≤ current element
#     (they can’t be NGE for any earlier element)
#     If stack is empty → answer = -1
#     Else → stack top is next greater
#     Push current element onto stack

def next_greater_optimal(arr):
    n = len(arr)
    res = [-1] * n
    stack = []  # holds elements in decreasing order

    for i in range(n - 1, -1, -1):  # traverse right → left
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])

    return res

# | Approach                                 | Time  | Space | Notes                |
# | ---------------------------------------- | ----- | ----- | -------------------- |
# | **Brute Force**                          | O(n²) | O(1)  | Slow for large input |
# | **Better (Left→Right Stack)**            | O(n)  | O(n)  | Good                 |
# | **Optimal (Right→Left Monotonic Stack)** | O(n)  | O(n)  | Cleanest & fastest   |
