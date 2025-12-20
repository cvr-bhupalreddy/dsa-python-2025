# What is Morris Traversal?
#
# Morris Traversal is a tree traversal technique
# that performs inorder or preorder traversal
# using O(1) extra space.
#
# It avoids recursion and avoids stack usage
# by temporarily modifying the tree structure.

# Goal: Traverse a binary tree in inorder (Left → Root → Right)
# without recursion or stack, i.e., O(1) extra space.
#
# Observation:
# - Standard inorder uses a stack to remember nodes.
# - Morris traversal temporarily modifies the tree:
# - Creates a “thread” from a node's inorder predecessor back to itself.
# - This simulates the stack: when we finish left subtree, we can return to root.
# - Each edge is visited at most twice:
# - First: create thread (unvisited)
# - Second: remove thread (visited)


# For each node:
# - If the node has no left child:
#     • Visit the node
#     • Move to the right child
# - If the node has a left child:
# • Find the rightmost node (predecessor) in the left subtree
# • If predecessor.right is NULL:
#     - Create a temporary thread to current node
#     - Move current to left child
# • Else (thread already exists):
#     - Remove the thread
#     - Visit the current node
#     - Move to right child
#
# Temporary threads allow returning to a node
# after finishing its left subtree without a stack.


# Why Morris Traversal Works
# - In inorder traversal, after finishing left subtree we must return to the parent.
# - Morris traversal creates a temporary link from inorder predecessor back to the parent.
# - This simulates recursion using tree pointers.
# - Tree is restored to original structure at the end.

def morrisInorder_annotated(root):
    curr = root

    while curr:
        if curr.left is None:
            # ---------------- CASE 1 ----------------
            # No left subtree: visit current node directly
            print(curr.val)  # visit node
            curr = curr.right
        else:
            # ---------------- CASE 2 ----------------
            # Find inorder predecessor in left subtree
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right

            if pred.right is None:
                # ---------------- CREATE THREAD ----------------
                # Left subtree unvisited: create thread from pred → curr
                pred.right = curr
                # If you want preorder before moving to left visit the node
                curr = curr.left  # move left to visit subtree
            else:
                # ---------------- REMOVE THREAD ----------------
                # Left subtree visited: thread exists
                pred.right = None  # remove thread
                print(curr.val)  # visit node , for Inorder before moving to right visit node then move to right
                curr = curr.right  # move to right subtree


def morrisInorder(root):
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result


def morrisPreorder(root):
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current
                result.append(current.val)  # this is the only difference for Inorder and Preorder
                current = current.left
            else:
                predecessor.right = None
                current = current.right

    return result
