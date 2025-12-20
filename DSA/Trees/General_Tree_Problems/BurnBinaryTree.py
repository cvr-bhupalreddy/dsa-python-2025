from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minTimeToBurn(root, target):
    if not root:
        return 0

    # Step 1: Build parent map
    parent = {}

    def build_parent(node, par=None):
        if not node:
            return
        parent[node] = par
        build_parent(node.left, node)
        build_parent(node.right, node)

    build_parent(root)

    # Step 2: Locate the target node
    def findTarget(node, value):
        if not node:
            return None
        if node.data == value:
            return node
        return findTarget(node.left, value) or findTarget(node.right, value)

    target_node = findTarget(root, target)
    if not target_node:
        return 0

    # Step 3: BFS from target
    queue = deque([target_node])
    visited = {target_node}
    time = 0

    while queue:
        size = len(queue)
        any_burned = False

        for _ in range(size):
            node = queue.popleft()

            for neighbor in (node.left, node.right, parent[node]):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    any_burned = True

        # only increment time if fire spread in this round
        if any_burned:
            time += 1

    return time


def minTimeToBurn_BFS_Only(root, target):
    if not root:
        return 0

    parent = {}
    target_node = None

    # Step 1: BFS to mark parent and find target simultaneously
    queue = deque([root])
    while queue:
        node = queue.popleft()

        if node.data == target:
            target_node = node

        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    # Step 2: BFS from target_node to simulate burning
    if not target_node:
        return 0

    visited = {target_node}
    queue = deque([target_node])
    time = 0

    while queue:
        size = len(queue)
        burned = False

        for _ in range(size):
            node = queue.popleft()
            for neighbor in (node.left, node.right, parent.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    burned = True

        if burned:
            time += 1

    return time
