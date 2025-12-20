# Given the root of a binary tree, a target node,
# and an integer K, return all node values
# that are exactly K distance away from the target.
#
# Distance is defined as the number of edges between two nodes.
#
# Nodes can be reached by moving:
#     - left
#     - right
#     - parent

# APPROACH 1: ITERATIVE BFS + PARENT TRACKING (BEST / RECOMMENDED)
#     1. Convert tree into an undirected graph using parent tracking.
#     2. Start BFS from the target node.
#     3. BFS level = distance.
#     4. When distance == K, collect nodes.


from collections import deque


def distanceK_BFS(root, target, K):
    if not root:
        return []

    parent = {root: None}
    queue = deque([root])

    # Build parent map
    while queue:
        node = queue.popleft()
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    visited = set([target])
    queue = deque([(target, 0)])
    result = []

    while queue:
        node, dist = queue.popleft()

        if dist == K:
            result.append(node.val)
            continue

        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))

    return result


# APPROACH 2: ITERATIVE DFS + PARENT TRACKING
#
#     1. Build parent map using DFS.
#     2. DFS from target in all 3 directions.
#     3. Track distance manually.
#     4. Stop recursion at distance K.

def distanceK_DFS(root, target, K):
    parent = {}

    # Build parent map using DFS
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

    visited = set()
    result = []

    def dfs(node, dist):
        if not node or node in visited:
            return
        visited.add(node)

        if dist == K:
            result.append(node.val)
            return

        dfs(node.left, dist + 1)
        dfs(node.right, dist + 1)
        dfs(parent[node], dist + 1)

    dfs(target, 0)
    return result


# APPROACH 3: OPTIMAL RECURSIVE DFS (POSTORDER IDEA)  it's not good , more complicated
# Core Idea
#
# - Find target using DFS.
# - While returning back (postorder),
# compute distance to target.
# - When distance == K, record node.
# - Search opposite subtree for remaining distance.
