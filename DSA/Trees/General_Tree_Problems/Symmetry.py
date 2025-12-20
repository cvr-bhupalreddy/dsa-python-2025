class Solution:
    def is_symmetric(self, root):
        if not root:
            return True
        return self.symmetry(root.left, root.right)

    def symmetry(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.data == right.data and self.symmetry(left.left, right.right) and self.symmetry(left.right, right.left)
