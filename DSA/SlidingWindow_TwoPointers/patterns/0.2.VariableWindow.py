# ===========================================
# 2️⃣ VARIABLE SIZE – CONDITION BASED
# ===========================================
#
# 📌 Pattern:
# Increase right pointer; shrink left pointer until a condition becomes valid
# (sum ≤ K, product < K, distinct ≤ K, etc.)
#
# 🔥 Popular Questions:
# 1. Longest subarray with sum ≤ K
# 2. Longest subarray with sum exactly K (positive numbers)
# 3. Subarray product < K  (LeetCode 713)
# 4. Smallest subarray with sum ≥ K
# 5. Longest substring with ≤ K distinct characters

# 📌 Complexity:
# Time: O(n)
# Space: O(1)
#
# 📌 Template Code:
def variable_window(arr, K):
    left = 0
    current = 0
    best = 0

    for right in range(len(arr)):
        current += arr[right]

        while current > K:
            current -= arr[left]
            left += 1

        best = max(best, right - left + 1)

    return best


def variable_window_while(arr, K):
    n = len(arr)
    left = 0
    right = 0
    current = 0
    best = 0

    while right < n:
        current += arr[right]

        # Shrink window if current sum exceeds K
        while current > K and left <= right:
            current -= arr[left]
            left += 1

        # Update best length
        best = max(best, right - left + 1)

        right += 1

    return best


# Only optimal length solutions it's applicable
def variable_window_while_optimal(arr, K):
    n = len(arr)
    left = 0
    right = 0
    current = 0
    best = 0

    while right < n:
        current += arr[right]

        # Shrink window if current sum exceeds K
        if current > K:
            current -= arr[left]
            left += 1

        # Update best length
        best = max(best, right - left + 1)

        right += 1

    return best
