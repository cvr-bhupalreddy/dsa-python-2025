# 1. Observation:
#     - To minimize added characters, find the **longest palindromic prefix** of s.
#     - Only the **remaining suffix** needs to be reversed and added to the front.
#
# 2. Approach:
#
# KMP Trick:
# a. Let rev_s = reversed string of s
# b. Create combined string: s + "#" + rev_s
#     - '#' ensures no overlap
# c. Compute LPS (Longest Prefix Suffix) array for the combined string
# d. LPS[-1] = length of **longest palindrome prefix**
# e. Characters after this prefix → reverse and add to front
#
# 3. Result:
# - Shortest palindrome = reversed(remaining suffix) + s


def shortestPalindrome(s: str) -> str:
    if not s:
        return s

    rev_s = s[::-1]
    combined = s + "#" + rev_s

    # Step 1: Compute LPS array
    lps = [0] * len(combined)
    for i in range(1, len(combined)):
        length = lps[i - 1]
        while length > 0 and combined[i] != combined[length]:
            length = lps[length - 1]
        if combined[i] == combined[length]:
            length += 1
        lps[i] = length

    # Step 2: Longest palindromic prefix
    palin_prefix_len = lps[-1]

    # Step 3: Characters to add at front
    add = s[palin_prefix_len:][::-1]

    return add + s

# ✅ Example
s = "aacecaaa"
print(shortestPalindrome(s))  # Output: "aaacecaaa"
