# | Approach                      | Core Idea                                | Time Complexity | Space| DP Used? |
# | ----------------------------- | ---------------------------------------- | --------------- | ------| -------- |
# | Naive Recursive               | Compute height for every node separately | `O(n²)`         | `O(h)`| ❌ No
# | Recursive DFS (Bottom-Up DP)  | Return height & balance together         | `O(n)`          | `O(h)`| ✅ Yes
# | Iterative DFS (Post-Order DP) | Store subtree heights in map             | `O(n)`          | `O(n)`| ✅ Yes
# | BFS / Level Order             | Level traversal only                     | ❌               | ❌   | ❌


# Approach 1: Naive Recursive
#
# Idea:
# For each node, compute the height of left and right subtrees separately.
# Check if their difference is <= 1.
# Recursively apply this to all nodes.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def isBalanced(root):
    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)


# Approach 2: Bottom-Up / Optimized Recursive (DP Applied)
# Idea:
#     Use post-order traversal.
#     Compute height and balance status in one recursion.
#     If a subtree is unbalanced, stop early.
# Each node’s height is calculated only once -> DP applied.


def checkBalanced(node):
    if not node:
        return 0, True
    left_height, left_bal = checkBalanced(node.left)
    right_height, right_bal = checkBalanced(node.right)

    current_bal = left_bal and right_bal and abs(left_height - right_height) <= 1
    current_height = 1 + max(left_height, right_height)

    return current_height, current_bal


def isBalancedDP(root):
    _, balanced = checkBalanced(root)
    return balanced


def checkBalancedSingle(node):
    if not node:
        return 0  # height of empty subtree

    left_h = checkBalancedSingle(node.left)
    if left_h == -1:  # left subtree is unbalanced
        return -1

    right_h = checkBalancedSingle(node.right)
    if right_h == -1:  # right subtree is unbalanced
        return -1
    if abs(left_h - right_h) > 1:  # current node is unbalanced
        return -1
    # return current node height if balanced
    return 1 + max(left_h, right_h)


def isBalancedDP_one_param(root):
    return checkBalancedSingle(root) != -1


#
# Approach 3: Iterative Postorder (Stack + DP)
#
# Idea:
#     Simulate post-order traversal using a stack.
#     Store height of each node in a dictionary.
#     Check balance while processing nodes.
#     Each node’s height is calculated once -> DP applied.


# Algorithm Explanation (Iterative Balance Check)
#
# Goal:
# Check if a binary tree is balanced using iteration, avoiding recursion.
#
# Key Idea:
# - A node is balanced if the height difference of its left and right subtrees <= 1.
# - In recursion, this is naturally a post-order traversal (process left, then right, then node).
# - To do this iteratively, we simulate post-order traversal using a stack.
#
# Steps:
# 1. Initialize a stack to simulate recursion: store tuples (node, visited_flag).
# - visited_flag = False -> node is not yet processed
# - visited_flag = True  -> node's children are processed; now calculate height & balance
#
# 2. Initialize a dictionary 'heights' to store height of nodes.
# - Key: node
# - Value: height of the subtree rooted at node
# - This is DP applied, each node's height calculated once.
#
# 3. While stack is not empty:
#     a. Pop (node, visited)
#     b. If node is None -> continue
#     c. If visited is True -> process the node:
#         - Get left and right heights from heights dictionary (0 if None)
#         - If abs(left - right) > 1 -> tree is unbalanced -> return False
#         - Else -> store node's height = 1 + max(left_height, right_height) in heights
#     d. If visited is False -> push node back as (node, True)
#         - Push right child as (node.right, False)
#         - Push left child as (node.left, False)
#         - This ensures left -> right -> node order, exactly like post-order traversal.


def isBalancedIterative(root):
    if not root:
        return True

    # Stack to simulate recursion
    # Each element: (node, visited_flag)
    # visited_flag = False -> node's children not yet processed
    # visited_flag = True  -> node's children processed, ready to check balance
    stack = [(root, False)]

    # Dictionary to store heights of subtrees (DP applied)
    # Key: node, Value: height of subtree rooted at node
    heights = {}

    while stack:
        node, visited = stack.pop()

        if node is None:
            continue

        if visited:
            # Node's children already processed, calculate its height
            left_h = heights.get(node.left, 0)  # height of left subtree
            right_h = heights.get(node.right, 0)  # height of right subtree

            # Check balance at current node
            if abs(left_h - right_h) > 1:
                return False

            # Store current node's height in dictionary
            heights[node] = 1 + max(left_h, right_h)
        else:
            # Push node back with visited=True to process after children
            stack.append((node, True))

            # Push children onto stack for processing
            # Right child first, then left child (so left is processed first)
            stack.append((node.right, False))
            stack.append((node.left, False))

    # If no imbalance found, tree is balanced
    return True


def isBalancedIterativeLastVisited(root):
    if not root:
        return True

    stack = []
    heights = {}  # store subtree heights for DP
    last_visited = None
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left  # go as left as possible
        else:
            peek_node = stack[-1]
            # if right child exists and not yet visited, move to right child
            if peek_node.right and last_visited != peek_node.right:
                node = peek_node.right
            else:
                # process the node
                left_h = heights.get(peek_node.left, 0)
                right_h = heights.get(peek_node.right, 0)

                # check balance
                if abs(left_h - right_h) > 1:
                    return False

                heights[peek_node] = 1 + max(left_h, right_h)
                last_visited = stack.pop()

    return True
