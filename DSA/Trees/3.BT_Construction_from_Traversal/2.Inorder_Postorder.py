# 1. postorder[postEnd] is always the root.
# 2. Find root index in inorder.
# 3. Number of nodes in left subtree = rootIndex - inStart
# 4. Divide inorder and postorder into left and right ranges.
# 5. Build left and right subtrees independently.


# Root: postorder[postEnd]
#
# Left Subtree:
#     inorder   : inStart → idx - 1
#     postorder : postStart → postStart + leftSize - 1
#
# Right Subtree:
#     inorder   : idx + 1 → inEnd
#     postorder : postStart + leftSize → postEnd - 1


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(inorder, postorder):
    inIndex = {val: i for i, val in enumerate(inorder)}

    def build(inStart, inEnd, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd:
            return None

        rootVal = postorder[postEnd]
        root = TreeNode(rootVal)

        idx = inIndex[rootVal]
        leftSize = idx - inStart

        # Build left subtree
        root.left = build(
            inStart,
            idx - 1,
            postStart,
            postStart + leftSize - 1
        )

        # Build right subtree
        root.right = build(
            idx + 1,
            inEnd,
            postStart + leftSize,
            postEnd - 1
        )

        return root

    return build(0, len(inorder) - 1, 0, len(postorder) - 1)
