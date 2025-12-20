# VERTICAL ORDER TRAVERSAL
# --------------------------------------------------------------------------------
# Best approach: BFS + Sorting
# Why DFS alone is insufficient:
# - Vertical order depends on:
#     1. Column (x)
#     2. Row (depth / y)
#     3. Value order (tie breaker)
#         - DFS traversal order can violate row ordering.
#
# Coordinates needed:
#     - Horizontal Distance (x)
#     - Depth (y)
#
# Why both coordinates are required:
#     - x groups nodes into vertical columns.
#     - y sorts nodes top to bottom within each column.
#     - Value resolves same (x, y) conflicts.
#
# Rule:
#     - Store (x, y, value)
#     - Sort by x, then y, then value.
# --------------------------------------------------------------------------------


# Traverse the tree column by column (vertical lines).
# - Nodes with the same horizontal distance (HD) are in the same vertical line.
# - Within the same vertical line:
#     • Nodes are ordered by level (top to bottom)
#     • If two nodes have same level and HD, order by value (optional)
# - Return a list of lists, where each sublist represents a vertical column.


# - Horizontal Distance (HD):
#     • Root → HD = 0
#     • Left child → HD = HD(parent) - 1
#     • Right child → HD = HD(parent) + 1
#
# - Level (depth):
#     • Root → level = 0
#     • Children → level = level(parent) + 1
#
# - Vertical ordering requires sorting nodes first by HD, then by level.


# 1️⃣ BFS (Level Order) – Preferred
# Idea:
# - BFS ensures nodes are processed top-to-bottom naturally.
# - Track both HD and level for each node.
# - For each HD, maintain a list of (level, node.val)
# - After BFS, sort nodes in each HD by level.
# - Collect HDs from min_HD → max_HD to form final vertical order.

# 1. If root is null → return empty list.
# 2. Initialize queue with (root, HD=0, level=0)
# 3. Initialize hd_map = dict() → HD → list of (level, value)
# 4. Track min_hd and max_hd
# 5. While queue is not empty:
#     a. Pop (node, hd, level)
#     b. Append (level, node.val) to hd_map[hd]
#     c. Update min_hd and max_hd
#     d. Enqueue left child → (node.left, hd-1, level+1)
#     e. Enqueue right child → (node.right, hd+1, level+1)
# 6. For HD in range(min_hd → max_hd):
# a. Sort hd_map[hd] by level
# b. Extract node.val for each tuple
# 7. Return result as list of lists


from collections import deque, defaultdict


def vertical_order_bfs(root):
    if root is None:
        return []

    hd_map = defaultdict(list)
    queue = deque([(root, 0, 0)])  # node, HD, level
    min_hd = max_hd = 0

    while queue:
        node, hd, level = queue.popleft()
        hd_map[hd].append((level, node.val))
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        if node.left:
            queue.append((node.left, hd - 1, level + 1))
        if node.right:
            queue.append((node.right, hd + 1, level + 1))

    result = []
    for hd in range(min_hd, max_hd + 1):
        # sort by level
        column = sorted(hd_map[hd], key=lambda x: x[0])
        result.append([val for lvl, val in column])
    return result


def vertical_order_dfs(root):
    if root is None:
        return []

    hd_map = defaultdict(list)
    min_hd = max_hd = 0

    def dfs(node, hd, level):
        nonlocal min_hd, max_hd
        if node is None:
            return

        hd_map[hd].append((level, node.val))
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        dfs(node.left, hd-1, level+1)
        dfs(node.right, hd+1, level+1)

    dfs(root, 0, 0)

    result = []
    for hd in range(min_hd, max_hd+1):
        column = sorted(hd_map[hd], key=lambda x: x[0])
        result.append([val for lvl, val in column])
    return result
