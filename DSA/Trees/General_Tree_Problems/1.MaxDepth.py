# 1️⃣ Max Depth of Binary Tree
# Problem Definition:
# ------------------------------------------------------------
# Find the maximum depth (height) of a binary tree.
# Depth of root = 1. Depth of empty tree = 0.


# - Recursive approach (DFS):
#     • Base case: if node is None → return 0
#     • Return 1 + max(depth(left), depth(right))

# - BFS approach:
# • Level order traversal → count number of levels
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)


def maxDepth_bfs(root: TreeNode) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


def maxDepth_dfs_iterative(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return max_depth

# | Approach            | Time   | Space  | Notes          |
# | ------------------- | ------ | ------ | -------------- |
# | Recursive DFS       | `O(n)` | `O(h)` | Clean & common |
# | Iterative BFS       | `O(n)` | `O(n)` | Level-based    |
# | Iterative DFS       | `O(n)` | `O(n)` | No recursion   |
# | Dynamic Programming | ❌     | ❌     | No improvement |
