# Problem: Palindromic Anagram
#
# Definition:
# Given a string s, determine if the letters of s can be rearranged to form a palindrome.

# Observation / Core Idea:
# A string can form a palindrome iff:
#     All characters have even counts, OR
#     All characters except one have even counts (the odd-count char goes in the middle)
# This is because in a palindrome, characters mirror each other around the center.


from collections import defaultdict


def can_form_palindrome_better(s):
    """
    Determine if string s can be rearranged to form a palindrome
    Using frequency map (dictionary)
    """
    freq = defaultdict(int)

    # Count frequency of each character
    for ch in s:
        freq[ch] += 1

    # Count characters with odd frequency
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)

    # Palindrome possible if at most 1 odd frequency
    return odd_count <= 1

# Optimal Approach: Using Bitmask (for lowercase letters)
# Logic:
#     Only lowercase letters a-z.
#     Keep a bitmask of 26 bits.
#     Flip the bit for each character in string.
#
# At the end:
#     If at most 1 bit is set → palindrome possible
#     This represents at most 1 character with odd count


def can_form_palindrome_optimal(s):
    """
    Determine if string s can be rearranged to form a palindrome
    Using bitmask for lowercase letters
    """
    bitmask = 0

    for ch in s:
        # Compute bit index: 0 for 'a', 1 for 'b', ..., 25 for 'z'
        idx = ord(ch) - ord('a')
        # Flip the bit
        bitmask ^= (1 << idx)

    # Check if at most 1 bit is set
    return bitmask == 0 or (bitmask & (bitmask - 1)) == 0

# Bitmask setting is used XOR logic
#
# s = "aabbc"
# Initial bitmask = 00000000
#
# Process 'a' (idx=0):
# bitmask ^= 1 << 0 → 00000001
#
# Process 'a' again:
# bitmask ^= 1 << 0 → 00000000  # even count → bit reset
#
# Process 'b' (idx=1):
# bitmask ^= 1 << 1 → 00000010
#
# Process 'b' again:
# bitmask ^= 1 << 1 → 00000000
#
# Process 'c' (idx=2):
# bitmask ^= 1 << 2 → 00000100
# Final bitmask = 00000100 → only c has odd count.


# Explanation:
#
# bitmask == 0 → all counts are even → palindrome possible.
# bitmask & (bitmask - 1) == 0 → checks if exactly one bit is set
#
# Why bitmask & (bitmask - 1) works
#
#     Property:
#     For any number x that is a power of 2 (only 1 bit set), x-1 flips all lower bits.
#     x & (x-1) → becomes 0

# | Approach | Key Idea                           | Time Complexity | Space Complexity |
# | -------- | ---------------------------------- | --------------- | ---------------- |
# | Better   | Count frequency → check odd counts | O(n)            | O(k)             |
# | Optimal  | Bitmask → flip bit per char        | O(n)            | O(1)             |
