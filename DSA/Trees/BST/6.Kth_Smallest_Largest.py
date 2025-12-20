# 1. Perform inorder traversal (Left → Root → Right)
# 2. Maintain a counter k
# 3. Decrement k when visiting each node
# 4. When k becomes 0, current node is the answer


def kthSmallest(root, k):
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1

        if k == 0:
            return root.val

        root = root.right


def kthSmallest_recursive(root, k):
    # Inner DFS function to perform inorder traversal
    def dfs(node):
        nonlocal k  # allows us to modify k from outer scope

        # BASE CASE:
        # If current node is None, nothing to process
        if not node:
            return None

        # STEP 1: Traverse LEFT subtree first (inorder)
        # dfs(node.left) returns:
        #   - None  → kth element NOT found in left subtree
        #   - value → kth element FOUND in left subtree
        left = dfs(node.left)

        # STEP 2: EARLY EXIT CHECK
        # If kth element was already found in left subtree,
        # immediately return it upward without further traversal
        if left is not None:
            return left

        # STEP 3: PROCESS CURRENT NODE
        # We are "visiting" this node in inorder sequence
        k -= 1  # decrement k as this node is visited

        # If k becomes 0, this is the kth smallest element
        if k == 0:
            return node.val  # return answer immediately

        # STEP 4: Traverse RIGHT subtree
        # Only executed if:
        # - left subtree didn't contain answer
        # - current node wasn't kth
        return dfs(node.right)

    # Start DFS from root
    return dfs(root)


# 1. Perform reverse inorder traversal (Right → Root → Left)
# 2. Maintain a counter k
# 3. Decrement k when visiting each node
# 4. When k becomes 0, current node is the answer


def kthLargest(root, k):
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.right

        root = stack.pop()
        k -= 1

        if k == 0:
            return root.val

        root = root.left

# Morris Traversal
#
# - Morris traversal does INORDER traversal without stack/recursion
# - It temporarily modifies tree by creating "threads"
# - Each edge is visited at most twice
# - Tree is fully restored after traversal


# 1. Perform Morris inorder traversal (Left → Root → Right)
# 2. Maintain counter k
# 3. Decrement k when a node is visited
# 4. When k becomes 0 → current node is kth smallest


def kthSmallest_morris(root, k):
    curr = root

    while curr:
        if curr.left is None:
            # Visit current node
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        else:
            # Find inorder predecessor
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right

            if pred.right is None:
                # Create thread
                pred.right = curr
                curr = curr.left
            else:
                # Thread exists -> remove it and visit node
                pred.right = None
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
