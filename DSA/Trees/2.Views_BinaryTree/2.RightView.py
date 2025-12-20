# RIGHT VIEW
# --------------------------------------------------------------------------------
# Best approach: DFS (Reverse Preorder)
# Why DFS is simpler than BFS:
#     - Same logic as left view.
#     - We only care about DEPTH.
#     - DFS lets us control traversal order easily.
#
# Coordinates needed:
#     - Only DEPTH (y coordinate)
#
# Traversal order:
#     - Visit RIGHT child before LEFT child.
#     - First node visited at each depth is the visible one.
#
# Why no x-coordinate needed:
#     - Right view depends only on depth and side preference.
# --------------------------------------------------------------------------------


# Key Insight for Right View:
#     DFS is often simpler for right view because you visit the rightmost node first at each level.
#     BFS requires tracking the last node at each level explicitly.
#
# Practical Recommendation:
#     DFS is slightly better for right view if you only need the rightmost nodes and want concise code.
#     BFS is more general for level-based operations.


from collections import deque


# 1️⃣ BFS (Level Order)
# Idea:
# - Use standard level order traversal with a queue.
# - For each level, record only the last node (rightmost).
# - Process nodes level by level from left to right.
#
# Steps:
# 1. If root is null, return empty list.
# 2. Initialize queue with root.
# 3. While queue is not empty:
#     a. Determine number of nodes at current level (level_size).
#     b. For i in range(level_size):
#         - Pop node from queue
#         - If i == level_size - 1 → rightmost node → add to result
#         - Append left and right children to queue if they exist
# 4. Return result


def rightViewBFS(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # last node of the level
            if i == level_size - 1:
                result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


# 2️⃣ DFS (Preorder Right-First)
# Idea:
#     - Traverse tree DFS: ROOT → RIGHT → LEFT
#     - Keep track of current level.
#     - If this is the first node visited at this level → add to result.
#
# Steps:
# 1. Initialize empty result list.
# 2. Define dfs(node, level):
#     a. If node is None → return
#     b. If level == len(result) → first node at this level → add node.val
#     c. Recurse dfs(node.right, level + 1)
#     d. Recurse dfs(node.left, level + 1)
# 3. Call dfs(root, 0)
# 4. Return result

def rightViewDFS(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        # first node at this level
        if level == len(result):
            result.append(node.data)
        # traverse right first
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)

    dfs(root, 0)
    return result

# WHICH ONE IS BETTER?
# | Approach | Pros                                                     | Cons                                    |
# | -------- | -------------------------------------------------------- | --------------------------------------- |
# | BFS      | - Easy to understand<br>- Naturally level-wise           | - Uses queue (extra space O(width))     |
# | DFS      | - Uses recursion (stack O(height))<br>- Simple & elegant | - Slightly less intuitive for beginners |
