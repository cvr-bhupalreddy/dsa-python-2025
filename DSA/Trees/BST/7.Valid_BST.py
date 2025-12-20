# - Use DFS recursion.
# - Keep track of valid range [min_val, max_val] for each node.
# - For root, range = (-inf, +inf)
# - For left child: range = (min_val, root.val)
# - For right child: range = (root.val, max_val)
# - If any node violates range → tree is invalid
# - Returns True if all nodes satisfy BST property


def isValidBST(root):
    def dfs(node, low, high):
        if not node:
            return True
        # Node value must be in (low, high)
        if node.val <= low or node.val >= high:
            return False
        # Check left and right subtrees with updated bounds
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float('-inf'), float('inf'))

#
# - Inorder traversal of BST gives sorted sequence.
# - Traverse tree iteratively using stack.
# - Keep track of previous visited node value.
# - If current node value ≤ previous → not a BST
# - Return True if entire inorder sequence is strictly increasing


def isValidBSTIterative(root):
    stack = []
    prev = float('-inf')
    curr = root

    while stack or curr:
        # Go as left as possible
        while curr:
            stack.append(curr)
            curr = curr.left

        # Visit node
        curr = stack.pop()
        if curr.val <= prev:
            return False
        prev = curr.val

        # Move to right subtree
        curr = curr.right

    return True
