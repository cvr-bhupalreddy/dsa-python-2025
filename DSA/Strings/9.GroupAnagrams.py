# Group Anagrams
#
# Definition:
# Given an array of strings, group the strings that are anagrams of each other.
# Return the groups in any order.
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]


# Core Idea
#     Anagrams have the same characters with same frequency, only order differs.
#     If we can find a canonical representation of a string, all anagrams will have the same representation.
#     Use this representation as a key in a map to group strings.
#
# Canonical Representations:
#     Sorted string: "eat" → "aet"
#     Frequency tuple: counts of characters


from collections import defaultdict


def group_anagrams_better(strs):
    """
    Use sorted string as key in dictionary.
    Time: O(n * k log k), Space: O(n*k)
    """
    groups = defaultdict(list)  # key: sorted string, value: list of anagrams

    for s in strs:
        key = "".join(sorted(s))  # sort string → canonical form
        groups[key].append(s)  # add string to corresponding group

    return list(groups.values())  # return list of all groups


def group_anagrams_optimal(strs):
    """
    Use character frequency as key (tuple) → avoids sorting
    Time: O(n*k), Space: O(n*k)
    """
    groups = defaultdict(list)

    for s in strs:
        # Initialize frequency array for lowercase letters
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1  # increment frequency
        key = tuple(count)  # tuple can be used as dictionary key
        groups[key].append(s)  # add string to correct group

    return list(groups.values())


# | Approach | Key Idea                       | Complexity      |
# | -------- | ------------------------------ | --------------- |
# | Better   | Sort each string, use dict key | O(n * k log k)  |
# | Optimal  | Frequency tuple as dict key    | O(n * k)        |
