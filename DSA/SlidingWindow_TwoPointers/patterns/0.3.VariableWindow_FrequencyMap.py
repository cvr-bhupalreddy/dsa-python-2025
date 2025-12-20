# ===========================================
# 3️⃣ VARIABLE SIZE – FREQUENCY MAP
# ===========================================
#
# 📌 Pattern:
# Maintain char/element counts in a hashmap.
# Shrink window until the condition becomes valid.
#
# 🔥 Popular Questions:
# 1. Longest substring without repeating characters  (LC 3)
# 2. Longest substring with K distinct characters
# 3. Longest substring with replacement (LC 424)
# 4. Minimum deletions to make freq valid (variation)
# 5. Longest prefix with 1 freq condition (advanced freq problems)
#
# 📌 Complexity:
# Time: O(n)
# Space: O(k)  (number of unique characters)
#
# 📌 Template Code:
def freq_window(s):
    left = 0
    seen = {}
    best = 0

    for right in range(len(s)):
        seen[s[right]] = seen.get(s[right], 0) + 1

        while seen[s[right]] > 1:   # violation: repeat char
            seen[s[left]] -= 1
            if seen[s[left]] == 0:
                del seen[s[left]]
            left += 1

        best = max(best, right - left + 1)

    return best


