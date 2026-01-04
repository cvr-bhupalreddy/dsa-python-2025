# 🔹 Core Techniques / Patterns
# 1️⃣ Frequency Map
#     - Count characters in both strings
#     - Compare counts
#     - O(n) time, O(26) or O(256) space for ASCII

def are_anagrams(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    # Count characters in s
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Subtract counts using t
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True


# 2️⃣ Sorting
#     - Sort both strings
#     - If sorted strings equal → anagram
#     - O(n log n) time, O(n) space

def are_anagrams_sorting(s, t):
    # If lengths differ, cannot be anagrams
    if len(s) != len(t):
        return False

    # Sort both strings
    return sorted(s) == sorted(t)


# 3️⃣ Sliding Window (For Substrings / Permutations)
#     - Keep frequency of current window
#     - Compare with pattern frequency
#     - Move window by 1
#     - O(n) time, O(26) space

def contains_anagram_map(pattern, text):
    """
    Check if 'text' contains a substring that is an anagram of 'pattern'
    using a frequency map (dictionary) instead of array.
    """

    n, m = len(text), len(pattern)
    if m > n:
        return False  # impossible if pattern is longer than text

    from collections import defaultdict

    # -----------------------------
    # Step 1: Build frequency map for pattern
    # -----------------------------
    freq_pattern = defaultdict(int)
    for ch in pattern:
        freq_pattern[ch] += 1

    # -----------------------------
    # Step 2: Initialize window frequency map for first window
    # -----------------------------
    freq_window = defaultdict(int)
    for ch in text[:m]:
        freq_window[ch] += 1

    # -----------------------------
    # Step 3: Check first window
    # -----------------------------
    if freq_window == freq_pattern:
        return True

    # -----------------------------
    # Step 4: Slide the window
    # -----------------------------
    for i in range(m, n):
        # Add next character (entering window)
        freq_window[text[i]] += 1

        # Remove leftmost character (exiting window)
        left_char = text[i - m]
        freq_window[left_char] -= 1
        if freq_window[left_char] == 0:
            # Remove key to keep dict comparison clean
            del freq_window[left_char]

        # Compare window freq with pattern freq
        if freq_window == freq_pattern:
            return True

    # -----------------------------
    # Step 5: No anagram found
    # -----------------------------
    return False
