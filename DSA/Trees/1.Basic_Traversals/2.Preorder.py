# Order: ROOT → LEFT → RIGHT
#
# - Visit node first
# - Then traverse left subtree
# - Then traverse right subtree
# - Uses call stack implicitly


def preorder_print_recursive(root):
    if root is None:
        return
    print(root.val, end=" ")
    preorder_print_recursive(root.left)
    preorder_print_recursive(root.right)


def preorder_return_recursive_with_null(root):
    result = []

    def dfs(node):
        if node is None:
            result.append(None)
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


def preorder_find_recursive(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    return (preorder_find_recursive(root.left, target) or
            preorder_find_recursive(root.right, target))


# ITERATIVE PREORDER TRAVERSAL – APPROACH
# ------------------------------------------------------------
# Traversal order:
# ROOT → LEFT → RIGHT
#
# Data structure used:
# - Stack (LIFO)
#
# Idea:
#     - Simulate recursive preorder using an explicit stack.
#     - Always process the node as soon as it is popped.
#
# Steps:
#     1. If root is null, return.
#     2. Initialize an empty stack.
#     3. Push root onto the stack.
#     4. While stack is not empty:
#         a. Pop the top node from stack.
#         b. Process the node (print / add to result).
#         c. Push right child onto stack if it exists.
#         d. Push left child onto stack if it exists.
#     5. Continue until stack becomes empty.
#
# Why push right before left:
#     - Stack is LIFO.
#     - Left child must be processed before right.
#     - Pushing right first ensures left is on top.
#
# Time Complexity:
#     - O(N), every node is processed once.
#
# Space Complexity:
#     - O(H), where H is height of tree (stack size).
#
# Key Insight:
# - Preorder = process node immediately.
# - Stack replaces recursion.
# ------------------------------------------------------------



def preorder_print_iterative(root):
    if root is None:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def preorder_return_iterative_with_null(root):
    if root is None:
        return [None]

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node is None:
            result.append(None)
            continue

        result.append(node.val)
        stack.append(node.right)
        stack.append(node.left)

    return result


def preorder_find_iterative(root, target):
    if root is None:
        return False

    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == target:
            return True

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return False
