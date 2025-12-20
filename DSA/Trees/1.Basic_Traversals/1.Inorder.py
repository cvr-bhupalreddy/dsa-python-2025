def inorder_recursive(root):
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)  # LEFT
        result.append(node.val)  # ROOT
        dfs(node.right)  # RIGHT

    dfs(root)
    return result


# ITERATIVE INORDER TRAVERSAL – APPROACH
# ------------------------------------------------------------
# Traversal order:
#     LEFT → ROOT → RIGHT
#
# Data structures:
#     - Stack
#     - Pointer curr
#
# Idea:
#     - Go as left as possible first.
#     - Use stack to remember nodes whose left subtree is processed.
#     - Process node only when there is no more left child.
#
# Steps:
#     1. Initialize empty stack and curr = root.
#     2. While curr is not null OR stack is not empty:
#         a. While curr is not null:
#             - Push curr into stack.
#             - Move curr to curr.left.
#         b. Pop node from stack.
#         c. Process popped node (add to result).
#         d. Move curr to popped node.right.
#     3. Repeat until stack is empty and curr is null.
#
# Why this works:
#     - Stack simulates recursive call stack.
#     - Left subtree is fully processed before root.
#     - Right subtree is processed after root.
#
# Time Complexity:
#     - O(N)
#
# Space Complexity:
#     - O(H), H = height of tree
# ------------------------------------------------------------


def inorder_iterative(root):
    result = []
    stack = []
    curr = root

    while curr is not None or stack:  # this can be simply written as while curr or stack
        while curr is not None:  # process all nodes in left subtree
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()  # process root
        result.append(curr.val)
        curr = curr.right  # Process right subtree of root

    return result
