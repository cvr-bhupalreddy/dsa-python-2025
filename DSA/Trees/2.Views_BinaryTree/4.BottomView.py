# BOTTOM VIEW
# --------------------------------------------------------------------------------
# Best approach: BFS
# Why DFS is NOT simpler:
#     - We care about lowest node in each column.
#     - DFS order does not guarantee deepest node is visited last.
#     - BFS ensures deeper levels are processed after shallow ones.
#
# Coordinates needed:
#     - Horizontal Distance (x coordinate)
#     - Depth (implicitly through BFS traversal)
#
# Rule:
#     - For each x, keep OVERWRITING node value.
#     - Last node seen at each x is bottom view.
# --------------------------------------------------------------------------------

# 1️⃣ BFS (Level Order) — Preferred
# Idea:
# - BFS ensures nodes are processed level by level.
# - For each HD, overwrite the node value → last node at HD remains.
#
# Steps:
# 1. If root is null, return empty list.
# 2. Initialize queue with tuple (root, HD=0).
# 3. Initialize empty dict hd_node_map.
# 4. Track min_hd and max_hd.
# 5. While queue is not empty:
#     a. Pop (node, hd)
#     b. hd_node_map[hd] = node.val  # overwrite previous value
#     c. Update min_hd and max_hd
#     d. If left child exists: enqueue (node.left, hd - 1)
#     e. If right child exists: enqueue (node.right, hd + 1)
# 6. Collect values from min_hd to max_hd
# 7. Return result


from collections import deque


def bottomView(root):
    if not root:
        return []

    hd_map = {}
    queue = deque([(root, 0)])

    while queue:
        node, x = queue.popleft()

        # overwrite each time (bottom-most node remains last)
        hd_map[x] = node.data

        if node.left:
            queue.append((node.left, x - 1))
        if node.right:
            queue.append((node.right, x + 1))

    # sort by horizontal distance for left-to-right order
    return [hd_map[k] for k in sorted(hd_map.keys())]


# 2️⃣ DFS
# Idea:
#     - DFS with tracking HD and depth.
#     - For each HD, store node if its depth >= existing depth (bottommost node).
#     - Traverse tree recursively: LEFT → RIGHT or RIGHT → LEFT
#     - Update hd_node_map only if current depth >= stored depth

def bottom_view_dfs(root):
    if root is None:
        return []

    hd_node_map = dict()  # HD -> (node.val, depth)
    min_hd = max_hd = 0

    def dfs(node, hd, depth):
        nonlocal min_hd, max_hd
        if node is None:
            return

        # Update node at HD if deeper (bottommost)
        if hd not in hd_node_map or depth >= hd_node_map[hd][1]:
            hd_node_map[hd] = (node.val, depth)

        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        dfs(node.left, hd - 1, depth + 1)
        dfs(node.right, hd + 1, depth + 1)

    dfs(root, 0, 0)
    result = [hd_node_map[hd][0] for hd in range(min_hd, max_hd + 1)]
    return result

# WHY BFS IS BETTER FOR BOTTOM VIEW
# | Approach | Reason
# | -------- | ---------------------------------------------------------------
# | BFS      | - Level order ensures bottommost node at each HD is last seen |
# | DFS      | - Must track depth for each HD and compare → more bookkeeping

