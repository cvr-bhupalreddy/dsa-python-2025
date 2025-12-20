# STATE-BASED DFS
# Data Structure:
#     - Stack of pairs: (node, state)
#
# State meaning:
#     - state = 1 → node just arrived (PREORDER time)
#     - state = 2 → left subtree done (INORDER time)
#     - state = 3 → both subtrees done (POSTORDER time)

# 1. Initialize empty stack.
# 2. Push (root, 1) into stack.
# 3. While stack is not empty:
# a. Pop (node, state)
#
# b. If state == 1:
#     - Add node to PREORDER
#     - Increment state to 2
#     - Push (node, 2) back to stack
#     - If left child exists:
#         push (left, 1)
#
# c. Else if state == 2:
#     - Add node to INORDER
#     - Increment state to 3
#     - Push (node, 3) back to stack
#     - If right child exists:
#         push (right, 1)
#
# d. Else if state == 3:
#     - Add node to POSTORDER
# ------------------------------------------------------------


# Recursive DFS visits each node 3 times:
#     1st time → before left subtree  → PREORDER
#     2nd time → between left & right → INORDER
#     3rd time → after both subtrees  → POSTORDER
#
# State variable SIMULATES recursion stack frames.
# Each state corresponds to one "moment" in recursion.


def all_traversals(root):
    if root is None:
        return [], [], []

    preorder = []
    inorder = []
    postorder = []

    # stack holds (node, state)
    # state 1 → preorder
    # state 2 → inorder
    # state 3 → postorder
    stack = [(root, 1)]

    while stack:
        node, state = stack.pop()

        if state == 1:
            preorder.append(node.val)
            stack.append((node, 2))     # next state
            if node.left:
                stack.append((node.left, 1))

        elif state == 2:
            inorder.append(node.val)
            stack.append((node, 3))     # next state
            if node.right:
                stack.append((node.right, 1))

        else:  # state == 3
            postorder.append(node.val)

    return preorder, inorder, postorder


def all_traversals_recursive(root):
    preorder = []
    inorder = []
    postorder = []

    def dfs(node):
        if node is None:
            return

        # PREORDER (before left subtree)
        preorder.append(node.val)

        dfs(node.left)

        # INORDER (between left and right subtree)
        inorder.append(node.val)

        dfs(node.right)

        # POSTORDER (after both subtrees)
        postorder.append(node.val)

    dfs(root)
    return preorder, inorder, postorder
