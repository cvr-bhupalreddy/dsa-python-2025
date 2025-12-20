# Maximum Path Sum in Binary Tree:
#
# A path is any sequence of nodes connected by edges.
#     The path does NOT need to pass through the root.
#     The path must contain at least one node.
#
# Find the maximum possible sum of values along any path.


def maxDownward(node):
    if not node:
        return 0
    return max(0, node.val + max(maxDownward(node.left),
                                 maxDownward(node.right)))


def maxPathSumNaive(root):
    if not root:
        return float('-inf')

    left = maxDownward(root.left)
    right = maxDownward(root.right)

    current = left + root.val + right
    return max(current,
               maxPathSumNaive(root.left),
               maxPathSumNaive(root.right))


def maxPathSum(root):
    max_sum = [float('-inf')]

    def dfs(node):
        if not node:
            return 0

        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        # update global max path
        max_sum[0] = max(max_sum[0], left + node.val + right)

        # return max downward path
        return node.val + max(left, right)

    dfs(root)
    return max_sum[0]


def maxPathSumIterative(root):
    if not root:
        return 0

    stack = []
    last_visited = None
    node = root
    dp = {}  # node -> max downward path sum
    max_sum = float('-inf')

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                node = peek.right
            else:
                left = max(0, dp.get(peek.left, 0))
                right = max(0, dp.get(peek.right, 0))

                max_sum = max(max_sum, peek.val + left + right)
                dp[peek] = peek.val + max(left, right)

                last_visited = stack.pop()
                node = None

    return max_sum


# | Approach                   | Core Idea                                      | Time    | Space   | DP |
# |----------------------------|------------------------------------------------|---------|---------|----|
# | Naive Recursive            | Compute paths repeatedly                       | O(n^2)  | O(h)    | ❌ |
# | Optimized Recursive (DP)   | Post-order, update global max                  | O(n)    | O(h)    | ✅ |
# | Iterative Post-order       | Stack + last_visited + DP dictionary           | O(n)    | O(n)    | ✅ |
