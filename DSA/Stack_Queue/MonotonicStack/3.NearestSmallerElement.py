# ✅ Nearest Smaller Element (NSE)
#
# For each element arr[i], find the nearest element to its left that is strictly smaller.

def nearestSmaller_better(arr):
    n = len(arr)
    res = []

    for i in range(n):
        j = i - 1
        while j >= 0 and arr[j] >= arr[i]:
            j -= 1
        res.append(arr[j] if j >= 0 else -1)

    return res

# ✅ 2) Optimal — Monotonic Increasing Stack (O(n))
# 🔥 Core Idea (IMPORTANT)
#
# Use a stack that keeps increasing elements
#
# For each arr[i]:
#     Pop until top of stack < arr[i] (i.e., valid smaller)
#     If stack empty → no smaller → answer = -1
#     Else → top of stack is nearest smaller
#     Push arr[i] onto stack


def nearestSmaller_optimal(arr):
    stack = []
    res = []

    for num in arr:
        # Pop all bigger or equal elements
        while stack and stack[-1] >= num:
            stack.pop()

        # Top is nearest smaller
        res.append(stack[-1] if stack else -1)

        # Push current element
        stack.append(num)

    return res
