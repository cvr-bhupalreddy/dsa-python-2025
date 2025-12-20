# Given a binary tree, find the **size (number of nodes)** of the largest subtree that is a BST.
#
# Input: root of binary tree
# Output: size of largest BST


# 1️⃣ Brute Force Approach
# - For each node in the tree:
#     1. Check if subtree rooted at node is a BST
#     2. If yes, count nodes in the subtree
# - Return the maximum size found


def isBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if root.val <= low or root.val >= high:
        return False
    return isBST(root.left, low, root.val) and isBST(root.right, root.val, high)


def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)


def largestBSTBrute(root):
    if not root:
        return 0
    if isBST(root):
        return countNodes(root)
    return max(largestBSTBrute(root.left), largestBSTBrute(root.right))

# Complexity:
#
# Time: O(n²) → For each node, traverse subtree to check BST and count nodes
# Space: O(h) recursion stack


# 2️⃣ Better Approach (Bottom-Up / Postorder Check)
#
# - Use postorder traversal
# - For each node, collect from left and right:
#     - Is left subtree BST?
#     - Is right subtree BST?
#     - Min and Max values
#     - Size of largest BST
# - If node satisfies BST property with left and right:
#     - Current subtree is BST → update size
# - Otherwise, propagate max size from children


def largestBSTOptimal(root):
    max_size = 0

    def postorder(node):
        nonlocal max_size
        if not node:
            return True, 0, float('inf'), float('-inf')

        l_isBST, l_size, l_min, l_max = postorder(node.left)
        r_isBST, r_size, r_min, r_max = postorder(node.right)

        if l_isBST and r_isBST and l_max < node.val < r_min:
            size = l_size + r_size + 1
            max_size = max(max_size, size)
            return True, size, min(l_min, node.val), max(r_max, node.val)
        return False, 0, 0, 0

    postorder(root)
    return max_size


# | Approach | Time Complexity | Space Complexity | Notes                                               |
# | -------- | --------------- | ---------------- | --------------------------------------------------- |
# | Brute    | O(n²)           | O(h)             | Simple, checks each subtree separately              |
# | Optimal  | O(n)            | O(h)             | Same as better, clean code with single return tuple |
