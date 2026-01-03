class TrieNode:
    def __init__(self):
        # children[i] represents the next node for character (chr(ord('a') + i))
        self.children = [None] * 26

        # prefix_count = number of words passing through this node
        self.prefix_count = 0

        # end_count = number of words ending at this node
        self.end_count = 0


class Trie:
    def __init__(self):
        # Root node does not store any character
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')  # map char to index 0–25

            # Create node if path doesn't exist
            if node.children[idx] is None:
                node.children[idx] = TrieNode()

            # Move to child
            node = node.children[idx]

            # Increment prefix count for every traversal
            node.prefix_count += 1

        # Increment end_count to support duplicates
        node.end_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            # Word path does not exist
            if node.children[idx] is None:
                return 0

            node = node.children[idx]

        # end_count gives frequency of exact word
        return node.end_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')

            # Prefix path does not exist
            if node.children[idx] is None:
                return 0

            node = node.children[idx]

        # prefix_count gives number of words with this prefix
        return node.prefix_count

    def erase_no_cleanup(self, word: str) -> None:
        node = self.root
        path = []

        # Traverse and store nodes
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return  # word does not exist
            node = node.children[idx]
            path.append(node)

        # Remove one occurrence of word
        node.end_count -= 1

        # Decrease prefix_count along the path
        for n in path:
            n.prefix_count -= 1

    def erase(self, word: str) -> None:
        node = self.root
        stack = []

        # Traverse and save (parent, index)
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return
            stack.append((node, idx))
            node = node.children[idx]

        node.end_count -= 1

        # Cleanup unused nodes from bottom
        for parent, idx in reversed(stack):
            child = parent.children[idx]
            child.prefix_count -= 1

            # Delete node if unused
            if child.prefix_count == 0 and child.end_count == 0:
                parent.children[idx] = None
            else:
                break
