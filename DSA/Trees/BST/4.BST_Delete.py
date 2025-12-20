
# Approach:
# - Search node to delete
# - Three cases:
# 1. Leaf → delete directly
# 2. One child → replace node with child
# 3. Two children → replace node with inorder successor
# - Recur to maintain BST structure


# FORMAL PROOF (COPY-READY)
# 
# Claim:
# Inorder successor of a node in BST has at most one child. that also right child
#
# Proof:
# • Successor is leftmost node in right subtree
# • Therefore, it cannot have a left child
# • It may or may not have a right child
# • Hence, successor has at most one child
#
# That's why 2 children case is boiling down to 1 child or 0 child case

def deleteBST(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteBST(root.left, key)

    elif key > root.val:
        root.right = deleteBST(root.right, key)

    else:
        # ---------- CASE 1: Leaf node (0 children) ----------
        if not root.left and not root.right:
            return None

        # ---------- CASE 2: Only right child ----------
        if not root.left:
            return root.right

        # ---------- CASE 3: Only left child ----------
        if not root.right:
            return root.left

        # ---------- CASE 4: Two children ----------
        successor = root.right
        while successor.left:
            successor = successor.left

        root.val = successor.val
        root.right = deleteBST(root.right, successor.val)

    return root


def deleteBST_1(root, key):
    def minNode(node):
        while node.left:
            node = node.left
        return node

    if not root:
        return None

    if key < root.val:
        root.left = deleteBST(root.left, key)

    elif key > root.val:
        root.right = deleteBST(root.right, key)

    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        successor = minNode(root.right)
        root.val = successor.val
        root.right = deleteBST(root.right, successor.val)

    return root


def bst_delete_iterative(root, key):
    # parent will track the parent of current node
    parent = None

    # curr is used to traverse the BST
    curr = root

    # STEP 1: Search for the node to delete
    # Stop when curr becomes None (key not found)
    # or when curr.val == key (node found)
    while curr and curr.val != key:
        parent = curr  # store parent before moving down

        # Move left or right using BST property
        if key < curr.val:
            curr = curr.left
        else:
            curr = curr.right

    # If key is not found, return original tree
    if curr is None:
        return root

    # STEP 2: Case 3 - node has TWO children
    if curr.left and curr.right:
        # Find inorder successor (minimum in right subtree)
        succ_parent = curr
        succ = curr.right

        # Move to leftmost node in right subtree
        while succ.left:
            succ_parent = succ
            succ = succ.left

        # Copy successor's value to current node
        curr.val = succ.val

        # Now delete successor instead
        curr = succ
        parent = succ_parent

    # STEP 3: Case 1 & 2 - node has ZERO or ONE child
    # child will be None (leaf) or the single child
    child = curr.left if curr.left else curr.right

    # STEP 4: If deleting the root node
    if parent is None:
        return child

    # STEP 5: Reconnect parent to child
    if parent.left == curr:
        parent.left = child
    else:
        parent.right = child

    # Return updated root
    return root
