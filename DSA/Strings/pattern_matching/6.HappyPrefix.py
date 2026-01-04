# 1. We need the longest prefix of s that is also a suffix (excluding the whole string).
# 2. This is exactly the information stored in the LPS array from KMP:
#     LPS[i] = length of the longest proper prefix of s[0..i]
#     which is also a suffix of s[0..i]
# 3. Compute LPS for the entire string s.
# 4. The value LPS[n-1] gives the length of the longest happy prefix.
# 5. Return s[0 : LPS[n-1]].


def longestHappyPrefix(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""

    # LPS[i] = length of longest proper prefix
    # which is also suffix for s[0..i]
    lps = [0] * n

    length = 0  # length of previous longest prefix-suffix
    i = 1

    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # fallback to shorter prefix
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    # LPS of last index gives longest happy prefix length
    return s[:lps[-1]]
