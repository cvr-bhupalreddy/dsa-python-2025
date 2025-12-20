# Given a BST, an "inverted pair" is a pair of nodes where
# the BST property is violated:
#
# - For a valid BST: Inorder traversal must be strictly increasing.
# - If there exists any pair (X, Y) such that X appears **before** Y in inorder traversal
# but X.val > Y.val → it's an inverted pair.
#
# Goal: Identify such pair(s) which indicate BST is not valid.


# 1. Perform **inorder traversal** (Left → Root → Right).
# 2. Maintain a pointer `prev` to previous node visited.
# 3. For each current node:
#     - If prev.val > current.val → inverted pair detected
# 4. Depending on requirement:
#     - Record first and second violation nodes
#     - Can detect multiple inverted pairs if BST has more than one violation


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findInvertedPairs(root):
    """
    Returns a list of inverted pairs (prev, curr) where prev.val > curr.val
    """
    inverted_pairs = []
    prev = None

    def inorder(node):
        nonlocal prev
        if not node:
            return
        # Visit left subtree
        inorder(node.left)

        # Check for inversion
        if prev and prev.val > node.val:
            inverted_pairs.append((prev.val, node.val))  # store as a tuple

        # Update previous node
        prev = node

        # Visit right subtree
        inorder(node.right)

    inorder(root)
    return inverted_pairs


def findInvertedPairsIterative(root):
    """
    Returns a list of inverted pairs (prev, curr) where prev.val > curr.val
    """
    stack = []  # stack to store nodes yet to be visited
    curr = root  # start from root
    prev = None  # previous visited node in inorder
    inverted_pairs = []  # list to store all inverted pairs

    while stack or curr:
        # ----------------- STEP 1: Go as left as possible -----------------
        while curr:
            stack.append(curr)  # push current node
            curr = curr.left  # move left

        # ----------------- STEP 2: Visit node -----------------
        curr = stack.pop()  # pop the top node from stack (next in inorder)

        # ----------------- STEP 3: Check for inversion -----------------
        if prev and prev.val > curr.val:
            # prev appears before curr but prev.val > curr.val → inverted pair
            inverted_pairs.append((prev.val, curr.val))

        # ----------------- STEP 4: Update prev -----------------
        prev = curr

        # ----------------- STEP 5: Move to right subtree -----------------
        curr = curr.right

    return inverted_pairs


# - Inorder traversal of BST produces sorted sequence.
# - If two nodes are swapped, inorder sequence will have **inverted pairs**:
# 1. For adjacent swap: one inverted pair
# 2. For non-adjacent swap: two inverted pairs
# - Keep track of:
#     - first node (first violation)
#     - second node (last violation)
# - After traversal:
# - Swap values of first and second → BST restored
# - Can implement both recursively or iteratively


def recoverBSTRecursive(root):
    """
    Recover a BST where two nodes are swapped using recursive inorder traversal.
    """
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if not node:
            return

        # Visit left subtree
        inorder(node.left)

        # Check for inverted pair
        if prev and prev.val > node.val:
            if not first:
                # First violation: prev is first node
                first = prev
            # Second node may be updated multiple times in non-adjacent swap
            second = node

        # Update prev to current
        prev = node

        # Visit right subtree
        inorder(node.right)

    inorder(root)

    # Swap values to fix BST
    if first and second:
        first.val, second.val = second.val, first.val


def recoverBSTIterative(root):
    """
    Recover a BST where two nodes are swapped using iterative inorder traversal.
    """
    stack = []
    curr = root
    prev = first = second = None

    while stack or curr:
        # Step 1: Go as left as possible
        while curr:
            stack.append(curr)
            curr = curr.left

        # Step 2: Visit node
        curr = stack.pop()

        # Step 3: Detect inverted pair
        if prev and prev.val > curr.val:
            if not first:
                first = prev  # first violation
            second = curr  # second violation (updated if multiple)

        # Step 4: Update prev
        prev = curr

        # Step 5: Move to right
        curr = curr.right

    # Swap values of first and second to recover BST
    if first and second:
        first.val, second.val = second.val, first.val


def recoverTreeMorris(root):
    first = second = prev = None
    current = root

    while current:
        if current.left is None:
            if prev and prev.data > current.data:
                if not first:
                    first = prev
                second = current
            prev = current
            current = current.right
        else:
            pre = current.left
            while pre.right and pre.right != current:
                pre = pre.right

            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                if prev and prev.data > current.data:
                    if not first:
                        first = prev
                    second = current
                prev = current
                current = current.right

    if first and second:
        first.data, second.data = second.data, first.data
