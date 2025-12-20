# Approach:
#     - Compare target with node value
#     - Move left if target < node.val
#     - Move right if target > node.val
#     - Return node if found, else None


def bst_search_recursive(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    elif target < root.val:
        return bst_search_recursive(root.left, target)
    else:
        return bst_search_recursive(root.right, target)


# Iterative Approach
# - Start from root
# - While current node exists:
#     • If node.val == target → return node
#     • If target < node.val → move left
#     • Else → move right
# - If we reach None → target not found

def bst_search_iterative(root, target):
    curr = root
    while curr:
        if curr.val == target:
            return curr
        elif target < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None
