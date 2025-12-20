# ==================== DFS + BACKTRACKING TREE PROBLEMS ====================
#
# GENERAL PATTERN:
# - Traverse from root to leaf using DFS
# - Carry state downward (sum, path, max, mask, etc.)
# - At leaf or condition node, update answer
# - Backtrack state when returning
#
# =========================================================================
#
#
# 1) PATH SUM I
# --------------------------------------------------------------------------
#
# Problem Statement:
# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
#
# Optimal Recursive Solution (DFS):

def hasPathSum(root, targetSum):
    def dfs(node, curr_sum):
        if not node:
            return False

        curr_sum += node.val

        if not node.left and not node.right:
            return curr_sum == targetSum

        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0)


# =========================================================================
#
#
# 2) PATH SUM II
# --------------------------------------------------------------------------
#
# Problem Statement:
# Given the root of a binary tree and an integer targetSum,
# return all root-to-leaf paths where the sum of node values
# in the path equals targetSum.
# Each path should be returned as a list of node values.
#
# Optimal Recursive Solution (DFS + Backtracking):

def pathSum(root, targetSum):
    result = []

    def dfs(node, curr_sum, path):
        if not node:
            return

        curr_sum += node.val
        path.append(node.val)

        if not node.left and not node.right and curr_sum == targetSum:
            result.append(path[:])

        dfs(node.left, curr_sum, path)
        dfs(node.right, curr_sum, path)

        path.pop()  # backtrack

    dfs(root, 0, [])
    return result


# =========================================================================
#
#
# 3) ROOT TO LEAF PATHS
# --------------------------------------------------------------------------
#
# Problem Statement:
# Given the root of a binary tree,
# return all root-to-leaf paths as strings
# in the format "root->child->leaf".
#
# Optimal Recursive Solution (DFS + Backtracking):

def binaryTreePaths(root):
    result = []

    def dfs(node, path):
        if not node:
            return

        path.append(str(node.val))

        if not node.left and not node.right:
            result.append("->".join(path))

        dfs(node.left, path)
        dfs(node.right, path)

        path.pop()  # backtrack

    dfs(root, [])
    return result


# =========================================================================
#
#
# 4) GOOD NODES IN BINARY TREE
# --------------------------------------------------------------------------
#
# Problem Statement:
# A node X in the tree is considered good if on the path from
# the root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
#
# Optimal Recursive Solution (DFS):

def goodNodes(root):
    def dfs(node, max_so_far):
        if not node:
            return 0

        good = 1 if node.val >= max_so_far else 0
        max_so_far = max(max_so_far, node.val)

        return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

    return dfs(root, root.val)


# =========================================================================
#
#
# 5) SUM OF LEFT LEAVES
# --------------------------------------------------------------------------
#
# Problem Statement:
# Given the root of a binary tree,
# return the sum of all left leaves.
# A left leaf is a leaf node that is the left child of its parent.
#
# Optimal Recursive Solution (DFS):

def sumOfLeftLeaves(root):
    def dfs(node, is_left):
        if not node:
            return 0

        if not node.left and not node.right and is_left:
            return node.val

        return dfs(node.left, True) + dfs(node.right, False)

    return dfs(root, False)


# =========================================================================
#
#
# 6) PSEUDO-PALINDROMIC PATHS IN A BINARY TREE
# --------------------------------------------------------------------------
#
# Problem Statement:
# Given a binary tree where node values are digits from 1 to 9,
# return the number of root-to-leaf paths where the sequence
# of node values can be rearranged to form a palindrome.
# A sequence is pseudo-palindromic if at most one digit
# appears an odd number of times.
#
# Optimal Recursive Solution (DFS + Bitmask):

def pseudoPalindromicPaths(root):
    count = 0

    def dfs(node, mask):
        nonlocal count
        if not node:
            return

        # toggle bit for current node value
        mask ^= (1 << node.val)

        if not node.left and not node.right:
            # check if at most one bit is set
            if mask & (mask - 1) == 0:
                count += 1

        dfs(node.left, mask)
        dfs(node.right, mask)

    dfs(root, 0)
    return count

# =========================================================================
#
#
# KEY TAKEAWAY (IMPORTANT):
# --------------------------------------------------------------------------
#
# - All these problems use:
# DFS + Backtracking
# Top-down traversal
# State passed from parent to child
#
# - Difference is ONLY in:
# What state you track
# When you update the answer
#
# - No DP memoization needed because:
# Each root-to-leaf path is unique
#
# =========================================================================
