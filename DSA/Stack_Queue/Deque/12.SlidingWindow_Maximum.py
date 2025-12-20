# 🟦 Sliding Window Maximum Problem
#
# Given an array arr and window size k, return the maximum of each window of size k.


def max_sliding_window_bruteforce(arr, k):
    n = len(arr)
    result = []
    for i in range(n - k + 1):
        result.append(max(arr[i:i + k]))
    return result

#
# 🟩 3. Optimal — Deque (Monotonic Queue) (O(N)) → BEST APPROACH
# ⭐ Key Idea (Very Important)
#
# Maintain a deque (double-ended queue) that stores indices in decreasing order of their values.
#
# For each index i:
#     Remove smaller elements from back
#
#     Remove elements out of window
#     (front index < i - k + 1)
#     Add current element index at back
#     Front of deque = max of window


from collections import deque

def max_sliding_window(arr, k):
    dq = deque()  # stores indices
    result = []

    for i in range(len(arr)):

        # Remove elements out of this window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller values from the back
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # Window starts at i >= k-1
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result
