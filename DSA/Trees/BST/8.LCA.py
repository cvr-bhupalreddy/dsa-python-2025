# Given a Binary Search Tree (BST) and two nodes p and q,
# find their Lowest Common Ancestor (LCA).
#
# Definition:
# - LCA of p and q is the **lowest node** in BST such that
# p and q are **in its left and right subtree** (or one of them is the node itself).
#
# BST Property:
#     - Left subtree values < node.val
#     - Right subtree values > node.val
# This property allows optimized LCA search.


# 1️⃣ Recursive Approach
# - Start at root
# - If both p and q < root → LCA is in left subtree
# - If both p and q > root → LCA is in right subtree
# - Otherwise, root is the split point → LCA found


def bstLCARecursive(root, p, q):
    if not root:
        return None

    if p.val < root.val and q.val < root.val:
        return bstLCARecursive(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return bstLCARecursive(root.right, p, q)
    else:
        # Split point: one node on left, one on right, or one node equals root
        return root

# 2️⃣ Iterative Approach
# - Start at root
# - Traverse down the tree:
#     - If both p and q < curr → move left
#     - If both p and q > curr → move right
# - Otherwise, curr is split point → LCA
# - Avoids recursion stack


def bstLCAIterative(root, p, q):
    curr = root

    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None
