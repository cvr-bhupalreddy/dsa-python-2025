# This is a classic Trie + prefix validation problem (often called Longest Complete String).
#
# We must:
#     Ensure every prefix of a word exists in the array
#     Pick the longest such word
#     If tie → lexicographically smallest
#     If none → "None"
#
# Key Insight
#
# A word is complete if while traversing it in a Trie:
# Every node on the path must mark the end of a word
#
# So:
#     Build a Trie
#     Insert all words
#     For each word, check if all prefixes are valid
#     Track best answer


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    # Check if every prefix of word exists
    def is_complete(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            node = node.children[idx]
            # Prefix must end as a word
            if node is None or not node.is_end:
                return False
        return True


def longestCompleteString(nums):
    trie = Trie()

    # Insert all words
    for word in nums:
        trie.insert(word)

    ans = ""

    # Check each word
    for word in nums:
        if trie.is_complete(word):
            if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                ans = word

    return ans if ans else "None"
