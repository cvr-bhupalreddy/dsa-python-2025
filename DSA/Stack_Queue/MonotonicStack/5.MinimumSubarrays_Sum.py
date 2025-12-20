# Identify PSE Index and NSE Index
# Number of Subarrays A[i] is small element = (i - PSE Index) *(NSE Index - i)
# no PSE index then -1
# no NSE Index then N
# Total Contribution = [(i - PSE Index) * (NSE Index - i)]*A[i]

# ✅ Sum of All Subarray Minimums – Explanation + Code
# 🔥 Goal
#
# For an array arr, consider every possible subarray and compute its minimum element.
# Return the sum of all these minimums.


# ✅ Core Idea (Monotonic Increasing Stack)
#
# Each element arr[i] is the minimum for some subarrays.
# We find:
#
# How many subarrays it is minimum from the left
# How many subarrays it is minimum to the right
#
# Let:
#     left[i] = number of greater elements to the left (strictly >)
#     right[i] = number of greater-or-equal elements to the right (>=)
#
# Contribution formula:
# Contribution of arr[i] = arr[i] * left[i] * right[i]


def sum_subarray_mins_bruteforce(arr):
    total = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            mn = float('inf')
            for k in range(i, j + 1):
                mn = min(mn, arr[k])
            total += mn
    return total


def sum_subarray_mins_dp(arr):
    total = 0
    n = len(arr)
    for i in range(n):
        mn = float('inf')
        for j in range(i, n):
            mn = min(mn, arr[j])
            total += mn
    return total


def sum_subarray_mins(arr):
    MOD = 10 ** 9 + 7
    n = len(arr)

    left = [0] * n
    right = [0] * n

    stack = []
    # Count strictly greater elements on the left
    for i in range(n):
        count = 1
        while stack and stack[-1][0] > arr[i]:
            count += stack.pop()[1]
        stack.append((arr[i], count))
        left[i] = count

    stack.clear()

    # Count greater or equal elements on the right
    for i in range(n - 1, -1, -1):
        count = 1
        while stack and stack[-1][0] >= arr[i]:
            count += stack.pop()[1]
        stack.append((arr[i], count))
        right[i] = count

    # Compute total contribution
    ans = 0
    for i in range(n):
        ans = (ans + arr[i] * left[i] * right[i]) % MOD

    return ans

# +----------------------------------------------------------------------------------+
# |                           SUM OF SUBARRAY MINIMUMS — SUMMARY TABLE               |
# +-------------------------------+---------------------------+----------------------+
# |           APPROACH            |      TIME COMPLEXITY      |   SPACE COMPLEXITY   |
# +-------------------------------+---------------------------+----------------------+
# | 1) Brute Force                |          O(n³)             |         O(1)        |
# |    (Enumerate all subarrays   |                           |                      |
# |     and scan minimum)         |                           |                      |
# +-------------------------------+---------------------------+----------------------+
# | 2) Improved DP /              |          O(n²)             |         O(1)        |
# |    Running Minimum            |                           |                      |
# |    (Reuse previous minimum    |                           |                      |
# |     while expanding window)   |                           |                      |
# +-------------------------------+---------------------------+----------------------+
# | 3) Monotonic Stack            |           O(n)             |         O(n)        |
# |    (Prev/Next smaller element |                           |                      |
# |     contribution method)      |                           |                      |
# +-------------------------------+---------------------------+-----------------------+
