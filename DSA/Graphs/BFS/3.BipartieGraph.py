# • Assign each node a color: 0 or 1
# • Start BFS from an unvisited node
# • Color start node as 0
# • For every edge (u → v):
#     - If v is uncolored → assign opposite color
#     - If v has same color as u → NOT bipartite
# • Repeat for all components


from collections import defaultdict, deque


def is_bipartite_coloring(graph):
    color = {}  # node -> 0 or 1

    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False  # conflict found

    return True


# Odd length cycle
#
# A graph is bipartite ⇔ It does NOT contain an odd-length cycle

# Odd length cycle will occur in same level nodes


def is_bipartite_bfs_odd_cycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    level = [0] * n

    for start in range(n):
        if visited[start]:
            continue

        queue = deque([start])
        visited[start] = True
        level[start] = 0

        while queue:
            u = queue.popleft()

            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    level[v] = level[u] + 1
                    queue.append(v)
                else:
                    # Same level ⇒ odd length cycle
                    if level[v] == level[u]:
                        return False

    return True
