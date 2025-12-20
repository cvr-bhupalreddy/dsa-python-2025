# - Preorder first element is the root.
#     - Elements less than root belong to left subtree.
#     - Elements greater than root belong to right subtree.
# - Use divide-and-conquer:
#     - Maintain index pointer to traverse preorder array
#     - Maintain min/max range for current subtree
# - Recursive construction ensures correct BST structure.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bstFromPreorder(preorder):
    index = 0  # pointer to current root in preorder

    def build(bound=float('inf')):
        nonlocal index
        if index == len(preorder) or preorder[index] > bound:
            return None

        root_val = preorder[index]
        index += 1
        root = TreeNode(root_val)

        # Build left subtree: values < root_val
        root.left = build(root_val)

        # Build right subtree: values > root_val but < bound
        root.right = build(bound)

        return root

    return build()


def bstFromPreorderSimple(preorder):
    inorder = sorted(preorder)  # inorder is sorted preorder

    # Map value → index in inorder for quick lookup
    idx_map = {val: i for i, val in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        in_index = idx_map[root_val]
        left_count = in_index - in_start

        # Build left subtree
        root.left = build(pre_start + 1, pre_start + left_count, in_start, in_index - 1)
        # Build right subtree
        root.right = build(pre_start + left_count + 1, pre_end, in_index + 1, in_end)

        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

# - Postorder last element is the root.
# - Elements less than root belong to left subtree.
# - Elements greater than root belong to right subtree.
# - Process from end of array.
# - Maintain min/max bounds to ensure BST validity.
# - Recursive construction builds right subtree first, then left subtree.


def bstFromPostorder(postorder):
    index = len(postorder) - 1  # start from end

    def build(bound=float('-inf')):
        nonlocal index
        if index < 0 or postorder[index] < bound:
            return None

        root_val = postorder[index]
        index -= 1
        root = TreeNode(root_val)

        # Build right subtree first: values > bound and < root_val
        root.right = build(root_val)

        # Build left subtree: values < root_val
        root.left = build(bound)

        return root

    return build()


# 1. For BST, inorder traversal is always the sorted order of elements.
# 2. If we have preorder (root → left → right) or postorder (left → right → root):
#     - We can sort the array to get inorder.
# 3. Then, we can use **standard divide-and-conquer** (like binary tree from inorder + preorder/postorder):
#     - Preorder + inorder → root = preorder[0], split left/right in inorder
#     - Postorder + inorder → root = postorder[-1], split left/right in inorder
# 4. Recurse for left and right subtrees.


def bstFromPostorderSimple(postorder):
    inorder = sorted(postorder)
    idx_map = {val: i for i, val in enumerate(inorder)}

    def build(post_start, post_end, in_start, in_end):
        if post_start > post_end or in_start > in_end:
            return None

        root_val = postorder[post_end]
        root = TreeNode(root_val)

        in_index = idx_map[root_val]
        left_count = in_index - in_start

        # Build left subtree
        root.left = build(post_start, post_start + left_count - 1, in_start, in_index - 1)
        # Build right subtree
        root.right = build(post_start + left_count, post_end - 1, in_index + 1, in_end)

        return root

    return build(0, len(postorder) - 1, 0, len(inorder) - 1)
