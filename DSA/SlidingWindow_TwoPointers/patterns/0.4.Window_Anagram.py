# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all original
# letters exactly once.
#
# ✔️ Key Points
#     Same characters
#     Same frequency of each character
#     Just rearranged
#     Meaning may be different

# ===========================================
# 4️⃣ WINDOW WITH COUNTER MATCHING (ANAGRAM / PERMUTATION)
# ===========================================
#
# 📌 Pattern:
# Maintain frequency of pattern; use sliding window to check if window matches.
#
# 🔥 Popular Questions:
# 1. Find all anagrams in a string (LC 438)
# 2. Permutation in string (LC 567)
# 3. Minimum window substring (LC 76)
# 4. Smallest substring containing all characters of another string
# 5. Check if two strings are anagrams (window version)
#
# 📌 Complexity:
# Time: O(n)
# Space: O(k)  (distinct characters)
#
# 📌 Template Code:
def find_anagrams(s, p):
    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1

    have = {}
    left = 0
    result = []
    match = 0

    for right in range(len(s)):
        ch = s[right]
        have[ch] = have.get(ch, 0) + 1

        if ch in need and have[ch] == need[ch]:
            match += 1

        while (right - left + 1) > len(p):
            left_ch = s[left]
            if left_ch in need and have[left_ch] == need[left_ch]:
                match -= 1
            have[left_ch] -= 1
            left += 1

        if match == len(need):
            result.append(left)

    return result


