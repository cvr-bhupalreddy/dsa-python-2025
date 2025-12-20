# Definitions:
# ------------------------------------------------------------
#     - Ceil(x)  → smallest node value ≥ x
#     - Floor(x) → largest node value ≤ x
#
# BST property:
#     - Left subtree < node.val
#     - Right subtree > node.val

# Ceil :
#     - If root is None → return None
#     - If root.val == target → ceil = root.val
#     - If root.val < target → search right subtree
#     - If root.val > target → ceil might be root.val or in left subtree

# - Initialize ceil = None
# - Start from root
# - While node exists:
#     • If node.val == target → return node.val
#     • If node.val < target → move right
#     • If node.val > target → ceil = node.val; move left
# - Return ceil


def ceil_bst_recursive(root, target):
    if root is None:
        return None
    if root.val == target:
        return root.val
    if root.val < target:
        return ceil_bst_recursive(root.right, target)
    # root.val > target
    left_ceil = ceil_bst_recursive(root.left, target)
    return left_ceil if left_ceil is not None else root.val


def ceil_bst_iterative(root, target):
    ceil = None
    curr = root
    while curr:
        if curr.val == target:
            return curr.val
        elif curr.val < target:
            curr = curr.right
        else:
            ceil = curr.val
            curr = curr.left
    return ceil


# Floor :
#     - If root is None → return None
#     - If root.val == target → floor = root.val
#     - If root.val > target → search left subtree
#     - If root.val < target → floor might be root.val or in right subtree

def floor_bst_recursive(root, target):
    if root is None:
        return None
    if root.val == target:
        return root.val
    if root.val > target:
        return floor_bst_recursive(root.left, target)
    # root.val < target
    right_floor = floor_bst_recursive(root.right, target)
    return right_floor if right_floor is not None else root.val


# - Initialize floor = None
# - Start from root
# - While node exists:
#     • If node.val == target → return node.val
#     • If node.val > target → move left
#     • If node.val < target → floor = node.val; move right
# - Return floor


def floor_bst_iterative(root, target):
    floor = None
    curr = root
    while curr:
        if curr.val == target:
            return curr.val
        elif curr.val > target:
            curr = curr.left
        else:
            floor = curr.val
            curr = curr.right
    return floor
