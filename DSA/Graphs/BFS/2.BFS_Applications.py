# ✅ Summary of BFS Patterns
#
# | Problem Type               | Key Idea                         |
# | -------------------------- | -------------------------------- |
# | Shortest path unweighted   | BFS level = distance             |
# | Connected components       | BFS from each unvisited node     |
# | Cycle detection undirected | BFS + parent                     |
# | Cycle detection directed   | BFS (Kahn / topological sort)    |
# | Bipartite check            | BFS + 2-coloring                 |
# | Spread problems            | Multi-source BFS with level/time |
# | Grid / Chess moves         | BFS in 2D with valid moves       |


# 1️⃣ Shortest Path in Unweighted Graph
#
# Core Idea:
#     guarantees shortest distance in unweighted graph.
#     Keep dist array to track distance from source.


from collections import defaultdict, deque


def bfs_shortest_path(n, edges, start):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected

    dist = [float('inf')] * n
    dist[start] = 0
    q = deque([start])

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


# 2️⃣ Number of Connected Components / Islands
# Core Idea:
#     Use BFS to traverse each unvisited node/component.
#     Count number of BFS calls → number of components.


def count_connected_components(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            count += 1
            q = deque([i])
            visited[i] = True
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
    return count


# 3️⃣ Cycle Detection in Undirected Graph
#
# Core Idea:
# BFS with parent tracking: neighbor visited & not parent → cycle.


def has_cycle_bfs_undirected(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    for start in range(n):
        if visited[start]:
            continue
        q = deque([(start, -1)])  # (node, parent)
        visited[start] = True
        while q:
            u, parent = q.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append((v, u))
                elif v != parent:
                    return True
    return False


# 5️⃣ Bipartite Graph Check
#
# Core Idea:
#     Use BFS to color nodes alternately.
#     Conflict in colors → not bipartite.

def is_bipartite(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * n  # 0: unvisited, 1: red, -1: blue
    for i in range(n):
        if color[i] != 0:
            continue
        q = deque([i])
        color[i] = 1
        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == 0:
                    color[v] = -color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True

# 6️⃣ Minimum Time to Spread Infection / Burn Tree / Rotting Oranges
#
# Core Idea:
#     Multi-source BFS.
#     Track time/level while traversing.
