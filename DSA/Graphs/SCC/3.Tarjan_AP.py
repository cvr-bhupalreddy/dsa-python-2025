# disc[u] = discovery time of node u
# low[u]  = lowest discovery time reachable from u (back edge allowed)
#
# DFS Tree Edge: (u → v)
# Back Edge:     (u → ancestor)
#
# low[u] = min(
#     disc[u],
#     disc[v]  for back edges,
#     low[v]   for DFS tree edges
# )


# ✅ Articulation Point (AP)
# 1) Root node with ≥ 2 DFS children
# 2) Non-root node u where: low[v] >= disc[u]  (for some child v)


# ✅ Bridge
# Edge (u, v) is a bridge if:
# low[v] > disc[u]

from collections import defaultdict


def articulation_points(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    visited = [False] * n
    ap = [False] * n

    time = 0

    def dfs(u):
        nonlocal time
        visited[u] = True
        disc[u] = low[u] = time
        time += 1
        children = 0

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                # Case 1: Root AP
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                # Case 2: Non-root AP
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return [i for i in range(n) if ap[i]]


# • During DFS:
#     - Handle ONLY non-root AP condition: low[v] >= disc[u]
#
# • After DFS(u) finishes:
#     - If u is root (parent == -1)
#     - AND it has more than 1 DFS child
# → mark it as articulation point


def articulation_points_simple(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    visited = [False] * n
    ap = [False] * n

    time = 0

    def dfs(u):
        nonlocal time
        visited[u] = True
        disc[u] = low[u] = time
        time += 1

        children = 0

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                # Non-root articulation condition
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

        # Root articulation condition (handled LAST)
        if parent[u] == -1 and children > 1:
            ap[u] = True

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return [i for i in range(n) if ap[i]]
