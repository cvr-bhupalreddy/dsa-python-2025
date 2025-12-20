# Given the root of a binary tree and a target node,
# return the path from the target node up to the root.
#
# Path is defined as a sequence of nodes starting from target and ending at root.


# APPROACH 1: BFS + PARENT TRACKING
#
#     1. Traverse tree using BFS and store parent of each node.
#     2. Once target is found, move upward using parent pointers.
#     3. Collect nodes until root is reached.


from collections import deque


def pathToRoot_BFS(root, target):
    if not root:
        return []

    parent = {root: None}
    queue = deque([root])

    # Build parent map
    while queue:
        node = queue.popleft()
        if node == target:
            break

        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    # Build path from target to root
    path = []
    while target:
        path.append(target.val)
        target = parent[target]

    return path  # target -> root


# APPROACH 2: DFS + PARENT TRACKING
# Core Idea
#     1. Build parent map using DFS.
#     2. Walk from target up to root using parent pointers.

def pathToRoot_DFS(root, target):
    parent = {}

    def build(node):
        if not node:
            return
        if node.left:
            parent[node.left] = node
            build(node.left)
        if node.right:
            parent[node.right] = node
            build(node.right)

    parent[root] = None
    build(root)

    path = []
    while target:
        path.append(target.val)
        target = parent[target]

    return path


# APPROACH 3: OPTIMAL RECURSIVE DFS (BACKTRACKING)
#     1. Use DFS to search for target.
#     2. When target is found, start adding nodes while returning.
#     3. Path naturally forms during backtracking.

def pathToRoot_Recursive(root, target):
    path = []

    def dfs(node):
        if not node:
            return False

        if node == target:
            path.append(node.val)
            return True

        if dfs(node.left) or dfs(node.right):
            path.append(node.val)
            return True

        return False

    dfs(root)
    return path  # target -> root


# Clean Python Code (Preorder + Backtracking)
#     - Visit node first (preorder)
#     - Add node to path
#     - If target found → return True
#     - Else search left and right
#     - If not found in both → remove node from path

def pathToNode_Preorder(root, target):
    path = []

    def dfs(node):
        if not node:
            return False

        # PREORDER: add before children
        path.append(node.val)

        if node == target:
            return True

        if dfs(node.left) or dfs(node.right):
            return True

        # target not found in this path → remove
        path.pop()
        return False

    dfs(root)
    return path
