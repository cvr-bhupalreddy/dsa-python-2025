# A binary tree satisfies the Children Sum Property if,
# for every node:
#     node.val = (left child value) + (right child value)
#
# If a child is missing, its value is treated as 0.
# Leaf nodes always satisfy the property.


def isChildrenSum(root):
    if not root or (not root.left and not root.right):
        return True

    left = root.left.val if root.left else 0
    right = root.right.val if root.right else 0

    return (root.val == left + right and
            isChildrenSum(root.left) and
            isChildrenSum(root.right))

# 2️⃣ Convert Binary Tree to Follow Children Sum Property
# Allowed Operation
#     You can increment node values only (no decrements)


# Optimal Recursive Solution
#     - Use post-order traversal
#     - Ensure children sum matches parent
#     - If children sum < parent → increment children
#     - If children sum > parent → update parent


def convertChildrenSum(root):
    if not root:
        return

    if not root.left and not root.right:
        return

    convertChildrenSum(root.left)
    convertChildrenSum(root.right)

    left = root.left.val if root.left else 0
    right = root.right.val if root.right else 0

    total = left + right

    if total >= root.val:
        root.val = total
    else:
        diff = root.val - total
        if root.left:
            root.left.val += diff
        elif root.right:
            root.right.val += diff
