# You are given:
#     A 2D grid of characters
#     A list of dictionary words
#
# Goal:
#     Find all words that can be formed by:
#     Moving up / down / left / right (sometimes diagonals in Boggle)
#     Using each cell at most once per word


# Optimized approach ✅
#     Insert all words into a Trie
#     Do DFS once per cell
#     Prune search early when prefix is invalid


# Core Data Structure: Trie
# Each Trie node stores:
#     children → next characters
#     is_end → word completion
#     (Optional) word → store full word at end node


# High-Level Algorithm
# Step 1: Build Trie
# Insert all dictionary words into a Trie
#
# Step 2: DFS from each grid cell
#     Start DFS from every cell (i, j)
#     Move in 4 (or 8) directions
#     Track visited cells
#
# Step 3: Trie-based pruning
# At every DFS step:
#     If current character not in Trie children → STOP
#     If is_end == True → word found


# Trie Pruning (Most Important Optimization)
# What is pruning?
# Stop DFS immediately if:
#     Current path is not a prefix of any word
#
# Why it matters?
#     Cuts off huge unnecessary search branches
#     Reduces exponential DFS


# LeetCode 212 – Word Search II
#     Grid with letters
#     Words list
#     Move in 4 direction
#     Return all valid words


# 1. Insert all words into a Trie.
# 2. Start DFS from each cell in the grid.
# 3. At each step:
#     - If character not in Trie → prune path.
#     - If Trie node marks word end → record result.
# 4. Use backtracking to explore all valid paths.


# board = [
#     ['o','a','a','n'],
#     ['e','t','a','e'],
#     ['i','h','k','r'],
#     ['i','f','l','v']
# ]
#
# words = ["oath","pea","eat","rain"]
#
# Output : ["oath", "eat"]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word at end node


def findWords(board, words):
    root = TrieNode()

    # 1️⃣ Build Trie
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word  # mark complete word

    rows, cols = len(board), len(board[0])
    result = []

    # 2️⃣ DFS function
    def dfs(r, c, node):
        ch = board[r][c]

        # If character not in Trie → prune
        if ch not in node.children:
            return

        next_node = node.children[ch]

        # Word found
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None  # avoid duplicates

        # Mark cell as visited
        board[r][c] = "#"

        # Explore 4 directions
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, next_node)

        # Backtrack
        board[r][c] = ch

    # 3️⃣ Start DFS from every cell
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return result


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
        node.word = word  # mark complete word


class Solution:
    def findWords(self, board, words):
        """
        Finds all dictionary words present in the board.
        Uses a separate visited matrix instead of modifying board.
        """
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        result = []

        def dfs(r, c, node):
            """
            DFS from board[r][c] while matching Trie nodes.
            """
            char = board[r][c]

            # Prune path if character not in Trie
            if char not in node.children:
                return

            next_node = node.children[char]

            # Found a complete word
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicates

            visited[r][c] = True

            # Explore 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    dfs(nr, nc, next_node)

            visited[r][c] = False  # backtrack

            # Trie pruning: remove leaf nodes
            if not next_node.children:
                node.children.pop(char)

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return result
