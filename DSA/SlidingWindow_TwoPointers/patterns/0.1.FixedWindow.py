# ===========================================
# 1️⃣ FIXED SIZE SLIDING WINDOW
# ===========================================
#
# 📌 Pattern:
# Window size is fixed (k).
# Move the right pointer, and when window size > k, move left pointer.
#
# 📌 Used For:
# • Maximum sum of subarray of size k
# • First negative number in each window
# • Count occurrences in fixed window
# • Average of subarray of fixed size
#
# 🔥 Popular Questions:
# 1. Maximum sum subarray of size k
# 2. First negative number in every window of size k
# 3. Count distinct numbers in every window
# 4. Average of all subarrays of size k
# 5. Max/Min of subarray of fixed size (non-monotonic)

# 📌 Complexity:
# Time: O(n)
# Space: O(1)

# 📌 Template Code:

def fixed_window(arr, k):
    left = 0
    result = []
    window_sum = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        if right - left + 1 == k:
            result.append(window_sum)
            window_sum -= arr[left]
            left += 1

    return result


