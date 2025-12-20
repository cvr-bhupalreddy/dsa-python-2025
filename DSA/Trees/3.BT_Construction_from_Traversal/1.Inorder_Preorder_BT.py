# Inorder traversal gives:
#     - Left subtree
#     - Root
#     - Right subtree
#


# 1. preorder[preStart] is always the root.
# 2. Find root index in inorder.
# 3. Number of nodes in left subtree = rootIndex - inStart
# 4. Divide preorder and inorder into left and right ranges.
# 5. Build left and right subtrees independently.

# Left Subtree:
#     inorder   : inStart → idx - 1
#     preorder  : preStart + 1 → preStart + leftSize
#
# Right Subtree:
#     inorder   : idx + 1 → inEnd
#     preorder  : preStart + leftSize + 1 → preEnd



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    inIndex = {val: i for i, val in enumerate(inorder)}

    def build(inStart, inEnd, preStart, preEnd):
        if inStart > inEnd or preStart > preEnd:
            return None

        rootVal = preorder[preStart]
        root = TreeNode(rootVal)

        idx = inIndex[rootVal]
        leftSize = idx - inStart

        # Build left subtree
        root.left = build(
            inStart,
            idx - 1,
            preStart + 1,
            preStart + leftSize
        )

        # Build right subtree
        root.right = build(
            idx + 1,
            inEnd,
            preStart + leftSize + 1,
            preEnd
        )

        return root

    return build(0, len(inorder) - 1, 0, len(preorder) - 1)


class Solution:
    def buildTree(self, preorder, inorder):
        # Create a map to store indices
        # of elements in the inorder traversal
        inMap = {val: idx for idx, val in enumerate(inorder)}

        # Recursive helper function to build the tree
        def helper(preStart, preEnd, inStart, inEnd):
            # Base case: If the start indices
            # exceed the end indices, return null
            if preStart > preEnd or inStart > inEnd:
                return None

            # Create a new TreeNode with value
            # at the current preorder index
            root_val = preorder[preStart]
            root = TreeNode(root_val)

            # Find the index of the current root
            # value in the inorder traversal
            inRoot = inMap[root_val]

            # Calculate the number of
            # elements in the left subtree
            numsLeft = inRoot - inStart

            # Recursively build the left subtree
            root.left = helper(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)

            # Recursively build the right subtree
            root.right = helper(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)

            # Return the current root node
            return root

        # Call the helper function to build the tree
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

    # Function to print the
    # inorder traversal of a tree
    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data, end=" ")
            self.printInorder(root.right)

    # Function to print the
    # given list
    def printList(self, lst):
        print(" ".join(map(str, lst)))


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]

    sol = Solution()

    print("Inorder List: ", end="")
    sol.printList(inorder)

    print("Preorder List: ", end="")
    sol.printList(preorder)

    root = sol.buildTree(preorder, inorder)

    print("Inorder of Unique Binary Tree Created:")
    sol.printInorder(root)
    print()
