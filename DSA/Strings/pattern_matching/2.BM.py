# Core Idea:
# Match pattern from right to left and skip characters aggressively.
#
# Key Heuristics:
#     1. Bad Character Rule
#     2. Good Suffix Rule
#
# Steps:
#     - Start comparing from the end of the pattern
#     - On mismatch, shift pattern intelligently
#
# When to use:
#     - Large alphabet (ASCII/Unicode)
#     - Real-world text search (editors, grep)
#
# Time Complexity:
#     - Best / Average: O(n)
#     - Worst: O(n * m)
#
# Space Complexity:
#     - O(Alphabet size)


"""
========================================================
BOYER–MOORE STRING MATCHING (Bad Character Heuristic)
========================================================

CORE IDEA:
----------
Compare pattern from RIGHT to LEFT.
On mismatch, shift the pattern intelligently using
information about the mismatched character.

Why fast?
---------
Large jumps → fewer comparisons → sublinear on average.

Time Complexity:
----------------
Best / Average: O(n)
Worst-case:     O(n * m)  (rare, pathological cases)

Space Complexity:
-----------------
O(Σ) where Σ = alphabet size
"""


# -------------------------------------------------------
# STEP 1: BUILD BAD CHARACTER TABLE
# -------------------------------------------------------

def build_bad_char_table(pattern):
    """
    Stores the LAST index of each character in the pattern.

    Example:
    pattern = "ABCDABD"
    table = {
        'A': 4,
        'B': 5,
        'C': 2,
        'D': 6
    }
    """

    bad_char = {}

    for i, ch in enumerate(pattern):
        bad_char[ch] = i  # overwrite → keeps last occurrence

    return bad_char


# -------------------------------------------------------
# STEP 2: BOYER–MOORE SEARCH
# -------------------------------------------------------

def boyer_moore_search(text, pattern):
    """
    Returns all starting indices where pattern occurs in text
    """

    n = len(text)
    m = len(pattern)

    if m == 0:
        return []

    bad_char = build_bad_char_table(pattern)
    result = []

    shift = 0  # how much pattern is shifted relative to text

    while shift <= n - m:

        j = m - 1  # start comparing from RIGHTMOST character

        # Move left while characters match
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        # If j < 0 → full match
        if j < 0:
            result.append(shift)

            # Shift pattern to align next possible match
            if shift + m < n:
                shift += m - bad_char.get(text[shift + m], -1)
            else:
                shift += 1
        else:
            # Mismatch happened at pattern[j]
            bad_char_index = bad_char.get(text[shift + j], -1)

            # Calculate shift using bad character rule
            shift += max(1, j - bad_char_index)

    return result


# -------------------------------------------------------
# STEP 3: DEMO
# -------------------------------------------------------

if __name__ == "__main__":
    text = "ABAAABCD"
    pattern = "ABC"

    print("Text    :", text)
    print("Pattern :", pattern)

    matches = boyer_moore_search(text, pattern)
    print("Pattern found at indices:", matches)
