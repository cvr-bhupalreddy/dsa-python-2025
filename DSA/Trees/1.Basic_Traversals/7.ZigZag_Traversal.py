# GOAL
# ------------------------------------------------------------
# Traverse the tree level by level.
# Alternate the direction of traversal for each level:
#     - Level 0 → left to right
#     - Level 1 → right to left
#     - Level 2 → left to right
#     - ...
# Return a list of nodes for each level in correct order.
# ------------------------------------------------------------
#
#
# DATA STRUCTURE
#     ------------------------------------------------------------
#     Queue (FIFO) to process nodes level by level
#     List to store current level nodes
#     Flag variable (left_to_right) to track direction
#     ------------------------------------------------------------
#
#
# 1. If root is null, return empty result.
#
# 2. Initialize queue and push root into it.
# 3. Initialize result list.
# 4. Initialize left_to_right = True
#
# 5. While queue is not empty:
#     a. level_size = length of queue
#     b. Initialize empty list current_level
#     c. Repeat level_size times:
#         - Pop node from queue
#         - Append node.val to current_level
#         - If left child exists, push to queue
#         - If right child exists, push to queue
#     d. If left_to_right is False:
#         - Reverse current_level
#     e. Append current_level to result
#     f. Toggle left_to_right for next level
#
# 6. Return result
# ------------------------------------------------------------


from collections import deque


def zigzag_level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

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

        if not left_to_right:
            current_level.reverse()

        result.append(current_level)
        left_to_right = not left_to_right

    return result


# 1. If root is null, return empty result.
# 2. Initialize queue and push root.
# 3. Initialize result list.
# 4. Initialize left_to_right = True
#
# 5. While queue is not empty:
#     a. level_size = len(queue)
#     b. Initialize empty list current_level of size level_size
#     c. For i in range(level_size):
#         - Pop node from queue
#         - Determine index to insert based on direction:
#             • left_to_right → index = i
#             • right_to_left → index = level_size - 1 - i
#         - current_level[index] = node.val
#         - Push left and right children to queue if they exist
#     d. Append current_level to result
#     e. Toggle left_to_right
#
# 6. Return result


def zigzag_level_order_no_reverse(root):
    if root is None:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = [0] * level_size  # pre-allocate list

        for i in range(level_size):
            node = queue.popleft()

            # Determine index based on direction
            index = i if left_to_right else (level_size - 1 - i)
            current_level[index] = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
        left_to_right = not left_to_right

    return result
