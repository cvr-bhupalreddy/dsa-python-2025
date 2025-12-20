# Problem Definition:
# ------------------------------------------------------------
# The maximum width of a binary tree is the maximum number of nodes
# present at any level when the tree is viewed as a complete binary tree.
#
# - Nodes are indexed as if the tree were complete.
# - Width = index_of_rightmost_node − index_of_leftmost_node + 1
# - Null (missing) nodes between two nodes ARE counted.

# • We are NOT counting actual nodes
# • We are counting positions as if the tree were complete
# • This captures gaps between nodes


# - Perform level order traversal (BFS)
# - Assign an index to each node:
#     • Root → index = 0
#     • Left child → 2 * index
#     • Right child → 2 * index + 1
# - For each level:
#     • Track leftmost index
#     • Track rightmost index
#     • Compute width = right - left + 1
# - Return maximum width across all levels


from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maximumWidth(root):
    if not root:
        return 0

    max_width = 0
    queue = deque([(root, 1)])  # (node, index)

    while queue:
        level_length = len(queue)
        _, first_index = queue[0]  # index of first node
        for i in range(level_length):
            node, index = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
        # width of current level = last_index - first_index + 1
        _, last_index = queue[-1] if queue else (None, index)
        max_width = max(max_width, last_index - first_index + 1)

    return max_width


def maximumWidth_optimized(root):
    if not root:
        return 0

    max_width = 0
    queue = deque([(root, 0)])  # (node, index)

    while queue:
        level_length = len(queue)
        first_index = queue[0][1]  # index of first node
        last_index = queue[-1][1]  # index of last node
        max_width = max(max_width, last_index - first_index + 1)

        # process all nodes in this level
        for _ in range(level_length):
            node, index = queue.popleft()
            # normalize index relative to first_index
            index -= first_index

            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))

    return max_width


# WHY DFS WORKS FOR THIS PROBLEM?
#
# - Even though the problem is level-based, DFS can be used
# - DFS allows us to visit nodes level-by-level while tracking:
#     • depth (level)
#     • index (virtual position)
#     - We store the first (leftmost) index seen at each level


# - Use DFS with parameters:
#     dfs(node, level, index)
#
# - For each level:
#     • Record the FIRST index encountered (leftmost)
#     • Normalize current index:
#         normalized_index = index − leftmost_index[level]
#
# - Width at current node:
#     normalized_index + 1
#
# - Track global maximum width


def maximumWidthDFS(root):
    max_width = 0
    leftmost = {}  # store first index at each level

    def dfs(node, level, index):
        nonlocal max_width
        if not node:
            return
        if level not in leftmost:
            leftmost[level] = index
        # width at this level
        max_width = max(max_width, index - leftmost[level] + 1)
        dfs(node.left, level + 1, 2 * index)
        dfs(node.right, level + 1, 2 * index + 1)

    dfs(root, 0, 1)
    return max_width
