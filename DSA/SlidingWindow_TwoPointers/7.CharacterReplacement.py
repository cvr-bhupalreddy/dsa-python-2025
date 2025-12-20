# Longest substring where you can replace ≤ k characters to make all characters identical.


# Idea
#     Generate all substrings (i, j).
#     Count frequency of characters in that substring.
#     Let max_freq = highest occurring char count.
#     If (substring length - max_freq) ≤ k, it can be made uniform.
#     Track max length.


def characterReplacement_bruteforce(s: str, k: int) -> int:
    n = len(s)
    ans = 0

    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            length = j - i + 1
            max_freq = max(freq.values())

            if length - max_freq <= k:
                ans = max(ans, length)

    return ans


# ✅ 2. BETTER SOLUTION (O(26 * n)) — Fix target char A..Z
# ✔️ Idea
#
# For each possible target character 'A' → 'Z':
# Use sliding window.
# Count how many characters in window are not equal to target.
# If replacements needed exceed k, shrink window.
# This reduces logic but still tries 26 chars.

def characterReplacement_better(s: str, k: int) -> int:
    ans = 0
    n = len(s)

    for target in range(26):
        ch = chr(ord('A') + target)
        left = 0
        mismatch = 0

        for right in range(n):
            if s[right] != ch:
                mismatch += 1

            while mismatch > k:
                if s[left] != ch:
                    mismatch -= 1
                left += 1

            ans = max(ans, right - left + 1)

    return ans


# ✅ 3. OPTIMAL SOLUTION (O(n)) — Sliding Window + max_freq trick
# ✔️ Core Observation
# We maintain:
# A window
# Count of characters in window (freq map)
# max_freq (max occurrence of any character in wind


def characterReplacement(s: str, k: int) -> int:
    freq = {}
    left = 0
    max_freq = 0
    ans = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])

        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans


def characterReplacement1(s: str, k: int) -> int:
    freq = {}
    left = 0
    max_freq = 0
    ans = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])

        if (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans

# | Approach       | Idea                                 | Time              |
# | -------------- | ------------------------------------ | ----------------- |
# | **Bruteforce** | Try all substrings                   | **O(n²)**         |
# | **Better**     | Fix target char A–Z                  | **O(26n) ≈ O(n)** |
# | **Optimal**    | Sliding window with running max_freq | **O(n)**          |
