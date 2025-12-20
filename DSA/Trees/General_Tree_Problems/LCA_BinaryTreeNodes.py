class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if not root:
        return None

    # If root is one of p or q
    if root.data == p or root.data == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If p and q are found in left and right subtree
    if left and right:
        return root

    # Either one side is None, return the non-None side
    return left if left else right


def lowestCommonAncestorIterative(root, p, q):
    parent = {root: None}
    stack = [root]

    # Build parent map
    while stack:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    # Collect ancestors of p
    ancestors = set()
    node = p
    while node:
        ancestors.add(node)
        node = parent[node]

    # Find first ancestor of q in p's ancestors
    node = q
    while node not in ancestors:
        node = parent[node]

    return node
