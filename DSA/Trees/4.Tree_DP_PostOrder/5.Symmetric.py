# Symmetric Binary Tree:
#     A binary tree is symmetric if the left subtree is a mirror image
#     of the right subtree.


# Idea:
# - Two trees are mirrors if:
#     1) Their root values are equal
#     2) Left subtree of one is mirror of right subtree of the other
#     3) Right subtree of one is mirror of left subtree of the other
#     - Recursively check mirror property.

from collections import deque


def isMirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False

    return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)


def isSymmetric(root):
    if not root:
        return True
    return isMirror(root.left, root.right)


def isSymmetricIterative(root):
    if not root:
        return True

    queue = deque()
    queue.append((root.left, root.right))

    while queue:
        left, right = queue.popleft()

        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True


def isSymmetricStack(root):
    if not root:
        return True

    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop()

        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        stack.append((left.left, right.right))
        stack.append((left.right, right.left))

    return True
