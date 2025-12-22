from collections import deque, defaultdict


def bfs(n, edges, start):
    """
    n: number of nodes (0 to n-1)
    edges: list of (u, v)
    start: starting node
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph

    visited = [False] * n
    q = deque([start])
    visited[start] = True

    while q:
        u = q.popleft()
        print(u, end=" ")  # Process node

        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
