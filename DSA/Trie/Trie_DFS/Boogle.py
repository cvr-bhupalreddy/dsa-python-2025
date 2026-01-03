# 1. Insert all words into a Trie.
# 2. For each cell in the board:
#     - Start DFS traversal.
# 3. While doing DFS:
#     - Check if current character exists in Trie.
#     - If not → prune search immediately.
# 4. If Trie node marks end of word:
#     - Add word to result.
# 5. Mark visited cells to avoid reuse.
# 6. Use Trie pruning to avoid useless DFS paths.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores complete word at terminal node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word


class Solution:
    def boggle(self, board, words):
        """
        Finds all dictionary words in a Boggle board.
        """
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        result = set()

        # 8 possible directions (including diagonals)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        def dfs(r, c, node):
            char = board[r][c]

            # Prune if character not in Trie
            if char not in node.children:
                return

            next_node = node.children[char]

            # Found complete word
            if next_node.word:
                result.add(next_node.word)
                next_node.word = None  # avoid duplicates

            visited[r][c] = True

            # Explore all 8 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    dfs(nr, nc, next_node)

            visited[r][c] = False  # backtrack

            # Trie pruning
            if not next_node.children:
                node.children.pop(char)

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return list(result)

# 🌳 What is Trie Pruning?
# Trie pruning = deleting useless trie nodes once they are no longer needed
#
# In DFS-based word search:
#     Once a word is found
#     And no other words depend on that prefix
#     👉 We remove that path from the Trie
#
# This prevents future DFS calls from exploring dead paths.


# node       → parent TrieNode
# char       → current character
# next_node  → child TrieNode (node.children[char])
# if not next_node.children
#     ✔ Means:
#         next_node has no further branches
#         No other words start with this prefix
# ✔ Remove this character edge from the trie
