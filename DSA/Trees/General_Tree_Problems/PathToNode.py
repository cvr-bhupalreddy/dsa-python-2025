class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findPathRecursive(root, target):
    path = []

    def dfs(node):
        if not node:
            return False

        path.append(node.data)

        # if current node is target
        if node.data == target:
            return True

        # search in left or right subtree
        if dfs(node.left) or dfs(node.right):
            return True

        # backtrack if not found
        path.pop()
        return False

    dfs(root)
    return path


def findPathIterative(root, target):
    if not root:
        return []

    stack = [(root, [root.data])]

    while stack:
        node, path = stack.pop()

        if node.data == target:
            return path

        # push right first so left is processed first
        if node.right:
            stack.append((node.right, path + [node.right.data]))
        if node.left:
            stack.append((node.left, path + [node.left.data]))

    return []
