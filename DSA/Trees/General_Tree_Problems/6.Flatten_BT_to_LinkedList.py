# Problem Definition:
# ------------------------------------------------------------
# Given a binary tree, flatten it into a linked list in-place.
# The linked list must follow PREORDER traversal:
# ROOT → LEFT → RIGHT
#
# Rules:
# • Use right pointers as "next"
# • Set all left pointers to None


# Preorder traversal = ROOT → LEFT → RIGHT
#
# Flattening means:
#     • Visit nodes in preorder
#     • Connect each node’s right pointer to the next preorder node
#     • Remove all left links

# APPROACH 1: RECURSIVE (Converse Postorder Traversal Right->Left->Root )
# Traverse the tree in reverse preorder: RIGHT → LEFT → ROOT
#
# Maintain a global "prev" pointer:
#     • At each node:
#     - node.right = prev
#     - node.left  = None
#     - prev = node
#
# This builds the list backward.

# WHY IT WORKS
# • Reverse preorder ensures next node is already processed
# • prev always points to the next node in preorder sequence
# • Linking happens bottom-up


class Solution:
    def flattenHelper(self, root):
        if not root:
            return

        self.flattenHelper(root.right)
        self.flattenHelper(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

    def flatten(self, root):
        self.prev = None  # RESET
        self.flattenHelper(root)


class Solution_Closure:
    def flatten(self, root):
        prev = None

        def dfs(node):
            nonlocal prev
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = prev
            node.left = None
            prev = node

        dfs(root)


class Solution1:  # this will not work always because ,
    # leetcode will reuse Solution object, and we are not resetting prev
    # above version is doing that or else we can use closure concept need to study that
    # Instance variables will not reset automatically
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root


# APPROACH 2: ITERATIVE USING STACK
#
# Simulate preorder traversal using a stack.
#
# At each step:
# • Pop current node
# • Push right child first, then left child
# • Link previous node’s right to current node
# • Set previous.left = None

def flatten_iterative_stack(root):
    if not root:
        return

    stack = [root]
    prev = None

    while stack:
        curr = stack.pop()

        if prev:
            prev.right = curr
            prev.left = None

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

        prev = curr


# above code is working , I wrote a code which is not working
# Need to debug why it's not working '

# Flattening requires linking to the PREVIOUS node
# Stack[-1] is a FUTURE node (and not guaranteed correct)


# APPROACH 3: MORRIS TRAVERSAL
#     For each node:
#     • If node has left child:
#         - Find rightmost node in left subtree (predecessor)
#         - Connect predecessor.right to node.right
#         - Move left subtree to right
#         - Set left = None
# • Move to node.right


def flatten_morris(root):
    node = root
    while node:
        if node.left:
            predecessor = node.left
            while predecessor.right:
                predecessor = predecessor.right
            predecessor.right = node.right
            node.right = node.left
            node.left = None
        node = node.right
    return root
