# Boundary Traversal
# ------------------------------------------------------------
# Traverse the boundary of a binary tree in the following order:
# 1. Root node
# 2. Left boundary (excluding leaves)
# 3. All leaf nodes (left to right)
# 4. Right boundary (excluding leaves, traverse bottom-up)
#
# Return a list of nodes in this order.
# ------------------------------------------------------------


# 1. If root is null, return empty list.
# 2. Initialize result list with root node (if not a leaf).
#
# 3. Process left boundary:
#     - Start from root.left
#     - Traverse down the tree
#     - At each node, if it is not a leaf, add to result
#     - Prefer left child; if not exists, go right
#
# 4. Process all leaf nodes:
#     - Traverse entire tree (DFS)
#     - Add node to result if node.left is None and node.right is None
#
# 5. Process right boundary:
#     - Start from root.right
#     - Traverse down the tree
#     - At each node, if it is not a leaf, store in a temporary list
#     - Prefer right child; if not exists, go left
#     - Reverse the temporary list and append to result
#
# 6. Return the result list.


def boundary_traversal(root):
    if root is None:
        return []

    def is_leaf(node):
        return node.left is None and node.right is None

    def add_left_boundary(node, res):
        curr = node
        while curr:
            if not is_leaf(curr):
                res.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def add_right_boundary(node, res):
        curr = node
        temp = []
        while curr:
            if not is_leaf(curr):
                temp.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        # Add right boundary in reverse (bottom-up)
        res.extend(reversed(temp))

    def add_leaves(node, res):
        if node is None:
            return
        if is_leaf(node):
            res.append(node.val)
        add_leaves(node.left, res)
        add_leaves(node.right, res)

    result = []
    if not is_leaf(root):
        result.append(root.val)

    add_left_boundary(root.left, result)
    add_leaves(root, result)
    add_right_boundary(root.right, result)

    return result


# • Separate left boundary, right boundary, and leaves to avoid duplicates
# • Right boundary must be added in reverse
# • Root is always first if it’s not a leaf
