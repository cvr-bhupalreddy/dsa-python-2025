# 1. Same length
# 2. One-to-one character mapping (bijection)
# 3. Mapping is consistent throughout the string


# | Approach         | Time  | Space | Recommended |
# | ---------------- | ----- | ----- | ----------- |
# | Two maps         | O(n)  | O(n)  | ⭐⭐⭐         |
# | Pattern encoding | O(n)  | O(n)  | ⭐⭐⭐         |


# Convert each string to a pattern:
#     - First new character → 0
#     - Next new character → 1
#     - Repeat previous numbers for repeated chars
#
# If patterns match → isomorphic


def encode(s):
    mapping = {}
    res = []
    idx = 0

    for ch in s:
        if ch not in mapping:
            mapping[ch] = idx
            idx += 1
        res.append(mapping[ch])

    return res


def isIsomorphic(s, t):

    return encode(s) == encode(t)


# Maintain:
#     - map_s_to_t
#     - map_t_to_s
#
# For each position:
#     - If mapping exists → must match
#     - If mapping doesn't exist → create it
#     - Any conflict → NOT isomorphic


def isIsomorphic_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for cs, ct in zip(s, t):
        # Check s → t mapping
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            s_to_t[cs] = ct

        # Check t → s mapping
        if ct in t_to_s:
            if t_to_s[ct] != cs:
                return False
        else:
            t_to_s[ct] = cs

    return True
