# To return ALL shortest paths (not just one) you must change one key thing in Dijkstra / BFS:
# 🔑 Store MULTIPLE parents for each node, not just one
#
# Because:
# A node can be reached with the same shortest distance from different parents
# All those parents must be preserved to reconstruct all paths


# Rules during relaxation:
# | Case                  | Action                       |
# | --------------------- | ---------------------------- |
# | `new_dist < dist[v]`  | overwrite distance & parents |
# | `new_dist == dist[v]` | add another parent           |
# | `new_dist > dist[v]`  | ignore                       |


# Works Best With
# Unweighted graph → BFS
# Weighted graph (non-negative) → Dijkstra

import heapq
from collections import defaultdict


def dijkstra_all_parents(graph, src):
    dist = {node: float('inf') for node in graph}
    parents = defaultdict(set)

    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w

            if nd < dist[v]:
                dist[v] = nd
                parents[v] = {u}  # overwrite
                heapq.heappush(pq, (nd, v))

            elif nd == dist[v]:
                parents[v].add(u)  # add alternate parent

    return dist, parents


def all_shortest_paths(parents, src, dest):
    # 'res' will store all shortest paths from src to dest
    # Each path will be a list of nodes
    res = []

    # 'path' keeps the current path during backtracking
    # We start from destination and go backwards to source
    path = [dest]

    def dfs(u):
        """
        Backtracking DFS on the parents graph.
        'u' is the current node we are visiting (moving backward).
        """

        # Base case:
        # If we reached the source node,
        # we have found one complete shortest path
        if u == src:
            # path is currently in reverse order (dest → src)
            # Reverse it to get (src → dest)
            res.append(path[::-1])
            return

        # Recursive case:
        # Try all possible parents of current node
        for p in parents[u]:
            # Choose parent 'p'
            path.append(p)

            # Continue DFS from parent
            dfs(p)

            # Backtrack: remove last added node
            # so we can explore another parent
            path.pop()

    # Start DFS from destination node
    dfs(dest)

    # Return all collected shortest paths
    return res
