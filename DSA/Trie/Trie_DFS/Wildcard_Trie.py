# 1. Store words in a Trie.
# 2. While searching:
#     - If character is normal → move to that child.
#     - If character is '.' → DFS into all children.
# 3. Word exists if any DFS path reaches a valid end node.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # -----------------------------------
    # Add Word (used by both problems)
    # -----------------------------------
    def addWord(self, word: str):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    # -----------------------------------
    # Wildcard Search (LC 211)
    # -----------------------------------
    def search(self, word: str) -> bool:
        """
        Searches a word in the trie.
        Supports '.' wildcard.
        """

        def dfs(index, node):
            # End of word
            if index == len(word):
                return node.is_end

            ch = word[index]

            # Normal character
            if ch != '.':
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

            # Wildcard case: try all children
            for child in node.children.values():
                if dfs(index + 1, child):
                    return True
            return False

        return dfs(0, self.root)

    # -----------------------------------
    # Auto Suggest / Top-K (LC 1268)
    # -----------------------------------
    def getSuggestions(self, prefix: str, k: int):
        """
        Returns top-k lexicographically smallest words
        starting with the given prefix.
        """
        node = self.root

        # Traverse prefix
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result = []

        def dfs(curr_node, path):
            if len(result) == k:
                return

            if curr_node.is_end:
                result.append(path)

            for ch in sorted(curr_node.children):
                dfs(curr_node.children[ch], path + ch)

        dfs(node, prefix)
        return result
