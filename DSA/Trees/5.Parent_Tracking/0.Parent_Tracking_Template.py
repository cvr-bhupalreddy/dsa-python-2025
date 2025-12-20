# Universal Parent-Tracking BFS Template
#
#     Algorithm:
#     1) Build parent map using DFS/BFS
#     2) BFS starting from target node
#     3) Traverse neighbors: left, right, parent
#     4) Track visited to prevent cycles

from collections import deque


def solveUsingParentTracking(root, target):
    parent = {}
    stack = [root]
    parent[root] = None

    while stack:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    queue = deque([target])
    visited = set([target])

    while queue:
        node = queue.popleft()

        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in visited:
                visited.add(nei)
                queue.append(nei)


# Step 1: Build Parent Map (DFS)

def buildParent(root):
    parent = {}

    def dfs(node):
        if not node:
            return
        if node.left:
            parent[node.left] = node
            dfs(node.left)
        if node.right:
            parent[node.right] = node
            dfs(node.right)

    parent[root] = None
    dfs(root)
    return parent


# Step 2: DFS Traversal Using Parent Tracking

# Goal:
# Traverse in all 3 directions:
#     - left child
#     - right child
#     - parent
# Avoid cycles using visited set.

def dfsFromTarget(node, parent, visited, state):
    if not node or node in visited:
        return

    visited.add(node)

    # ===== PROCESS NODE HERE =====
    # Examples:
    # - check distance
    # - update answer
    # - build path
    # ==============================

    dfsFromTarget(node.left, parent, visited, state)
    dfsFromTarget(node.right, parent, visited, state)
    dfsFromTarget(parent[node], parent, visited, state)


# Step 3: Combine Everything (Master Template)
def solveParentTrackingDFS(root, target):
    parent = buildParent(root)
    visited = set()

    # optional: state (distance, path, count, etc.)
    state = {}

    dfsFromTarget(target, parent, visited, state)

#
# Short Answer (Interview Safe)
#
# - Parent tracking problems can be solved using DFS.
# - BFS is best suited when:
#     • distance / time / levels are involved
#     • shortest path is required
#     • spreading process is simulated
# - DFS is best suited when:
#     • path reconstruction is required
#     • ancestor relationships are needed

# | Problem Type                  | DFS | BFS | Best |
# |------------------------------ |-----|-----|------|
# | Path reconstruction           | ✅  | ❌  | DFS  |
# | LCA                           | ✅  | ❌  | DFS  |
# | Distance K                    | ⚠️  | ✅  | BFS  |
# | Infection / Burning Tree      | ❌  | ✅  | BFS  |
# | Nearest Leaf                  | ❌  | ✅  | BFS  |
# | Time / Spread / Levels        | ❌  | ✅  | BFS  |


# 6) Delete Nodes and Return Forest
#
# Problem:
#     Given a list of nodes to delete,
#     delete them and return remaining forest roots.
#
# Why Parent Tracking:
#     - Need to disconnect children from parent
#     - Root detection after deletion


#
# 7) Nodes at Distance K from Leaf
#
# Problem:
#     Return all nodes that are exactly K distance
#     from any leaf node.
#
# Why Parent Tracking:
# - Move upward from leaf nodes


# 8) Find Nearest Leaf to Given Node
#
# Problem:
#     Given a node in binary tree,
#     find the closest leaf to it.
#
#
# Why Parent Tracking:
# - Leaf may be in upward direction
