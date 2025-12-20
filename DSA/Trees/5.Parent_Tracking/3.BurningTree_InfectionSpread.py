# Burning Tree
#
# Problem:
#     Given a starting node,
#     fire spreads to adjacent nodes every second.
#     Return time to burn entire tree.


# Binary Tree Infection
#
# Problem:
#     Starting from a given node,
#     infection spreads to adjacent nodes every minute.
#     Return total time to infect entire tree.


from collections import deque


def minTime_BFS(root, target):
    if not root:
        return 0

    # Step 1: Build parent map
    parent = {root: None}
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    # Step 2: BFS from target
    visited = set([target])
    queue = deque([target])
    time = -1

    while queue:
        size = len(queue)
        time += 1

        for _ in range(size):
            node = queue.popleft()

            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

    return time


def minTime_BFS_1(root, target):
    if not root:
        return 0

    # Step 1: Build parent map
    parent = {root: None}
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    # Step 2: BFS from target (node, time)
    visited = set([target])
    queue = deque([(target, 0)])
    max_time = 0

    while queue:
        node, time = queue.popleft()
        max_time = max(max_time, time)

        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in visited:
                visited.add(nei)
                queue.append((nei, time + 1))

    return max_time


def minTime_DFS(root, target):
    parent = {}

    # Build parent map
    def build(node):
        if not node:
            return
        if node.left:
            parent[node.left] = node
            build(node.left)
        if node.right:
            parent[node.right] = node
            build(node.right)

    parent[root] = None
    build(root)

    visited = set()
    max_time = 0

    def dfs(node, time):
        nonlocal max_time
        if not node or node in visited:
            return
        visited.add(node)
        max_time = max(max_time, time)

        dfs(node.left, time + 1)
        dfs(node.right, time + 1)
        dfs(parent[node], time + 1)

    dfs(target, 0)
    return max_time
