# Serialization   → Convert a binary tree into a string / array
# Deserialization → Convert that string / array back into the same tree
#
# APPROACH 1: Preorder DFS + NULL Markers (Most Popular)
# Idea
#     Use preorder traversal.
#     Store null nodes explicitly using a marker (e.g. '#').

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    result = []

    def dfs(node):
        if not node:
            result.append('#')
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ','.join(result)


def deserialize(data):
    values = iter(data.split(','))

    def dfs():
        val = next(values)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


# APPROACH 2: Level Order (BFS) Serialization
# Idea
#     Use queue and level order traversal.
#     Store null nodes.


def serialize_bfs(root):
    if not root:
        return ""

    q = deque([root])
    result = []

    while q:
        node = q.popleft()
        if node:
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            result.append('#')

    return ','.join(result)


def deserialize_bfs(data):
    if not data:
        return None

    values = data.split(',')
    root = TreeNode(int(values[0]))
    q = deque([root])
    i = 1

    while q:
        node = q.popleft()

        if values[i] != '#':
            node.left = TreeNode(int(values[i]))
            q.append(node.left)
        i += 1

        if values[i] != '#':
            node.right = TreeNode(int(values[i]))
            q.append(node.right)
        i += 1

    return root

#
# | Approach        | Time | Space | Preferred |
# |----------------|------|-------|-----------|
# | Preorder DFS   | O(n) | O(n)  | ⭐ BEST   |
# | Level Order BFS| O(n) | O(n)  | Good      |
# | Postorder DFS  | O(n) | O(n)  | Good      |
# | Inorder Only   | ❌   | ❌    | Invalid   |
