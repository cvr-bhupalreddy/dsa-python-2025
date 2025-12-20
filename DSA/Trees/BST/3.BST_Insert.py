# Approach:
#     - Traverse BST like search
#     - When None is reached, insert new node
#     - Maintain BST property: left < root < right

# Problem Definition:
# ------------------------------------------------------------
# Given a Binary Search Tree (BST) and a value, insert the value
# into the BST while maintaining the BST property:
#     - Left subtree < node.val
#     - Right subtree > node.val
#     - No duplicates (or handle according to requirement)

# 1️⃣ RECURSIVE APPROACH
# - Base case: if node is None → create new node
# - If val < node.val → insert in left subtree
# - If val > node.val → insert in right subtree
# - Return node after insertion


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst_insert_recursive(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = bst_insert_recursive(root.left, val)
    elif val > root.val:
        root.right = bst_insert_recursive(root.right, val)
    # else: val already exists; do nothing

    return root


def bst_insert_iterative(root, val):
    new_node = TreeNode(val)
    if root is None:
        return new_node

    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = new_node
                break
            curr = curr.left
        elif val > curr.val:
            if curr.right is None:
                curr.right = new_node
                break
            curr = curr.right
        else:
            # val already exists; do nothing
            break
    return root


# Strategy 1: Duplicates on Right

def bst_insert_recursive_dup_right(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = bst_insert_recursive_dup_right(root.left, val)
    else:
        # duplicates go to right
        root.right = bst_insert_recursive_dup_right(root.right, val)

    return root


def bst_insert_iterative_dup_right(root, val):
    new_node = TreeNode(val)
    if root is None:
        return new_node

    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = new_node
                break
            curr = curr.left
        else:
            # duplicates go to right
            if curr.right is None:
                curr.right = new_node
                break
            curr = curr.right
    return root


# Strategy 2: Duplicates on Left
def bst_insert_recursive_dup_left(root, val):
    if root is None:
        return TreeNode(val)

    if val <= root.val:
        # duplicates go to left
        root.left = bst_insert_recursive_dup_left(root.left, val)
    else:
        root.right = bst_insert_recursive_dup_left(root.right, val)

    return root


def bst_insert_iterative_dup_left(root, val):
    new_node = TreeNode(val)
    if root is None:
        return new_node

    curr = root
    while True:
        if val <= curr.val:
            # duplicates go to left
            if curr.left is None:
                curr.left = new_node
                break
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = new_node
                break
            curr = curr.right
    return root
