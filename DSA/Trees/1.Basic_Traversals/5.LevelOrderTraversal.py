# LEVEL ORDER TRAVERSAL
# ------------------------------------------------------------
# Traverse the tree level by level.
# For each level, collect nodes from LEFT to RIGHT.
# Return a list where:
#     - Each index represents one level
#     - Each element is the list of nodes at that level
# ------------------------------------------------------------

#
# 1. If root is null, return empty result.
#
# 2. Initialize an empty queue.
#     Push root into queue.
# 3. Initialize empty result list.
# 4. While queue is not empty:
#     a. level_size = length of queue
#     (number of nodes at current level)
#
#     b. Initialize empty list current_level.
#     c. Repeat level_size times:
#         - Pop node from queue
#         - Add node value to current_level
#         - If left child exists, push to queue
#         - If right child exists, push to queue
#     d. Append current_level to result.
#
# 5. Return result.
# ------------------------------------------------------------


from collections import deque


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def level_order_with_level_number(root):
    if root is None:
        return []

    result = []  # [(level, [nodes])]
    queue = deque([root])
    level = 0

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append((level, current_level))
        level += 1

    return result


def levelOrder(self, root):
    if root is None:
        return []

    queue = deque([(root, 0)])
    result = []
    while queue:
        current, level = queue.popleft()

        if len(result) == level:  # Ensure a new sublist exists for this level
            result.append([])
        result[level].append(current.data)
        if current.left:
            queue.append((current.left, level + 1))
        if current.right:
            queue.append((current.right, level + 1))
    return result
