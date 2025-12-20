# Design an iterator over a Binary Search Tree (BST) with the following methods:
#
# 1. next(): Returns the next smallest number in the BST.
# 2. hasNext(): Returns True if there are more nodes to visit.
#
# Constraints:
# - Space-efficient: O(h) space (h = height of BST)
# - next() should return elements in **sorted order**.

# Core Idea / Approach
# - Inorder traversal of BST produces sorted sequence.
# - Instead of generating the entire sequence upfront (O(n) space), simulate iterative inorder traversal using a stack
# - Stack stores the path from root to current node (or its leftmost descendant).
# - Each call to next():
#     1. Pop node from stack (next smallest element)
#     2. If popped node has right child, push all its left descendants to stack
# - hasNext(): simply checks if stack is non-empty


# Why It Works
# - Inorder traversal visits nodes in ascending order.
# - Stack always contains the nodes that are next in inorder sequence.
# - By pushing left children initially, and right children when popping, we preserve correct order.
# - Space complexity is O(h) (height of tree) instead of O(n)


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left_branch(root)

    def _push_left_branch(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        value = node.data
        if node.right:
            self._push_left_branch(node.right)
        return value


# - Reverse inorder traversal: Right → Root → Left gives descending order.
# - Stack stores path from root to current node (or its rightmost descendant).
# - Each call to next():
#     1. Pop top node from stack (current largest)
#     2. If node has left child, push all its right descendants to stack
# - hasNext(): checks if stack is non-empty


class BSTReverseIterator:
    def __init__(self, root):
        # Stack stores nodes yet to be visited in descending order
        self.stack = []
        # Initialize stack with all rightmost nodes from root
        self._pushRight(root)

    # Helper: push node and all its right descendants to stack
    def _pushRight(self, node):
        while node:
            self.stack.append(node)  # push current node
            node = node.right  # move to right child (larger values)

    # Return True if there are more elements
    def hasNext(self):
        return len(self.stack) > 0

    # Return next largest element
    def next(self):
        if not self.hasNext():
            return None

        # Pop the top node (current largest)
        node = self.stack.pop()
        result = node.val  # this is the next largest value

        # If node has left child, push all its right descendants
        # because those are next largest nodes after current
        if node.left:
            self._pushRight(node.left)

        return result
