# ===========================================
# 6️⃣ SLIDING WINDOW WITH MONOTONIC QUEUES
# ===========================================
#
# 📌 Pattern:
# Use deque to maintain max/min in O(1).
#
# 🔥 Popular Questions:
# 1. Sliding Window Maximum (LC 239)
# 2. Sliding Window Minimum
# 3. Longest continuous subarray with max-min ≤ limit (LC 1438)
# 4. Find max for each window in streaming data
# 5. Problems requiring max/min in every window
#
# 📌 Complexity:
# Time: O(n)
# Space: O(k)
#
#
# 📌 Template Code:
from collections import deque


def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for right in range(len(nums)):
        while dq and nums[dq[-1]] <= nums[right]:
            dq.pop()
        dq.append(right)

        if dq[0] == right - k:
            dq.popleft()

        if right >= k - 1:
            result.append(nums[dq[0]])

    return result
