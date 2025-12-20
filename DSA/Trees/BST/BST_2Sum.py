# 1️⃣ Using Inorder + Two Pointers
#
# - Inorder traversal of BST gives sorted array of node values.
# - Use two pointers (left, right) on sorted array:
#     - sum < target → move left pointer right
#     - sum > target → move right pointer left
#     - sum == target → return True
# - Time: O(n), Space: O(n) for array


def twoSumBST(root, target):
    # Step 1: Inorder traversal to get sorted array
    def inorder(node, arr):
        if not node:
            return
        inorder(node.left, arr)
        arr.append(node.val)
        inorder(node.right, arr)

    nums = []
    inorder(root, nums)

    # Step 2: Two pointers
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return False


# 2️⃣ Using Two BST Iterators (O(h) Space)
#
# - Use two iterators:
#     1. Normal BST iterator → next smallest
#     2. Reverse BST iterator → next largest
# - Start with smallest and largest
# - Move pointers inward based on sum comparison
# - Time: O(n), Space: O(h)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return bool(self.stack)

    def next(self):
        node = self.stack.pop()
        val = node.data
        if node.right:
            self._push_left(node.right)
        return val


class BSTReverseIterator:
    def __init__(self, root):
        self.stack = []
        self._push_right(root)

    def _push_right(self, node):
        while node:
            self.stack.append(node)
            node = node.right

    def hasPrev(self):
        return bool(self.stack)

    def prev(self):
        node = self.stack.pop()
        val = node.data
        if node.left:
            self._push_right(node.left)
        return val


def findTarget(root, k):
    if not root:
        return False

    left_it = BSTIterator(root)
    right_it = BSTReverseIterator(root)

    i = left_it.next()
    j = right_it.prev()

    while i < j:
        total = i + j
        if total == k:
            return True
        elif total < k:
            if left_it.hasNext():
                i = left_it.next()
            else:
                break
        else:
            if right_it.hasPrev():
                j = right_it.prev()
            else:
                break

    return False


class BSTIterator:
    def __init__(self, root, forward=True):
        self.stack = []
        self.forward = forward  # True = next smallest, False = next largest
        if forward:
            self._pushLeft(root)
        else:
            self._pushRight(root)

    def _pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def _pushRight(self, node):
        while node:
            self.stack.append(node)
            node = node.right

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        val = node.val
        if self.forward:
            if node.right:
                self._pushLeft(node.right)
        else:
            if node.left:
                self._pushRight(node.left)
        return val


def twoSumBSTIterative(root, target):
    if not root:
        return False

    left_iter = BSTIterator(root, forward=True)  # smallest to largest
    right_iter = BSTIterator(root, forward=False)  # largest to smallest

    left_val = left_iter.next() if left_iter.hasNext() else None
    right_val = right_iter.next() if right_iter.hasNext() else None

    while left_val is not None and right_val is not None and left_val < right_val:
        curr_sum = left_val + right_val
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left_val = left_iter.next() if left_iter.hasNext() else None
        else:
            right_val = right_iter.next() if right_iter.hasNext() else None

    return False
