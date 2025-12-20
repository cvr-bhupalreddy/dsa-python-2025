# Problem Definition:
# ------------------------------------------------------------
# Given a binary tree and two nodes p and q,
# find their Lowest Common Ancestor (LCA).
#
# Lowest Common Ancestor:
#     - The lowest (deepest) node in the tree
#     - That has BOTH p and q as descendants
#     - A node can be a descendant of itself


# Algorithm:
#     1) Build parent map using DFS/BFS
#     2) BFS starting from target node
#     3) Traverse neighbors: left, right, parent
#     4) Track visited to prevent cycles


# APPROACH 3: OPTIMAL RECURSIVE DFS (POSTORDER)
# Use postorder traversal.
#
# - If current node is None → return None
# - If current node == p or q → return current node
# - Recurse left and right
# - If both sides return non-null → current node is LCA
# - Else return non-null child


from collections import deque


def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# 1.Iterative BFS Parent tracking
#
#     1. Use BFS to build a parent map for each node.
#     2. Store all ancestors of node p.
#     3. Traverse ancestors of node q upwards.
#     4. First common ancestor is the LCA.


def lowestCommonAncestor_BFS(root, p, q):
    parent = {root: None}
    queue = deque([root])

    # Build parent map
    while p not in parent or q not in parent:
        node = queue.popleft()

        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    # Store ancestors of p
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    # Find first common ancestor
    while q not in ancestors:
        q = parent[q]

    return q


# APPROACH 2: ITERATIVE DFS + PARENT TRACKING
#
# 1. Use DFS (stack) to build parent map.
# 2. Stop once both p and q are found.
# 3. Same ancestor comparison logic as BFS.


def lowestCommonAncestor_DFS(root, p, q):
    parent = {root: None}
    stack = [root]

    # Build parent map using DFS
    while p not in parent or q not in parent:
        node = stack.pop()

        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]

    return q
