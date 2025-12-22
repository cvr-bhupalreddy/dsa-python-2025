from collections import defaultdict


def bridges(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    visited = [False] * n
    result = []

    time = 0

    def dfs(u):
        nonlocal time
        visited[u] = True
        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)

                low[u] = min(low[u], low[v])

                # Bridge condition
                if low[v] > disc[u]:
                    result.append((u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return result
