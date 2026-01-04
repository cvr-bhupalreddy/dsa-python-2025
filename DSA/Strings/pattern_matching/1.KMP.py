# these pattern matching algorithms are useful only when we need to find all positions where pattern appears in string

"""
========================================================
KMP (Knuth–Morris–Pratt) String Matching Algorithm
========================================================

CORE IDEA:
----------
Avoid re-checking characters in the text by using
information from previous matches.

Time Complexity:
----------------
LPS Construction: O(m)
Pattern Search:   O(n)
Total:            O(n + m)

Space Complexity:
-----------------
O(m) for LPS array

Where:
n = length of text
m = length of pattern
"""
# Core Idea:
# Avoid rechecking characters by using information from previous matches.
#
# Key Insight:
# If mismatch occurs, we already know some prefix = suffix.
# Use LPS (Longest Prefix Suffix) array.
#
# Steps:
# 1. Precompute LPS array for pattern
# 2. Traverse text and pattern simultaneously
# 3. On mismatch:
#     - Jump pattern index using LPS instead of restarting
#
# When to use:
#     - Single pattern search
#     - Large text
#     - Need guaranteed linear time
#
# Time Complexity:
#     - Preprocessing: O(m)
#     - Matching: O(n)
#     - Total: O(n + m)
#
# Space Complexity:
#     - O(m)


# -------------------------------------------------------
# STEP 1: BUILD LPS ARRAY
# -------------------------------------------------------

def build_lps(pattern):
    """
    LPS (Longest Prefix Suffix) Array

    lps[i] = length of the longest proper prefix of
             pattern[0..i] which is also a suffix

    Proper prefix ≠ whole string

    Example:
    pattern = "abab"
    lps     = [0, 0, 1, 2]
    """

    lps = [0] * len(pattern)

    # j = length of the previous longest prefix-suffix
    j = 0

    # Start from index 1 because lps[0] is always 0
    for i in range(1, len(pattern)):

        # If mismatch occurs:
        # fall back to previous longest prefix
        # index:   0 1 2 3 4 5 6
        # pattern: a b a b a c a
        # lps:     0 0 1 2 3 0 1
        # we need to fall back until we find a match or j =0

        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        # If characters match:
        # extend the current prefix
        if pattern[i] == pattern[j]:
            j += 1

        lps[i] = j

    return lps


# -------------------------------------------------------
# STEP 2: KMP SEARCH ALGORITHM
# -------------------------------------------------------

def kmp_search(text, pattern):
    """
    Finds all occurrences of pattern in text using KMP

    Returns:
    --------
    List of starting indices where pattern is found
    """

    # Edge case: empty pattern
    if not pattern:
        return []

    lps = build_lps(pattern)

    result = []

    # j = index for pattern
    j = 0

    # i = index for text
    for i in range(len(text)):

        # Mismatch after some matches:
        # fall back using lps same thing here also we need to fallback j to first matching  or J =0
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        # Match current characters
        if text[i] == pattern[j]:
            j += 1

        # Full pattern matched
        if j == len(pattern):
            # Match ends at i, so start index:
            result.append(i - j + 1)

            # Prepare j for next possible match
            j = lps[j - 1]

    return result


# -------------------------------------------------------
# STEP 3: DEMONSTRATION
# -------------------------------------------------------

if __name__ == "__main__":
    text = "ababcababcababc"
    pattern = "ababc"

    print("Text    :", text)
    print("Pattern :", pattern)

    print("\n--- LPS ARRAY ---")
    lps = build_lps(pattern)
    print("LPS:", lps)

    print("\n--- KMP SEARCH ---")
    matches = kmp_search(text, pattern)
    print("Pattern found at indices:", matches)
