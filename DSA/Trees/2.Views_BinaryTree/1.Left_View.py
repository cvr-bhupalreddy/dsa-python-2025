# LEFT VIEW
# --------------------------------------------------------------------------------
# Best approach: DFS (Preorder)
# Why DFS is simpler than BFS:
#     - We only care about DEPTH (level).
#     - At each depth, we need the FIRST node seen from the left.
#     - DFS naturally goes depth-first, so first visit at a depth is enough.
#
# Coordinates needed:
#     - Only DEPTH (y coordinate)
#     - No horizontal distance required.
#
# Why no x-coordinate needed:
#     - Left view ignores column position.
#     - Visibility depends only on depth and traversal order (left before right).
#
# Rule:
# - If depth not visited before → take node.
# --------------------------------------------------------------------------------


from collections import deque


# 1️⃣ BFS (Level Order)
# Idea:
#     - Do a standard level order traversal using a queue.
#     - For each level, record only the first node (leftmost).
#     - Process nodes level by level from left to right.
#
# Steps:
# 1. If root is null, return empty list.
# 2. Initialize queue with root.
# 3. While queue is not empty:
#     a. Determine number of nodes at current level (level_size).
#     b. For i in range(level_size):
#         - Pop node from queue
#         - If i == 0 → leftmost node → add to result
#         - Append left and right children to queue if they exist
# 4. Return result


def leftViewBFS(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # first node of the level
            if i == 0:
                result.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


# 2️⃣ DFS (Preorder)
# Idea:
#     - Traverse tree preorder: ROOT → LEFT → RIGHT
#     - Keep track of current level.
#     - If this is the first node visited at this level → add to result.
#
# Steps:
# 1. Initialize empty result list.
# 2. Define dfs(node, level):
#     a. If node is None → return
#     b. If level == len(result) → first node at this level → add node.val
#     c. Recurse dfs(node.left, level + 1)
#     d. Recurse dfs(node.right, level + 1)
# 3. Call dfs(root, 0)
# 4. Return result


def leftViewDFS(root):
    result = []

    def dfs(node, level):
        if not node:
            return
        # first node at this level
        if level == len(result):
            result.append(node.data)
        # traverse left first
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result

# WHICH ONE IS BETTER?
# | Approach | Pros                                                     | Cons                                    |
# | -------- | -------------------------------------------------------- | --------------------------------------- |
# | BFS      | - Easy to understand<br>- Naturally level-wise           | - Uses queue (extra space O(width))     |
# | DFS      | - Uses recursion (stack O(height))<br>- Simple & elegant | - Slightly less intuitive for beginners |
