# Each unique path in a suffix trie represents a unique substring
# 👉 Number of distinct substrings = total nodes in suffix trie
# (➕ 1 for the empty substring)
#
# ✅ Core Idea
#
#     Insert all suffixes of the string into a Trie
#     Every new node created corresponds to a new distinct substring
#     Count total nodes created
#     Add 1 for empty substring


class TrieNode:
    def __init__(self):
        # children[i] represents character (chr(ord('a') + i))
        self.children = [None] * 26


def countDistinctSubstrings(s: str) -> int:
    root = TrieNode()
    count = 0  # counts number of unique substrings (nodes)

    # Insert all suffixes
    for i in range(len(s)):
        node = root

        # Insert suffix starting at index i
        for j in range(i, len(s)):
            idx = ord(s[j]) - ord('a')

            # Create node only if not present
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
                count += 1  # new node = new distinct substring

            node = node.children[idx]

    # +1 for empty substring
    return count + 1
