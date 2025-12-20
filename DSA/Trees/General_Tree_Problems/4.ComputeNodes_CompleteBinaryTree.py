# Problem Definition:
# ------------------------------------------------------------
# Given the root of a COMPLETE binary tree,
# return the total number of nodes.
#
# Complete Binary Tree:
#     - All levels are completely filled except possibly the last
#     - Last level nodes are as far left as possible

# BFS/DFS
# Idea:
# ------------------------------------------------------------
# - Traverse every node and count
# - Works for any binary tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes_brute(root):
    if root is None:
        return 0
    return 1 + count_nodes_brute(root.left) + count_nodes_brute(root.right)


# 2.Check Perfect Subtree
# Idea:
# ------------------------------------------------------------
# - For each node:
#     • Find leftmost height (go left)
#     • Find rightmost height (go right)
# - If heights are equal:
#     → subtree is PERFECT
#     → nodes = 2^height - 1
# - Else:
#     → recurse on left and right


def countNodes(root):
    if not root:
        return 0

    # find left height
    def leftHeight(node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    # find right height
    def rightHeight(node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h

    lh = leftHeight(root)
    rh = rightHeight(root)

    # if perfect tree
    if lh == rh:
        return (1 << lh) - 1  # 2^lh - 1

    # else recurse
    return 1 + countNodes(root.left) + countNodes(root.right)


# OPTIMAL (Divide & Conquer)
#
# Idea:
# ------------------------------------------------------------
# - Uses complete tree properties
# - At each node:
#     • Compute leftmost height
#     • Compute rightmost height
# - If equal → perfect subtree → direct formula
# - Else → recurse
#     - Height computation takes O(log N)

def count_nodes_optimal(root):
    if root is None:
        return 0

    left = root.left
    right = root.right
    lh = rh = 1

    while left:
        lh += 1
        left = left.left

    while right:
        rh += 1
        right = right.right

    if lh == rh:
        return (1 << lh) - 1

    return 1 + count_nodes_optimal(root.left) + count_nodes_optimal(root.right)

# Approach     | Time Complexity     | Space | Key Idea
# ------------------------------------------------------------
# Brute        | O(N)                | O(H)  | Traverse all nodes
# Better       | O(N) worst case     | O(H)  | Detect perfect subtrees
# Optimal      | O((log N)^2)        | O(log N) | Use complete tree height property
