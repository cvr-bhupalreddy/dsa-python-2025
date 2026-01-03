from collections import defaultdict, deque
import math

# 🧠 Mental Model
#     Topo order → left to right
#     Distances flow forward
#     Each node finalized once


# 🧠 Core Idea
#
# Topologically sort the DAG
#     Ensures all edges go left → right
#     For any edge u → v, u comes before v
#
# Initialize distances
#     dist[source] = 0
#     All other nodes → ∞
#
# Relax edges in topological order
#     For each node u in topo order:
#     For each outgoing edge (u → v, weight w):
#         if dist[u] + w < dist[v]:
#             dist[v] = dist[u] + w
#
# Each edge is relaxed exactly once

def shortest_path_dag(n, edges, source):
    """
    n      : number of vertices (0 to n-1)
    edges  : list of (u, v, w) -> directed edge u -> v with weight w
    source : starting node
    """

    # -------------------------------
    # STEP 1: Build adjacency list
    # -------------------------------
    graph = defaultdict(list)
    indegree = [0] * n

    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    # -------------------------------
    # STEP 2: Topological Sort (Kahn)
    # -------------------------------
    queue = deque()

    # nodes with indegree 0 can start
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v, _ in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # -------------------------------
    # STEP 3: Initialize distances
    # -------------------------------
    dist = [math.inf] * n
    dist[source] = 0  # distance to source is 0

    # -------------------------------
    # STEP 4: Relax edges in topo order
    # -------------------------------
    for u in topo_order:

        # if u is unreachable, skip
        if dist[u] == math.inf:
            continue

        for v, weight in graph[u]:
            # relaxation step
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    return dist

# ⏱ Complexity
# | Operation  | Cost         |
# | ---------- | ------------ |
# | Topo Sort  | O(V + E)     |
# | Relaxation | O(E)         |
# | **Total**  | **O(V + E)** |


# 🧠 Final Mental Model
# Topo order ensures:
# all incoming paths known before relaxing edges
# → shortest path finalized in one pass

# 🔁 Comparison
# | Algorithm         | Works with Cycles | Negative Weights   | Time       |
# | ----------------- | ----------------- | ----------------   | ---------- |
# | DAG Shortest Path | ❌ No              | ✔ Yes             | O(V+E)     |
# | Dijkstra          | ✔ Yes             | ❌ No              | O(E log V) |
# | Bellman-Ford      | ✔ Yes             | ✔ Yes              | O(VE)      |
