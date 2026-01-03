# • BFS while tracking parent
# • If a visited neighbor is NOT parent → cycle exists

# Plain BFS can detect only cycles in Undirected graph

from collections import deque, defaultdict


def has_cycle_bfs(graph):
    visited = set()

    for start in graph:
        if start not in visited:
            queue = deque([(start, None)])
            visited.add(start)

            while queue:
                u, parent = queue.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, u))
                    elif v != parent:
                        return True  # cycle detected

    return False


def cycle_kahn(graph):
    indegree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([u for u in graph if indegree[u] == 0])
    count = 0

    while queue:
        u = queue.popleft()
        count += 1
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # If all nodes not processed → cycle exists
    return count != len(graph)
# Problem                    | BFS Technique Used
# ---------------------------|-------------------
# Bipartite check            | Coloring (0/1)
# Odd-length cycle           | Same color conflict
# Cycle (Undirected)         | Parent tracking
# Cycle (Directed)           | Kahn’s algorithm
