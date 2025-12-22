# • Greedy algorithm
#     • Always expand the node with the minimum known distance
#     • Works ONLY when all edge weights are NON-NEGATIVE
#     • Uses priority queue (min-heap)


import heapq
from collections import defaultdict


def dijkstra(n, edges, src):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float('inf')] * n
    dist[src] = 0

    pq = [(0, src)]  # (distance, node)

    while pq:
        curr_dist, u = heapq.heappop(pq)

        # Ignore outdated entries
        if curr_dist > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist
