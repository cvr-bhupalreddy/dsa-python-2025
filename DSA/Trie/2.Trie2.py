# Why This Works
#
# prefix_count
#     Counts all words passing through
#     Used for startsWith
#
# end_count
#     Counts exact word occurrences
#     Used for equals
#
# erase
#     Decrements counts
#     Removes nodes when no longer needed


class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0  # number of words with this prefix
        self.end_count = 0  # number of words ending here


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.end_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.end_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root
        stack = []

        # Traverse and store path
        for ch in word:
            if ch not in node.children:
                return  # word doesn't exist
            stack.append((node, ch))
            node = node.children[ch]

        node.end_count -= 1

        # Decrease prefix_count and clean up nodes if needed
        for parent, ch in reversed(stack):
            child = parent.children[ch]
            child.prefix_count -= 1
            if child.prefix_count == 0 and child.end_count == 0:
                del parent.children[ch]
            else:
                break

    def erase_no_cleanup(self, word: str) -> None:
        node = self.root
        nodes = []

        # Traverse and store nodes
        for ch in word:
            if ch not in node.children:
                return  # word doesn't exist
            node = node.children[ch]
            nodes.append(node)

        # Reduce end count (remove one occurrence)
        node.end_count -= 1

        # Reduce prefix count along the path
        for n in nodes:
            n.prefix_count -= 1
