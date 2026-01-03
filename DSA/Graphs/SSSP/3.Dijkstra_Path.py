# Algorithm Steps
#
# Initialize:
#     dist[node] = ∞
#     parent[node] = None
#
# Run Dijkstra normally
# For every successful relaxation → update parent
# Reconstruct path using parent


import heapq


# def dijkstra(n, edges, src):
#     graph = defaultdict(list)
#     for u, v, w in edges:
#         graph[u].append((v, w))
def dijkstra_with_path(graph, src):
    dist = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    dist[src] = 0
    pq = [(0, src)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        # ignore outdated entries
        if curr_dist > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > curr_dist + w:
                dist[v] = curr_dist + w
                parent[v] = u  # 🔑 track path
                heapq.heappush(pq, (dist[v], v))

    return dist, parent


def get_path(parent, src, dest):
    path = []
    curr = dest

    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()

    if path[0] == src:
        return path
    return []  # no path exists


# Edge Cases to Mention in Interviews
# | Case                    | Handling                  |
# | ----------------------- | ------------------------- |
# | No path                 | parent[dest] remains None |
# | Multiple shortest paths | One valid path returned   |
# | Source = Destination    | Path is `[src]`           |


# Time & Space Complexity
# | Component            | Complexity       |
# | -------------------- | ---------------- |
# | Dijkstra             | O((V + E) log V) |
# | Path reconstruction  | O(V)             |
# | Extra space (parent) | O(V)             |
