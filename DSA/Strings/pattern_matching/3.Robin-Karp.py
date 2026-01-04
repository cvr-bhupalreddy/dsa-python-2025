# Core Idea:
# Use hashing to compare substrings instead of characters.
#
# Key Insight:
# If hash(pattern) == hash(substring), then check characters.
#
# Steps:
#     1. Compute hash of pattern
#     2. Compute rolling hash of text window
#     3. Slide window and update hash in O(1)
#
# When to use:
#     - Multiple pattern search
#     - Plagiarism detection
#     - Average-case fast matching
#
# Time Complexity:
#     - Average: O(n + m)
#     - Worst (hash collision): O(n * m)
#
# Space Complexity:
#     - O(1)


# | Name     | Meaning                        |
# | -------- | ------------------------------ |
# | `B`      | Base (alphabet size, e.g. 256) |
# | `MOD`    | Large prime (e.g. 1e9+7)       |
# | `m`      | Window / pattern length        |
# | `H`      | Current rolling hash           |
# | `power`  | B^(m−1) % MOD                  |
# | `val(c)` | Numeric value of character     |

# H ← 0
# FOR i FROM 0 TO m-1:
# H ← (H × B + val(text[i])) % MOD


# REMOVE left_char:
#     H ← H - val(text[i]) × power
#     H ← H % MOD
#
# SHIFT window:
#     H ← H × B
#     H ← H % MOD
#
# ADD right_char:
#     H ← H + val(text[i+m])
#     H ← H % MOD
#
# ENSURE positivity:
#     IF H < 0:
#     H ← H + MOD


"""
========================================================
RABIN–KARP STRING MATCHING ALGORITHM
========================================================

CORE IDEA:
----------
Use a rolling hash to compare substrings in O(1) time.
Only when hash matches → do character-by-character check.

Why fast?
---------
Avoids repeated substring comparisons.

Time Complexity:
----------------
Average / Expected: O(n + m)
Worst-case:         O(n * m)   (many hash collisions)

Space Complexity:
-----------------
O(1) extra space
"""


# -------------------------------------------------------
# STEP 1: RABIN–KARP SEARCH
# -------------------------------------------------------

def rabin_karp(text, pattern):
    """
    Returns all starting indices where pattern occurs in text
    """

    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return []

    # Base for rolling hash (alphabet size)
    base = 256

    # Large prime modulus to reduce collisions
    mod = 10 ** 9 + 7

    # Hash values
    pattern_hash = 0
    window_hash = 0

    # base^(m-1) % mod → used to remove leftmost char
    highest_base = 1
    for _ in range(m - 1):
        highest_base = (highest_base * base) % mod

    # ((c0 * base + c1) * base + c2) * base + ... this is computed like this

    # ---------------------------------------------------
    # INITIAL HASH COMPUTATION
    # ---------------------------------------------------
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod

    result = []

    # ---------------------------------------------------
    # SLIDE THE WINDOW
    # ---------------------------------------------------
    for i in range(n - m + 1):

        # If hash matches → verify characters
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                result.append(i)

        # Compute hash of next window
        if i < n - m:
            # Remove leftmost character
            window_hash = (window_hash - ord(text[i]) * highest_base) % mod

            # Shift left (multiply by base)
            window_hash = (window_hash * base) % mod

            # Add next character
            window_hash = (window_hash + ord(text[i + m])) % mod

            # Ensure positive hash
            window_hash = (window_hash + mod) % mod

    return result


# -------------------------------------------------------
# STEP 2: DEMO
# -------------------------------------------------------

if __name__ == "__main__":
    text = "abracadabra"
    pattern = "abra"

    print("Text    :", text)
    print("Pattern :", pattern)

    matches = rabin_karp(text, pattern)
    print("Pattern found at indices:", matches)
