# ===========================================
# 5️⃣ MINIMUM / MAXIMUM WINDOW PROBLEMS
# ===========================================
#
# 📌 Pattern:
# Use a hashmap to track needed characters.
# Expand right; once all chars are found, shrink from left.
#
# 🔥 Popular Questions:
# 1. Minimum Window Substring (LC 76)
# 2. Smallest substring containing all characters of set T
# 3. Smallest subarray with sum ≥ K
# 4. Shortest substring with all unique characters
# 5. Window problems involving “minimum length” or “shortest range”
#
#
# 📌 Complexity:
# Time: O(n)
# Space: O(k)
#
#
# 📌 Template Code:
def min_window(s, t):
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    have = {}
    required = len(need)
    formed = 0
    left = 0
    best = (float("inf"), 0, 0)

    for right in range(len(s)):
        ch = s[right]
        have[ch] = have.get(ch, 0) + 1

        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)

            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1

    if best[0] == float("inf"):
        return ""
    return s[best[1]:best[2] + 1]
