# TOP VIEW
# --------------------------------------------------------------------------------
# Best approach: BFS
# Why DFS is NOT simpler:
#     - We care about both HORIZONTAL position and HEIGHT.
#     - A node higher in the tree blocks nodes below it in same column.
#     - DFS can reach deeper nodes before shallower ones → incorrect.
#
# Coordinates needed:
#     - Horizontal Distance (x coordinate)
#     - Depth (implicitly handled by BFS order)
#
# Why BFS works:
#     - BFS visits nodes level by level.
#     - First node seen at each horizontal distance is the topmost one.
#
# Rule:
#     - For each x, keep FIRST node encountered.
# --------------------------------------------------------------------------------


# - Horizontal Distance (HD):
#     • Root → HD = 0
#     • Left child → HD = HD(parent) - 1
#     • Right child → HD = HD(parent) + 1
# - For top view, only the first node encountered at each HD is included.


# 1️⃣ BFS (Level Order) — Preferred
# Idea:
#     - BFS guarantees the first node encountered at a horizontal distance is the topmost node.
#     - Use a queue to process nodes along with their HD.
#
# Steps:
#     1. If root is null, return empty list.
#     2. Initialize queue with tuple (root, HD=0).
#     3. Initialize empty dict hd_node_map.
#     4. Track min_hd and max_hd.
#     5. While queue is not empty:
#         a. Pop (node, hd) from queue
#         b. If hd not in hd_node_map:
#             - hd_node_map[hd] = node.val  # first node at this HD
#         c. Update min_hd and max_hd
#         d. If left child exists:
#             enqueue (node.left, hd - 1)
#         e. If right child exists:
#             enqueue (node.right, hd + 1)
#     6. Traverse hd_node_map from min_hd to max_hd and collect values.
#     7. Return the result list.


from collections import deque


def top_view(root):
    if root is None:
        return []

    hd_node_map = dict()  # HD -> node.val
    queue = deque([(root, 0)])
    min_hd = max_hd = 0

    while queue:
        node, hd = queue.popleft()

        if hd not in hd_node_map:
            hd_node_map[hd] = node.val

        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Collect nodes from leftmost HD to rightmost HD
    result = [hd_node_map[hd] for hd in range(min_hd, max_hd + 1)]
    return result


# 2️⃣ DFS (Optional, Slightly Tricky)
# Idea:
#     - Use DFS with tracking HD and level (depth).
#     - For each HD, store the node with smallest depth (topmost).
#     - Preorder DFS can be used: ROOT → LEFT → RIGHT or RIGHT → LEFT
#     - Update hd_node_map only if current depth < existing depth at HD.

def top_view_dfs(root):
    if root is None:
        return []

    hd_node_map = dict()  # HD -> (node.val, depth)
    min_hd = max_hd = 0

    def dfs(node, hd, depth):
        nonlocal min_hd, max_hd
        if node is None:
            return

        # If this HD is not recorded OR current node is higher (smaller depth)
        if hd not in hd_node_map or depth < hd_node_map[hd][1]:
            hd_node_map[hd] = (node.val, depth)

        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        dfs(node.left, hd - 1, depth + 1)
        dfs(node.right, hd + 1, depth + 1)

    dfs(root, 0, 0)

    # Collect nodes from leftmost HD to rightmost HD
    result = [hd_node_map[hd][0] for hd in range(min_hd, max_hd + 1)]
    return result

