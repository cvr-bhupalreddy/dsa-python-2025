# Diameter of a binary tree:
#     The diameter (or width) of a binary tree is the length of the longest path
#     between any two nodes in the tree. The path may or may not pass through the root.
#
# Length is measured in number of edges between nodes.


# Approach 1: Naive Recursive (Compute Height Separately)
#
# Idea:
# - For each node, compute height of left and right subtree separately.
# - Diameter at node = left_height + right_height
# - Recursively compute diameter for all nodes.
#     - Return max diameter among all nodes.


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameterNaive(root):
    if not root:
        return 0

    left_diameter = diameterNaive(root.left)
    right_diameter = diameterNaive(root.right)

    left_height = height(root.left)
    right_height = height(root.right)

    current_diameter = left_height + right_height  # edges
    return max(current_diameter, left_diameter, right_diameter)


# Approach 2: Optimized Recursive / DP (Single Traversal)
# Idea:
# - Use post-order traversal.
# - For each node, compute:
#     - left_height, right_height
#     - current diameter = left_height + right_height
#     - Keep a global variable to store max diameter found so far.
# - Each node’s height calculated only once -> DP applied


def diameterOptimized(root):
    max_diameter = [0]  # use list to allow updates in nested function

    def height(node):
        if not node:
            return 0
        left_h = height(node.left)
        right_h = height(node.right)

        # update max diameter at this node
        max_diameter[0] = max(max_diameter[0], left_h + right_h)

        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter[0]


def diameterSingleReturn(root):
    max_diameter = [0]

    def dfs(node):
        if not node:
            return 0  # height
        left_h = dfs(node.left)
        right_h = dfs(node.right)

        # update max diameter
        max_diameter[0] = max(max_diameter[0], left_h + right_h)

        return 1 + max(left_h, right_h)  # return height

    dfs(root)
    return max_diameter[0]


def diameterIterative(root):
    if not root:
        return 0

    stack = []
    heights = {}
    max_diameter = 0
    last_visited = None
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                node = peek_node.right
            else:
                left_h = heights.get(peek_node.left, 0)
                right_h = heights.get(peek_node.right, 0)

                max_diameter = max(max_diameter, left_h + right_h)
                heights[peek_node] = 1 + max(left_h, right_h)

                last_visited = stack.pop()
                node = None

    return max_diameter

# Summary Table
# | Approach                     | Core Idea                                      | Time      | Space    | DP Applied|
# |-------------------------------|-----------------------------------------------|----------|-----------|-------------|
# | Naive Recursive               | Compute heights separately at each node       | O(n^2)   | O(h)      | ❌          |
# | Optimized Recursive (DP)      | Post-order, compute height & update max diameter| O(n)     | O(h)    | ✅          |
# | Single Return Value           | Encode diameter using global, return only height| O(n)     | O(h)    | ✅          |
# | Iterative Post-Order          | Stack + last_visited, store heights, update max | O(n)     | O(n)    | ✅          |
