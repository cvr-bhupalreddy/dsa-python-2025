from collections import deque, defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodesAtDistanceK(root, target, k):
    if not root:
        return []

    # Step 1: Build parent map
    parent = {}

    def build_parent(node, par=None):
        if not node:
            return
        parent[node] = par
        build_parent(node.left, node)
        build_parent(node.right, node)

    build_parent(root)

    # Step 2: BFS from target
    queue = deque([(target, 0)])
    visited = {target}
    result = []

    while queue:
        node, dist = queue.popleft()

        if dist == k:
            result.append(node.data)

        if dist > k:
            break

        for neighbor in (node.left, node.right, parent[node]):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return result
