def postorder_recursive(root):
    result = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)  # LEFT
        dfs(node.right)  # RIGHT
        result.append(node.val)  # ROOT

    dfs(root)
    return result


# ITERATIVE POSTORDER TRAVERSAL – APPROACH
# ------------------------------------------------------------
# Traversal order:
# LEFT → RIGHT → ROOT
#
# Data structures:
#     - Stack
#     - Pointer curr
#     - Pointer last_visited
#
# Idea:
#     - Postorder requires processing a node only AFTER both children.
#     - Use stack to simulate recursion.
#     - Track the last visited node to know whether right subtree is processed.
#
# Steps:
# 1. Initialize empty stack.
# 2. Set curr = root and last_visited = null.
# 3. While curr is not null OR stack is not empty:
#     a. If curr is not null:
#         - Push curr into stack.
#         - Move curr to curr.left.
#     b. Else:
#         - Peek top node from stack.
#         - If right child exists AND right child is NOT last_visited:
#             - Move curr to right child.
#         - Else:
#             - Process peek node (add to result).
#             - Pop node from stack.
#             - Set last_visited = processed node.
# 4. Repeat until stack is empty and curr is null.
#
# Why last_visited is needed:
#     - To avoid visiting right subtree multiple times.
#     - To know when both children are already processed.
#
# Time Complexity:
# - O(N)
#
# Space Complexity:
# - O(H), H = height of tree
# ------------------------------------------------------------


def postorder_iterative(root):
    result = []
    stack = []
    curr = root
    last_visited = None

    while curr is not None or stack:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            if peek.right is not None and last_visited != peek.right:
                curr = peek.right
            else:
                result.append(peek.val)
                last_visited = stack.pop()

    return result

# APPROACH (2 STACKS)
# ------------------------------------------------------------
# Data structures:
#     - Stack1 (processing stack)
#     - Stack2 (output stack)
#
# Idea:
#     - Reverse the logic of preorder traversal.
#     - Preorder is: ROOT → LEFT → RIGHT
#     - If we do: ROOT → RIGHT → LEFT
#     - And then reverse the result
#     → we get LEFT → RIGHT → ROOT (postorder)
#
# Steps:
#     1. If root is null, return empty result.
#     2. Push root into stack1.
#     3. While stack1 is not empty:
#         a. Pop node from stack1.
#         b. Push popped node into stack2.
#         c. Push left child into stack1 (if exists).
#         d. Push right child into stack1 (if exists).
#     4. After loop, pop all nodes from stack2 and add to result.
#     5. Result is postorder traversal.
#
# Time Complexity:
# - O(N)
#
# Space Complexity:
# - O(N)
# ------------------------------------------------------------


# 1) Stack1 does a modified preorder traversal
#     Order produced into stack2:
#     ROOT → RIGHT → LEFT
# 2) Stack2 reverses this order automatically (LIFO)
# 3) Reversing ROOT → RIGHT → LEFT gives:
#     LEFT → RIGHT → ROOT
# 4) LEFT → RIGHT → ROOT is exactly POSTORDER


def postorder_iterative_two_stacks(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().val)

    return result
