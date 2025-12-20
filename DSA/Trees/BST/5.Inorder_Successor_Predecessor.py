# RELATION BETWEEN CEIL/FLOOR AND INORDER SUCCESSOR/PREDECESSOR
#
# | Concept      | BST Term            | Explanation             |
# | ------------ | ------------------- | ------------------------|
# | **Ceil(x)**  | Inorder Successor   | Smallest node value ≥ x |
# | **Floor(x)** | Inorder Predecessor | Largest node value ≤ x. |


# Inorder Successor
#
# Case 1: Node has right child
# - Successor = leftmost node in right subtree
#
# Case 2: Node has no right child
# - Successor = nearest ancestor for which node is in left subtree
# - Traverse from root:
#     • If node.val < target → go right
#     • If node.val > target → successor = node; go left

def inorder_successor_recursive(root, target):
    if root is None:
        return None

    if root.val <= target:
        return inorder_successor_recursive(root.right, target)
    else:
        left_succ = inorder_successor_recursive(root.left, target)
        return left_succ if left_succ else root


def inorder_successor_iterative(root, target):
    succ = None
    curr = root
    while curr:
        if curr.val <= target:
            curr = curr.right
        else:
            succ = curr
            curr = curr.left
    return succ


# Inorder Predecessor
#
# Case 1: Node has left child
# - Predecessor = rightmost node in left subtree
#
# Case 2: Node has no left child
# - Predecessor = nearest ancestor for which node is in right subtree
# - Traverse from root:
#     • If node.val > target → go left
#     • If node.val < target → predecessor = node; go right


def inorder_predecessor_recursive(root, target):
    if root is None:
        return None

    if root.val >= target:
        return inorder_predecessor_recursive(root.left, target)
    else:
        right_pred = inorder_predecessor_recursive(root.right, target)
        return right_pred if right_pred else root


def inorder_predecessor_iterative(root, target):
    pred = None
    curr = root
    while curr:
        if curr.val >= target:
            curr = curr.left
        else:
            pred = curr
            curr = curr.right
    return pred
