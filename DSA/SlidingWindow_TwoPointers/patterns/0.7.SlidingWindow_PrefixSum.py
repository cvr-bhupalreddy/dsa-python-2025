# ===========================================
# 7️⃣ SLIDING WINDOW WITH PREFIX SUMS
# ===========================================
#
# 📌 Pattern:
# Use prefix sums to compute window sums in O(1) time.
#
# 🔥 Popular Questions:
# 1. Number of sub arrays with sum = K (LC 560)
# 2. Longest subarray with sum K
# 3. Subarray sum divisible by K (LC 974)
# 4. Count sub arrays with even/odd sum
# 5. Subarray sum equals zero
#
#
# 📌 Complexity:
# Time: O(n)
# Space: O(n)
#
# 📌 Template Code:
def prefix_window(arr):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)

    # sum of window l..r:
    # prefix[r+1] - prefix[l]

    return prefix

