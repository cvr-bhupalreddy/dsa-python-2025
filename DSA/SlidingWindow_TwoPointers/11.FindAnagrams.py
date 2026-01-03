# Problem
# Given:
#     s = text string
#     p = pattern
#     Find all starting indices in s where an anagram of p begins.
#
# Core Idea
# Anagrams ⇒ same character frequencies
# Maintain a fixed-size sliding window of length len(p)
#
# Track:
#     frequency of characters in p
#     frequency of current window in s
# When both frequencies match → anagram found


def findAnagrams(s: str, p: str):
    if len(p) > len(s):
        return []

    result = []
    p_count = {}
    window = {}

    # build frequency map for p
    for ch in p:
        p_count[ch] = p_count.get(ch, 0) + 1

    left = 0
    for right in range(len(s)):
        # add current char to window
        window[s[right]] = window.get(s[right], 0) + 1

        # shrink window if size exceeds p
        if right - left + 1 > len(p):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # check anagram
        if right - left + 1 == len(p) and window == p_count:
            result.append(left)

    return result
